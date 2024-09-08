import streamlit as st
from code_editor import code_editor


st.set_page_config(
    layout="wide",
    page_title="Streamlit Code Editor",
)

col1, col2 = st.columns(2)
col1.header("Code Editor")
col2.header("Code View")

with col1.container(border=False):
    

    custom_btns = [
        {
            "name": "copy",
            "feather": "Copy",
            "hasText": True,
            "alwaysOn": True,
            "commands": ["copyAll"],
            "style": {"top": "0.46rem", "right": "0.4rem"},
        },
        {
            "name": "Run",
            "feather": "Play",
            "primary": True,
            "hasText": True,
            "showWithIcon": True,
            "commands": ["submit"],
            "style": {"bottom": "0.44rem", "right": "0.4rem"},
        },
    ]

    code_editor(
        code="import streamlit as st\n\n",
        height=[10, 20],
        key="code_input",
        focus=True,
        theme="dark",
        buttons=custom_btns,
        info={
            "name": "language info",
            "css": "\nbackground-color: #bee1e5;\n\nbody > #root .ace-streamlit-dark~& {\n   background-color: #262830;\n}\n\n.ace-streamlit-dark~& span {\n   color: #fff;\n    opacity: 0.6;\n}\n\nspan {\n   color: #000;\n    opacity: 0.5;\n}\n\n.code_editor-info.message {\n    width: inherit;\n    margin-right: 75px;\n    order: 2;\n    text-align: center;\n    opacity: 0;\n    transition: opacity 0.7s ease-out;\n}\n\n.code_editor-info.message.show {\n    opacity: 0.6;\n}\n\n.ace-streamlit-dark~& .code_editor-info.message.show {\n    opacity: 0.5;\n}\n",
            "style": {
                "order": "1",
                "display": "flex",
                "flexDirection": "row",
                "alignItems": "center",
                "width": "100%",
                "height": "2.5rem",
                "padding": "0rem 0.6rem",
                "padding-bottom": "0.2rem",
                "margin-bottom": "-5px",
                "borderRadius": "8px 8px 0px 0px",
                "zIndex": "9993",
            },
            "info": [{"name": "python", "style": {"width": "100px"}}],
        },
    )

if (
    "code_input" in st.session_state
    and st.session_state["code_input"] is not None
):
    code: str = st.session_state["code_input"]["text"]
    code = code.replace("import streamlit as st\n\n", "")

    
    with col2:
        exec(code)
