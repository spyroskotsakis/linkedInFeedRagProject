# YuqueLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.yuque.YuqueLoader.html
**Word Count:** 128
**Links Count:** 456
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# YuqueLoader\#

_class _langchain\_community.document\_loaders.yuque.YuqueLoader\(

    _access\_token : str_,     _api\_url : str = 'https://www.yuque.com'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader)\#     

Load documents from Yuque.

Initialize with Yuque access\_token and api\_url.

Parameters:     

  * **access\_token** \(_str_\) – Personal access token - see <https://www.yuque.com/settings/tokens>.

  * **api\_url** \(_str_\) – Yuque API url.

Attributes

`headers` |    ---|---      Methods

`__init__`\(access\_token\[, api\_url\]\) | Initialize with Yuque access\_token and api\_url.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `get_books`\(user\_id\) |    `get_document`\(book\_id, document\_id\) |    `get_document_ids`\(book\_id\) |    `get_documents`\(\) |    `get_user_id`\(\) |    `http_get`\(url\) |    `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents from Yuque.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `parse_document`\(document\) |    `parse_document_body`\(body\) |       \_\_init\_\_\(

    _access\_token : str_,     _api\_url : str = 'https://www.yuque.com'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader.__init__)\#     

Initialize with Yuque access\_token and api\_url.

Parameters:     

  * **access\_token** \(_str_\) – Personal access token - see <https://www.yuque.com/settings/tokens>.

  * **api\_url** \(_str_\) – Yuque API url.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

get\_books\(

    _user\_id : int_, \) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader.get_books)\#     

Parameters:     

**user\_id** \(_int_\)

Return type:     

_List_\[_Dict_\]

get\_document\(

    _book\_id : int_,     _document\_id : int_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader.get_document)\#     

Parameters:     

  * **book\_id** \(_int_\)

  * **document\_id** \(_int_\)

Return type:     

_Dict_

get\_document\_ids\(

    _book\_id : int_, \) → List\[int\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader.get_document_ids)\#     

Parameters:     

**book\_id** \(_int_\)

Return type:     

_List_\[int\]

get\_documents\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader.get_documents)\#     

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

get\_user\_id\(\) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader.get_user_id)\#     

Return type:     

int

http\_get\(_url : str_\) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader.http_get)\#     

Parameters:     

**url** \(_str_\)

Return type:     

_Dict_

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader.load)\#     

Load documents from Yuque.

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

parse\_document\(

    _document : Dict_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader.parse_document)\#     

Parameters:     

**document** \(_Dict_\)

Return type:     

[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")

_static _parse\_document\_body\(_body : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/yuque.html#YuqueLoader.parse_document_body)\#     

Parameters:     

**body** \(_str_\)

Return type:     

str

Examples using YuqueLoader

  * [Yuque](https://python.langchain.com/docs/integrations/document_loaders/yuque/)

__On this page