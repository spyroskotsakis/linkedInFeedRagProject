# MastodonTootsLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mastodon.MastodonTootsLoader.html
**Word Count:** 235
**Links Count:** 420
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# MastodonTootsLoader\#

_class _langchain\_community.document\_loaders.mastodon.MastodonTootsLoader\(

    _mastodon\_accounts : Sequence\[str\]_,     _number\_toots : int | None = 100_,     _exclude\_replies : bool = False_,     _access\_token : str | None = None_,     _api\_base\_url : str = 'https://mastodon.social'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mastodon.html#MastodonTootsLoader)\#     

Load the Mastodon ‘toots’.

Instantiate Mastodon toots loader.

Parameters:     

  * **mastodon\_accounts** \(_Sequence_ _\[__str_ _\]_\) – The list of Mastodon accounts to query.

  * **number\_toots** \(_Optional_ _\[__int_ _\]_\) – How many toots to pull for each account. Defaults to 100.

  * **exclude\_replies** \(_bool_\) – Whether to exclude reply toots from the load. Defaults to False.

  * **access\_token** \(_Optional_ _\[__str_ _\]_\) – An access token if toots are loaded as a Mastodon app. Can also be specified via the environment variables “MASTODON\_ACCESS\_TOKEN”.

  * **api\_base\_url** \(_str_\) – A Mastodon API base URL to talk to, if not using the default. Defaults to “<https://mastodon.social>”.

Methods

`__init__`\(mastodon\_accounts\[, number\_toots, ...\]\) | Instantiate Mastodon toots loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Load toots into documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _mastodon\_accounts : Sequence\[str\]_,     _number\_toots : int | None = 100_,     _exclude\_replies : bool = False_,     _access\_token : str | None = None_,     _api\_base\_url : str = 'https://mastodon.social'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mastodon.html#MastodonTootsLoader.__init__)\#     

Instantiate Mastodon toots loader.

Parameters:     

  * **mastodon\_accounts** \(_Sequence_ _\[__str_ _\]_\) – The list of Mastodon accounts to query.

  * **number\_toots** \(_int_ _|__None_\) – How many toots to pull for each account. Defaults to 100.

  * **exclude\_replies** \(_bool_\) – Whether to exclude reply toots from the load. Defaults to False.

  * **access\_token** \(_str_ _|__None_\) – An access token if toots are loaded as a Mastodon app. Can also be specified via the environment variables “MASTODON\_ACCESS\_TOKEN”.

  * **api\_base\_url** \(_str_\) – A Mastodon API base URL to talk to, if not using the default. Defaults to “<https://mastodon.social>”.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mastodon.html#MastodonTootsLoader.lazy_load)\#     

Load toots into documents.

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

Examples using MastodonTootsLoader

  * [Mastodon](https://python.langchain.com/docs/integrations/document_loaders/mastodon/)

__On this page