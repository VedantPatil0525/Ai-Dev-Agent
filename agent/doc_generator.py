from utils.llm_handler import query_llm

def generate_docs(code):
    prompt = f"""
    Generate proper documentation for this code:

    {code}
    """
    return query_llm(prompt)