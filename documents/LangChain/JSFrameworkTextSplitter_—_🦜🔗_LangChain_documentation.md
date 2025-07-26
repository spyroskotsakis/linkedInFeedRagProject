# JSFrameworkTextSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/jsx/langchain_text_splitters.jsx.JSFrameworkTextSplitter.html
**Word Count:** 411
**Links Count:** 134
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# JSFrameworkTextSplitter\#

_class _langchain\_text\_splitters.jsx.JSFrameworkTextSplitter\(

    _separators : list\[str\] | None = None_,     _chunk\_size : int = 2000_,     _chunk\_overlap : int = 0_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/jsx.html#JSFrameworkTextSplitter)\#     

Text splitter that handles React \(JSX\), Vue, and Svelte code.

This splitter extends RecursiveCharacterTextSplitter to handle React \(JSX\), Vue, and Svelte code by: 1\. Detecting and extracting custom component tags from the text 2\. Using those tags as additional separators along with standard JS syntax

The splitter combines: \- Custom component tags as separators \(e.g. <Component, <div\) \- JavaScript syntax elements \(function, const, if, etc\) \- Standard text splitting on newlines

This allows chunks to break at natural boundaries in React, Vue, and Svelte component code.

Initialize the JS Framework text splitter.

Parameters:     

  * **separators** \(_list_ _\[__str_ _\]__|__None_\) – Optional list of custom separator strings to use

  * **chunk\_size** \(_int_\) – Maximum size of chunks to return

  * **chunk\_overlap** \(_int_\) – Overlap in characters between chunks

  * **\*\*kwargs** \(_Any_\) – Additional arguments to pass to parent class

Methods

`__init__`\(\[separators, chunk\_size, chunk\_overlap\]\) | Initialize the JS Framework text splitter.   ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `create_documents`\(texts\[, metadatas\]\) | Create documents from a list of texts.   `from_huggingface_tokenizer`\(tokenizer, \*\*kwargs\) | Text splitter that uses HuggingFace tokenizer to count length.   `from_language`\(language, \*\*kwargs\) | Return an instance of this class based on a specific language.   `from_tiktoken_encoder`\(\[encoding\_name, ...\]\) | Text splitter that uses tiktoken encoder to count length.   `get_separators_for_language`\(language\) | Retrieve a list of separators specific to the given language.   `split_documents`\(documents\) | Split documents.   `split_text`\(text\) | Split text into chunks.   `transform_documents`\(documents, \*\*kwargs\) | Transform sequence of documents by splitting them.      \_\_init\_\_\(

    _separators : list\[str\] | None = None_,     _chunk\_size : int = 2000_,     _chunk\_overlap : int = 0_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/jsx.html#JSFrameworkTextSplitter.__init__)\#     

Initialize the JS Framework text splitter.

Parameters:     

  * **separators** \(_list_ _\[__str_ _\]__|__None_\) – Optional list of custom separator strings to use

  * **chunk\_size** \(_int_\) – Maximum size of chunks to return

  * **chunk\_overlap** \(_int_\) – Overlap in characters between chunks

  * **\*\*kwargs** \(_Any_\) – Additional arguments to pass to parent class

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

_classmethod _from\_language\(

    _language : [Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")_,     _\*\* kwargs: Any_, \) → [RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html#langchain_text_splitters.character.RecursiveCharacterTextSplitter "langchain_text_splitters.character.RecursiveCharacterTextSplitter")\#     

Return an instance of this class based on a specific language.

This method initializes the text splitter with language-specific separators.

Parameters:     

  * **language** \([_Language_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")\) – The language to configure the text splitter for.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments to customize the splitter.

Returns:     

An instance of the text splitter configured for the specified language.

Return type:     

[RecursiveCharacterTextSplitter](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html#langchain_text_splitters.character.RecursiveCharacterTextSplitter "langchain_text_splitters.character.RecursiveCharacterTextSplitter")

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

_static _get\_separators\_for\_language\(

    _language : [Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")_, \) → list\[str\]\#     

Retrieve a list of separators specific to the given language.

Parameters:     

**language** \([_Language_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")\) – The language for which to get the separators.

Returns:     

A list of separators appropriate for the specified language.

Return type:     

List\[str\]

split\_documents\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Split documents.

Parameters:     

**documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_text\(_text : str_\) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/jsx.html#JSFrameworkTextSplitter.split_text)\#     

Split text into chunks.

This method splits the text into chunks by: \- Extracting unique opening component tags using regex \- Creating separators list with extracted tags and JS separators \- Splitting the text using the separators by calling the parent class method

Parameters:     

**text** \(_str_\) – String containing code to split

Returns:     

List of text chunks split on component and JS boundaries

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

__On this page