# GithubFileLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.github.GithubFileLoader.html
**Word Count:** 109
**Links Count:** 429
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# GithubFileLoader\#

_class _langchain\_community.document\_loaders.github.GithubFileLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/github.html#GithubFileLoader)\#     

Bases: [`BaseGitHubLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.github.BaseGitHubLoader.html#langchain_community.document_loaders.github.BaseGitHubLoader "langchain_community.document_loaders.github.BaseGitHubLoader"), `ABC`

Load GitHub File

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _access\_token _: str_ _\[Required\]_\#     

Personal access token - see [settings/tokens](https://github.com/settings/tokens?type=beta)

_param _branch _: str_ _ = 'main'_\#     

_param _file\_filter _: Callable\[\[str\], bool\] | None_ _\[Required\]_\#     

_param _github\_api\_url _: str_ _ = 'https://api.github.com'_\#     

URL of GitHub API

_param _repo _: str_ _\[Required\]_\#     

Name of repository

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

get\_file\_content\_by\_path\(_path : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/github.html#GithubFileLoader.get_file_content_by_path)\#     

Parameters:     

**path** \(_str_\)

Return type:     

str

get\_file\_paths\(\) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/github.html#GithubFileLoader.get_file_paths)\#     

Return type:     

_List_\[_Dict_\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/github.html#GithubFileLoader.lazy_load)\#     

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

_property _headers _: Dict\[str, str\]_\#     

Examples using GithubFileLoader

  * [GitHub](https://python.langchain.com/docs/integrations/document_loaders/github/)

__On this page