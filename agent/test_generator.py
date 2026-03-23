from utils.llm_handler import query_llm

def generate_tests(code):
    prompt = f"""
    Generate unit tests for this code:

    {code}
    """
    return query_llm(prompt)