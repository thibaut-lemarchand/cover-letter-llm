import streamlit as st
from utils.utils import *
from prompts import cover_letter_prompts
import pyperclip
from dotenv import load_dotenv
from langchain.callbacks.base import BaseCallbackHandler
import time
load_dotenv()


def main():
    if 'cover_letter' not in st.session_state:
        st.session_state.cover_letter = None
    if 'generation_placeholder' not in st.session_state:
        st.session_state.generation_placeholder = None

    st.title("Cover Letter Generator")

    # Upload Resume
    st.header("1. Upload Resume")
    resume_file = st.file_uploader("Choose a file or drag and drop", type=["pdf"])
    resume_text = None
    if resume_file is not None:
        resume_text = parse_resume(resume_file)

    # Input Job Listing
    st.header("2. Input Job Listing")
    job_listing_type = st.radio("Select input type", ("URL", "Text"))
    job_listing_text = st.session_state.job_listing_text if "job_listing_text" in st.session_state else None
    if job_listing_type == "URL":
        job_listing_url = st.text_input("Enter job listing URL", "")
        if st.button("Fetch Job Listing"):
            job_listing_text = parse_job_listing(job_listing_url)
            st.session_state.job_listing_text = job_listing_text
    elif job_listing_type == "Text":
        job_listing_text = st.text_area("Enter job listing text", "")

    # Optional: Upload Old Cover Letter
    st.header("Optional: Upload Old Cover Letter")
    old_cover_letter_file = st.file_uploader("Upload your old cover letter (optional)", type=["pdf", "txt"], key="old_cover_letter_file")
    old_cover_letter_text = None
    if old_cover_letter_file is not None:
        # If the file is a PDF, use parse_resume to extract text; otherwise, read directly
        if old_cover_letter_file.type == "application/pdf":
            old_cover_letter_text = parse_resume(old_cover_letter_file)
        else:
            old_cover_letter_text = old_cover_letter_file.read().decode("utf-8")

    # Select Cover Letter Style (only used if no old cover letter is provided)
    st.header("3. Select Cover Letter Style")
    cover_letter_style = st.radio("Select style", ("Classic", "Modern"))

    # Select Language
    st.header("4. Select Language")
    language_option = st.radio("Select language", ("English", "Français"))

    # Generate Cover Letter
    st.header("5. Generate Cover Letter")
    if st.button("Generate Cover Letter"):
        if resume_text is not None and job_listing_text is not None:
            # Choose the prompt template based on whether an old cover letter is provided and the selected language.
            if old_cover_letter_text:
                if language_option == "Français":
                    prompt_template = cover_letter_prompts.prompt_template_with_old_fr
                else:
                    prompt_template = cover_letter_prompts.prompt_template_with_old
            else:
                if cover_letter_style == "Classic":
                    if language_option == "Français":
                        prompt_template = cover_letter_prompts.prompt_template_classic_fr
                    else:
                        prompt_template = cover_letter_prompts.prompt_template_classic
                else:
                    if language_option == "Français":
                        prompt_template = cover_letter_prompts.prompt_template_modern_fr
                    else:
                        prompt_template = cover_letter_prompts.prompt_template_modern

            # Create placeholders for the "thinking" expander and the streaming result.
            thinking_button_placeholder = st.empty()
            placeholder = st.empty()
            
            streaming_text = []
            is_thinking = False
            current_thinking = ""
            thinking_start_time = None

            class StreamingCallbackHandler(BaseCallbackHandler):
                def on_llm_new_token(self, token: str, **kwargs):
                    nonlocal is_thinking, current_thinking, thinking_start_time
                    # Detect start of a thinking phase.
                    if '<think>' in token:
                        is_thinking = True
                        current_thinking = ""
                        thinking_start_time = time.time()
                        return
                    # Detect end of a thinking phase.
                    elif '</think>' in token:
                        is_thinking = False
                        duration = round(time.time() - thinking_start_time)
                        with thinking_button_placeholder.container():
                            with st.expander(f"Thought for {duration} seconds"):
                                st.markdown(current_thinking)
                        return
                    # While in a thinking phase, update the temporary holder.
                    if is_thinking:
                        current_thinking += token
                        with thinking_button_placeholder.container():
                            with st.expander("Thinking..."):
                                st.markdown(current_thinking)
                    # Otherwise, stream tokens to the main output.
                    else:
                        streaming_text.append(token)
                        placeholder.markdown(''.join(streaming_text))

            # Generate cover letter with streaming callbacks
            if old_cover_letter_text:
                raw_cover_letter = generate_cover_letter_with_old(
                    resume_text, 
                    job_listing_text, 
                    old_cover_letter_text,
                    prompt_template, 
                    callbacks=[StreamingCallbackHandler()]
                )
            else:
                raw_cover_letter = generate_cover_letter(
                    resume_text, 
                    job_listing_text, 
                    prompt_template, 
                    callbacks=[StreamingCallbackHandler()]
                )
            
            # Remove any remaining thinking tags from the final output.
            import re
            cover_letter = re.sub(r'<think>.*?</think>', '', raw_cover_letter, flags=re.DOTALL)
            
            # Display the final cover letter and update session state.
            placeholder.markdown(cover_letter)
            st.session_state.cover_letter = cover_letter
        else:
            st.warning("Please upload a resume and provide a job listing.")

    # Copy Cover Letter to Clipboard
    if st.session_state.cover_letter is not None:
        if st.button("Copy to Clipboard"):
            pyperclip.copy(st.session_state.cover_letter)
            st.success("Cover letter copied to clipboard!")

if __name__ == "__main__":
    main()
