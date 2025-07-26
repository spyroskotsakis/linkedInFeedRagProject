# ChainInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.ChainInput.html
**Word Count:** 47
**Links Count:** 168
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# ChainInput\#

_class _langchain\_community.chains.pebblo\_retrieval.models.ChainInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/models.html#ChainInput)\#     

Bases: `BaseModel`

Input for PebbloRetrievalQA chain.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _auth\_context _: [AuthContext](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.AuthContext.html#langchain_community.chains.pebblo_retrieval.models.AuthContext "langchain_community.chains.pebblo_retrieval.models.AuthContext") | None_ _ = None_\#     

_param _query _: str_ _\[Required\]_\#     

_param _semantic\_context _: [SemanticContext](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.SemanticContext.html#langchain_community.chains.pebblo_retrieval.models.SemanticContext "langchain_community.chains.pebblo_retrieval.models.SemanticContext") | None_ _ = None_\#     

Examples using ChainInput

  * [Identity-enabled RAG using PebbloRetrievalQA](https://python.langchain.com/docs/integrations/providers/pebblo/pebblo_retrieval_qa/)

__On this page