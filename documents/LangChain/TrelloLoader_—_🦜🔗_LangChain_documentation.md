# TrelloLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.trello.TrelloLoader.html
**Word Count:** 384
**Links Count:** 424
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# TrelloLoader\#

_class _langchain\_community.document\_loaders.trello.TrelloLoader\(

    _client : TrelloClient_,     _board\_name : str_,     _\*_ ,     _include\_card\_name : bool = True_,     _include\_comments : bool = True_,     _include\_checklist : bool = True_,     _card\_filter : Literal\['closed', 'open', 'all'\] = 'all'_,     _extra\_metadata : Tuple\[str, ...\] = \('due\_date', 'labels', 'list', 'closed'\)_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/trello.html#TrelloLoader)\#     

Load cards from a Trello board.

Initialize Trello loader.

Parameters:     

  * **client** \(_TrelloClient_\) – Trello API client.

  * **board\_name** \(_str_\) – The name of the Trello board.

  * **include\_card\_name** \(_bool_\) – Whether to include the name of the card in the document.

  * **include\_comments** \(_bool_\) – Whether to include the comments on the card in the document.

  * **include\_checklist** \(_bool_\) – Whether to include the checklist on the card in the document.

  * **card\_filter** \(_Literal_ _\[__'closed'__,__'open'__,__'all'__\]_\) – Filter on card status. Valid values are “closed”, “open”, “all”.

  * **extra\_metadata** \(_Tuple_ _\[__str_ _,__...__\]_\) – List of additional metadata fields to include as document metadata.Valid values are “due\_date”, “labels”, “list”, “closed”.

Methods

`__init__`\(client, board\_name, \*\[, ...\]\) | Initialize Trello loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `from_credentials`\(board\_name, \*\[, api\_key, token\]\) | Convenience constructor that builds TrelloClient init param for you.   `lazy_load`\(\) | Loads all cards from the specified Trello board.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _client : TrelloClient_,     _board\_name : str_,     _\*_ ,     _include\_card\_name : bool = True_,     _include\_comments : bool = True_,     _include\_checklist : bool = True_,     _card\_filter : Literal\['closed', 'open', 'all'\] = 'all'_,     _extra\_metadata : Tuple\[str, ...\] = \('due\_date', 'labels', 'list', 'closed'\)_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/trello.html#TrelloLoader.__init__)\#     

Initialize Trello loader.

Parameters:     

  * **client** \(_TrelloClient_\) – Trello API client.

  * **board\_name** \(_str_\) – The name of the Trello board.

  * **include\_card\_name** \(_bool_\) – Whether to include the name of the card in the document.

  * **include\_comments** \(_bool_\) – Whether to include the comments on the card in the document.

  * **include\_checklist** \(_bool_\) – Whether to include the checklist on the card in the document.

  * **card\_filter** \(_Literal_ _\[__'closed'__,__'open'__,__'all'__\]_\) – Filter on card status. Valid values are “closed”, “open”, “all”.

  * **extra\_metadata** \(_Tuple_ _\[__str_ _,__...__\]_\) – List of additional metadata fields to include as document metadata.Valid values are “due\_date”, “labels”, “list”, “closed”.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_classmethod _from\_credentials\(

    _board\_name : str_,     _\*_ ,     _api\_key : str | None = None_,     _token : str | None = None_,     _\*\* kwargs: Any_, \) → TrelloLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/trello.html#TrelloLoader.from_credentials)\#     

Convenience constructor that builds TrelloClient init param for you.

Parameters:     

  * **board\_name** \(_str_\) – The name of the Trello board.

  * **api\_key** \(_str_ _|__None_\) – Trello API key. Can also be specified as environment variable TRELLO\_API\_KEY.

  * **token** \(_str_ _|__None_\) – Trello token. Can also be specified as environment variable TRELLO\_TOKEN.

  * **include\_card\_name** – Whether to include the name of the card in the document.

  * **include\_comments** – Whether to include the comments on the card in the document.

  * **include\_checklist** – Whether to include the checklist on the card in the document.

  * **card\_filter** – Filter on card status. Valid values are “closed”, “open”, “all”.

  * **extra\_metadata** – List of additional metadata fields to include as document metadata.Valid values are “due\_date”, “labels”, “list”, “closed”.

  * **kwargs** \(_Any_\)

Return type:     

_TrelloLoader_

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/trello.html#TrelloLoader.lazy_load)\#     

Loads all cards from the specified Trello board.

You can filter the cards, metadata and text included by using the optional     

> parameters.

Returns:     

A list of documents, one for each card in the board.

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

Examples using TrelloLoader

  * [Trello](https://python.langchain.com/docs/integrations/document_loaders/trello/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)