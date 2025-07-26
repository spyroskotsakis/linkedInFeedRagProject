# TensorflowDatasets — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.tensorflow_datasets.TensorflowDatasets.html
**Word Count:** 155
**Links Count:** 278
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# TensorflowDatasets\#

_class _langchain\_community.utilities.tensorflow\_datasets.TensorflowDatasets[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/tensorflow_datasets.html#TensorflowDatasets)\#     

Bases: `BaseModel`

Access to the TensorFlow Datasets.

The Current implementation can work only with datasets that fit in a memory.

TensorFlow Datasets is a collection of datasets ready to use, with TensorFlow or other Python ML frameworks, such as Jax. All datasets are exposed as tf.data.Datasets. To get started see the Guide: <https://www.tensorflow.org/datasets/overview> and the list of datasets: <https://www.tensorflow.org/datasets/catalog/>

> overview\#all\_datasets

You have to provide the sample\_to\_document\_function: a function that     

a sample from the dataset-specific format to the Document.

dataset\_name\#     

the name of the dataset to load

split\_name\#     

the name of the split to load. Defaults to “train”.

load\_max\_docs\#     

a limit to the number of loaded documents. Defaults to 100.

sample\_to\_document\_function\#     

a function that converts a dataset sample to a Document

Example               from langchain_community.utilities import TensorflowDatasets          def mlqaen_example_to_document(example: dict) -> Document:         return Document(             page_content=decode_to_str(example["context"]),             metadata={                 "id": decode_to_str(example["id"]),                 "title": decode_to_str(example["title"]),                 "question": decode_to_str(example["question"]),                 "answer": decode_to_str(example["answers"]["text"][0]),             },         )          tsds_client = TensorflowDatasets(             dataset_name="mlqa/en",             split_name="train",             load_max_docs=MAX_DOCS,             sample_to_document_function=mlqaen_example_to_document,         )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _dataset\_name _: str_ _ = ''_\#     

_param _load\_max\_docs _: int_ _ = 100_\#     

_param _sample\_to\_document\_function _: Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\] | None_ _ = None_\#     

_param _split\_name _: str_ _ = 'train'_\#     

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/tensorflow_datasets.html#TensorflowDatasets.lazy_load)\#     

Download a selected dataset lazily.

Returns: an iterator of Documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/tensorflow_datasets.html#TensorflowDatasets.load)\#     

Download a selected dataset.

Returns: a list of Documents.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page