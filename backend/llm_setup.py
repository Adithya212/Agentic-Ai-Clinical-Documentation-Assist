from langchain_community.llms import Ollama

def get_llm():
    # Make sure 'ollama run llama3' is running
    return Ollama(model="llama3.2")
