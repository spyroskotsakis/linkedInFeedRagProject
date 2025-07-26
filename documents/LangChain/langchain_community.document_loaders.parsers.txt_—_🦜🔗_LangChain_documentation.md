# langchain_community.document_loaders.parsers.txt — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/txt.html
**Word Count:** 15
**Links Count:** 14
**Scraped:** 2025-07-21 09:14:05
**Status:** completed

---

# Source code for langchain\_community.document\_loaders.parsers.txt               """Module for parsing text files.."""          from typing import Iterator          from langchain_core.documents import Document          from langchain_community.document_loaders.base import BaseBlobParser     from langchain_community.document_loaders.blob_loaders import Blob                              [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.txt.TextParser.html#langchain_community.document_loaders.parsers.txt.TextParser)     class TextParser(BaseBlobParser):         """Parser for text blobs."""                         [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.txt.TextParser.html#langchain_community.document_loaders.parsers.txt.TextParser.lazy_parse)         def lazy_parse(self, blob: Blob) -> Iterator[Document]:             """Lazily parse the blob."""             yield Document(page_content=blob.as_string(), metadata={"source": blob.source})