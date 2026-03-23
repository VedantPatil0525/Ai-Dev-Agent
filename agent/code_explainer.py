from utils.llm_handler import query_llm

def explain_code(code):
    prompt = f"""
    Explain the following code in simple terms:

    {code}
    """
    return query_llm(prompt)