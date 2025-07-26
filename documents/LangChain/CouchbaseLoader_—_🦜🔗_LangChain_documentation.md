# CouchbaseLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.couchbase.CouchbaseLoader.html
**Word Count:** 262
**Links Count:** 418
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# CouchbaseLoader\#

_class _langchain\_community.document\_loaders.couchbase.CouchbaseLoader\(

    _connection\_string : str_,     _db\_username : str_,     _db\_password : str_,     _query : str_,     _\*_ ,     _page\_content\_fields : List\[str\] | None = None_,     _metadata\_fields : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/couchbase.html#CouchbaseLoader)\#     

Load documents from Couchbase.

Each document represents one row of the result. The page\_content\_fields are written into the page\_content\`of the document. The \`metadata\_fields are written into the metadata of the document. By default, all columns are written into the page\_content and none into the metadata.

Initialize Couchbase document loader.

Parameters:     

  * **connection\_string** \(_str_\) – The connection string to the Couchbase cluster.

  * **db\_username** \(_str_\) – The username to connect to the Couchbase cluster.

  * **db\_password** \(_str_\) – The password to connect to the Couchbase cluster.

  * **query** \(_str_\) – The SQL++ query to execute.

  * **page\_content\_fields** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – The columns to write into the page\_content field of the document. By default, all columns are written.

  * **metadata\_fields** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – The columns to write into the metadata field of the document. By default, no columns are written.

Methods

`__init__`\(connection\_string, db\_username, ...\) | Initialize Couchbase document loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load Couchbase data into Document objects lazily.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _connection\_string : str_,     _db\_username : str_,     _db\_password : str_,     _query : str_,     _\*_ ,     _page\_content\_fields : List\[str\] | None = None_,     _metadata\_fields : List\[str\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/couchbase.html#CouchbaseLoader.__init__)\#     

Initialize Couchbase document loader.

Parameters:     

  * **connection\_string** \(_str_\) – The connection string to the Couchbase cluster.

  * **db\_username** \(_str_\) – The username to connect to the Couchbase cluster.

  * **db\_password** \(_str_\) – The password to connect to the Couchbase cluster.

  * **query** \(_str_\) – The SQL++ query to execute.

  * **page\_content\_fields** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – The columns to write into the page\_content field of the document. By default, all columns are written.

  * **metadata\_fields** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – The columns to write into the metadata field of the document. By default, no columns are written.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/couchbase.html#CouchbaseLoader.lazy_load)\#     

Load Couchbase data into Document objects lazily.

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

Examples using CouchbaseLoader

  * [Couchbase](https://python.langchain.com/docs/integrations/document_loaders/couchbase/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)