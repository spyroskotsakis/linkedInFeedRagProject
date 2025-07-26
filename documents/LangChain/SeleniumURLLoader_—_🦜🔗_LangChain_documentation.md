# SeleniumURLLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.url_selenium.SeleniumURLLoader.html
**Word Count:** 184
**Links Count:** 432
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# SeleniumURLLoader\#

_class _langchain\_community.document\_loaders.url\_selenium.SeleniumURLLoader\(

    _urls : List\[str\]_,     _continue\_on\_failure : bool = True_,     _browser : Literal\['chrome', 'firefox'\] = 'chrome'_,     _binary\_location : str | None = None_,     _executable\_path : str | None = None_,     _headless : bool = True_,     _arguments : List\[str\] = \[\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_selenium.html#SeleniumURLLoader)\#     

Load HTML pages with Selenium and parse with Unstructured.

This is useful for loading pages that require javascript to render.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **continue\_on\_failure** \(_bool_\)

  * **browser** \(_Literal_ _\[__'chrome'__,__'firefox'__\]_\)

  * **binary\_location** \(_str_ _|__None_\)

  * **executable\_path** \(_str_ _|__None_\)

  * **headless** \(_bool_\)

  * **arguments** \(_List_ _\[__str_ _\]_\)

urls\#     

List of URLs to load.

Type:     

List\[str\]

continue\_on\_failure\#     

If True, continue loading other URLs on failure.

Type:     

bool

browser\#     

The browser to use, either ‘chrome’ or ‘firefox’.

Type:     

str

binary\_location\#     

The location of the browser binary.

Type:     

Optional\[str\]

executable\_path\#     

The path to the browser executable.

Type:     

Optional\[str\]

headless\#     

If True, the browser will run in headless mode.

Type:     

bool

arguments\[_List_ , _str_\]\#     

List of arguments to pass to the browser.

Load a list of URLs using Selenium and unstructured.

Methods

`__init__`\(urls\[, continue\_on\_failure, ...\]\) | Load a list of URLs using Selenium and unstructured.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load the specified URLs using Selenium and create Document instances.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _urls : List\[str\]_,     _continue\_on\_failure : bool = True_,     _browser : Literal\['chrome', 'firefox'\] = 'chrome'_,     _binary\_location : str | None = None_,     _executable\_path : str | None = None_,     _headless : bool = True_,     _arguments : List\[str\] = \[\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_selenium.html#SeleniumURLLoader.__init__)\#     

Load a list of URLs using Selenium and unstructured.

Parameters:     

  * **urls** \(_List_ _\[__str_ _\]_\)

  * **continue\_on\_failure** \(_bool_\)

  * **browser** \(_Literal_ _\[__'chrome'__,__'firefox'__\]_\)

  * **binary\_location** \(_str_ _|__None_\)

  * **executable\_path** \(_str_ _|__None_\)

  * **headless** \(_bool_\)

  * **arguments** \(_List_ _\[__str_ _\]_\)

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/url_selenium.html#SeleniumURLLoader.load)\#     

Load the specified URLs using Selenium and create Document instances.

Returns:     

A list of Document instances with loaded content.

Return type:     

List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

Examples using SeleniumURLLoader

  * [URL](https://python.langchain.com/docs/integrations/document_loaders/url/)

__On this page