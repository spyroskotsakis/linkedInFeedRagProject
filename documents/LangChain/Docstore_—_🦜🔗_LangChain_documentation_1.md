# Docstore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.Docstore.html
**Word Count:** 49
**Links Count:** 111
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# Docstore\#

_class _langchain\_community.docstore.base.Docstore[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/base.html#Docstore)\#     

Interface to access to place that stores documents.

Methods

`delete`\(ids\) | Deleting IDs from in memory dictionary.   ---|---   `search`\(search\) | Search for document.      delete\(_ids : List_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/base.html#Docstore.delete)\#     

Deleting IDs from in memory dictionary.

Parameters:     

**ids** \(_List_\)

Return type:     

None

_abstractmethod _search\(

    _search : str_, \) → str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/base.html#Docstore.search)\#     

Search for document.

If page exists, return the page summary, and a Document object. If page does not exist, return similar entries.

Parameters:     

**search** \(_str_\)

Return type:     

str | [_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

__On this page