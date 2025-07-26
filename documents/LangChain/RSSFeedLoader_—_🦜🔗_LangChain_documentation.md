# RSSFeedLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.rss.RSSFeedLoader.html
**Word Count:** 230
**Links Count:** 422
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# RSSFeedLoader\#

_class _langchain\_community.document\_loaders.rss.RSSFeedLoader\(

    _urls : Sequence\[str\] | None = None_,     _opml : str | None = None_,     _continue\_on\_failure : bool = True_,     _show\_progress\_bar : bool = False_,     _\*\* newsloader\_kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rss.html#RSSFeedLoader)\#     

Load news articles from RSS feeds using Unstructured.

Parameters:     

  * **urls** \(_Sequence_ _\[__str_ _\]__|__None_\) – URLs for RSS feeds to load. Each articles in the feed is loaded into its own document.

  * **opml** \(_str_ _|__None_\) – OPML file to load feed urls from. Only one of urls or opml should be provided. The value

  * **string** \(_can be a URL_\)

  * **string.** \(_or OPML markup contents as byte or_\)

  * **continue\_on\_failure** \(_bool_\) – If True, continue loading documents even if loading fails for a particular URL.

  * **show\_progress\_bar** \(_bool_\) – If True, use tqdm to show a loading progress bar. Requires tqdm to be installed, `pip install tqdm`.

  * **\*\*newsloader\_kwargs** \(_Any_\) – Any additional named arguments to pass to NewsURLLoader.

Example               from langchain_community.document_loaders import RSSFeedLoader          loader = RSSFeedLoader(         urls=["<url-1>", "<url-2>"],     )     docs = loader.load()     

The loader uses feedparser to parse RSS feeds. The feedparser library is not installed by default so you should install it if using this loader: <https://pythonhosted.org/feedparser/>

If you use OPML, you should also install listparser: <https://pythonhosted.org/listparser/>

Finally, newspaper is used to process each article: <https://newspaper.readthedocs.io/en/latest/>

Initialize with urls or OPML.

Methods

`__init__`\(\[urls, opml, continue\_on\_failure, ...\]\) | Initialize with urls or OPML.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _urls : Sequence\[str\] | None = None_,     _opml : str | None = None_,     _continue\_on\_failure : bool = True_,     _show\_progress\_bar : bool = False_,     _\*\* newsloader\_kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rss.html#RSSFeedLoader.__init__)\#     

Initialize with urls or OPML.

Parameters:     

  * **urls** \(_Sequence_ _\[__str_ _\]__|__None_\)

  * **opml** \(_str_ _|__None_\)

  * **continue\_on\_failure** \(_bool_\)

  * **show\_progress\_bar** \(_bool_\)

  * **newsloader\_kwargs** \(_Any_\)

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rss.html#RSSFeedLoader.lazy_load)\#     

A lazy loader for Documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rss.html#RSSFeedLoader.load)\#     

Load data into Document objects.

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

Examples using RSSFeedLoader

  * [RSS Feeds](https://python.langchain.com/docs/integrations/document_loaders/rss/)

__On this page