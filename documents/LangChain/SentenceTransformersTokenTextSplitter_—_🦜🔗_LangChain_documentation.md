# SentenceTransformersTokenTextSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/sentence_transformers/langchain_text_splitters.sentence_transformers.SentenceTransformersTokenTextSplitter.html
**Word Count:** 252
**Links Count:** 127
**Scraped:** 2025-07-21 07:58:35
**Status:** completed

---

# SentenceTransformersTokenTextSplitter\#

_class _langchain\_text\_splitters.sentence\_transformers.SentenceTransformersTokenTextSplitter\(

    _chunk\_overlap : int = 50_,     _model\_name : str = 'sentence-transformers/all-mpnet-base-v2'_,     _tokens\_per\_chunk : int | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/sentence_transformers.html#SentenceTransformersTokenTextSplitter)\#     

Splitting text to tokens using sentence model tokenizer.

Create a new TextSplitter.

Methods

`__init__`\(\[chunk\_overlap, model\_name, ...\]\) | Create a new TextSplitter.   ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `count_tokens`\(\*, text\) | Counts the number of tokens in the given text.   `create_documents`\(texts\[, metadatas\]\) | Create documents from a list of texts.   `from_huggingface_tokenizer`\(tokenizer, \*\*kwargs\) | Text splitter that uses HuggingFace tokenizer to count length.   `from_tiktoken_encoder`\(\[encoding\_name, ...\]\) | Text splitter that uses tiktoken encoder to count length.   `split_documents`\(documents\) | Split documents.   `split_text`\(text\) | Splits the input text into smaller components by splitting text on tokens.   `transform_documents`\(documents, \*\*kwargs\) | Transform sequence of documents by splitting them.      Parameters:     

  * **chunk\_overlap** \(_int_\)

  * **model\_name** \(_str_\)

  * **tokens\_per\_chunk** \(_Optional_ _\[__int_ _\]_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _chunk\_overlap : int = 50_,     _model\_name : str = 'sentence-transformers/all-mpnet-base-v2'_,     _tokens\_per\_chunk : int | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/sentence_transformers.html#SentenceTransformersTokenTextSplitter.__init__)\#     

Create a new TextSplitter.

Parameters:     

  * **chunk\_overlap** \(_int_\)

  * **model\_name** \(_str_\)

  * **tokens\_per\_chunk** \(_int_ _|__None_\)

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

count\_tokens\(

    _\*_ ,     _text : str_, \) → int[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/sentence_transformers.html#SentenceTransformersTokenTextSplitter.count_tokens)\#     

Counts the number of tokens in the given text.

This method encodes the input text using a private \_encode method and calculates the total number of tokens in the encoded result.

Parameters:     

**text** \(_str_\) – The input text for which the token count is calculated.

Returns:     

The number of tokens in the encoded text.

Return type:     

int

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

split\_text\(

    _text : str_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/sentence_transformers.html#SentenceTransformersTokenTextSplitter.split_text)\#     

Splits the input text into smaller components by splitting text on tokens.

This method encodes the input text using a private \_encode method, then strips the start and stop token IDs from the encoded result. It returns the processed segments as a list of strings.

Parameters:     

**text** \(_str_\) – The input text to be split.

Returns:     

A list of string components derived from the input text after encoding and processing.

Return type:     

List\[str\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Transform sequence of documents by splitting them.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using SentenceTransformersTokenTextSplitter

  * [How to split text by tokens ](https://python.langchain.com/docs/how_to/split_by_token/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)