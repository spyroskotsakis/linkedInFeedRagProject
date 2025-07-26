# langchain_community.document_loaders.imsdb — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/imsdb.html
**Word Count:** 8
**Links Count:** 14
**Scraped:** 2025-07-21 09:18:00
**Status:** completed

---

# Source code for langchain\_community.document\_loaders.imsdb               from typing import List          from langchain_core.documents import Document          from langchain_community.document_loaders.web_base import WebBaseLoader                              [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.imsdb.IMSDbLoader.html#langchain_community.document_loaders.imsdb.IMSDbLoader)     class IMSDbLoader(WebBaseLoader):         """Load `IMSDb` webpages."""                         [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.imsdb.IMSDbLoader.html#langchain_community.document_loaders.imsdb.IMSDbLoader.load)         def load(self) -> List[Document]:             """Load webpage."""             soup = self.scrape()             text = soup.select_one("td[class='scrtext']").text             metadata = {"source": self.web_path}             return [Document(page_content=text, metadata=metadata)]