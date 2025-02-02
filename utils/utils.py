from langchain_community.document_loaders import AsyncChromiumLoader
from pypdf import PdfReader
from langchain_community.document_transformers import Html2TextTransformer
from agents.ollama import get_parsing_agent, get_generation_agent
from prompts import job_listing_prompt


def parse_resume(path):
    loader = PdfReader(path)
    text = loader.pages[0].extract_text()
    return text


def parse_job_listing(url):
    # Load HTML
    loader = AsyncChromiumLoader([url])
    html = loader.load()
    # Extract text from HTML
    html2text = Html2TextTransformer()
    raw_text = html2text.transform_documents(html)[0].page_content
    # Find relevant text using the smaller model
    agent = get_parsing_agent(temperature=1.0)
    prompt_template = job_listing_prompt.prompt_template.format(raw_text=raw_text)
    resp = agent.invoke(prompt_template.format(raw_text=raw_text))
    return resp


def generate_cover_letter(resume_text, job_listing_text, prompt_template, callbacks=None):
    # Use the larger model for cover letter generation
    agent = get_generation_agent(callbacks=callbacks)
    resp = agent.invoke(prompt_template.format(resume=resume_text, job_listing=job_listing_text))
    return resp


def generate_cover_letter_with_old(resume_text, job_listing_text, old_cover_letter_text, prompt_template, callbacks=None):
    """
    Uses the larger model for updated cover letter generation, incorporating the old cover letter
    to imitate the original style and tone while adapting to the new resume and job listing.
    """
    agent = get_generation_agent(callbacks=callbacks)
    prompt = prompt_template.format(resume=resume_text, job_listing=job_listing_text, old_cover_letter=old_cover_letter_text)
    resp = agent.invoke(prompt)
    return resp