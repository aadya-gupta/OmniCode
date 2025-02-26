import streamlit as st
from features.code_generate import generate_code
from features.bug_detect import detect_bug
from features.unit_test_generate import gen_unit_test
from features.code_explain import explanation

st.set_page_config(page_title="OmniCode", page_icon="💻", layout="wide")

custom_css = """
<style>
body {
    background-color: #f2f7fb;
}
h1, h2, h3 {
    color: #3b6ba5;
}
.stButton>button {
    background-color: #85c1e9;
    color: white;
    border-radius: 8px;
    padding: 10px 20px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #5dade2;
}
textarea {
    border-radius: 8px;
    border: 1px solid #85c1e9;
}
footer {
    visibility: hidden;
}
#custom-footer {
    position: fixed;
    bottom: 10px;
    left: 10px;
    font-size: 14px;
    color: #3b6ba5;
}
#custom-footer a {
    text-decoration: none;
    color: #3b6ba5;
    font-weight: bold;
}
#custom-footer a:hover {
    color: #1f4e79;
}
</style>
"""

st.markdown(custom_css, unsafe_allow_html=True)

st.title("OmniCode")
st.subheader("Your developer best friend!")

tabs = st.tabs(["Generate Code", "Detect Bugs", "Generate Unit Tests", "Explain Code"])

with tabs[0]:
    desc = st.text_area("Enter the code description:")
    if st.button("Generate Code"):
        if desc.strip():
            with st.spinner("Generating code..."):
                code = generate_code(desc)
                st.code(code, language="python")
        else:
            st.warning("Please enter a description.")

with tabs[1]:
    code_input = st.text_area("Paste the code:")
    if st.button("Detect Bugs"):
        if code_input.strip():
            with st.spinner("Detecting bugs..."):
                lang, static_report, analysis = detect_bug(code_input)
                st.write(f"**Detected Language:** {lang}")
                st.write("**Static Analysis Report:**")
                st.code(static_report or "No issues found.")
                st.write("**Gemini Analysis:**")
                st.write(analysis)
        else:
            st.warning("Please enter code.")

with tabs[2]:
    test_code = st.text_area("Paste the code for unit tests:")
    if st.button("Generate Unit Tests"):
        if test_code.strip():
            with st.spinner("Generating unit tests..."):
                tests = gen_unit_test(test_code)
                st.code(tests, language="python")
        else:
            st.warning("Please enter code.")

with tabs[3]:
    code_to_explain = st.text_area("Paste the code to explain:")
    if st.button("Explain Code"):
        if code_to_explain.strip():
            with st.spinner("Explaining code..."):
                explanation = explanation(code_to_explain)
                st.write(explanation)
        else:
            st.warning("Please enter code.")

st.markdown(
    """
    <div id="custom-footer">
        Created with love by <a href="https://github.com/aadya-gupta" target="_blank">Aadya</a>
    </div>
    """,
    unsafe_allow_html=True
)