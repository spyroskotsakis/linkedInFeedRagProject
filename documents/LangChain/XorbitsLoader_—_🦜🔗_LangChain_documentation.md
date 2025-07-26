# XorbitsLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.xorbits.XorbitsLoader.html
**Word Count:** 147
**Links Count:** 417
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# XorbitsLoader\#

_class _langchain\_community.document\_loaders.xorbits.XorbitsLoader\(

    _data\_frame : Any_,     _page\_content\_column : str = 'text'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/xorbits.html#XorbitsLoader)\#     

Load Xorbits DataFrame.

Initialize with dataframe object.

Requirements:     

Must have xorbits installed. You can install with pip install xorbits.

Parameters:     

  * **data\_frame** \(_Any_\) – Xorbits DataFrame object.

  * **page\_content\_column** \(_str_\) – Name of the column containing the page content. Defaults to “text”.

Methods

`__init__`\(data\_frame\[, page\_content\_column\]\) | Initialize with dataframe object.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load records from dataframe.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _data\_frame : Any_,     _page\_content\_column : str = 'text'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/xorbits.html#XorbitsLoader.__init__)\#     

Initialize with dataframe object.

Requirements:     

Must have xorbits installed. You can install with pip install xorbits.

Parameters:     

  * **data\_frame** \(_Any_\) – Xorbits DataFrame object.

  * **page\_content\_column** \(_str_\) – Name of the column containing the page content. Defaults to “text”.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Lazy load records from dataframe.

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

Examples using XorbitsLoader

  * [Xorbits Pandas DataFrame](https://python.langchain.com/docs/integrations/document_loaders/xorbits/)

__On this page