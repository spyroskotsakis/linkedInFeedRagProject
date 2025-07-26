# TokenTextSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html
**Word Count:** 220
**Links Count:** 131
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# TokenTextSplitter\#

_class _langchain\_text\_splitters.base.TokenTextSplitter\(

    _encoding\_name : str = 'gpt2'_,     _model\_name : str | None = None_,     _allowed\_special : Literal\['all'\] | Set\[str\] = \{\}_,     _disallowed\_special : Literal\['all'\] | Collection\[str\] = 'all'_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TokenTextSplitter)\#     

Splitting text to tokens using model tokenizer.

Create a new TextSplitter.

Methods

`__init__`\(\[encoding\_name, model\_name, ...\]\) | Create a new TextSplitter.   ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `create_documents`\(texts\[, metadatas\]\) | Create documents from a list of texts.   `from_huggingface_tokenizer`\(tokenizer, \*\*kwargs\) | Text splitter that uses HuggingFace tokenizer to count length.   `from_tiktoken_encoder`\(\[encoding\_name, ...\]\) | Text splitter that uses tiktoken encoder to count length.   `split_documents`\(documents\) | Split documents.   `split_text`\(text\) | Splits the input text into smaller chunks based on tokenization.   `transform_documents`\(documents, \*\*kwargs\) | Transform sequence of documents by splitting them.      Parameters:     

  * **encoding\_name** \(_str_\)

  * **model\_name** \(_Optional_ _\[__str_ _\]_\)

  * **allowed\_special** \(_Union_ _\[__Literal_ _\[__'all'__\]__,__AbstractSet_ _\[__str_ _\]__\]_\)

  * **disallowed\_special** \(_Union_ _\[__Literal_ _\[__'all'__\]__,__Collection_ _\[__str_ _\]__\]_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _encoding\_name : str = 'gpt2'_,     _model\_name : str | None = None_,     _allowed\_special : Literal\['all'\] | Set\[str\] = \{\}_,     _disallowed\_special : Literal\['all'\] | Collection\[str\] = 'all'_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TokenTextSplitter.__init__)\#     

Create a new TextSplitter.

Parameters:     

  * **encoding\_name** \(_str_\)

  * **model\_name** \(_str_ _|__None_\)

  * **allowed\_special** \(_Literal_ _\[__'all'__\]__|__~collections.abc.Set_ _\[__str_ _\]_\)

  * **disallowed\_special** \(_Literal_ _\[__'all'__\]__|__~collections.abc.Collection_ _\[__str_ _\]_\)

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

split\_text\(_text : str_\) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#TokenTextSplitter.split_text)\#     

Splits the input text into smaller chunks based on tokenization.

This method uses a custom tokenizer configuration to encode the input text into tokens, processes the tokens in chunks of a specified size with overlap, and decodes them back into text chunks. The splitting is performed using the split\_text\_on\_tokens function.

Parameters:     

**text** \(_str_\) – The input text to be split into smaller chunks.

Returns:     

A list of text chunks, where each chunk is derived from a portion of the input text based on the tokenization and chunking rules.

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

Examples using TokenTextSplitter

  * [Apache Doris](https://python.langchain.com/docs/integrations/vectorstores/apache_doris/)

  * [AzureAISearchRetriever](https://python.langchain.com/docs/integrations/retrievers/azure_ai_search/)

  * [How to handle long text when doing extraction](https://python.langchain.com/docs/how_to/extraction_long_text/)

  * [How to split text by tokens ](https://python.langchain.com/docs/how_to/split_by_token/)

  * [StarRocks](https://python.langchain.com/docs/integrations/vectorstores/starrocks/)

__On this page