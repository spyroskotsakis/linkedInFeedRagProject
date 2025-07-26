# langchain_text_splitters.python — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_text_splitters/python.html
**Word Count:** 14
**Links Count:** 14
**Scraped:** 2025-07-21 08:58:20
**Status:** completed

---

# Source code for langchain\_text\_splitters.python               from __future__ import annotations          from typing import Any          from langchain_text_splitters.base import Language     from langchain_text_splitters.character import RecursiveCharacterTextSplitter                              [[docs]](https://python.langchain.com/api_reference/text_splitters/python/langchain_text_splitters.python.PythonCodeTextSplitter.html#langchain_text_splitters.python.PythonCodeTextSplitter)     class PythonCodeTextSplitter(RecursiveCharacterTextSplitter):         """Attempts to split the text along Python syntax."""                         [[docs]](https://python.langchain.com/api_reference/text_splitters/python/langchain_text_splitters.python.PythonCodeTextSplitter.html#langchain_text_splitters.python.PythonCodeTextSplitter.__init__)         def __init__(self, **kwargs: Any) -> None:             """Initialize a PythonCodeTextSplitter."""             separators = self.get_separators_for_language(Language.PYTHON)             super().__init__(separators=separators, **kwargs)