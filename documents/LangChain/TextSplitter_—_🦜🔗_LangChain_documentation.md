# TextSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html
**Word Count:** 240
**Links Count:** 131
**Scraped:** 2025-07-21 07:57:45
**Status:** completed

---

# TextSplitter\#

_class _langchain\_text\_splitters.base.TextSplitter\(_chunk\_size: int = 4000, chunk\_overlap: int = 200, length\_function: ~typing.Callable\[\[str\], int\] = <built-in function len>, keep\_separator: bool | ~typing.Literal\['start', 'end'\] = False, add\_start\_index: bool = False, strip\_whitespace: bool = True_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TextSplitter)\#     

Interface for splitting text into chunks.

Create a new TextSplitter.

Parameters:     

  * **chunk\_size** \(_int_\) – Maximum size of chunks to return

  * **chunk\_overlap** \(_int_\) – Overlap in characters between chunks

  * **length\_function** \(_Callable_ _\[__\[__str_ _\]__,__int_ _\]_\) – Function that measures the length of given chunks

  * **keep\_separator** \(_Union_ _\[__bool_ _,__Literal_ _\[__'start'__,__'end'__\]__\]_\) – Whether to keep the separator and where to place it in each corresponding chunk \(True=’start’\)

  * **add\_start\_index** \(_bool_\) – If True, includes chunk’s start index in metadata

  * **strip\_whitespace** \(_bool_\) – If True, strips whitespace from the start and end of every document

Methods

`__init__`\(\[chunk\_size, chunk\_overlap, ...\]\) | Create a new TextSplitter.   ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `create_documents`\(texts\[, metadatas\]\) | Create documents from a list of texts.   `from_huggingface_tokenizer`\(tokenizer, \*\*kwargs\) | Text splitter that uses HuggingFace tokenizer to count length.   `from_tiktoken_encoder`\(\[encoding\_name, ...\]\) | Text splitter that uses tiktoken encoder to count length.   `split_documents`\(documents\) | Split documents.   `split_text`\(text\) | Split text into multiple components.   `transform_documents`\(documents, \*\*kwargs\) | Transform sequence of documents by splitting them.      \_\_init\_\_\(_chunk\_size: int = 4000, chunk\_overlap: int = 200, length\_function: ~typing.Callable\[\[str\], int\] = <built-in function len>, keep\_separator: bool | ~typing.Literal\['start', 'end'\] = False, add\_start\_index: bool = False, strip\_whitespace: bool = True_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TextSplitter.__init__)\#     

Create a new TextSplitter.

Parameters:     

  * **chunk\_size** \(_int_\) – Maximum size of chunks to return

  * **chunk\_overlap** \(_int_\) – Overlap in characters between chunks

  * **length\_function** \(_Callable_ _\[__\[__str_ _\]__,__int_ _\]_\) – Function that measures the length of given chunks

  * **keep\_separator** \(_bool_ _|__Literal_ _\[__'start'__,__'end'__\]_\) – Whether to keep the separator and where to place it in each corresponding chunk \(True=’start’\)

  * **add\_start\_index** \(_bool_\) – If True, includes chunk’s start index in metadata

  * **strip\_whitespace** \(_bool_\) – If True, strips whitespace from the start and end of every document

Return type:     

None

_async _atransform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Asynchronously transform a list of documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of Documents to be transformed.

  * **kwargs** \(_Any_\)

Returns:     

A sequence of transformed Documents.

Return type:     

Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

create\_documents\(

    _texts : list\[str\]_,     _metadatas : list\[dict\[Any, Any\]\] | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TextSplitter.create_documents)\#     

Create documents from a list of texts.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\[__Any_ _,__Any_ _\]__\]__|__None_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_classmethod _from\_huggingface\_tokenizer\(

    _tokenizer : Any_,     _\*\* kwargs: Any_, \) → TextSplitter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TextSplitter.from_huggingface_tokenizer)\#     

Text splitter that uses HuggingFace tokenizer to count length.

Parameters:     

  * **tokenizer** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

_TextSplitter_

_classmethod _from\_tiktoken\_encoder\(

    _encoding\_name : str = 'gpt2'_,     _model\_name : str | None = None_,     _allowed\_special : Literal\['all'\] | Set\[str\] = \{\}_,     _disallowed\_special : Literal\['all'\] | Collection\[str\] = 'all'_,     _\*\* kwargs: Any_, \) → TS[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TextSplitter.from_tiktoken_encoder)\#     

Text splitter that uses tiktoken encoder to count length.

Parameters:     

  * **encoding\_name** \(_str_\)

  * **model\_name** \(_str_ _|__None_\)

  * **allowed\_special** \(_Literal_ _\[__'all'__\]__|__~collections.abc.Set_ _\[__str_ _\]_\)

  * **disallowed\_special** \(_Literal_ _\[__'all'__\]__|__~collections.abc.Collection_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_TS_

split\_documents\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TextSplitter.split_documents)\#     

Split documents.

Parameters:     

**documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_abstractmethod _split\_text\(_text : str_\) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TextSplitter.split_text)\#     

Split text into multiple components.

Parameters:     

**text** \(_str_\)

Return type:     

list\[str\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TextSplitter.transform_documents)\#     

Transform sequence of documents by splitting them.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page