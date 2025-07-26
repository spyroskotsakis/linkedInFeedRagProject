# GitLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.git.GitLoader.html
**Word Count:** 232
**Links Count:** 418
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# GitLoader\#

_class _langchain\_community.document\_loaders.git.GitLoader\(

    _repo\_path : str_,     _clone\_url : str | None = None_,     _branch : str | None = 'main'_,     _file\_filter : Callable\[\[str\], bool\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/git.html#GitLoader)\#     

Load Git repository files.

The Repository can be local on disk available at repo\_path, or remote at clone\_url that will be cloned to repo\_path. Currently, supports only text files.

Each document represents one file in the repository. The path points to the local Git repository, and the branch specifies the branch to load files from. By default, it loads from the main branch.

Parameters:     

  * **repo\_path** \(_str_\) – The path to the Git repository.

  * **clone\_url** \(_str_ _|__None_\) – Optional. The URL to clone the repository from.

  * **branch** \(_str_ _|__None_\) – Optional. The branch to load files from. Defaults to main.

  * **file\_filter** \(_Callable_ _\[__\[__str_ _\]__,__bool_ _\]__|__None_\) – Optional. A function that takes a file path and returns a boolean indicating whether to load the file. Defaults to None.

Methods

`__init__`\(repo\_path\[, clone\_url, branch, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _repo\_path : str_,     _clone\_url : str | None = None_,     _branch : str | None = 'main'_,     _file\_filter : Callable\[\[str\], bool\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/git.html#GitLoader.__init__)\#     

Parameters:     

  * **repo\_path** \(_str_\) – The path to the Git repository.

  * **clone\_url** \(_str_ _|__None_\) – Optional. The URL to clone the repository from.

  * **branch** \(_str_ _|__None_\) – Optional. The branch to load files from. Defaults to main.

  * **file\_filter** \(_Callable_ _\[__\[__str_ _\]__,__bool_ _\]__|__None_\) – Optional. A function that takes a file path and returns a boolean indicating whether to load the file. Defaults to None.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/git.html#GitLoader.lazy_load)\#     

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

Examples using GitLoader

  * [Git](https://python.langchain.com/docs/integrations/document_loaders/git/)

__On this page