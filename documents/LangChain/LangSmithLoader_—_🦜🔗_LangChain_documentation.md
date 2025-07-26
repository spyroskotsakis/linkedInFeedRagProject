# LangSmithLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.langsmith.LangSmithLoader.html
**Word Count:** 543
**Links Count:** 135
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# LangSmithLoader\#

_class _langchain\_core.document\_loaders.langsmith.LangSmithLoader\(

    _\*_ ,     _dataset\_id : UUID | str | None = None_,     _dataset\_name : str | None = None_,     _example\_ids : Sequence\[UUID | str\] | None = None_,     _as\_of : datetime | str | None = None_,     _splits : Sequence\[str\] | None = None_,     _inline\_s3\_urls : bool = True_,     _offset : int = 0_,     _limit : int | None = None_,     _metadata : dict | None = None_,     _filter : str | None = None_,     _content\_key : str = ''_,     _format\_content : Callable\[\[...\], str\] | None = None_,     _client : Client | None = None_,     _\*\* client\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/document_loaders/langsmith.html#LangSmithLoader)\#     

Load LangSmith Dataset examples as Documents.

Loads the example inputs as the Document page content and places the entire example into the Document metadata. This allows you to easily create few-shot example retrievers from the loaded documents.

Lazy load               from langchain_core.document_loaders import LangSmithLoader          loader = LangSmithLoader(dataset_id="...", limit=100)     docs = []     for doc in loader.lazy_load():         docs.append(doc)                    # -> [Document("...", metadata={"inputs": {...}, "outputs": {...}, ...}), ...]     

Added in version 0.2.34.

Create a LangSmith loader.

Parameters:     

  * **dataset\_id** \(_UUID_ _|__str_ _|__None_\) – The ID of the dataset to filter by. Defaults to None.

  * **dataset\_name** \(_str_ _|__None_\) – The name of the dataset to filter by. Defaults to None.

  * **content\_key** \(_str_\) – The inputs key to set as Document page content. `"."` characters are interpreted as nested keys. E.g. `content_key="first.second"` will result in `Document(page_content=format_content(example.inputs["first"]["second"]))`

  * **format\_content** \(_Callable_ _\[__\[__...__\]__,__str_ _\]__|__None_\) – Function for converting the content extracted from the example inputs into a string. Defaults to JSON-encoding the contents.

  * **example\_ids** \(_Sequence_ _\[__UUID_ _|__str_ _\]__|__None_\) – The IDs of the examples to filter by. Defaults to None.

  * **as\_of** \(_datetime_ _|__str_ _|__None_\) – The dataset version tag OR timestamp to retrieve the examples as of. Response examples will only be those that were present at the time of the tagged \(or timestamped\) version.

  * **splits** \(_Sequence_ _\[__str_ _\]__|__None_\) – A list of dataset splits, which are divisions of your dataset such as ‘train’, ‘test’, or ‘validation’. Returns examples only from the specified splits.

  * **inline\_s3\_urls** \(_bool_\) – Whether to inline S3 URLs. Defaults to True.

  * **offset** \(_int_\) – The offset to start from. Defaults to 0.

  * **limit** \(_int_ _|__None_\) – The maximum number of examples to return.

  * **metadata** \(_dict_ _|__None_\) – Metadata to filter by. Defaults to None.

  * **filter** \(_str_ _|__None_\) – A structured filter string to apply to the examples.

  * **client** \(_Client_ _|__None_\) – LangSmith Client. If not provided will be initialized from below args.

  * **client\_kwargs** \(_Any_\) – Keyword args to pass to LangSmith client init. Should only be specified if `client` isn’t.

Methods

`__init__`\(\*\[, dataset\_id, dataset\_name, ...\]\) | Create a LangSmith loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _\*_ ,     _dataset\_id : UUID | str | None = None_,     _dataset\_name : str | None = None_,     _example\_ids : Sequence\[UUID | str\] | None = None_,     _as\_of : datetime | str | None = None_,     _splits : Sequence\[str\] | None = None_,     _inline\_s3\_urls : bool = True_,     _offset : int = 0_,     _limit : int | None = None_,     _metadata : dict | None = None_,     _filter : str | None = None_,     _content\_key : str = ''_,     _format\_content : Callable\[\[...\], str\] | None = None_,     _client : Client | None = None_,     _\*\* client\_kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/document_loaders/langsmith.html#LangSmithLoader.__init__)\#     

Create a LangSmith loader.

Parameters:     

  * **dataset\_id** \(_UUID_ _|__str_ _|__None_\) – The ID of the dataset to filter by. Defaults to None.

  * **dataset\_name** \(_str_ _|__None_\) – The name of the dataset to filter by. Defaults to None.

  * **content\_key** \(_str_\) – The inputs key to set as Document page content. `"."` characters are interpreted as nested keys. E.g. `content_key="first.second"` will result in `Document(page_content=format_content(example.inputs["first"]["second"]))`

  * **format\_content** \(_Callable_ _\[__\[__...__\]__,__str_ _\]__|__None_\) – Function for converting the content extracted from the example inputs into a string. Defaults to JSON-encoding the contents.

  * **example\_ids** \(_Sequence_ _\[__UUID_ _|__str_ _\]__|__None_\) – The IDs of the examples to filter by. Defaults to None.

  * **as\_of** \(_datetime_ _|__str_ _|__None_\) – The dataset version tag OR timestamp to retrieve the examples as of. Response examples will only be those that were present at the time of the tagged \(or timestamped\) version.

  * **splits** \(_Sequence_ _\[__str_ _\]__|__None_\) – A list of dataset splits, which are divisions of your dataset such as ‘train’, ‘test’, or ‘validation’. Returns examples only from the specified splits.

  * **inline\_s3\_urls** \(_bool_\) – Whether to inline S3 URLs. Defaults to True.

  * **offset** \(_int_\) – The offset to start from. Defaults to 0.

  * **limit** \(_int_ _|__None_\) – The maximum number of examples to return.

  * **metadata** \(_dict_ _|__None_\) – Metadata to filter by. Defaults to None.

  * **filter** \(_str_ _|__None_\) – A structured filter string to apply to the examples.

  * **client** \(_Client_ _|__None_\) – LangSmith Client. If not provided will be initialized from below args.

  * **client\_kwargs** \(_Any_\) – Keyword args to pass to LangSmith client init. Should only be specified if `client` isn’t.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/document_loaders/langsmith.html#LangSmithLoader.lazy_load)\#     

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

Examples using LangSmithLoader

  * [LangSmithLoader](https://python.langchain.com/docs/integrations/document_loaders/langsmith/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)