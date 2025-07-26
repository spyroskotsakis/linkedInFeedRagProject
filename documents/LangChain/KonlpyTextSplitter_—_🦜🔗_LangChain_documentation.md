# KonlpyTextSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/konlpy/langchain_text_splitters.konlpy.KonlpyTextSplitter.html
**Word Count:** 139
**Links Count:** 123
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# KonlpyTextSplitter\#

_class _langchain\_text\_splitters.konlpy.KonlpyTextSplitter\(

    _separator : str = '\n\n'_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/konlpy.html#KonlpyTextSplitter)\#     

Splitting text using Konlpy package.

It is good for splitting Korean text.

Initialize the Konlpy text splitter.

Methods

`__init__`\(\[separator\]\) | Initialize the Konlpy text splitter.   ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `create_documents`\(texts\[, metadatas\]\) | Create documents from a list of texts.   `from_huggingface_tokenizer`\(tokenizer, \*\*kwargs\) | Text splitter that uses HuggingFace tokenizer to count length.   `from_tiktoken_encoder`\(\[encoding\_name, ...\]\) | Text splitter that uses tiktoken encoder to count length.   `split_documents`\(documents\) | Split documents.   `split_text`\(text\) | Split incoming text and return chunks.   `transform_documents`\(documents, \*\*kwargs\) | Transform sequence of documents by splitting them.      Parameters:     

  * **separator** \(_str_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _separator : str = '\n\n'_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/konlpy.html#KonlpyTextSplitter.__init__)\#     

Initialize the Konlpy text splitter.

Parameters:     

  * **separator** \(_str_\)

  * **kwargs** \(_Any_\)

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

    _texts : list\[str\]_,     _metadatas : list\[dict\[Any, Any\]\] | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Create documents from a list of texts.

Parameters:     

  * **texts** \(_list_ _\[__str_ _\]_\)

  * **metadatas** \(_list_ _\[__dict_ _\[__Any_ _,__Any_ _\]__\]__|__None_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_classmethod _from\_huggingface\_tokenizer\(

    _tokenizer : Any_,     _\*\* kwargs: Any_, \) → [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter")\#     

Text splitter that uses HuggingFace tokenizer to count length.

Parameters:     

  * **tokenizer** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter")

_classmethod _from\_tiktoken\_encoder\(

    _encoding\_name : str = 'gpt2'_,     _model\_name : str | None = None_,     _allowed\_special : Literal\['all'\] | Set\[str\] = \{\}_,     _disallowed\_special : Literal\['all'\] | Collection\[str\] = 'all'_,     _\*\* kwargs: Any_, \) → TS\#     

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

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Split documents.

Parameters:     

**documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_text\(_text : str_\) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/konlpy.html#KonlpyTextSplitter.split_text)\#     

Split incoming text and return chunks.

Parameters:     

**text** \(_str_\)

Return type:     

list\[str\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Transform sequence of documents by splitting them.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using KonlpyTextSplitter

  * [How to split text by tokens ](https://python.langchain.com/docs/how_to/split_by_token/)

__On this page