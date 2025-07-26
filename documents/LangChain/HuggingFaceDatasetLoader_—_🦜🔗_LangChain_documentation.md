# HuggingFaceDatasetLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.hugging_face_dataset.HuggingFaceDatasetLoader.html
**Word Count:** 234
**Links Count:** 423
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# HuggingFaceDatasetLoader\#

_class _langchain\_community.document\_loaders.hugging\_face\_dataset.HuggingFaceDatasetLoader\(

    _path : str_,     _page\_content\_column : str = 'text'_,     _name : str | None = None_,     _data\_dir : str | None = None_,     _data\_files : str | Sequence\[str\] | Mapping\[str, str | Sequence\[str\]\] | None = None_,     _cache\_dir : str | None = None_,     _keep\_in\_memory : bool | None = None_,     _save\_infos : bool = False_,     _use\_auth\_token : bool | str | None = None_,     _num\_proc : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/hugging_face_dataset.html#HuggingFaceDatasetLoader)\#     

Load from Hugging Face Hub datasets.

Initialize the HuggingFaceDatasetLoader.

Parameters:     

  * **path** \(_str_\) – Path or name of the dataset.

  * **page\_content\_column** \(_str_\) – Page content column name. Default is “text”.

  * **name** \(_str_ _|__None_\) – Name of the dataset configuration.

  * **data\_dir** \(_str_ _|__None_\) – Data directory of the dataset configuration.

  * **data\_files** \(_str_ _|__Sequence_ _\[__str_ _\]__|__Mapping_ _\[__str_ _,__str_ _|__Sequence_ _\[__str_ _\]__\]__|__None_\) – Path\(s\) to source data file\(s\).

  * **cache\_dir** \(_str_ _|__None_\) – Directory to read/write data.

  * **keep\_in\_memory** \(_bool_ _|__None_\) – Whether to copy the dataset in-memory.

  * **save\_infos** \(_bool_\) – Save the dataset information \(checksums/size/splits/…\). Default is False.

  * **use\_auth\_token** \(_bool_ _|__str_ _|__None_\) – Bearer token for remote files on the Dataset Hub.

  * **num\_proc** \(_int_ _|__None_\) – Number of processes.

Methods

`__init__`\(path\[, page\_content\_column, name, ...\]\) | Initialize the HuggingFaceDatasetLoader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load documents lazily.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `parse_obj`\(page\_content\) |       \_\_init\_\_\(

    _path : str_,     _page\_content\_column : str = 'text'_,     _name : str | None = None_,     _data\_dir : str | None = None_,     _data\_files : str | Sequence\[str\] | Mapping\[str, str | Sequence\[str\]\] | None = None_,     _cache\_dir : str | None = None_,     _keep\_in\_memory : bool | None = None_,     _save\_infos : bool = False_,     _use\_auth\_token : bool | str | None = None_,     _num\_proc : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/hugging_face_dataset.html#HuggingFaceDatasetLoader.__init__)\#     

Initialize the HuggingFaceDatasetLoader.

Parameters:     

  * **path** \(_str_\) – Path or name of the dataset.

  * **page\_content\_column** \(_str_\) – Page content column name. Default is “text”.

  * **name** \(_str_ _|__None_\) – Name of the dataset configuration.

  * **data\_dir** \(_str_ _|__None_\) – Data directory of the dataset configuration.

  * **data\_files** \(_str_ _|__Sequence_ _\[__str_ _\]__|__Mapping_ _\[__str_ _,__str_ _|__Sequence_ _\[__str_ _\]__\]__|__None_\) – Path\(s\) to source data file\(s\).

  * **cache\_dir** \(_str_ _|__None_\) – Directory to read/write data.

  * **keep\_in\_memory** \(_bool_ _|__None_\) – Whether to copy the dataset in-memory.

  * **save\_infos** \(_bool_\) – Save the dataset information \(checksums/size/splits/…\). Default is False.

  * **use\_auth\_token** \(_bool_ _|__str_ _|__None_\) – Bearer token for remote files on the Dataset Hub.

  * **num\_proc** \(_int_ _|__None_\) – Number of processes.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/hugging_face_dataset.html#HuggingFaceDatasetLoader.lazy_load)\#     

Load documents lazily.

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

parse\_obj\(

    _page\_content : str | object_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/hugging_face_dataset.html#HuggingFaceDatasetLoader.parse_obj)\#     

Parameters:     

**page\_content** \(_str_ _|__object_\)

Return type:     

str

Examples using HuggingFaceDatasetLoader

  * [Hugging Face](https://python.langchain.com/docs/integrations/providers/huggingface/)

  * [HuggingFace dataset](https://python.langchain.com/docs/integrations/document_loaders/hugging_face_dataset/)

__On this page