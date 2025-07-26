# O365BaseLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.base_o365.O365BaseLoader.html
**Word Count:** 184
**Links Count:** 428
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# O365BaseLoader\#

_class _langchain\_community.document\_loaders.base\_o365.O365BaseLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/base_o365.html#O365BaseLoader)\#     

Bases: [`BaseLoader`](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader"), `BaseModel`

Base class for all loaders that uses O365 Package

_param _auth\_with\_token _: bool_ _ = False_\#     

Whether to authenticate with a token or not. Defaults to False.

_param _chunk\_size _: int | str_ _ = 5242880_\#     

Number of bytes to retrieve from each api call to the server. int or ‘auto’.

_param _handlers _: Dict\[str, Any\] | None_ _ = \{\}_\#     

Provide custom handlers for MimeTypeBasedParser.

Pass a dictionary mapping either file extensions \(like “doc”, “pdf”, etc.\) or MIME types \(like “application/pdf”, “text/plain”, etc.\) to parsers. Note that you must use either file extensions or MIME types exclusively and cannot mix them.

Do not include the leading dot for file extensions.

Example using file extensions: \`\`\`python

> handlers = \{ >      >  > “doc”: MsWordParser\(\), “pdf”: PDFMinerParser\(\), “txt”: TextParser\(\) >  > \}

\`\`\`

Example using MIME types: \`\`\`python

> handlers = \{ >      >  > “application/msword”: MsWordParser\(\), “application/pdf”: PDFMinerParser\(\), “text/plain”: TextParser\(\) >  > \}

\`\`\`

_param _modified\_since _: datetime | None_ _ = None_\#     

Only fetch documents modified since given datetime. The datetime object must be timezone aware.

_param _recursive _: bool_ _ = False_\#     

Should the loader recursively load subfolders?

_param _settings _: \_O365Settings_ _\[Optional\]_\#     

Settings for the Office365 API client.

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

__On this page