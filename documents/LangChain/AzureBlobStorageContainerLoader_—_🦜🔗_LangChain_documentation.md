# AzureBlobStorageContainerLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.azure_blob_storage_container.AzureBlobStorageContainerLoader.html
**Word Count:** 108
**Links Count:** 419
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# AzureBlobStorageContainerLoader\#

_class _langchain\_community.document\_loaders.azure\_blob\_storage\_container.AzureBlobStorageContainerLoader\(

    _conn\_str : str_,     _container : str_,     _prefix : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/azure_blob_storage_container.html#AzureBlobStorageContainerLoader)\#     

Load from Azure Blob Storage container.

Initialize with connection string, container and blob prefix.

Attributes

Methods

`__init__`\(conn\_str, container\[, prefix\]\) | Initialize with connection string, container and blob prefix.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **conn\_str** \(_str_\)

  * **container** \(_str_\)

  * **prefix** \(_str_\)

\_\_init\_\_\(

    _conn\_str : str_,     _container : str_,     _prefix : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/azure_blob_storage_container.html#AzureBlobStorageContainerLoader.__init__)\#     

Initialize with connection string, container and blob prefix.

Parameters:     

  * **conn\_str** \(_str_\)

  * **container** \(_str_\)

  * **prefix** \(_str_\)

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/azure_blob_storage_container.html#AzureBlobStorageContainerLoader.load)\#     

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

Examples using AzureBlobStorageContainerLoader

  * [Azure Blob Storage Container](https://python.langchain.com/docs/integrations/document_loaders/azure_blob_storage_container/)

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page