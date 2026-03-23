from utils.llm_handler import query_llm

def smart_agent(code):
    prompt = f"""
    Analyze the code and decide the best action:
    - Explain
    - Debug
    - Document
    - Test

    Then perform that action.

    Code:
    {code}
    """
    return query_llm(prompt)