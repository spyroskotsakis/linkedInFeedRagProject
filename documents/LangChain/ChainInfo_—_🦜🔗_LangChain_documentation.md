# ChainInfo — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.ChainInfo.html
**Word Count:** 39
**Links Count:** 167
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# ChainInfo\#

_class _langchain\_community.chains.pebblo\_retrieval.models.ChainInfo[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/models.html#ChainInfo)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _model _: [Model](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Model.html#langchain_community.chains.pebblo_retrieval.models.Model "langchain_community.chains.pebblo_retrieval.models.Model") | None_ _\[Required\]_\#     

_param _name _: str_ _\[Required\]_\#     

_param _vector\_dbs _: List\[[VectorDB](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.VectorDB.html#langchain_community.chains.pebblo_retrieval.models.VectorDB "langchain_community.chains.pebblo_retrieval.models.VectorDB")\] | None_ _\[Required\]_\#     

__On this page