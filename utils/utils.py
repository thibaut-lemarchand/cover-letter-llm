from langchain_community.document_loaders import AsyncChromiumLoader
from pypdf import PdfReader
from langchain_community.document_transformers import Html2TextTransformer
from agents.ollama import get_parsing_agent, get_generation_agent
from prompts import job_listing_prompt, company_info_prompt


def parse_resume(path):
    loader = PdfReader(path)
    text = loader.pages[0].extract_text()
    return text

def preprocess_job_listing(raw_text):
    agent = get_parsing_agent(temperature=1.0)
    prompt_template = job_listing_prompt.prompt_template.format(raw_text=raw_text)
    resp = agent.invoke(prompt_template.format(raw_text=raw_text))
    return resp

def parse_job_listing(url):
    # Load HTML
    loader = AsyncChromiumLoader([url])
    html = loader.load()
    # Extract text from HTML
    html2text = Html2TextTransformer()
    raw_text = html2text.transform_documents(html)[0].page_content

    resp = preprocess_job_listing(raw_text)
    return resp

def preprocess_company_context(raw_text):
    agent = get_parsing_agent(temperature=1.0)
    prompt_template = company_info_prompt.prompt_template.format(raw_text=raw_text)
    resp = agent.invoke(prompt_template.format(raw_text=raw_text))
    return resp

def generate_cover_letter(prompt, callbacks=None):
    # Use the larger model for cover letter generation
    agent = get_generation_agent(callbacks=callbacks)
    resp = agent.invoke(prompt)
    return resp
