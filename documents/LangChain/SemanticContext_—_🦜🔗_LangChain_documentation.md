# SemanticContext — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.SemanticContext.html
**Word Count:** 48
**Links Count:** 166
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# SemanticContext\#

_class _langchain\_community.chains.pebblo\_retrieval.models.SemanticContext[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/models.html#SemanticContext)\#     

Bases: `BaseModel`

Class for a semantic context.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _pebblo\_semantic\_entities _: [SemanticEntities](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.SemanticEntities.html#langchain_community.chains.pebblo_retrieval.models.SemanticEntities "langchain_community.chains.pebblo_retrieval.models.SemanticEntities") | None_ _ = None_\#     

_param _pebblo\_semantic\_topics _: [SemanticTopics](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.SemanticTopics.html#langchain_community.chains.pebblo_retrieval.models.SemanticTopics "langchain_community.chains.pebblo_retrieval.models.SemanticTopics") | None_ _ = None_\#     

Examples using SemanticContext

  * [Identity-enabled RAG using PebbloRetrievalQA](https://python.langchain.com/docs/integrations/providers/pebblo/pebblo_retrieval_qa/)

__On this page