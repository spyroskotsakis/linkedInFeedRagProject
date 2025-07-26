# OneNoteLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.onenote.OneNoteLoader.html
**Word Count:** 163
**Links Count:** 430
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# OneNoteLoader\#

_class _langchain\_community.document\_loaders.onenote.OneNoteLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/onenote.html#OneNoteLoader)\#     

Bases: [`BaseLoader`](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader"), `BaseModel`

Load pages from OneNote notebooks.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _access\_token _: str_ _ = ''_\#     

Personal access token

_param _auth\_with\_token _: bool_ _ = False_\#     

Whether to authenticate with a token or not. Defaults to False.

_param _authority\_url _: str_ _ = 'https://login.microsoftonline.com/consumers/'_\#     

A URL that identifies a token authority

_param _notebook\_name _: str | None_ _ = None_\#     

Filter on notebook name

_param _object\_ids _: List\[str\] | None_ _ = None_\#     

The IDs of the objects to load data from.

_param _onenote\_api\_base\_url _: str_ _ = 'https://graph.microsoft.com/v1.0/me/onenote'_\#     

URL of Microsoft Graph API for OneNote

_param _page\_title _: str | None_ _ = None_\#     

Filter on section name

_param _section\_name _: str | None_ _ = None_\#     

Filter on section name

_param _settings _: \_OneNoteGraphSettings_ _\[Optional\]_\#     

Settings for the Microsoft Graph API client.

_param _token\_path _: Annotated\[Path, PathType\(path\_type=file\)\]__ = PosixPath\('/home/runner/.credentials/onenote\_graph\_token.txt'\)_\#     

Path to the file where the access token is stored

Constraints:     

  * **path\_type** = file

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/onenote.html#OneNoteLoader.lazy_load)\#     

Get pages from OneNote notebooks.

Returns:     

  * page\_content

  * metadata          * title

Return type:     

A list of Documents with attributes

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

Examples using OneNoteLoader

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

  * [Microsoft OneNote](https://python.langchain.com/docs/integrations/document_loaders/microsoft_onenote/)

__On this page