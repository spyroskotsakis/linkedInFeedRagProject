# langchain_community.document_loaders.college_confidential — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/college_confidential.html
**Word Count:** 11
**Links Count:** 14
**Scraped:** 2025-07-21 09:17:38
**Status:** completed

---

# Source code for langchain\_community.document\_loaders.college\_confidential               from typing import List          from langchain_core.documents import Document          from langchain_community.document_loaders.web_base import WebBaseLoader                              [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.college_confidential.CollegeConfidentialLoader.html#langchain_community.document_loaders.college_confidential.CollegeConfidentialLoader)     class CollegeConfidentialLoader(WebBaseLoader):         """Load `College Confidential` webpages."""                         [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.college_confidential.CollegeConfidentialLoader.html#langchain_community.document_loaders.college_confidential.CollegeConfidentialLoader.load)         def load(self) -> List[Document]:             """Load webpages as Documents."""             soup = self.scrape()             text = soup.select_one("main[class='skin-handler']").text             metadata = {"source": self.web_path}             return [Document(page_content=text, metadata=metadata)]