# langchain_community.document_loaders.onedrive — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/onedrive.html
**Word Count:** 22
**Links Count:** 13
**Scraped:** 2025-07-21 09:15:40
**Status:** completed

---

# Source code for langchain\_community.document\_loaders.onedrive               from typing import Any          from pydantic import Field          from langchain_community.document_loaders import SharePointLoader                              [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.onedrive.OneDriveLoader.html#langchain_community.document_loaders.onedrive.OneDriveLoader)     class OneDriveLoader(SharePointLoader):         """         Load documents from Microsoft OneDrive.         Uses `SharePointLoader` under the hood.         """              drive_id: str = Field(...)         """The ID of the OneDrive drive to load data from."""              def __init__(self, **kwargs: Any) -> None:             kwargs["document_library_id"] = kwargs["drive_id"]             super().__init__(**kwargs)