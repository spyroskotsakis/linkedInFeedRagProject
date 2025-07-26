# TwitterTweetLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.twitter.TwitterTweetLoader.html
**Word Count:** 135
**Links Count:** 430
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# TwitterTweetLoader\#

_class _langchain\_community.document\_loaders.twitter.TwitterTweetLoader\(

    _auth\_handler : OAuthHandler | OAuth2BearerHandler_,     _twitter\_users : Sequence\[str\]_,     _number\_tweets : int | None = 100_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/twitter.html#TwitterTweetLoader)\#     

Load Twitter tweets.

Read tweets of the user’s Twitter handle.

First you need to go to https://developer.twitter.com/en/docs/twitter-api /getting-started/getting-access-to-the-twitter-api to get your token. And create a v2 version of the app.

Methods

`__init__`\(auth\_handler, twitter\_users\[, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `from_bearer_token`\(oauth2\_bearer\_token, ...\) | Create a TwitterTweetLoader from OAuth2 bearer token.   `from_secrets`\(access\_token, ...\[, number\_tweets\]\) | Create a TwitterTweetLoader from access tokens and secrets.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load tweets.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **auth\_handler** \(_Union_ _\[__OAuthHandler_ _,__OAuth2BearerHandler_ _\]_\)

  * **twitter\_users** \(_Sequence_ _\[__str_ _\]_\)

  * **number\_tweets** \(_Optional_ _\[__int_ _\]_\)

\_\_init\_\_\(

    _auth\_handler : OAuthHandler | OAuth2BearerHandler_,     _twitter\_users : Sequence\[str\]_,     _number\_tweets : int | None = 100_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/twitter.html#TwitterTweetLoader.__init__)\#     

Parameters:     

  * **auth\_handler** \(_Union_ _\[__OAuthHandler_ _,__OAuth2BearerHandler_ _\]_\)

  * **twitter\_users** \(_Sequence_ _\[__str_ _\]_\)

  * **number\_tweets** \(_Optional_ _\[__int_ _\]_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_classmethod _from\_bearer\_token\(

    _oauth2\_bearer\_token : str_,     _twitter\_users : Sequence\[str\]_,     _number\_tweets : int | None = 100_, \) → TwitterTweetLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/twitter.html#TwitterTweetLoader.from_bearer_token)\#     

Create a TwitterTweetLoader from OAuth2 bearer token.

Parameters:     

  * **oauth2\_bearer\_token** \(_str_\)

  * **twitter\_users** \(_Sequence_ _\[__str_ _\]_\)

  * **number\_tweets** \(_int_ _|__None_\)

Return type:     

_TwitterTweetLoader_

_classmethod _from\_secrets\(

    _access\_token : str_,     _access\_token\_secret : str_,     _consumer\_key : str_,     _consumer\_secret : str_,     _twitter\_users : Sequence\[str\]_,     _number\_tweets : int | None = 100_, \) → TwitterTweetLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/twitter.html#TwitterTweetLoader.from_secrets)\#     

Create a TwitterTweetLoader from access tokens and secrets.

Parameters:     

  * **access\_token** \(_str_\)

  * **access\_token\_secret** \(_str_\)

  * **consumer\_key** \(_str_\)

  * **consumer\_secret** \(_str_\)

  * **twitter\_users** \(_Sequence_ _\[__str_ _\]_\)

  * **number\_tweets** \(_int_ _|__None_\)

Return type:     

_TwitterTweetLoader_

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/twitter.html#TwitterTweetLoader.load)\#     

Load tweets.

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

Examples using TwitterTweetLoader

  * [Twitter](https://python.langchain.com/docs/integrations/document_loaders/twitter/)

__On this page