# DocstoreFn — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.arbitrary_fn.DocstoreFn.html
**Word Count:** 56
**Links Count:** 118
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# DocstoreFn\#

_class _langchain\_community.docstore.arbitrary\_fn.DocstoreFn\(

    _lookup\_fn : Callable\[\[str\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | str\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/arbitrary_fn.html#DocstoreFn)\#     

Docstore via arbitrary lookup function.

This is useful when:     

  * it’s expensive to construct an InMemoryDocstore/dict

  * you retrieve documents from remote sources

  * you just want to reuse existing objects

Methods

`__init__`\(lookup\_fn\) |    ---|---   `delete`\(ids\) | Deleting IDs from in memory dictionary.   `search`\(search\) | Search for a document.      Parameters:     

**lookup\_fn** \(_Callable_ _\[__\[__str_ _\]__,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _|__str_ _\]_\)

\_\_init\_\_\(

    _lookup\_fn : Callable\[\[str\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | str\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/arbitrary_fn.html#DocstoreFn.__init__)\#     

Parameters:     

**lookup\_fn** \(_Callable_ _\[__\[__str_ _\]__,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _|__str_ _\]_\)

delete\(_ids : List_\) → None\#     

Deleting IDs from in memory dictionary.

Parameters:     

**ids** \(_List_\)

Return type:     

None

search\(

    _search : str_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/arbitrary_fn.html#DocstoreFn.search)\#     

Search for a document.

Parameters:     

**search** \(_str_\) – search string

Returns:     

Document if found, else error message.

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

__On this page