# Blob — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html
**Word Count:** 365
**Links Count:** 141
**Scraped:** 2025-07-21 07:56:55
**Status:** completed

---

# Blob\#

_class _langchain\_core.documents.base.Blob[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/base.html#Blob)\#     

Bases: [`BaseMedia`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.BaseMedia.html#langchain_core.documents.base.BaseMedia "langchain_core.documents.base.BaseMedia")

Blob represents raw data by either reference or value.

Provides an interface to materialize the blob in different representations, and help to decouple the development of data loaders from the downstream parsing of the raw data.

Inspired by: <https://developer.mozilla.org/en-US/docs/Web/API/Blob>

Example: Initialize a blob from in-memory data

>  >     from langchain_core.documents import Blob >      >     blob = Blob.from_data("Hello, world!") >      >     # Read the blob as a string >     print(blob.as_string()) >      >     # Read the blob as bytes >     print(blob.as_bytes()) >      >     # Read the blob as a byte stream >     with blob.as_bytes_io() as f: >         print(f.read()) >     

Example: Load from memory and specify mime-type and metadata

>  >     from langchain_core.documents import Blob >      >     blob = Blob.from_data( >         data="Hello, world!", >         mime_type="text/plain", >         metadata={"source": "https://example.com"} >     ) >     

Example: Load the blob from a file

>  >     from langchain_core.documents import Blob >      >     blob = Blob.from_path("path/to/file.txt") >      >     # Read the blob as a string >     print(blob.as_string()) >      >     # Read the blob as bytes >     print(blob.as_bytes()) >      >     # Read the blob as a byte stream >     with blob.as_bytes_io() as f: >         print(f.read()) >     

_param _data _: bytes | str | None_ _ = None_\#     

Raw data associated with the blob.

_param _encoding _: str_ _ = 'utf-8'_\#     

Encoding to use if decoding the bytes into a string.

Use utf-8 as default encoding, if decoding to string.

_param _id _: str | None_ _ = None_\#     

An optional identifier for the document.

Ideally this should be unique across the document collection and formatted as a UUID, but this will not be enforced.

Added in version 0.2.11.

Constraints:     

  * **coerce\_numbers\_to\_str** = True

_param _metadata _: dict_ _\[Optional\]_\#     

Arbitrary metadata associated with the content.

_param _mimetype _: str | None_ _ = None_\#     

MimeType not to be confused with a file extension.

_param _path _: PathLike | None_ _ = None_\#     

Location where the original content was found.

_classmethod _from\_data\(

    _data : str | bytes_,     _\*_ ,     _encoding : str = 'utf-8'_,     _mime\_type : str | None = None_,     _path : str | None = None_,     _metadata : dict | None = None_, \) → Blob[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/base.html#Blob.from_data)\#     

Initialize the blob from in-memory data.

Parameters:     

  * **data** \(_str_ _|__bytes_\) – the in-memory data associated with the blob

  * **encoding** \(_str_\) – Encoding to use if decoding the bytes into a string

  * **mime\_type** \(_str_ _|__None_\) – if provided, will be set as the mime-type of the data

  * **path** \(_str_ _|__None_\) – if provided, will be set as the source from which the data came

  * **metadata** \(_dict_ _|__None_\) – Metadata to associate with the blob

Returns:     

Blob instance

Return type:     

_Blob_

_classmethod _from\_path\(

    _path : str | PurePath_,     _\*_ ,     _encoding : str = 'utf-8'_,     _mime\_type : str | None = None_,     _guess\_type : bool = True_,     _metadata : dict | None = None_, \) → Blob[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/base.html#Blob.from_path)\#     

Load the blob from a path like object.

Parameters:     

  * **path** \(_str_ _|__PurePath_\) – path like object to file to be read

  * **encoding** \(_str_\) – Encoding to use if decoding the bytes into a string

  * **mime\_type** \(_str_ _|__None_\) – if provided, will be set as the mime-type of the data

  * **guess\_type** \(_bool_\) – If True, the mimetype will be guessed from the file extension, if a mime-type was not provided

  * **metadata** \(_dict_ _|__None_\) – Metadata to associate with the blob

Returns:     

Blob instance

Return type:     

_Blob_

as\_bytes\(\) → bytes[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/base.html#Blob.as_bytes)\#     

Read data as bytes.

Return type:     

bytes

as\_bytes\_io\(\) → Generator\[BytesIO | BufferedReader, None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/base.html#Blob.as_bytes_io)\#     

Read data as a byte stream.

Return type:     

Generator\[Union\[BytesIO, BufferedReader\], None, None\]

as\_string\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/documents/base.html#Blob.as_string)\#     

Read data as a string.

Return type:     

str

_property _source _: str | None_\#     

The source location of the blob as string if known otherwise none.

If a path is associated with the blob, it will default to the path location.

Unless explicitly set via a metadata field called “source”, in which case that value will be used instead.

Examples using Blob

  * [Google](https://python.langchain.com/docs/integrations/providers/google/)

  * [Google Cloud Document AI](https://python.langchain.com/docs/integrations/document_transformers/google_docai/)

  * [How to create a custom Document Loader](https://python.langchain.com/docs/how_to/document_loader_custom/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)