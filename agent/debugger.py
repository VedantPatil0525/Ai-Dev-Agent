from utils.llm_handler import query_llm

def debug_code(code):
    prompt = f"""
    Find bugs in the code and fix them:

    {code}
    """
    return query_llm(prompt)