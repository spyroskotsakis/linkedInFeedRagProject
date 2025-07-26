# index — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.api.index.html
**Word Count:** 645
**Links Count:** 124
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# index\#

langchain\_core.indexing.api.index\(

    _docs\_source : [BaseLoader](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader") | Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _record\_manager : [RecordManager](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.RecordManager.html#langchain_core.indexing.base.RecordManager "langchain_core.indexing.base.RecordManager")_,     _vector\_store : [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore") | [DocumentIndex](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.DocumentIndex.html#langchain_core.indexing.base.DocumentIndex "langchain_core.indexing.base.DocumentIndex")_,     _\*_ ,     _batch\_size : int = 100_,     _cleanup : Literal\['incremental', 'full', 'scoped\_full'\] | None = None_,     _source\_id\_key : str | Callable\[\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\], str\] | None = None_,     _cleanup\_batch\_size : int = 1000_,     _force\_update : bool = False_,     _key\_encoder : Literal\['sha1', 'sha256', 'sha512', 'blake2b'\] | Callable\[\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\], str\] = 'sha1'_,     _upsert\_kwargs : dict\[str, Any\] | None = None_, \) → [IndexingResult](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.api.IndexingResult.html#langchain_core.indexing.api.IndexingResult "langchain_core.indexing.api.IndexingResult")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/indexing/api.html#index)\#     

Index data from the loader into the vector store.

Indexing functionality uses a manager to keep track of which documents are in the vector store.

This allows us to keep track of which documents were updated, and which documents were deleted, which documents should be skipped.

For the time being, documents are indexed using their hashes, and users     

are not able to specify the uid of the document.

Important

  * In full mode, the loader should be returning the entire dataset, and not just a subset of the dataset. Otherwise, the auto\_cleanup will remove documents that it is not supposed to.

  * In incremental mode, if documents associated with a particular source id appear across different batches, the indexing API will do some redundant work. This will still result in the correct end state of the index, but will unfortunately not be 100% efficient. For example, if a given document is split into 15 chunks, and we index them using a batch size of 5, we’ll have 3 batches all with the same source id. In general, to avoid doing too much redundant work select as big a batch size as possible.

>   * The scoped\_full mode is suitable if determining an appropriate batch size is challenging or if your data loader cannot return the entire dataset at once. This mode keeps track of source IDs in memory, which should be fine for most use cases. If your dataset is large \(10M+ docs\), you will likely need to parallelize the indexing process regardless. >  > 

Parameters:     

  * **docs\_source** \([_BaseLoader_](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader") _|__Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – Data loader or iterable of documents to index.

  * **record\_manager** \([_RecordManager_](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.RecordManager.html#langchain_core.indexing.base.RecordManager "langchain_core.indexing.base.RecordManager")\) – Timestamped set to keep track of which documents were updated.

  * **vector\_store** \([_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore") _|_[_DocumentIndex_](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.base.DocumentIndex.html#langchain_core.indexing.base.DocumentIndex "langchain_core.indexing.base.DocumentIndex")\) – VectorStore or DocumentIndex to index the documents into.

  * **batch\_size** \(_int_\) – Batch size to use when indexing. Default is 100.

  * **cleanup** \(_Literal_ _\[__'incremental'__,__'full'__,__'scoped\_full'__\]__|__None_\) – 

How to handle clean up of documents. Default is None. \- incremental: Cleans up all documents that haven’t been updated AND

> that are associated with source ids that were seen during indexing. Clean up is done continuously during indexing helping to minimize the probability of users seeing duplicated content.

    * full: Delete all documents that have not been returned by the loader     

during this run of indexing. Clean up runs after all documents have been indexed. This means that users may see duplicated content during indexing.

    * scoped\_full: Similar to Full, but only deletes all documents     

that haven’t been updated AND that are associated with source ids that were seen during indexing.

    * None: Do not delete any documents.

  * **source\_id\_key** \(_str_ _|__Callable_ _\[__\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__,__str_ _\]__|__None_\) – Optional key that helps identify the original source of the document. Default is None.

  * **cleanup\_batch\_size** \(_int_\) – Batch size to use when cleaning up documents. Default is 1\_000.

  * **force\_update** \(_bool_\) – Force update documents even if they are present in the record manager. Useful if you are re-indexing with updated embeddings. Default is False.

  * **key\_encoder** \(_Literal_ _\[__'sha1'__,__'sha256'__,__'sha512'__,__'blake2b'__\]__|__~typing.Callable_ _\[__\[__~langchain\_core.documents.base.Document_ _\]__,__str_ _\]_\) – 

Hashing algorithm to use for hashing the document content and metadata. Default is “sha1”. Other options include “blake2b”, “sha256”, and “sha512”.

Added in version 0.3.66.

  * **key\_encoder** – 

Hashing algorithm to use for hashing the document. If not provided, a default encoder using SHA-1 will be used. SHA-1 is not collision-resistant, and a motivated attacker could craft two different texts that hash to the same cache key.

New applications should use one of the alternative encoders or provide a custom and strong key encoder function to avoid this risk.

When changing the key encoder, you must change the index as well to avoid duplicated documents in the cache.

  * **upsert\_kwargs** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – 

Additional keyword arguments to pass to the add\_documents     

method of the VectorStore or the upsert method of the DocumentIndex. For example, you can use this to specify a custom vector\_field: upsert\_kwargs=\{“vector\_field”: “embedding”\}

Added in version 0.3.10.

Returns:     

Indexing result which contains information about how many documents were added, updated, deleted, or skipped.

Raises:     

  * **ValueError** – If cleanup mode is not one of ‘incremental’, ‘full’ or None

  * **ValueError** – If cleanup mode is incremental and source\_id\_key is None.

  * **ValueError** – If vectorstore does not have “delete” and “add\_documents” required methods.

  * **ValueError** – If source\_id\_key is not None, but is not a string or callable.

Return type:     

[_IndexingResult_](https://python.langchain.com/api_reference/core/indexing/langchain_core.indexing.api.IndexingResult.html#langchain_core.indexing.api.IndexingResult "langchain_core.indexing.api.IndexingResult")

Examples using index

  * [How to use the LangChain indexing API](https://python.langchain.com/docs/how_to/indexing/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)