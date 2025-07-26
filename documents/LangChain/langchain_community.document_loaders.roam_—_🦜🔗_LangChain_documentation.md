# langchain_community.document_loaders.roam — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/roam.html
**Word Count:** 14
**Links Count:** 15
**Scraped:** 2025-07-21 09:12:16
**Status:** completed

---

# Source code for langchain\_community.document\_loaders.roam               from pathlib import Path     from typing import List, Union          from langchain_core.documents import Document          from langchain_community.document_loaders.base import BaseLoader                              [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.roam.RoamLoader.html#langchain_community.document_loaders.roam.RoamLoader)     class RoamLoader(BaseLoader):         """Load `Roam` files from a directory."""                         [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.roam.RoamLoader.html#langchain_community.document_loaders.roam.RoamLoader.__init__)         def __init__(self, path: Union[str, Path]):             """Initialize with a path."""             self.file_path = path                                        [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.roam.RoamLoader.html#langchain_community.document_loaders.roam.RoamLoader.load)         def load(self) -> List[Document]:             """Load documents."""             ps = list(Path(self.file_path).glob("**/*.md"))             docs = []             for p in ps:                 with open(p) as f:                     text = f.read()                 metadata = {"source": str(p)}                 docs.append(Document(page_content=text, metadata=metadata))             return docs