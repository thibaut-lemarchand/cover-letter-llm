from langchain_ollama.llms import OllamaLLM

def get_agent(temperature=0.7, streaming=False, callbacks=None):
    return OllamaLLM(
        # model="deepseek-r1:32b",
        # model="hf.co/bartowski/Qwen2.5-14B-Instruct-1M-GGUF:Q4_K_M",
        # model="hf.co/bartowski/Qwen2.5-7B-Instruct-1M-GGUF:IQ4_NL",
        model="deepseek-r1:1.5b",
        temperature=temperature,
        streaming=True,  # Always set to True
        callbacks=callbacks
    )
