# ChatGPTLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.chatgpt.ChatGPTLoader.html
**Word Count:** 133
**Links Count:** 419
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# ChatGPTLoader\#

_class _langchain\_community.document\_loaders.chatgpt.ChatGPTLoader\(_log\_file : str_, _num\_logs : int = -1_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/chatgpt.html#ChatGPTLoader)\#     

Load conversations from exported ChatGPT data.

Initialize a class object.

Parameters:     

  * **log\_file** \(_str_\) – Path to the log file

  * **num\_logs** \(_int_\) – Number of logs to load. If 0, load all logs.

Methods

`__init__`\(log\_file\[, num\_logs\]\) | Initialize a class object.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(_log\_file : str_, _num\_logs : int = -1_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/chatgpt.html#ChatGPTLoader.__init__)\#     

Initialize a class object.

Parameters:     

  * **log\_file** \(_str_\) – Path to the log file

  * **num\_logs** \(_int_\) – Number of logs to load. If 0, load all logs.

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/chatgpt.html#ChatGPTLoader.load)\#     

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

Examples using ChatGPTLoader

  * [ChatGPT Data](https://python.langchain.com/docs/integrations/document_loaders/chatgpt_loader/)

  * [OpenAI](https://python.langchain.com/docs/integrations/providers/openai/)

__On this page