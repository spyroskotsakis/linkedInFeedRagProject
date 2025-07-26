# HuggingFaceModelLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.hugging_face_model.HuggingFaceModelLoader.html
**Word Count:** 309
**Links Count:** 427
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# HuggingFaceModelLoader\#

_class _langchain\_community.document\_loaders.hugging\_face\_model.HuggingFaceModelLoader\(

    _\*_ ,     _search : str | None = None_,     _author : str | None = None_,     _filter : str | None = None_,     _sort : str | None = None_,     _direction : str | None = None_,     _limit : int | None = 3_,     _full : bool | None = None_,     _config : bool | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/hugging_face_model.html#HuggingFaceModelLoader)\#     

Load model information from Hugging Face Hub, including README content.

This loader interfaces with the Hugging Face Models API to fetch and load model metadata and README files. The API allows you to search and filter models based on specific criteria such as model tags, authors, and more.

API URL: <https://huggingface.co/api/models> DOC URL: <https://huggingface.co/docs/hub/en/api>

Examples               from langchain_community.document_loaders import HuggingFaceModelLoader          # Initialize the loader with search criteria     loader = HuggingFaceModelLoader(search="bert", limit=10)          # Load models     documents = loader.load()          # Iterate through the fetched documents     for doc in documents:         print(doc.page_content)  # README content of the model         print(doc.metadata)      # Metadata of the model     

Initialize the HuggingFaceModelLoader.

Parameters:     

  * **search** \(_str_ _|__None_\) – Filter based on substrings for repos and their usernames.

  * **author** \(_str_ _|__None_\) – Filter models by an author or organization.

  * **filter** \(_str_ _|__None_\) – Filter based on tags.

  * **sort** \(_str_ _|__None_\) – Property to use when sorting.

  * **direction** \(_str_ _|__None_\) – Direction in which to sort.

  * **limit** \(_int_ _|__None_\) – Limit the number of models fetched.

  * **full** \(_bool_ _|__None_\) – Whether to fetch most model data.

  * **config** \(_bool_ _|__None_\) – Whether to also fetch the repo config.

Attributes

`BASE_URL` |    ---|---   `README_BASE_URL` |       Methods

`__init__`\(\*\[, search, author, filter, sort, ...\]\) | Initialize the HuggingFaceModelLoader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `fetch_models`\(\) | Fetch model information from Hugging Face Hub.   `fetch_readme_content`\(model\_id\) | Fetch the README content for a given model.   `lazy_load`\(\) | Load model information lazily, including README content.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _\*_ ,     _search : str | None = None_,     _author : str | None = None_,     _filter : str | None = None_,     _sort : str | None = None_,     _direction : str | None = None_,     _limit : int | None = 3_,     _full : bool | None = None_,     _config : bool | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/hugging_face_model.html#HuggingFaceModelLoader.__init__)\#     

Initialize the HuggingFaceModelLoader.

Parameters:     

  * **search** \(_str_ _|__None_\) – Filter based on substrings for repos and their usernames.

  * **author** \(_str_ _|__None_\) – Filter models by an author or organization.

  * **filter** \(_str_ _|__None_\) – Filter based on tags.

  * **sort** \(_str_ _|__None_\) – Property to use when sorting.

  * **direction** \(_str_ _|__None_\) – Direction in which to sort.

  * **limit** \(_int_ _|__None_\) – Limit the number of models fetched.

  * **full** \(_bool_ _|__None_\) – Whether to fetch most model data.

  * **config** \(_bool_ _|__None_\) – Whether to also fetch the repo config.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

fetch\_models\(\) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/hugging_face_model.html#HuggingFaceModelLoader.fetch_models)\#     

Fetch model information from Hugging Face Hub.

Return type:     

_List_\[dict\]

fetch\_readme\_content\(

    _model\_id : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/hugging_face_model.html#HuggingFaceModelLoader.fetch_readme_content)\#     

Fetch the README content for a given model.

Parameters:     

**model\_id** \(_str_\)

Return type:     

str

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/hugging_face_model.html#HuggingFaceModelLoader.lazy_load)\#     

Load model information lazily, including README content.

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)