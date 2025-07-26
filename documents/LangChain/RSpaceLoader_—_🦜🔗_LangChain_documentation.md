# RSpaceLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.rspace.RSpaceLoader.html
**Word Count:** 313
**Links Count:** 422
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# RSpaceLoader\#

_class _langchain\_community.document\_loaders.rspace.RSpaceLoader\(

    _global\_id : str_,     _api\_key : str | None = None_,     _url : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rspace.html#RSpaceLoader)\#     

Load content from RSpace notebooks, folders, documents or PDF Gallery files.

Map RSpace document <-> Langchain Document in 1-1. PDFs are imported using PyPDF.

Requirements are rspace\_client \(pip install rspace\_client\) and PyPDF if importing     

PDF docs \(pip install pypdf\).

api\_key: RSpace API key - can also be supplied as environment variable ‘RSPACE\_API\_KEY’ url: str The URL of your RSpace instance - can also be supplied as environment variable ‘RSPACE\_URL’ global\_id: str

> The global ID of the resource to load,

e.g. ‘SD12344’ \(a single document\); ‘GL12345’\(A PDF file in the gallery\); ‘NB4567’ \(a notebook\); ‘FL12244’ \(a folder\)

Methods

`__init__`\(global\_id\[, api\_key, url\]\) | api\_key: RSpace API key - can also be supplied as environment variable 'RSPACE\_API\_KEY' url: str The URL of your RSpace instance - can also be supplied as environment variable 'RSPACE\_URL' global\_id: str The global ID of the resource to load, e.g. 'SD12344' \(a single document\); 'GL12345'\(A PDF file in the gallery\); 'NB4567' \(a notebook\); 'FL12244' \(a folder\).   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `validate_environment`\(values\) | Validate that API key and URL exist in environment.      Parameters:     

  * **global\_id** \(_str_\)

  * **api\_key** \(_str_ _|__None_\)

  * **url** \(_str_ _|__None_\)

\_\_init\_\_\(

    _global\_id : str_,     _api\_key : str | None = None_,     _url : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rspace.html#RSpaceLoader.__init__)\#     

api\_key: RSpace API key - can also be supplied as environment variable ‘RSPACE\_API\_KEY’ url: str The URL of your RSpace instance - can also be supplied as environment variable ‘RSPACE\_URL’ global\_id: str

> The global ID of the resource to load,

e.g. ‘SD12344’ \(a single document\); ‘GL12345’\(A PDF file in the gallery\); ‘NB4567’ \(a notebook\); ‘FL12244’ \(a folder\)

Parameters:     

  * **global\_id** \(_str_\)

  * **api\_key** \(_str_ _|__None_\)

  * **url** \(_str_ _|__None_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rspace.html#RSpaceLoader.lazy_load)\#     

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

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/rspace.html#RSpaceLoader.validate_environment)\#     

Validate that API key and URL exist in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

Examples using RSpaceLoader

  * [\# replace these ids with some from your own research notes.](https://python.langchain.com/docs/integrations/document_loaders/rspace/)

__On this page