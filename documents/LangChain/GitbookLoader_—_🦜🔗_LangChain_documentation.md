# GitbookLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.gitbook.GitbookLoader.html
**Word Count:** 510
**Links Count:** 419
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# GitbookLoader\#

_class _langchain\_community.document\_loaders.gitbook.GitbookLoader\(

    _web\_page : str_,     _load\_all\_paths : bool = False_,     _base\_url : str | None = None_,     _content\_selector : str = 'main'_,     _continue\_on\_failure : bool = False_,     _show\_progress : bool = True_,     _\*_ ,     _sitemap\_url : str | None = None_,     _allowed\_domains : Set\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/gitbook.html#GitbookLoader)\#     

Load GitBook data.

  1. load from either a single page, or

  2. load all \(relative\) paths in the sitemap, handling nested sitemap indexes.

When load\_all\_paths=True, the loader parses XML sitemaps and requires the lxml package to be installed \(pip install lxml\).

Initialize with web page and whether to load all paths.

Parameters:     

  * **web\_page** \(_str_\) – The web page to load or the starting point from where relative paths are discovered.

  * **load\_all\_paths** \(_bool_\) – If set to True, all relative paths in the navbar are loaded instead of only web\_page. Requires lxml package.

  * **base\_url** \(_str_ _|__None_\) – If load\_all\_paths is True, the relative paths are appended to this base url. Defaults to web\_page.

  * **content\_selector** \(_str_\) – The CSS selector for the content to load. Defaults to “main”.

  * **continue\_on\_failure** \(_bool_\) – whether to continue loading the sitemap if an error occurs loading a url, emitting a warning instead of raising an exception. Setting this to True makes the loader more robust, but also may result in missing data. Default: False

  * **show\_progress** \(_bool_\) – whether to show a progress bar while loading. Default: True

  * **sitemap\_url** \(_str_ _|__None_\) – Custom sitemap URL to use when load\_all\_paths is True. Defaults to “\{base\_url\}/sitemap.xml”.

  * **allowed\_domains** \(_Set_ _\[__str_ _\]__|__None_\) – Optional set of allowed domains to fetch from. If None \(default\), the loader will restrict crawling to the domain of the web\_page URL to prevent potential SSRF vulnerabilities. Provide an explicit set \(e.g., \{“example.com”, “docs.example.com”\}\) to allow crawling across multiple domains. Use with caution in server environments where users might control the input URLs.

Methods

`__init__`\(web\_page\[, load\_all\_paths, ...\]\) | Initialize with web page and whether to load all paths.   ---|---   `alazy_load`\(\) | Asynchronously fetch text from GitBook page\(s\).   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Fetch text from one single GitBook page or recursively from sitemap.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _web\_page : str_,     _load\_all\_paths : bool = False_,     _base\_url : str | None = None_,     _content\_selector : str = 'main'_,     _continue\_on\_failure : bool = False_,     _show\_progress : bool = True_,     _\*_ ,     _sitemap\_url : str | None = None_,     _allowed\_domains : Set\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/gitbook.html#GitbookLoader.__init__)\#     

Initialize with web page and whether to load all paths.

Parameters:     

  * **web\_page** \(_str_\) – The web page to load or the starting point from where relative paths are discovered.

  * **load\_all\_paths** \(_bool_\) – If set to True, all relative paths in the navbar are loaded instead of only web\_page. Requires lxml package.

  * **base\_url** \(_str_ _|__None_\) – If load\_all\_paths is True, the relative paths are appended to this base url. Defaults to web\_page.

  * **content\_selector** \(_str_\) – The CSS selector for the content to load. Defaults to “main”.

  * **continue\_on\_failure** \(_bool_\) – whether to continue loading the sitemap if an error occurs loading a url, emitting a warning instead of raising an exception. Setting this to True makes the loader more robust, but also may result in missing data. Default: False

  * **show\_progress** \(_bool_\) – whether to show a progress bar while loading. Default: True

  * **sitemap\_url** \(_str_ _|__None_\) – Custom sitemap URL to use when load\_all\_paths is True. Defaults to “\{base\_url\}/sitemap.xml”.

  * **allowed\_domains** \(_Set_ _\[__str_ _\]__|__None_\) – Optional set of allowed domains to fetch from. If None \(default\), the loader will restrict crawling to the domain of the web\_page URL to prevent potential SSRF vulnerabilities. Provide an explicit set \(e.g., \{“example.com”, “docs.example.com”\}\) to allow crawling across multiple domains. Use with caution in server environments where users might control the input URLs.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/gitbook.html#GitbookLoader.alazy_load)\#     

Asynchronously fetch text from GitBook page\(s\).

Return type:     

_AsyncIterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/gitbook.html#GitbookLoader.lazy_load)\#     

Fetch text from one single GitBook page or recursively from sitemap.

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

Examples using GitbookLoader

  * [GitBook](https://python.langchain.com/docs/integrations/document_loaders/gitbook/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)