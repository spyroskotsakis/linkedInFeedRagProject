# JoplinLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.joplin.JoplinLoader.html
**Word Count:** 211
**Links Count:** 419
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# JoplinLoader\#

_class _langchain\_community.document\_loaders.joplin.JoplinLoader\(

    _access\_token : str | None = None_,     _port : int = 41184_,     _host : str = 'localhost'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/joplin.html#JoplinLoader)\#     

Load notes from Joplin.

In order to use this loader, you need to have Joplin running with the Web Clipper enabled \(look for “Web Clipper” in the app settings\).

To get the access token, you need to go to the Web Clipper options and under “Advanced Options” you will find the access token.

You can find more information about the Web Clipper service here: <https://joplinapp.org/clipper/>

Parameters:     

  * **access\_token** \(_str_ _|__None_\) – The access token to use.

  * **port** \(_int_\) – The port where the Web Clipper service is running. Default is 41184.

  * **host** \(_str_\) – The host where the Web Clipper service is running. Default is localhost.

Methods

`__init__`\(\[access\_token, port, host\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _access\_token : str | None = None_,     _port : int = 41184_,     _host : str = 'localhost'_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/joplin.html#JoplinLoader.__init__)\#     

Parameters:     

  * **access\_token** \(_str_ _|__None_\) – The access token to use.

  * **port** \(_int_\) – The port where the Web Clipper service is running. Default is 41184.

  * **host** \(_str_\) – The host where the Web Clipper service is running. Default is localhost.

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/joplin.html#JoplinLoader.lazy_load)\#     

A lazy loader for Documents.

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

Examples using JoplinLoader

  * [Joplin](https://python.langchain.com/docs/integrations/document_loaders/joplin/)

__On this page