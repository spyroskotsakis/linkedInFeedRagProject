# UnstructuredAPIFileLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.unstructured.UnstructuredAPIFileLoader.html
**Word Count:** 270
**Links Count:** 422
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# UnstructuredAPIFileLoader\#

_class _langchain\_community.document\_loaders.unstructured.UnstructuredAPIFileLoader\(

    _file\_path : str | List\[str\]_,     _\*_ ,     _mode : str = 'single'_,     _url : str = 'https://api.unstructuredapp.io/general/v0/general'_,     _api\_key : str = ''_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/unstructured.html#UnstructuredAPIFileLoader)\#     

Deprecated since version 0.2.8: Use `:class:`~langchain_unstructured.UnstructuredLoader`` instead. It will not be removed until langchain-community==1.0.

Load files using Unstructured API.

By default, the loader makes a call to the hosted Unstructured API. If you are running the unstructured API locally, you can change the API rule by passing in the url parameter when you initialize the loader. The hosted Unstructured API requires an API key. See the links below to learn more about our API offerings and get an API key.

You can run the loader in different modes: “single”, “elements”, and “paged”. The default “single” mode will return a single langchain Document object. If you use “elements” mode, the unstructured library will split the document into elements such as Title and NarrativeText and return those as individual langchain Document objects. In addition to these post-processing modes \(which are specific to the LangChain Loaders\), Unstructured has its own “chunking” parameters for post-processing elements into more useful chunks for uses cases such as Retrieval Augmented Generation \(RAG\). You can pass in additional unstructured kwargs to configure different unstructured settings.

Examples \`\`\`python from langchain\_community.document\_loaders import UnstructuredAPIFileLoader

loader = UnstructuredAPIFileLoader\(     

“example.pdf”, mode=”elements”, strategy=”fast”, api\_key=”MY\_API\_KEY”,

\) docs = loader.load\(\)

References

<https://docs.unstructured.io/api-reference/api-services/sdk> <https://docs.unstructured.io/api-reference/api-services/overview> <https://docs.unstructured.io/open-source/core-functionality/partitioning> <https://docs.unstructured.io/open-source/core-functionality/chunking>

Initialize with file path.

Methods

`__init__`\(file\_path, \*\[, mode, url, api\_key\]\) | Initialize with file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load file.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **file\_path** \(_Union_ _\[__str_ _,__List_ _\[__str_ _\]__\]_\)

  * **mode** \(_str_\)

  * **url** \(_str_\)

  * **api\_key** \(_str_\)

  * **unstructured\_kwargs** \(_Any_\)

\_\_init\_\_\(

    _file\_path : str | List\[str\]_,     _\*_ ,     _mode : str = 'single'_,     _url : str = 'https://api.unstructuredapp.io/general/v0/general'_,     _api\_key : str = ''_,     _\*\* unstructured\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/unstructured.html#UnstructuredAPIFileLoader.__init__)\#     

Initialize with file path.

Parameters:     

  * **file\_path** \(_str_ _|__List_ _\[__str_ _\]_\)

  * **mode** \(_str_\)

  * **url** \(_str_\)

  * **api\_key** \(_str_\)

  * **unstructured\_kwargs** \(_Any_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load file.

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