# AthenaLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.athena.AthenaLoader.html
**Word Count:** 259
**Links Count:** 420
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# AthenaLoader\#

_class _langchain\_community.document\_loaders.athena.AthenaLoader\(

    _query : str_,     _database : str_,     _s3\_output\_uri : str_,     _profile\_name : str | None = None_,     _metadata\_columns : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/athena.html#AthenaLoader)\#     

Load documents from AWS Athena.

Each document represents one row of the result. \- By default, all columns are written into the page\_content of the document and none into the metadata of the document. \- If metadata\_columns are provided then these columns are written into the metadata of the document while the rest of the columns are written into the page\_content of the document.

To authenticate, the AWS client uses this method to automatically load credentials: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

If a specific credential profile should be used, you must pass the name of the profile from the ~/.aws/credentials file that is to be used.

Make sure the credentials / roles used have the required policies to access the Amazon Textract service.

Initialize Athena document loader.

Parameters:     

  * **query** \(_str_\) – The query to run in Athena.

  * **database** \(_str_\) – Athena database.

  * **s3\_output\_uri** \(_str_\) – Athena output path.

  * **profile\_name** \(_Optional_ _\[__str_ _\]_\) – Optional. AWS credential profile, if profiles are being used.

  * **metadata\_columns** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. Columns written to Document metadata.

Methods

`__init__`\(query, database, s3\_output\_uri\[, ...\]\) | Initialize Athena document loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _query : str_,     _database : str_,     _s3\_output\_uri : str_,     _profile\_name : str | None = None_,     _metadata\_columns : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/athena.html#AthenaLoader.__init__)\#     

Initialize Athena document loader.

Parameters:     

  * **query** \(_str_\) – The query to run in Athena.

  * **database** \(_str_\) – Athena database.

  * **s3\_output\_uri** \(_str_\) – Athena output path.

  * **profile\_name** \(_str_ _|__None_\) – Optional. AWS credential profile, if profiles are being used.

  * **metadata\_columns** \(_List_ _\[__str_ _\]__|__None_\) – Optional. Columns written to Document metadata.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/athena.html#AthenaLoader.lazy_load)\#     

A lazy loader for Documents.

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

Examples using AthenaLoader

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [Athena](https://python.langchain.com/docs/integrations/document_loaders/athena/)

__On this page