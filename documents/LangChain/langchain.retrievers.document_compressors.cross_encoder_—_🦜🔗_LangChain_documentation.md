# langchain.retrievers.document_compressors.cross_encoder — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/retrievers/document_compressors/cross_encoder.html
**Word Count:** 18
**Links Count:** 14
**Scraped:** 2025-07-21 07:59:00
**Status:** completed

---

# Source code for langchain.retrievers.document\_compressors.cross\_encoder               from abc import ABC, abstractmethod                              [[docs]](https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder.html#langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder)     class BaseCrossEncoder(ABC):         """Interface for cross encoder models."""                         [[docs]](https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder.html#langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder.score)         @abstractmethod         def score(self, text_pairs: list[tuple[str, str]]) -> list[float]:             """Score pairs' similarity.                  Args:                 text_pairs: List of pairs of texts.                  Returns:                 List of scores.             """