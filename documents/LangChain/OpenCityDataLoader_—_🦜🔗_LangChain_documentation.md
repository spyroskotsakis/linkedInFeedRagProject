# OpenCityDataLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.open_city_data.OpenCityDataLoader.html
**Word Count:** 149
**Links Count:** 421
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# OpenCityDataLoader\#

_class _langchain\_community.document\_loaders.open\_city\_data.OpenCityDataLoader\(

    _city\_id : str_,     _dataset\_id : str_,     _limit : int_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/open_city_data.html#OpenCityDataLoader)\#     

Load from Open City.

Initialize with dataset\_id. Example: <https://dev.socrata.com/foundry/data.sfgov.org/vw6y-z8j6> e.g., city\_id = data.sfgov.org e.g., dataset\_id = vw6y-z8j6

Parameters:     

  * **city\_id** \(_str_\) – The Open City city identifier.

  * **dataset\_id** \(_str_\) – The Open City dataset identifier.

  * **limit** \(_int_\) – The maximum number of documents to load.

Methods

`__init__`\(city\_id, dataset\_id, limit\) | Initialize with dataset\_id.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load records.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _city\_id : str_,     _dataset\_id : str_,     _limit : int_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/open_city_data.html#OpenCityDataLoader.__init__)\#     

Initialize with dataset\_id. Example: <https://dev.socrata.com/foundry/data.sfgov.org/vw6y-z8j6> e.g., city\_id = data.sfgov.org e.g., dataset\_id = vw6y-z8j6

Parameters:     

  * **city\_id** \(_str_\) – The Open City city identifier.

  * **dataset\_id** \(_str_\) – The Open City dataset identifier.

  * **limit** \(_int_\) – The maximum number of documents to load.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/open_city_data.html#OpenCityDataLoader.lazy_load)\#     

Lazy load records.

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

Examples using OpenCityDataLoader

  * [Geopandas](https://python.langchain.com/docs/integrations/document_loaders/geopandas/)

  * [Open City Data](https://python.langchain.com/docs/integrations/document_loaders/open_city_data/)

__On this page