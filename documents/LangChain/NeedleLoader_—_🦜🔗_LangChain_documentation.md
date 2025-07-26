# NeedleLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.needle.NeedleLoader.html
**Word Count:** 250
**Links Count:** 422
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# NeedleLoader\#

_class _langchain\_community.document\_loaders.needle.NeedleLoader\(

    _needle\_api\_key : str | None = None_,     _collection\_id : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/needle.html#NeedleLoader)\#     

NeedleLoader is a document loader for managing documents stored in a collection.

Setup:     

Install the needle-python library and set your Needle API key.               pip install needle-python     export NEEDLE_API_KEY="your-api-key"     

Key init args:     

  * needle\_api\_key \(Optional\[str\]\): API key for authenticating with Needle.

  * collection\_id \(str\): Needle collection to load documents from.

Usage:                    from langchain_community.document_loaders.needle import NeedleLoader          loader = NeedleLoader(         needle_api_key="your-api-key",         collection_id="your-collection-id"     )          # Load documents     documents = loader.load()     for doc in documents:         print(doc.metadata)          # Lazy load documents     for doc in loader.lazy_load():         print(doc.metadata)     

Initializes the NeedleLoader with API key and collection ID.

Parameters:     

  * **needle\_api\_key** \(_Optional_ _\[__str_ _\]_\) – API key for authenticating with Needle.

  * **collection\_id** \(_Optional_ _\[__str_ _\]_\) – Identifier for the Needle collection.

Raises:     

  * **ImportError** – If the needle-python library is not installed.

  * **ValueError** – If the collection ID is not provided.

Methods

`__init__`\(\[needle\_api\_key, collection\_id\]\) | Initializes the NeedleLoader with API key and collection ID.   ---|---   `add_files`\(files\) | Adds files to the Needle collection.   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazily loads documents from the Needle collection.   `load`\(\) | Loads all documents from the Needle collection.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _needle\_api\_key : str | None = None_,     _collection\_id : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/needle.html#NeedleLoader.__init__)\#     

Initializes the NeedleLoader with API key and collection ID.

Parameters:     

  * **needle\_api\_key** \(_Optional_ _\[__str_ _\]_\) – API key for authenticating with Needle.

  * **collection\_id** \(_Optional_ _\[__str_ _\]_\) – Identifier for the Needle collection.

Raises:     

  * **ImportError** – If the needle-python library is not installed.

  * **ValueError** – If the collection ID is not provided.

Return type:     

None

add\_files\(

    _files : Dict\[str, str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/needle.html#NeedleLoader.add_files)\#     

Adds files to the Needle collection.

Parameters:     

**files** \(_Dict_ _\[__str_ _,__str_ _\]_\) – Dictionary where keys are file names and values are file URLs.

Raises:     

  * **ImportError** – If the needle-python library is not installed.

  * **ValueError** – If the collection is not properly initialized.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/needle.html#NeedleLoader.lazy_load)\#     

Lazily loads documents from the Needle collection.

Yields:     

_Iterator\[Document\]_ – An iterator over the documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/needle.html#NeedleLoader.load)\#     

Loads all documents from the Needle collection.

Returns:     

A list of documents from the collection.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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