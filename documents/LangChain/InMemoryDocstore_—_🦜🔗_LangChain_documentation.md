# InMemoryDocstore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.in_memory.InMemoryDocstore.html
**Word Count:** 80
**Links Count:** 128
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# InMemoryDocstore\#

_class _langchain\_community.docstore.in\_memory.InMemoryDocstore\(

    _\_dict : Dict\[str, [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/in_memory.html#InMemoryDocstore)\#     

Simple in memory docstore in the form of a dict.

Initialize with dict.

Methods

`__init__`\(\[\_dict\]\) | Initialize with dict.   ---|---   `add`\(texts\) | Add texts to in memory dictionary.   `delete`\(ids\) | Deleting IDs from in memory dictionary.   `search`\(search\) | Search via direct lookup.      Parameters:     

**\_dict** \(_Dict_ _\[__str_ _,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__|__None_\)

\_\_init\_\_\(

    _\_dict : Dict\[str, [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/in_memory.html#InMemoryDocstore.__init__)\#     

Initialize with dict.

Parameters:     

**\_dict** \(_Dict_ _\[__str_ _,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__|__None_\)

add\(

    _texts : Dict\[str, [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/in_memory.html#InMemoryDocstore.add)\#     

Add texts to in memory dictionary.

Parameters:     

**texts** \(_Dict_ _\[__str_ _,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – dictionary of id -> document.

Returns:     

None

Return type:     

None

delete\(_ids : List_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/in_memory.html#InMemoryDocstore.delete)\#     

Deleting IDs from in memory dictionary.

Parameters:     

**ids** \(_List_\)

Return type:     

None

search\(

    _search : str_, \) → str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/in_memory.html#InMemoryDocstore.search)\#     

Search via direct lookup.

Parameters:     

**search** \(_str_\) – id of a document to search for.

Returns:     

Document if found, else error message.

Return type:     

str | [_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

Examples using InMemoryDocstore

  * [Annoy](https://python.langchain.com/docs/integrations/vectorstores/annoy/)

  * [Faiss](https://python.langchain.com/docs/integrations/vectorstores/faiss/)

  * [How to use a time-weighted vector store retriever](https://python.langchain.com/docs/how_to/time_weighted_vectorstore/)

__On this page