import streamlit as st
import streamlit as st
import streamlit.components.v1 as components


st.title("Home Page")
st.markdown(":red[Welcome] to the home page of this Streamlit app!")
st.write("This is a simple example of how to create a home page using :blue[Streamlit].")

mermaid_code = """
graph TD
    A[开始] --> B{是否已完成？}
    B -- 是 --> C[继续]
    B -- 否 --> D[继续处理]
    D --> B
    C --> E{test}
    E -- 是 --> A
"""

html_code = f"""
<div class="mermaid">
{mermaid_code}
</div>

<script type="module">
import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
mermaid.initialize({{ startOnLoad: true }});
</script>
"""

st.title("Mermaid 图表示例")
components.html(html_code,scrolling=True,height=500)
