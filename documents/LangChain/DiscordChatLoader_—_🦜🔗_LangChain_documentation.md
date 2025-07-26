# DiscordChatLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.discord.DiscordChatLoader.html
**Word Count:** 142
**Links Count:** 418
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# DiscordChatLoader\#

_class _langchain\_community.document\_loaders.discord.DiscordChatLoader\(

    _chat\_log : pd.DataFrame_,     _user\_id\_col : str = 'ID'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/discord.html#DiscordChatLoader)\#     

Load Discord chat logs.

Initialize with a Pandas DataFrame containing chat logs.

Parameters:     

  * **chat\_log** \(_pd.DataFrame_\) – Pandas DataFrame containing chat logs.

  * **user\_id\_col** \(_str_\) – Name of the column containing the user ID. Defaults to “ID”.

Methods

`__init__`\(chat\_log\[, user\_id\_col\]\) | Initialize with a Pandas DataFrame containing chat logs.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load all chat messages.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _chat\_log : pd.DataFrame_,     _user\_id\_col : str = 'ID'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/discord.html#DiscordChatLoader.__init__)\#     

Initialize with a Pandas DataFrame containing chat logs.

Parameters:     

  * **chat\_log** \(_pd.DataFrame_\) – Pandas DataFrame containing chat logs.

  * **user\_id\_col** \(_str_\) – Name of the column containing the user ID. Defaults to “ID”.

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/discord.html#DiscordChatLoader.load)\#     

Load all chat messages.

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

Examples using DiscordChatLoader

  * [Discord](https://python.langchain.com/docs/integrations/document_loaders/discord/)

__On this page