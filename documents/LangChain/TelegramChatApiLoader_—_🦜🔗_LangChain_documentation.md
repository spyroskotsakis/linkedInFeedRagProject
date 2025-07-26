# TelegramChatApiLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.telegram.TelegramChatApiLoader.html
**Word Count:** 179
**Links Count:** 422
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# TelegramChatApiLoader\#

_class _langchain\_community.document\_loaders.telegram.TelegramChatApiLoader\(

    _chat\_entity : EntityLike | None = None_,     _api\_id : int | None = None_,     _api\_hash : str | None = None_,     _username : str | None = None_,     _file\_path : str = 'telegram\_data.json'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/telegram.html#TelegramChatApiLoader)\#     

Load Telegram chat json directory dump.

Initialize with API parameters.

Parameters:     

  * **chat\_entity** \(_Optional_ _\[__EntityLike_ _\]_\) – The chat entity to fetch data from.

  * **api\_id** \(_Optional_ _\[__int_ _\]_\) – The API ID.

  * **api\_hash** \(_Optional_ _\[__str_ _\]_\) – The API hash.

  * **username** \(_Optional_ _\[__str_ _\]_\) – The username.

  * **file\_path** \(_str_\) – The file path to save the data to. Defaults to “telegram\_data.json”.

Methods

`__init__`\(\[chat\_entity, api\_id, api\_hash, ...\]\) | Initialize with API parameters.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `fetch_data_from_telegram`\(\) | Fetch data from Telegram API and save it as a JSON file.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _chat\_entity : EntityLike | None = None_,     _api\_id : int | None = None_,     _api\_hash : str | None = None_,     _username : str | None = None_,     _file\_path : str = 'telegram\_data.json'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/telegram.html#TelegramChatApiLoader.__init__)\#     

Initialize with API parameters.

Parameters:     

  * **chat\_entity** \(_Optional_ _\[__EntityLike_ _\]_\) – The chat entity to fetch data from.

  * **api\_id** \(_Optional_ _\[__int_ _\]_\) – The API ID.

  * **api\_hash** \(_Optional_ _\[__str_ _\]_\) – The API hash.

  * **username** \(_Optional_ _\[__str_ _\]_\) – The username.

  * **file\_path** \(_str_\) – The file path to save the data to. Defaults to “telegram\_data.json”.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _fetch\_data\_from\_telegram\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/telegram.html#TelegramChatApiLoader.fetch_data_from_telegram)\#     

Fetch data from Telegram API and save it as a JSON file.

Return type:     

None

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/telegram.html#TelegramChatApiLoader.load)\#     

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

Examples using TelegramChatApiLoader

  * [Telegram](https://python.langchain.com/docs/integrations/document_loaders/telegram/)

__On this page