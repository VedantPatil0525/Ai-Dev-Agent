import streamlit as st
from agent.code_explainer import explain_code
from agent.debugger import debug_code
from agent.doc_generator import generate_docs
from agent.test_generator import generate_tests
from agent.smart_agent import smart_agent

st.title("🧠 AI Developer Assistant")

code = st.text_area("Paste your code here:")

option = st.selectbox(
    "Choose Task",
    ["Explain Code", "Debug Code", "Generate Docs", "Generate Tests", "Auto Mode"]
)

if st.button("Run Agent"):
    if option == "Explain Code":
        result = explain_code(code)
    elif option == "Debug Code":
        result = debug_code(code)
    elif option == "Generate Docs":
        result = generate_docs(code)
    elif option == "Generate Tests":
        result = generate_tests(code)
    elif option == "Auto Mode":
        result = smart_agent(code)

    st.code(result, language='python')