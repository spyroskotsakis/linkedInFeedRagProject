# langchain_community.document_loaders.azlyrics — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/azlyrics.html
**Word Count:** 10
**Links Count:** 14
**Scraped:** 2025-07-21 09:18:00
**Status:** completed

---

# Source code for langchain\_community.document\_loaders.azlyrics               from typing import List          from langchain_core.documents import Document          from langchain_community.document_loaders.web_base import WebBaseLoader                              [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.azlyrics.AZLyricsLoader.html#langchain_community.document_loaders.azlyrics.AZLyricsLoader)     class AZLyricsLoader(WebBaseLoader):         """Load `AZLyrics` webpages."""                         [[docs]](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.azlyrics.AZLyricsLoader.html#langchain_community.document_loaders.azlyrics.AZLyricsLoader.load)         def load(self) -> List[Document]:             """Load webpages into Documents."""             soup = self.scrape()             title = soup.title.text             lyrics = soup.find_all("div", {"class": ""})[2].text             text = title + lyrics             metadata = {"source": self.web_path}             return [Document(page_content=text, metadata=metadata)]