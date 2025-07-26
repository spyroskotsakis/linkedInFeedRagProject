# BaseCrossEncoder — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder.html
**Word Count:** 24
**Links Count:** 110
**Scraped:** 2025-07-21 07:49:02
**Status:** completed

---

# BaseCrossEncoder\#

_class _langchain.retrievers.document\_compressors.cross\_encoder.BaseCrossEncoder[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/retrievers/document_compressors/cross_encoder.html#BaseCrossEncoder)\#     

Interface for cross encoder models.

Methods

`score`\(text\_pairs\) | Score pairs' similarity.   ---|---      _abstractmethod _score\(

    _text\_pairs : list\[tuple\[str, str\]\]_, \) → list\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/retrievers/document_compressors/cross_encoder.html#BaseCrossEncoder.score)\#     

Score pairs’ similarity.

Parameters:     

**text\_pairs** \(_list_ _\[__tuple_ _\[__str_ _,__str_ _\]__\]_\) – List of pairs of texts.

Returns:     

List of scores.

Return type:     

list\[float\]

__On this page