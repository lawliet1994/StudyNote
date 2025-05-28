import streamlit as st
import os
import streamlit.components.v1 as components
from io import BytesIO

BASE_DIR = "./files"

# st.set_page_config(page_title="文件管理器", layout="wide")
st.title("📁 美观网页文件管理器")

# --------- 功能函数 ---------
def save_file(uploaded_file, directory):
    save_path = os.path.join(directory, uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"文件已上传到 {save_path}")

def serve_file(file_path):
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            st.download_button("点击下载文件", f, file_name=os.path.basename(file_path))

def generate_html_tree(path):
    def walk(p):
        html = "<ul>"
        for item in sorted(os.listdir(p)):
            full_path = os.path.join(p, item)
            rel_path = os.path.relpath(full_path, BASE_DIR)
            if os.path.isdir(full_path):
                html += f"<li><details><summary>{item}</summary>{walk(full_path)}</details></li>"
            else:
                html += f"<li>{item} - <a href='?download={rel_path}' target='_self'>下载</a></li>"
        html += "</ul>"
        return html
    return walk(path)

# --------- 处理下载请求 ---------
query_params = st.experimental_get_query_params()
if "download" in query_params:
    download_target = os.path.join(BASE_DIR, query_params["download"][0])
    serve_file(download_target)
    st.stop()

# --------- 上传文件 ---------
st.markdown("### 📤 上传文件到根目录")
uploaded = st.file_uploader("选择文件上传", type=None)
if uploaded:
    save_file(uploaded, BASE_DIR)

# --------- 渲染 HTML 文件树 ---------
html_code = f"""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
<style>
.tree ul {{
    list-style-type: none;
    padding-left: 20px;
}}
.tree li::before {{
    content: '\\f07b';
    font-family: FontAwesome;
    padding-right: 8px;
}}
.tree a {{
    text-decoration: none;
    color: #1a73e8;
}}
</style>
<div class='tree'>
  {generate_html_tree(BASE_DIR)}
</div>
<script>
document.querySelectorAll('details').forEach(d => {{
  d.addEventListener('toggle', () => {{
    document.querySelectorAll('details').forEach(o => {{
      if (o !== d && d.contains(o)) o.open = true;
    }});
  }});
}});
</script>
"""

components.html(html_code, height=600, scrolling=True)