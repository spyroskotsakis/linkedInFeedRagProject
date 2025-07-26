# AirtableLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.airtable.AirtableLoader.html
**Word Count:** 166
**Links Count:** 420
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# AirtableLoader\#

_class _langchain\_community.document\_loaders.airtable.AirtableLoader\(

    _api\_token : str_,     _table\_id : str_,     _base\_id : str_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/airtable.html#AirtableLoader)\#     

Load the Airtable tables.

Initialize with API token and the IDs for table and base.

Parameters:     

  * **api\_token** \(_str_\) – Airtable API token.

  * **table\_id** \(_str_\) – Airtable table ID.

  * **base\_id** \(_str_\)

  * **kwargs** \(_Any_\) – Additional parameters to pass to Table.all\(\). Refer to the pyairtable documentation for available options: <https://pyairtable.readthedocs.io/en/latest/api.html#pyairtable.Table.all>

Methods

`__init__`\(api\_token, table\_id, base\_id, \*\*kwargs\) | Initialize with API token and the IDs for table and base.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load Documents from table.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _api\_token : str_,     _table\_id : str_,     _base\_id : str_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/airtable.html#AirtableLoader.__init__)\#     

Initialize with API token and the IDs for table and base.

Parameters:     

  * **api\_token** \(_str_\) – Airtable API token.

  * **table\_id** \(_str_\) – Airtable table ID.

  * **base\_id** \(_str_\)

  * **kwargs** \(_Any_\) – Additional parameters to pass to Table.all\(\). Refer to the pyairtable documentation for available options: <https://pyairtable.readthedocs.io/en/latest/api.html#pyairtable.Table.all>

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/airtable.html#AirtableLoader.lazy_load)\#     

Lazy load Documents from table.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

Examples using AirtableLoader

  * [Airtable](https://python.langchain.com/docs/integrations/document_loaders/airtable/)

__On this page