# AzureBlobStorageFileLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.azure_blob_storage_file.AzureBlobStorageFileLoader.html
**Word Count:** 108
**Links Count:** 419
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# AzureBlobStorageFileLoader\#

_class _langchain\_community.document\_loaders.azure\_blob\_storage\_file.AzureBlobStorageFileLoader\(

    _conn\_str : str_,     _container : str_,     _blob\_name : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/azure_blob_storage_file.html#AzureBlobStorageFileLoader)\#     

Load from Azure Blob Storage files.

Initialize with connection string, container and blob name.

Attributes

Methods

`__init__`\(conn\_str, container, blob\_name\) | Initialize with connection string, container and blob name.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **conn\_str** \(_str_\)

  * **container** \(_str_\)

  * **blob\_name** \(_str_\)

\_\_init\_\_\(

    _conn\_str : str_,     _container : str_,     _blob\_name : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/azure_blob_storage_file.html#AzureBlobStorageFileLoader.__init__)\#     

Initialize with connection string, container and blob name.

Parameters:     

  * **conn\_str** \(_str_\)

  * **container** \(_str_\)

  * **blob\_name** \(_str_\)

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/azure_blob_storage_file.html#AzureBlobStorageFileLoader.load)\#     

Load documents.

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

Examples using AzureBlobStorageFileLoader

  * [Azure Blob Storage File](https://python.langchain.com/docs/integrations/document_loaders/azure_blob_storage_file/)

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page