# VectorstoreIndexCreator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorstoreIndexCreator.html
**Word Count:** 119
**Links Count:** 131
**Scraped:** 2025-07-21 07:50:02
**Status:** completed

---

# VectorstoreIndexCreator\#

_class _langchain.indexes.vectorstore.VectorstoreIndexCreator[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/indexes/vectorstore.html#VectorstoreIndexCreator)\#     

Bases: `BaseModel`

Logic for creating indexes.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _embedding _: [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_ _\[Required\]_\#     

_param _text\_splitter _: [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter")_ _\[Optional\]_\#     

_param _vectorstore\_cls _: type\[[VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\]__\[Optional\]_\#     

_param _vectorstore\_kwargs _: dict_ _\[Optional\]_\#     

_async _afrom\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → [VectorStoreIndexWrapper](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html#langchain.indexes.vectorstore.VectorStoreIndexWrapper "langchain.indexes.vectorstore.VectorStoreIndexWrapper")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/indexes/vectorstore.html#VectorstoreIndexCreator.afrom_documents)\#     

Asynchronously create a vectorstore index from a list of documents.

Parameters:     

**documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A list of Document objects.

Returns:     

A VectorStoreIndexWrapper containing the constructed vectorstore.

Return type:     

[_VectorStoreIndexWrapper_](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html#langchain.indexes.vectorstore.VectorStoreIndexWrapper "langchain.indexes.vectorstore.VectorStoreIndexWrapper")

_async _afrom\_loaders\(

    _loaders : list\[[BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader")\]_, \) → [VectorStoreIndexWrapper](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html#langchain.indexes.vectorstore.VectorStoreIndexWrapper "langchain.indexes.vectorstore.VectorStoreIndexWrapper")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/indexes/vectorstore.html#VectorstoreIndexCreator.afrom_loaders)\#     

Asynchronously create a vectorstore index from a list of loaders.

Parameters:     

**loaders** \(_list_ _\[_[_BaseLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader") _\]_\) – A list of BaseLoader instances to load documents.

Returns:     

A VectorStoreIndexWrapper containing the constructed vectorstore.

Return type:     

[_VectorStoreIndexWrapper_](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html#langchain.indexes.vectorstore.VectorStoreIndexWrapper "langchain.indexes.vectorstore.VectorStoreIndexWrapper")

from\_documents\(

    _documents : list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → [VectorStoreIndexWrapper](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html#langchain.indexes.vectorstore.VectorStoreIndexWrapper "langchain.indexes.vectorstore.VectorStoreIndexWrapper")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/indexes/vectorstore.html#VectorstoreIndexCreator.from_documents)\#     

Create a vectorstore index from a list of documents.

Parameters:     

**documents** \(_list_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A list of Document objects.

Returns:     

A VectorStoreIndexWrapper containing the constructed vectorstore.

Return type:     

[_VectorStoreIndexWrapper_](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html#langchain.indexes.vectorstore.VectorStoreIndexWrapper "langchain.indexes.vectorstore.VectorStoreIndexWrapper")

from\_loaders\(

    _loaders : list\[[BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader")\]_, \) → [VectorStoreIndexWrapper](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html#langchain.indexes.vectorstore.VectorStoreIndexWrapper "langchain.indexes.vectorstore.VectorStoreIndexWrapper")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/indexes/vectorstore.html#VectorstoreIndexCreator.from_loaders)\#     

Create a vectorstore index from a list of loaders.

Parameters:     

**loaders** \(_list_ _\[_[_BaseLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader") _\]_\) – A list of BaseLoader instances to load documents.

Returns:     

A VectorStoreIndexWrapper containing the constructed vectorstore.

Return type:     

[_VectorStoreIndexWrapper_](https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html#langchain.indexes.vectorstore.VectorStoreIndexWrapper "langchain.indexes.vectorstore.VectorStoreIndexWrapper")

Examples using VectorstoreIndexCreator

  * [Apify Dataset](https://python.langchain.com/docs/integrations/document_loaders/apify_dataset/)

  * [Figma](https://python.langchain.com/docs/integrations/document_loaders/figma/)

  * [HuggingFace dataset](https://python.langchain.com/docs/integrations/document_loaders/hugging_face_dataset/)

  * [Iugu](https://python.langchain.com/docs/integrations/document_loaders/iugu/)

  * [Modern Treasury](https://python.langchain.com/docs/integrations/document_loaders/modern_treasury/)

  * [Spreedly](https://python.langchain.com/docs/integrations/document_loaders/spreedly/)

  * [Stripe](https://python.langchain.com/docs/integrations/document_loaders/stripe/)

__On this page