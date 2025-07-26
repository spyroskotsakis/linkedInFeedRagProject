# NucliaLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.nuclia.NucliaLoader.html
**Word Count:** 87
**Links Count:** 422
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# NucliaLoader\#

_class _langchain\_community.document\_loaders.nuclia.NucliaLoader\(

    _path : str_,     _nuclia\_tool : [NucliaUnderstandingAPI](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI.html#langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI "langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/nuclia.html#NucliaLoader)\#     

Load from any file type using Nuclia Understanding API.

Methods

`__init__`\(path, nuclia\_tool\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **path** \(_str_\)

  * **nuclia\_tool** \([_NucliaUnderstandingAPI_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI.html#langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI "langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI")\)

\_\_init\_\_\(

    _path : str_,     _nuclia\_tool : [NucliaUnderstandingAPI](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI.html#langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI "langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI")_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/nuclia.html#NucliaLoader.__init__)\#     

Parameters:     

  * **path** \(_str_\)

  * **nuclia\_tool** \([_NucliaUnderstandingAPI_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI.html#langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI "langchain_community.tools.nuclia.tool.NucliaUnderstandingAPI")\)

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/nuclia.html#NucliaLoader.load)\#     

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

Examples using NucliaLoader

  * [Nuclia](https://python.langchain.com/docs/integrations/document_loaders/nuclia/)

__On this page