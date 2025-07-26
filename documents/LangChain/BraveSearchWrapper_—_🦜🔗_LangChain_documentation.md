# BraveSearchWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.brave_search.BraveSearchWrapper.html
**Word Count:** 120
**Links Count:** 263
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# BraveSearchWrapper\#

_class _langchain\_community.utilities.brave\_search.BraveSearchWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/brave_search.html#BraveSearchWrapper)\#     

Bases: `BaseModel`

Wrapper around the Brave search engine.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_key _: SecretStr_ _\[Optional\]_\#     

The API key to use for the Brave search engine.

_param _base\_url _: str_ _ = 'https://api.search.brave.com/res/v1/web/search'_\#     

The base URL for the Brave search engine.

_param _search\_kwargs _: dict_ _\[Optional\]_\#     

Additional keyword arguments to pass to the search request.

download\_documents\(

    _query : str_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/brave_search.html#BraveSearchWrapper.download_documents)\#     

Query the Brave search engine and return the results as a list of Documents.

Parameters:     

**query** \(_str_\) – The query to search for.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Returns: The results as a list of Documents.

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/brave_search.html#BraveSearchWrapper.run)\#     

Query the Brave search engine and return the results as a JSON string.

Parameters:     

**query** \(_str_\) – The query to search for.

Return type:     

str

Returns: The results as a JSON string.

__On this page