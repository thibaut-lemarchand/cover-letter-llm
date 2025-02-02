from langchain_ollama.llms import OllamaLLM

def get_parsing_agent(temperature=0.7, callbacks=None):
    """Smaller, faster model for parsing tasks"""
    return OllamaLLM(
        model="llama3.2",
        temperature=temperature,
        streaming=True,
        callbacks=callbacks
    )

def get_generation_agent(temperature=0.7, callbacks=None):
    """Larger model for creative text generation"""
    return OllamaLLM(
        model="mistral-small",  # Using the larger model for generation
        temperature=temperature,
        streaming=True,
        callbacks=callbacks
    )
