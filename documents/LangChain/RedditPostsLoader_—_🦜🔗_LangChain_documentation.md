# RedditPostsLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.reddit.RedditPostsLoader.html
**Word Count:** 177
**Links Count:** 421
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# RedditPostsLoader\#

_class _langchain\_community.document\_loaders.reddit.RedditPostsLoader\(

    _client\_id : str_,     _client\_secret : str_,     _user\_agent : str_,     _search\_queries : Sequence\[str\]_,     _mode : str_,     _categories : Sequence\[str\] = \['new'\]_,     _number\_posts : int | None = 10_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/reddit.html#RedditPostsLoader)\#     

Load Reddit posts.

Read posts on a subreddit. First, you need to go to <https://www.reddit.com/prefs/apps/> and create your application

Initialize with client\_id, client\_secret, user\_agent, search\_queries, mode,     

categories, number\_posts.

Example: <https://www.reddit.com/r/learnpython/>

Parameters:     

  * **client\_id** \(_str_\) – Reddit client id.

  * **client\_secret** \(_str_\) – Reddit client secret.

  * **user\_agent** \(_str_\) – Reddit user agent.

  * **search\_queries** \(_Sequence_ _\[__str_ _\]_\) – The search queries.

  * **mode** \(_str_\) – The mode.

  * **categories** \(_Sequence_ _\[__str_ _\]_\) – The categories. Default: \[“new”\]

  * **number\_posts** \(_Optional_ _\[__int_ _\]_\) – The number of posts. Default: 10

Methods

`__init__`\(client\_id, client\_secret, ...\[, ...\]\) | Initialize with client\_id, client\_secret, user\_agent, search\_queries, mode,   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load reddits.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _client\_id : str_,     _client\_secret : str_,     _user\_agent : str_,     _search\_queries : Sequence\[str\]_,     _mode : str_,     _categories : Sequence\[str\] = \['new'\]_,     _number\_posts : int | None = 10_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/reddit.html#RedditPostsLoader.__init__)\#     

Initialize with client\_id, client\_secret, user\_agent, search\_queries, mode,     

categories, number\_posts.

Example: <https://www.reddit.com/r/learnpython/>

Parameters:     

  * **client\_id** \(_str_\) – Reddit client id.

  * **client\_secret** \(_str_\) – Reddit client secret.

  * **user\_agent** \(_str_\) – Reddit user agent.

  * **search\_queries** \(_Sequence_ _\[__str_ _\]_\) – The search queries.

  * **mode** \(_str_\) – The mode.

  * **categories** \(_Sequence_ _\[__str_ _\]_\) – The categories. Default: \[“new”\]

  * **number\_posts** \(_int_ _|__None_\) – The number of posts. Default: 10

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/reddit.html#RedditPostsLoader.load)\#     

Load reddits.

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

Examples using RedditPostsLoader

  * [Reddit](https://python.langchain.com/docs/integrations/document_loaders/reddit/)

__On this page