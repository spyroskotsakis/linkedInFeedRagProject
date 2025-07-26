# NotionDBLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.notiondb.NotionDBLoader.html
**Word Count:** 188
**Links Count:** 426
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# NotionDBLoader\#

_class _langchain\_community.document\_loaders.notiondb.NotionDBLoader\(

    _integration\_token : str_,     _database\_id : str_,     _request\_timeout\_sec : int | None = 10_,     _\*_ ,     _filter\_object : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notiondb.html#NotionDBLoader)\#     

Load from Notion DB.

Reads content from pages within a Notion Database. :param integration\_token: Notion integration token. :type integration\_token: str :param database\_id: Notion database id. :type database\_id: str :param request\_timeout\_sec: Timeout for Notion requests in seconds.

> Defaults to 10.

Parameters:     

  * **filter\_object** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – 

Filter object used to limit returned entries based on specified criteria. E.g.: \{

> ”timestamp”: “last\_edited\_time”, “last\_edited\_time”: \{ >
>> ”on\_or\_after”: “2024-02-07” >  > \}

\} -> will only return entries that were last edited     

on or after 2024-02-07

Notion docs: <https://developers.notion.com/reference/post-database-query-filter> Defaults to None, which will return ALL entries.

  * **integration\_token** \(_str_\)

  * **database\_id** \(_str_\)

  * **request\_timeout\_sec** \(_int_\)

Initialize with parameters.

Methods

`__init__`\(integration\_token, database\_id\[, ...\]\) | Initialize with parameters.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents from the Notion database.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `load_page`\(page\_summary\) | Read a page.      \_\_init\_\_\(

    _integration\_token : str_,     _database\_id : str_,     _request\_timeout\_sec : int | None = 10_,     _\*_ ,     _filter\_object : Dict\[str, Any\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notiondb.html#NotionDBLoader.__init__)\#     

Initialize with parameters.

Parameters:     

  * **integration\_token** \(_str_\)

  * **database\_id** \(_str_\)

  * **request\_timeout\_sec** \(_int_ _|__None_\)

  * **filter\_object** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notiondb.html#NotionDBLoader.load)\#     

Load documents from the Notion database. :returns: List of documents. :rtype: List\[Document\]

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load Documents and split into chunks. Chunks are returned as Documents.

Do not override this method. It should be considered to be deprecated\!

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_page\(

    _page\_summary : Dict\[str, Any\]_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/notiondb.html#NotionDBLoader.load_page)\#     

Read a page.

Parameters:     

**page\_summary** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – Page summary from Notion API.

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

Examples using NotionDBLoader

  * [Notion DB](https://python.langchain.com/docs/integrations/providers/notion/)

  * [Notion DB 2/2](https://python.langchain.com/docs/integrations/document_loaders/notiondb/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)