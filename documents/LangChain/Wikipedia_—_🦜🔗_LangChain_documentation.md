# Wikipedia — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.wikipedia.Wikipedia.html
**Word Count:** 74
**Links Count:** 114
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# Wikipedia\#

_class _langchain\_community.docstore.wikipedia.Wikipedia[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/wikipedia.html#Wikipedia)\#     

Wikipedia API.

Check that wikipedia package is installed.

Methods

`__init__`\(\) | Check that wikipedia package is installed.   ---|---   `delete`\(ids\) | Deleting IDs from in memory dictionary.   `search`\(search\) | Try to search for wiki page.      \_\_init\_\_\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/wikipedia.html#Wikipedia.__init__)\#     

Check that wikipedia package is installed.

Return type:     

None

delete\(_ids : List_\) → None\#     

Deleting IDs from in memory dictionary.

Parameters:     

**ids** \(_List_\)

Return type:     

None

search\(

    _search : str_, \) → str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/docstore/wikipedia.html#Wikipedia.search)\#     

Try to search for wiki page.

If page exists, return the page summary, and a PageWithLookups object. If page does not exist, return similar entries.

Parameters:     

**search** \(_str_\) – search string.

Return type:     

str | [_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

Returns: a Document object or error message.

__On this page