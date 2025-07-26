# DocugamiLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.docugami.DocugamiLoader.html
**Word Count:** 217
**Links Count:** 437
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# DocugamiLoader\#

_class _langchain\_community.document\_loaders.docugami.DocugamiLoader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/docugami.html#DocugamiLoader)\#     

Bases: [`BaseLoader`](https://python.langchain.com/api_reference/core/document_loaders/langchain_core.document_loaders.base.BaseLoader.html#langchain_core.document_loaders.base.BaseLoader "langchain_core.document_loaders.base.BaseLoader"), `BaseModel`

Deprecated since version 0.0.24: Use `:class:`~docugami_langchain.DocugamiLoader`` instead. It will not be removed until langchain-community==1.0.

Load from Docugami.

To use, you should have the `dgml-utils` python package installed.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _access\_token _: str | None_ _ = None_\#     

The Docugami API access token to use.

_param _api _: str_ _ = 'https://api.docugami.com/v1preview1'_\#     

The Docugami API endpoint to use.

_param _docset\_id _: str | None_ _ = None_\#     

The Docugami API docset ID to use.

_param _document\_ids _: Sequence\[str\] | None_ _ = None_\#     

The Docugami API document IDs to use.

_param _file\_paths _: Sequence\[Path | str\] | None_ _\[Required\]_\#     

The local file paths to use.

_param _include\_project\_metadata\_in\_doc\_metadata _: bool_ _ = True_\#     

Set to True if you want to include the project metadata in the doc metadata.

_param _include\_xml\_tags _: bool_ _ = False_\#     

Set to true for XML tags in chunk output text.

_param _max\_metadata\_length _: int_ _ = 512_\#     

Max length of metadata text returned.

_param _max\_text\_length _: int_ _ = 4096_\#     

Max length of chunk text returned.

_param _min\_text\_length _: int_ _ = 32_\#     

Threshold under which chunks are appended to next to avoid over-chunking.

_param _parent\_hierarchy\_levels _: int_ _ = 0_\#     

Set appropriately to get parent chunks using the chunk hierarchy.

_param _parent\_id\_key _: str_ _ = 'doc\_id'_\#     

Metadata key for parent doc ID.

_param _sub\_chunk\_tables _: bool_ _ = False_\#     

Set to True to return sub-chunks within tables.

_param _whitespace\_normalize\_text _: bool_ _ = True_\#     

Set to False if you want to full whitespace formatting in the original XML doc, including indentation.

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/docugami.html#DocugamiLoader.load)\#     

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

__On this page