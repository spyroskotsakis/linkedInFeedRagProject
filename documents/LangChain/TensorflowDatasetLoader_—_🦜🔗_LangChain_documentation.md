# TensorflowDatasetLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.tensorflow_datasets.TensorflowDatasetLoader.html
**Word Count:** 205
**Links Count:** 430
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# TensorflowDatasetLoader\#

_class _langchain\_community.document\_loaders.tensorflow\_datasets.TensorflowDatasetLoader\(

    _dataset\_name : str_,     _split\_name : str_,     _load\_max\_docs : int | None = 100_,     _sample\_to\_document\_function : Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/tensorflow_datasets.html#TensorflowDatasetLoader)\#     

Load from TensorFlow Dataset.

dataset\_name\#     

the name of the dataset to load

split\_name\#     

the name of the split to load.

load\_max\_docs\#     

a limit to the number of loaded documents. Defaults to 100.

sample\_to\_document\_function\#     

a function that converts a dataset sample into a Document

Example               from langchain_community.document_loaders import TensorflowDatasetLoader          def mlqaen_example_to_document(example: dict) -> Document:         return Document(             page_content=decode_to_str(example["context"]),             metadata={                 "id": decode_to_str(example["id"]),                 "title": decode_to_str(example["title"]),                 "question": decode_to_str(example["question"]),                 "answer": decode_to_str(example["answers"]["text"][0]),             },         )          tsds_client = TensorflowDatasetLoader(             dataset_name="mlqa/en",             split_name="test",             load_max_docs=100,             sample_to_document_function=mlqaen_example_to_document,         )     

Initialize the TensorflowDatasetLoader.

Parameters:     

  * **dataset\_name** \(_str_\) – the name of the dataset to load

  * **split\_name** \(_str_\) – the name of the split to load.

  * **load\_max\_docs** \(_int_ _|__None_\) – a limit to the number of loaded documents. Defaults to 100.

  * **sample\_to\_document\_function** \(_Callable_ _\[__\[__Dict_ _\]__,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__|__None_\) – a function that converts a dataset sample into a Document.

Attributes

Methods

`__init__`\(dataset\_name, split\_name\[, ...\]\) | Initialize the TensorflowDatasetLoader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _dataset\_name : str_,     _split\_name : str_,     _load\_max\_docs : int | None = 100_,     _sample\_to\_document\_function : Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/tensorflow_datasets.html#TensorflowDatasetLoader.__init__)\#     

Initialize the TensorflowDatasetLoader.

Parameters:     

  * **dataset\_name** \(_str_\) – the name of the dataset to load

  * **split\_name** \(_str_\) – the name of the split to load.

  * **load\_max\_docs** \(_int_ _|__None_\) – a limit to the number of loaded documents. Defaults to 100.

  * **sample\_to\_document\_function** \(_Callable_ _\[__\[__Dict_ _\]__,_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__|__None_\) – a function that converts a dataset sample into a Document.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/tensorflow_datasets.html#TensorflowDatasetLoader.lazy_load)\#     

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

Examples using TensorflowDatasetLoader

  * [TensorFlow Datasets](https://python.langchain.com/docs/integrations/document_loaders/tensorflow_datasets/)

__On this page