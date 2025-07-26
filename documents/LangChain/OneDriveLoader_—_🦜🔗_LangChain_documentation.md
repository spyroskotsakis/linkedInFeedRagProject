# OneDriveLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.onedrive.OneDriveLoader.html
**Word Count:** 364
**Links Count:** 450
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# OneDriveLoader\#

_class _langchain\_community.document\_loaders.onedrive.OneDriveLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/onedrive.html#OneDriveLoader)\#     

Bases: [`SharePointLoader`](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.sharepoint.SharePointLoader.html#langchain_community.document_loaders.sharepoint.SharePointLoader "langchain_community.document_loaders.sharepoint.SharePointLoader")

Load documents from Microsoft OneDrive. Uses SharePointLoader under the hood.

_param _auth\_with\_token _: bool_ _ = False_\#     

Whether to authenticate with a token or not. Defaults to False.

_param _chunk\_size _: int | str_ _ = 5242880_\#     

Number of bytes to retrieve from each api call to the server. int or ‘auto’.

_param _document\_library\_id _: str_ _\[Required\]_\#     

The ID of the SharePoint document library to load data from.

_param _drive\_id _: str_ _\[Required\]_\#     

The ID of the OneDrive drive to load data from.

_param _folder\_id _: str | None_ _ = None_\#     

The ID of the folder to load data from.

_param _folder\_path _: str | None_ _ = None_\#     

The path to the folder to load data from.

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

_param _load\_auth _: bool | None_ _ = False_\#     

Whether to load authorization identities.

_param _load\_extended\_metadata _: bool | None_ _ = False_\#     

Whether to load extended metadata. Size, Owner and full\_path.

_param _modified\_since _: datetime | None_ _ = None_\#     

Only fetch documents modified since given datetime. The datetime object must be timezone aware.

_param _object\_ids _: List\[str\] | None_ _ = None_\#     

The IDs of the objects to load data from.

_param _recursive _: bool_ _ = False_\#     

Should the loader recursively load subfolders?

_param _settings _: \_O365Settings_ _\[Optional\]_\#     

Settings for the Office365 API client.

_param _token\_path _: Path_ _ = PosixPath\('/home/runner/.credentials/o365\_token.txt'\)_\#     

The path to the token to make api calls

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

authorized\_identities\(

    _file\_id : str_, \) → List\#     

Retrieve the access identities \(user/group emails\) for a given file. :param file\_id: The ID of the file. :type file\_id: str

Returns:     

A list of group names \(email addresses\) that have     

access to the file.

Return type:     

List

Parameters:     

**file\_id** \(_str_\)

get\_extended\_metadata\(

    _file\_id : str_, \) → Dict\#     

Retrieve extended metadata for a file in SharePoint. As of today, following fields are supported in the extended metadata: \- size: size of the source file. \- owner: display name of the owner of the source file. \- full\_path: pretty human readable path of the source file. :param file\_id: The ID of the file. :type file\_id: str

Returns:     

A dictionary containing the extended metadata of the file,     

including size, owner, and full path.

Return type:     

dict

Parameters:     

**file\_id** \(_str_\)

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load documents lazily. Use this when working at a large scale. :Yields: _Document_ – A document object representing the parsed blob.

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

Examples using OneDriveLoader

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

  * [Microsoft OneDrive](https://python.langchain.com/docs/integrations/document_loaders/microsoft_onedrive/)

__On this page