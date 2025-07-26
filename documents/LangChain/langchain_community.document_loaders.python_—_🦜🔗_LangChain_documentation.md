# langchain_community.document_loaders.python — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/python.html
**Word Count:** 24
**Links Count:** 14
**Scraped:** 2025-07-21 08:58:43
**Status:** completed

---

# Source code for langchain\_community.document\_loaders.python               import tokenize     from pathlib import Path     from typing import Union          from langchain_community.document_loaders.text import TextLoader                              [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.python.PythonLoader.html#langchain_community.document_loaders.python.PythonLoader)     class PythonLoader(TextLoader):         """Load `Python` files, respecting any non-default encoding if specified."""                         [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.python.PythonLoader.html#langchain_community.document_loaders.python.PythonLoader.__init__)         def __init__(self, file_path: Union[str, Path]):             """Initialize with a file path.                  Args:                 file_path: The path to the file to load.             """             with open(file_path, "rb") as f:                 encoding, _ = tokenize.detect_encoding(f.readline)             super().__init__(file_path=file_path, encoding=encoding)