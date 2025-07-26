# AsyncHtmlLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.async_html.AsyncHtmlLoader.html
**Word Count:** 128
**Links Count:** 426
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# AsyncHtmlLoader\#

_class _langchain\_community.document\_loaders.async\_html.AsyncHtmlLoader\(

    _web\_path : str | List\[str\]_,     _header\_template : dict | None = None_,     _verify\_ssl : bool | None = True_,     _proxies : dict | None = None_,     _autoset\_encoding : bool = True_,     _encoding : str | None = None_,     _default\_parser : str = 'html.parser'_,     _requests\_per\_second : int = 2_,     _requests\_kwargs : Dict\[str, Any\] | None = None_,     _raise\_for\_status : bool = False_,     _ignore\_load\_errors : bool = False_,     _\*_ ,     _preserve\_order : bool = True_,     _trust\_env : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/async_html.html#AsyncHtmlLoader)\#     

Load HTML asynchronously.

Initialize with a webpage path.

Methods

`__init__`\(web\_path\[, header\_template, ...\]\) | Initialize with a webpage path.   ---|---   `alazy_load`\(\) | Lazy load text from the url\(s\) in web\_path.   `aload`\(\) | Load data into Document objects.   `fetch_all`\(urls\) | Fetch all urls concurrently with rate limiting.   `lazy_load`\(\) | Lazy load text from the url\(s\) in web\_path.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **web\_path** \(_str_ _|__List_ _\[__str_ _\]_\)

  * **header\_template** \(_dict_ _|__None_\)

  * **verify\_ssl** \(_bool_ _|__None_\)

  * **proxies** \(_dict_ _|__None_\)

  * **autoset\_encoding** \(_bool_\)

  * **encoding** \(_str_ _|__None_\)

  * **default\_parser** \(_str_\)

  * **requests\_per\_second** \(_int_\)

  * **requests\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **raise\_for\_status** \(_bool_\)

  * **ignore\_load\_errors** \(_bool_\)

  * **preserve\_order** \(_bool_\)

  * **trust\_env** \(_bool_\)

\_\_init\_\_\(

    _web\_path : str | List\[str\]_,     _header\_template : dict | None = None_,     _verify\_ssl : bool | None = True_,     _proxies : dict | None = None_,     _autoset\_encoding : bool = True_,     _encoding : str | None = None_,     _default\_parser : str = 'html.parser'_,     _requests\_per\_second : int = 2_,     _requests\_kwargs : Dict\[str, Any\] | None = None_,     _raise\_for\_status : bool = False_,     _ignore\_load\_errors : bool = False_,     _\*_ ,     _preserve\_order : bool = True_,     _trust\_env : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/async_html.html#AsyncHtmlLoader.__init__)\#     

Initialize with a webpage path.

Parameters:     

  * **web\_path** \(_str_ _|__List_ _\[__str_ _\]_\)

  * **header\_template** \(_dict_ _|__None_\)

  * **verify\_ssl** \(_bool_ _|__None_\)

  * **proxies** \(_dict_ _|__None_\)

  * **autoset\_encoding** \(_bool_\)

  * **encoding** \(_str_ _|__None_\)

  * **default\_parser** \(_str_\)

  * **requests\_per\_second** \(_int_\)

  * **requests\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

  * **raise\_for\_status** \(_bool_\)

  * **ignore\_load\_errors** \(_bool_\)

  * **preserve\_order** \(_bool_\)

  * **trust\_env** \(_bool_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/async_html.html#AsyncHtmlLoader.alazy_load)\#     

Lazy load text from the url\(s\) in web\_path.

Return type:     

_AsyncIterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _fetch\_all\(

    _urls : List\[str\]_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/async_html.html#AsyncHtmlLoader.fetch_all)\#     

Fetch all urls concurrently with rate limiting.

Parameters:     

**urls** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[str\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/async_html.html#AsyncHtmlLoader.lazy_load)\#     

Lazy load text from the url\(s\) in web\_path.

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

Examples using AsyncHtmlLoader

  * [Activeloop Deep Memory](https://python.langchain.com/docs/integrations/retrievers/activeloop/)

  * [AsyncHtml](https://python.langchain.com/docs/integrations/document_loaders/async_html/)

  * [HTML to text](https://python.langchain.com/docs/integrations/document_transformers/html2text/)

  * [Markdownify](https://python.langchain.com/docs/integrations/document_transformers/markdownify/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)