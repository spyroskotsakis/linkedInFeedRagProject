# GoogleDriveLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/drive/langchain_google_community.drive.GoogleDriveLoader.html
**Word Count:** 192
**Links Count:** 143
**Scraped:** 2025-07-21 07:59:55
**Status:** completed

---

# GoogleDriveLoader\#

_class _langchain\_google\_community.drive.GoogleDriveLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/drive.html#GoogleDriveLoader)\#     

Bases: [`BaseLoader`](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader"), `BaseModel`

Load Google Docs from Google Drive.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _credentials _: Any_ _ = None_\#     

Your own google credentials created via your own mechanism

_param _credentials\_path _: Path_ _ = PosixPath\('/home/runner/.credentials/credentials.json'\)_\#     

Path to the credentials file.

_param _document\_ids _: List\[str\] | None_ _ = None_\#     

The document ids to load from.

_param _file\_ids _: List\[str\] | None_ _ = None_\#     

The file ids to load from.

_param _file\_loader\_cls _: Any_ _ = None_\#     

The file loader class to use.

_param _file\_loader\_kwargs _: Dict\[str, Any\]__ = \{\}_\#     

The file loader kwargs to use.

_param _file\_types _: Sequence\[str\] | None_ _ = None_\#     

The file types to load. Only applies when folder\_id is given.

_param _folder\_id _: str | None_ _ = None_\#     

The folder id to load from.

_param _load\_auth _: bool_ _ = False_\#     

Whether to load authorization identities.

_param _load\_extended\_metadata _: bool_ _ = False_\#     

Whether to load extended metadata.

_param _load\_trashed\_files _: bool_ _ = False_\#     

Whether to load trashed files. Only applies when folder\_id is given.

_param _recursive _: bool_ _ = False_\#     

Whether to load recursively. Only applies when folder\_id is given.

_param _scopes _: List\[str\]__ = \['https://www.googleapis.com/auth/drive.file'\]_\#     

The credential scopes to use for Google Drive API access. Default is drive.file scope.

_param _service\_account\_key _: Path_ _ = PosixPath\('/home/runner/.credentials/keys.json'\)_\#     

Path to the service account key file.

_param _token\_path _: Path_ _ = PosixPath\('/home/runner/.credentials/token.json'\)_\#     

Path to the token file.

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/drive.html#GoogleDriveLoader.load)\#     

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

VALID\_SCOPES _: ClassVar\[Tuple\[str, ...\]\]__ = \('https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive.readonly', 'https://www.googleapis.com/auth/drive.meet.readonly', 'https://www.googleapis.com/auth/drive.metadata.readonly', 'https://www.googleapis.com/auth/drive.metadata'\)_\#     

__On this page