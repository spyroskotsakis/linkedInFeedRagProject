# GlueCatalogLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.glue_catalog.GlueCatalogLoader.html
**Word Count:** 280
**Links Count:** 420
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# GlueCatalogLoader\#

_class _langchain\_community.document\_loaders.glue\_catalog.GlueCatalogLoader\(

    _database : str_,     _\*_ ,     _session : Session | None = None_,     _profile\_name : str | None = None_,     _table\_filter : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/glue_catalog.html#GlueCatalogLoader)\#     

Load table schemas from AWS Glue.

This loader fetches the schema of each table within a specified AWS Glue database. The schema details include column names and their data types, similar to pandas dtype representation.

AWS credentials are automatically loaded using boto3, following the standard AWS method: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

If a specific AWS profile is required, it can be specified and will be used to establish the session.

Initialize Glue database loader.

Parameters:     

  * **database** \(_str_\) – The name of the Glue database from which to load table schemas.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Optional. A boto3 Session object. If not provided, a new session will be created.

  * **profile\_name** \(_Optional_ _\[__str_ _\]_\) – Optional. The name of the AWS profile to use for credentials.

  * **table\_filter** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. List of table names to fetch schemas for, fetching all if None.

Methods

`__init__`\(database, \*\[, session, ...\]\) | Initialize Glue database loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazily load table schemas as Document objects.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _database : str_,     _\*_ ,     _session : Session | None = None_,     _profile\_name : str | None = None_,     _table\_filter : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/glue_catalog.html#GlueCatalogLoader.__init__)\#     

Initialize Glue database loader.

Parameters:     

  * **database** \(_str_\) – The name of the Glue database from which to load table schemas.

  * **session** \(_Optional_ _\[__Session_ _\]_\) – Optional. A boto3 Session object. If not provided, a new session will be created.

  * **profile\_name** \(_Optional_ _\[__str_ _\]_\) – Optional. The name of the AWS profile to use for credentials.

  * **table\_filter** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. List of table names to fetch schemas for, fetching all if None.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/glue_catalog.html#GlueCatalogLoader.lazy_load)\#     

Lazily load table schemas as Document objects.

Yields:     

Document objects, each representing the schema of a table.

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

Examples using GlueCatalogLoader

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [Glue Catalog](https://python.langchain.com/docs/integrations/document_loaders/glue_catalog/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)