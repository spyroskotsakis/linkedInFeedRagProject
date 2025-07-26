# OutlineAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.outline.OutlineAPIWrapper.html
**Word Count:** 89
**Links Count:** 266
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# OutlineAPIWrapper\#

_class _langchain\_community.utilities.outline.OutlineAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/outline.html#OutlineAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around OutlineAPI.

This wrapper will use the Outline API to query the documents of your instance. By default it will return the document content of the top-k results. It limits the document content by doc\_content\_chars\_max.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _doc\_content\_chars\_max _: int_ _ = 4000_\#     

_param _load\_all\_available\_meta _: bool_ _ = False_\#     

_param _outline\_api\_key _: str | None_ _ = None_\#     

_param _outline\_instance\_url _: str | None_ _ = None_\#     

_param _outline\_search\_endpoint _: str_ _ = '/api/documents.search'_\#     

_param _top\_k\_results _: int_ _ = 3_\#     

run\(

    _query : str_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/outline.html#OutlineAPIWrapper.run)\#     

Run Outline search and get the document content plus the meta information.

Returns: a list of documents.

Parameters:     

**query** \(_str_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page