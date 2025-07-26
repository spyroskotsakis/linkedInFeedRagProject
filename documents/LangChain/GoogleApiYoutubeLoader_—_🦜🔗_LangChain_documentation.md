# GoogleApiYoutubeLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.GoogleApiYoutubeLoader.html
**Word Count:** 141
**Links Count:** 425
**Scraped:** 2025-07-21 08:18:46
**Status:** completed

---

# GoogleApiYoutubeLoader\#

_class _langchain\_community.document\_loaders.youtube.GoogleApiYoutubeLoader\(

    _google\_api\_client : [GoogleApiClient](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.GoogleApiClient.html#langchain_community.document_loaders.youtube.GoogleApiClient "langchain_community.document_loaders.youtube.GoogleApiClient")_,     _channel\_name : str | None = None_,     _video\_ids : List\[str\] | None = None_,     _add\_video\_info : bool = True_,     _captions\_language : str = 'en'_,     _continue\_on\_failure : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/youtube.html#GoogleApiYoutubeLoader)\#     

Load all Videos from a YouTube Channel.

To use, you should have the `googleapiclient,youtube_transcript_api` python package installed. As the service needs a google\_api\_client, you first have to initialize the GoogleApiClient.

Additionally you have to either provide a channel name or a list of videoids “<https://developers.google.com/docs/api/quickstart/python>”

Example               from langchain_community.document_loaders import GoogleApiClient     from langchain_community.document_loaders import GoogleApiYoutubeLoader     google_api_client = GoogleApiClient(         service_account_path=Path("path_to_your_sec_file.json")     )     loader = GoogleApiYoutubeLoader(         google_api_client=google_api_client,         channel_name = "CodeAesthetic"     )     load.load()     

Attributes

`add_video_info` |    ---|---   `captions_language` |    `channel_name` |    `continue_on_failure` |    `video_ids` |       Methods

`__init__`\(\*args, \*\*kwargs\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `validate_channel_or_videoIds_is_set`\(values\) | Validate that either folder\_id or document\_ids is set, but not both.      Parameters:     

  * **google\_api\_client** \([_GoogleApiClient_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.youtube.GoogleApiClient.html#langchain_community.document_loaders.youtube.GoogleApiClient "langchain_community.document_loaders.youtube.GoogleApiClient")\)

  * **channel\_name** \(_str_ _|__None_\)

  * **video\_ids** \(_List_ _\[__str_ _\]__|__None_\)

  * **add\_video\_info** \(_bool_\)

  * **captions\_language** \(_str_\)

  * **continue\_on\_failure** \(_bool_\)

\_\_init\_\_\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → None\#     

Parameters:     

  * **\_\_dataclass\_self\_\_** \(_PydanticDataclass_\)

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/youtube.html#GoogleApiYoutubeLoader.load)\#     

Load documents.

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

_classmethod _validate\_channel\_or\_videoIds\_is\_set\(

    _values : Any_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/youtube.html#GoogleApiYoutubeLoader.validate_channel_or_videoIds_is_set)\#     

Validate that either folder\_id or document\_ids is set, but not both.

Parameters:     

**values** \(_Any_\)

Return type:     

_Any_

Examples using GoogleApiYoutubeLoader

  * [YouTube](https://python.langchain.com/docs/integrations/providers/youtube/)

  * [YouTube transcripts](https://python.langchain.com/docs/integrations/document_loaders/youtube_transcript/)

__On this page