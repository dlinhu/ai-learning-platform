import os
import json
import markdown
from markdown.extensions.codehilite import CodeHiliteExtension
from markdown.extensions.fenced_code import FencedCodeExtension
from markdown.extensions.tables import TableExtension
from typing import Optional, Dict
import nbformat
from nbconvert import HTMLExporter

class ContentRenderer:
    def __init__(self, content_base_path: str):
        self.content_base_path = content_base_path
        self.md = markdown.Markdown(
            extensions=[
                'fenced_code',
                'codehilite',
                'tables',
                'toc',
                'nl2br'
            ],
            extension_configs={
                'codehilite': {
                    'css_class': 'highlight',
                    'linenums': False
                }
            }
        )
        self.nb_exporter = HTMLExporter()
        self.nb_exporter.template_name = 'classic'
    
    def get_file_path(self, relative_path: str) -> Optional[str]:
        possible_paths = [
            os.path.join(self.content_base_path, relative_path),
            os.path.join(self.content_base_path, relative_path.replace('/', os.sep)),
        ]
        for path in possible_paths:
            if os.path.exists(path):
                return path
        return None
    
    def render_markdown(self, file_path: str) -> Dict:
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}", "content": ""}
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        self.md.reset()
        html_content = self.md.convert(content)
        
        return {
            "type": "markdown",
            "raw": content,
            "html": html_content,
            "toc": self.md.toc if hasattr(self.md, 'toc') else ""
        }
    
    def render_notebook(self, file_path: str) -> Dict:
        if not os.path.exists(file_path):
            return {"error": f"File not found: {file_path}", "content": ""}
        
        with open(file_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        (body, resources) = self.nb_exporter.from_notebook_node(nb)
        
        return {
            "type": "notebook",
            "html": body,
            "metadata": nb.metadata if hasattr(nb, 'metadata') else {}
        }
    
    def render_content(self, relative_path: str) -> Dict:
        file_path = self.get_file_path(relative_path)
        if not file_path:
            return {"error": f"File not found: {relative_path}", "content": ""}
        
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.md':
            return self.render_markdown(file_path)
        elif ext == '.ipynb':
            return self.render_notebook(file_path)
        elif ext == '.py':
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return {
                "type": "python",
                "raw": content,
                "html": f'<pre class="highlight"><code class="language-python">{content}</code></pre>'
            }
        else:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            return {
                "type": "text",
                "raw": content,
                "html": f'<pre>{content}</pre>'
            }
