# langchain_text_splitters.latex — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_text_splitters/latex.html
**Word Count:** 15
**Links Count:** 14
**Scraped:** 2025-07-21 08:58:20
**Status:** completed

---

# Source code for langchain\_text\_splitters.latex               from __future__ import annotations          from typing import Any          from langchain_text_splitters.base import Language     from langchain_text_splitters.character import RecursiveCharacterTextSplitter                              [[docs]](https://python.langchain.com/api_reference/text_splitters/latex/langchain_text_splitters.latex.LatexTextSplitter.html#langchain_text_splitters.latex.LatexTextSplitter)     class LatexTextSplitter(RecursiveCharacterTextSplitter):         """Attempts to split the text along Latex-formatted layout elements."""                         [[docs]](https://python.langchain.com/api_reference/text_splitters/latex/langchain_text_splitters.latex.LatexTextSplitter.html#langchain_text_splitters.latex.LatexTextSplitter.__init__)         def __init__(self, **kwargs: Any) -> None:             """Initialize a LatexTextSplitter."""             separators = self.get_separators_for_language(Language.LATEX)             super().__init__(separators=separators, **kwargs)