# MaxComputeLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.max_compute.MaxComputeLoader.html
**Word Count:** 274
**Links Count:** 429
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# MaxComputeLoader\#

_class _langchain\_community.document\_loaders.max\_compute.MaxComputeLoader\(

    _query : str_,     _api\_wrapper : [MaxComputeAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.max_compute.MaxComputeAPIWrapper.html#langchain_community.utilities.max_compute.MaxComputeAPIWrapper "langchain_community.utilities.max_compute.MaxComputeAPIWrapper")_,     _\*_ ,     _page\_content\_columns : Sequence\[str\] | None = None_,     _metadata\_columns : Sequence\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/max_compute.html#MaxComputeLoader)\#     

Load from Alibaba Cloud MaxCompute table.

Initialize Alibaba Cloud MaxCompute document loader.

Parameters:     

  * **query** \(_str_\) – SQL query to execute.

  * **api\_wrapper** \([_MaxComputeAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.max_compute.MaxComputeAPIWrapper.html#langchain_community.utilities.max_compute.MaxComputeAPIWrapper "langchain_community.utilities.max_compute.MaxComputeAPIWrapper")\) – MaxCompute API wrapper.

  * **page\_content\_columns** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – The columns to write into the page\_content of the Document. If unspecified, all columns will be written to page\_content.

  * **metadata\_columns** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – The columns to write into the metadata of the Document. If unspecified, all columns not added to page\_content will be written.

Methods

`__init__`\(query, api\_wrapper, \*\[, ...\]\) | Initialize Alibaba Cloud MaxCompute document loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `from_params`\(query, endpoint, project, \*\[, ...\]\) | Convenience constructor that builds the MaxCompute API wrapper from   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _query : str_,     _api\_wrapper : [MaxComputeAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.max_compute.MaxComputeAPIWrapper.html#langchain_community.utilities.max_compute.MaxComputeAPIWrapper "langchain_community.utilities.max_compute.MaxComputeAPIWrapper")_,     _\*_ ,     _page\_content\_columns : Sequence\[str\] | None = None_,     _metadata\_columns : Sequence\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/max_compute.html#MaxComputeLoader.__init__)\#     

Initialize Alibaba Cloud MaxCompute document loader.

Parameters:     

  * **query** \(_str_\) – SQL query to execute.

  * **api\_wrapper** \([_MaxComputeAPIWrapper_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.max_compute.MaxComputeAPIWrapper.html#langchain_community.utilities.max_compute.MaxComputeAPIWrapper "langchain_community.utilities.max_compute.MaxComputeAPIWrapper")\) – MaxCompute API wrapper.

  * **page\_content\_columns** \(_Sequence_ _\[__str_ _\]__|__None_\) – The columns to write into the page\_content of the Document. If unspecified, all columns will be written to page\_content.

  * **metadata\_columns** \(_Sequence_ _\[__str_ _\]__|__None_\) – The columns to write into the metadata of the Document. If unspecified, all columns not added to page\_content will be written.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_classmethod _from\_params\(

    _query : str_,     _endpoint : str_,     _project : str_,     _\*_ ,     _access\_id : str | None = None_,     _secret\_access\_key : str | None = None_,     _\*\* kwargs: Any_, \) → MaxComputeLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/max_compute.html#MaxComputeLoader.from_params)\#     

Convenience constructor that builds the MaxCompute API wrapper from     

given parameters.

Parameters:     

  * **query** \(_str_\) – SQL query to execute.

  * **endpoint** \(_str_\) – MaxCompute endpoint.

  * **project** \(_str_\) – A project is a basic organizational unit of MaxCompute, which is similar to a database.

  * **access\_id** \(_str_ _|__None_\) – MaxCompute access ID. Should be passed in directly or set as the environment variable MAX\_COMPUTE\_ACCESS\_ID.

  * **secret\_access\_key** \(_str_ _|__None_\) – MaxCompute secret access key. Should be passed in directly or set as the environment variable MAX\_COMPUTE\_SECRET\_ACCESS\_KEY.

  * **kwargs** \(_Any_\)

Return type:     

_MaxComputeLoader_

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/max_compute.html#MaxComputeLoader.lazy_load)\#     

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

Examples using MaxComputeLoader

  * [Alibaba Cloud](https://python.langchain.com/docs/integrations/providers/alibaba_cloud/)

  * [Alibaba Cloud MaxCompute](https://python.langchain.com/docs/integrations/document_loaders/alibaba_cloud_maxcompute/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)