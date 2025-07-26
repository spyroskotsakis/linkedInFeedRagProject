# ApifyDatasetLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader.html
**Word Count:** 178
**Links Count:** 420
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# ApifyDatasetLoader\#

_class _langchain\_community.document\_loaders.apify\_dataset.ApifyDatasetLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/apify_dataset.html#ApifyDatasetLoader)\#     

Bases: [`BaseLoader`](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader"), `BaseModel`

Deprecated since version 0.3.18: This class is deprecated and will be removed in a future version. You can swap to using the ApifyDatasetLoader implementation in langchain\_apify package. See <[apify/langchain-apify](https://github.com/apify/langchain-apify)> Use `:class:`~langchain_apify.ApifyDatasetLoader`` instead.

Load datasets from Apify web scraping, crawling, and data extraction platform.

For details, see <https://docs.apify.com/platform/integrations/langchain>

Example               from langchain_community.document_loaders import ApifyDatasetLoader     from langchain_core.documents import Document          loader = ApifyDatasetLoader(         dataset_id="YOUR-DATASET-ID",         dataset_mapping_function=lambda dataset_item: Document(             page_content=dataset_item["text"], metadata={"source": dataset_item["url"]}         ),     )     documents = loader.load()     

Initialize the loader with an Apify dataset ID and a mapping function.

Parameters:     

  * **dataset\_id** \(_str_\) – The ID of the dataset on the Apify platform.

  * **dataset\_mapping\_function** \(_Callable_\) – A function that takes a single dictionary \(an Apify dataset item\) and converts it to an instance of the Document class.

_param _apify\_client _: Any_ _\[Required\]_\#     

An instance of the ApifyClient class from the apify-client Python package.

_param _dataset\_id _: str_ _\[Required\]_\#     

The ID of the dataset on the Apify platform.

_param _dataset\_mapping\_function _: Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]__\[Required\]_\#     

A custom function that takes a single dictionary \(an Apify dataset item\) and converts it to an instance of the Document class.

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/apify_dataset.html#ApifyDatasetLoader.load)\#     

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

Examples using ApifyDatasetLoader

  * [Apify](https://python.langchain.com/docs/integrations/providers/apify/)

  * [Apify Dataset](https://python.langchain.com/docs/integrations/document_loaders/apify_dataset/)

__On this page