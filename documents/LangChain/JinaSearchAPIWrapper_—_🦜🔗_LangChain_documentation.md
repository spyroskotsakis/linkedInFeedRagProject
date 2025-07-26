# JinaSearchAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.jina_search.JinaSearchAPIWrapper.html
**Word Count:** 103
**Links Count:** 261
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# JinaSearchAPIWrapper\#

_class _langchain\_community.utilities.jina\_search.JinaSearchAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jina_search.html#JinaSearchAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around the Jina search engine.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_key _: SecretStr_ _\[Required\]_\#     

_param _base\_url _: str_ _ = 'https://s.jina.ai/'_\#     

The base URL for the Jina search engine.

download\_documents\(

    _query : str_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jina_search.html#JinaSearchAPIWrapper.download_documents)\#     

Query the Jina search engine and return the results as a list of Documents.

Parameters:     

**query** \(_str_\) – The query to search for.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Returns: The results as a list of Documents.

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jina_search.html#JinaSearchAPIWrapper.run)\#     

Query the Jina search engine and return the results as a JSON string.

Parameters:     

**query** \(_str_\) – The query to search for.

Return type:     

str

Returns: The results as a JSON string.

__On this page