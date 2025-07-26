# App — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.App.html
**Word Count:** 39
**Links Count:** 179
**Scraped:** 2025-07-21 08:00:56
**Status:** completed

---

# App\#

_class _langchain\_community.chains.pebblo\_retrieval.models.App[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/models.html#App)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _chains _: List\[[ChainInfo](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.ChainInfo.html#langchain_community.chains.pebblo_retrieval.models.ChainInfo "langchain_community.chains.pebblo_retrieval.models.ChainInfo")\]__\[Required\]_\#     

_param _client\_version _: [Framework](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Framework.html#langchain_community.chains.pebblo_retrieval.models.Framework "langchain_community.chains.pebblo_retrieval.models.Framework")_ _\[Required\]_\#     

_param _description _: str | None_ _\[Required\]_\#     

_param _framework _: [Framework](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Framework.html#langchain_community.chains.pebblo_retrieval.models.Framework "langchain_community.chains.pebblo_retrieval.models.Framework")_ _\[Required\]_\#     

_param _name _: str_ _\[Required\]_\#     

_param _owner _: str_ _\[Required\]_\#     

_param _plugin\_version _: str_ _\[Required\]_\#     

_param _runtime _: [Runtime](https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.Runtime.html#langchain_community.chains.pebblo_retrieval.models.Runtime "langchain_community.chains.pebblo_retrieval.models.Runtime")_ _\[Required\]_\#     

__On this page