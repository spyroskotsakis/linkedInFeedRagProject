# ReadTheDocsLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.readthedocs.ReadTheDocsLoader.html
**Word Count:** 419
**Links Count:** 418
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# ReadTheDocsLoader\#

_class _langchain\_community.document\_loaders.readthedocs.ReadTheDocsLoader\(

    _path : str | Path_,     _encoding : str | None = None_,     _errors : str | None = None_,     _custom\_html\_tag : Tuple\[str, dict\] | None = None_,     _patterns : Sequence\[str\] = \('\*.htm', '\*.html'\)_,     _exclude\_links\_ratio : float = 1.0_,     _\*\* kwargs: Any | None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/readthedocs.html#ReadTheDocsLoader)\#     

Load ReadTheDocs documentation directory.

Initialize ReadTheDocsLoader

The loader loops over all files under path and extracts the actual content of the files by retrieving main html tags. Default main html tags include <main id=”main-content>, <div role=”main>, and <article role=”main”>. You can also define your own html tags by passing custom\_html\_tag, e.g. \(“div”, “class=main”\). The loader iterates html tags with the order of custom html tags \(if exists\) and default html tags. If any of the tags is not empty, the loop will break and retrieve the content out of that tag.

Parameters:     

  * **path** \(_Union_ _\[__str_ _,__Path_ _\]_\) – The location of pulled readthedocs folder.

  * **encoding** \(_Optional_ _\[__str_ _\]_\) – The encoding with which to open the documents.

  * **errors** \(_Optional_ _\[__str_ _\]_\) – Specify how encoding and decoding errors are to be handled—this cannot be used in binary mode.

  * **custom\_html\_tag** \(_Optional_ _\[__Tuple_ _\[__str_ _,__dict_ _\]__\]_\) – Optional custom html tag to retrieve the content from files.

  * **patterns** \(_Sequence_ _\[__str_ _\]_\) – The file patterns to load, passed to glob.rglob.

  * **exclude\_links\_ratio** \(_float_\) – The ratio of links:content to exclude pages from. This is to reduce the frequency at which index pages make their way into retrieved results. Recommended: 0.5

  * **kwargs** \(_Optional_ _\[__Any_ _\]_\) – named arguments passed to bs4.BeautifulSoup.

Methods

`__init__`\(path\[, encoding, errors, ...\]\) | Initialize ReadTheDocsLoader   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _path : str | Path_,     _encoding : str | None = None_,     _errors : str | None = None_,     _custom\_html\_tag : Tuple\[str, dict\] | None = None_,     _patterns : Sequence\[str\] = \('\*.htm', '\*.html'\)_,     _exclude\_links\_ratio : float = 1.0_,     _\*\* kwargs: Any | None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/readthedocs.html#ReadTheDocsLoader.__init__)\#     

Initialize ReadTheDocsLoader

The loader loops over all files under path and extracts the actual content of the files by retrieving main html tags. Default main html tags include <main id=”main-content>, <div role=”main>, and <article role=”main”>. You can also define your own html tags by passing custom\_html\_tag, e.g. \(“div”, “class=main”\). The loader iterates html tags with the order of custom html tags \(if exists\) and default html tags. If any of the tags is not empty, the loop will break and retrieve the content out of that tag.

Parameters:     

  * **path** \(_str_ _|__Path_\) – The location of pulled readthedocs folder.

  * **encoding** \(_str_ _|__None_\) – The encoding with which to open the documents.

  * **errors** \(_str_ _|__None_\) – Specify how encoding and decoding errors are to be handled—this cannot be used in binary mode.

  * **custom\_html\_tag** \(_Tuple_ _\[__str_ _,__dict_ _\]__|__None_\) – Optional custom html tag to retrieve the content from files.

  * **patterns** \(_Sequence_ _\[__str_ _\]_\) – The file patterns to load, passed to glob.rglob.

  * **exclude\_links\_ratio** \(_float_\) – The ratio of links:content to exclude pages from. This is to reduce the frequency at which index pages make their way into retrieved results. Recommended: 0.5

  * **kwargs** \(_Any_ _|__None_\) – named arguments passed to bs4.BeautifulSoup.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/readthedocs.html#ReadTheDocsLoader.lazy_load)\#     

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

Examples using ReadTheDocsLoader

  * [ReadTheDocs Documentation](https://python.langchain.com/docs/integrations/document_loaders/readthedocs_documentation/)

__On this page