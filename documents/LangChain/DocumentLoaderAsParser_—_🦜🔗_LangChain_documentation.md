# DocumentLoaderAsParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.documentloader_adapter.DocumentLoaderAsParser.html
**Word Count:** 264
**Links Count:** 414
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# DocumentLoaderAsParser\#

_class _langchain\_community.document\_loaders.parsers.documentloader\_adapter.DocumentLoaderAsParser\(

    _document\_loader\_class : Type\[[BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader")\]_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/documentloader_adapter.html#DocumentLoaderAsParser)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

A wrapper class that adapts a document loader to function as a parser.

This class is a work-around that adapts a document loader to function as a parser. It is recommended to use a proper parser, if available.

Requires the document loader to accept a file\_path parameter.

Initializes the DocumentLoaderAsParser with a specific document loader class and additional arguments.

Parameters:     

  * **document\_loader\_class** \(_Type_ _\[_[_BaseLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader") _\]_\) – The document loader class to adapt

  * **parser.** \(_as a_\)

  * **\*\*kwargs** – Additional arguments passed to the document loader’s constructor.

Raises:     

**TypeError** – If the specified document loader does not accept a file\_path parameter, an exception is raised, as only loaders with this parameter can be adapted.

Example

\`\`\` from langchain\_community.document\_loaders.excel import UnstructuredExcelLoader

\# Initialize parser adapter with a document loader excel\_parser = DocumentLoaderAsParser\(UnstructuredExcelLoader, mode=”elements”\) \`\`\`

Attributes

Methods

`__init__`\(document\_loader\_class, \*\*kwargs\) | Initializes the DocumentLoaderAsParser with a specific document loader class and additional arguments.   ---|---   `lazy_parse`\(blob\) | Use underlying DocumentLoader to lazily parse the blob.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _document\_loader\_class : Type\[[BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader")\]_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/documentloader_adapter.html#DocumentLoaderAsParser.__init__)\#     

Initializes the DocumentLoaderAsParser with a specific document loader class and additional arguments.

Parameters:     

  * **document\_loader\_class** \(_Type_ _\[_[_BaseLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader") _\]_\) – The document loader class to adapt

  * **parser.** \(_as a_\)

  * **\*\*kwargs** – Additional arguments passed to the document loader’s constructor.

Raises:     

**TypeError** – If the specified document loader does not accept a file\_path parameter, an exception is raised, as only loaders with this parameter can be adapted.

Return type:     

None

Example

\`\`\` from langchain\_community.document\_loaders.excel import UnstructuredExcelLoader

\# Initialize parser adapter with a document loader excel\_parser = DocumentLoaderAsParser\(UnstructuredExcelLoader, mode=”elements”\) \`\`\`

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/documentloader_adapter.html#DocumentLoaderAsParser.lazy_parse)\#     

Use underlying DocumentLoader to lazily parse the blob.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\(_blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Eagerly parse the blob into a document or documents.

This is a convenience method for interactive development environment.

Production applications should favor the lazy\_parse method instead.

Subclasses should generally not over-ride this parse method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

List of documents

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page