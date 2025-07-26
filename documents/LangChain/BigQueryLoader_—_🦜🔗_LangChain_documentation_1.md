# BigQueryLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/bigquery/langchain_google_community.bigquery.BigQueryLoader.html
**Word Count:** 253
**Links Count:** 119
**Scraped:** 2025-07-21 07:59:55
**Status:** completed

---

# BigQueryLoader\#

_class _langchain\_google\_community.bigquery.BigQueryLoader\(

    _query : str_,     _project : str | None = None_,     _page\_content\_columns : List\[str\] | None = None_,     _metadata\_columns : List\[str\] | None = None_,     _credentials : Credentials | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/bigquery.html#BigQueryLoader)\#     

Load from the Google Cloud Platform BigQuery.

Each document represents one row of the result. The page\_content\_columns are written into the page\_content of the document. The metadata\_columns are written into the metadata of the document. By default, all columns are written into the page\_content and none into the metadata.

Initialize BigQuery document loader.

Parameters:     

  * **query** \(_str_\) – The query to run in BigQuery.

  * **project** \(_Optional_ _\[__str_ _\]_\) – Optional. The project to run the query in.

  * **page\_content\_columns** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. The columns to write into the page\_content of the document.

  * **metadata\_columns** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. The columns to write into the metadata of the document.

  * **credentials** \(_Optional_ _\[__Credentials_ _\]_\) – 

google.auth.credentials.Credentials, optional Credentials for accessing Google APIs. Use this parameter to override

> default credentials, such as to use Compute Engine \(google.auth.compute\_engine.Credentials\) or Service Account \(google.oauth2.service\_account.Credentials\) credentials directly.

Methods

`__init__`\(query\[, project, ...\]\) | Initialize BigQuery document loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _query : str_,     _project : str | None = None_,     _page\_content\_columns : List\[str\] | None = None_,     _metadata\_columns : List\[str\] | None = None_,     _credentials : Credentials | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/bigquery.html#BigQueryLoader.__init__)\#     

Initialize BigQuery document loader.

Parameters:     

  * **query** \(_str_\) – The query to run in BigQuery.

  * **project** \(_Optional_ _\[__str_ _\]_\) – Optional. The project to run the query in.

  * **page\_content\_columns** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. The columns to write into the page\_content of the document.

  * **metadata\_columns** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. The columns to write into the metadata of the document.

  * **credentials** \(_Optional_ _\[__Credentials_ _\]_\) – 

google.auth.credentials.Credentials, optional Credentials for accessing Google APIs. Use this parameter to override

> default credentials, such as to use Compute Engine \(google.auth.compute\_engine.Credentials\) or Service Account \(google.oauth2.service\_account.Credentials\) credentials directly.

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/bigquery.html#BigQueryLoader.load)\#     

Load data into Document objects.

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

__On this page