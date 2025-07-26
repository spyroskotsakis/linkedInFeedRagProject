# SemanticChunker — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/text_splitter/langchain_experimental.text_splitter.SemanticChunker.html
**Word Count:** 113
**Links Count:** 140
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# SemanticChunker\#

_class _langchain\_experimental.text\_splitter.SemanticChunker\(

    _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _buffer\_size : int = 1_,     _add\_start\_index : bool = False_,     _breakpoint\_threshold\_type : Literal\['percentile', 'standard\_deviation', 'interquartile', 'gradient'\] = 'percentile'_,     _breakpoint\_threshold\_amount : float | None = None_,     _number\_of\_chunks : int | None = None_,     _sentence\_split\_regex : str = '\(?<=\[.?\!\]\)\\\s+'_,     _min\_chunk\_size : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/text_splitter.html#SemanticChunker)\#     

Split the text based on semantic similarity.

Taken from Greg Kamradt’s wonderful notebook: [FullStackRetrieval-com/RetrievalTutorials](https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/main/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb)

All credits to him.

At a high level, this splits into sentences, then groups into groups of 3 sentences, and then merges one that are similar in the embedding space.

Methods

`__init__`\(embeddings\[, buffer\_size, ...\]\) |    ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `create_documents`\(texts\[, metadatas\]\) | Create documents from a list of texts.   `split_documents`\(documents\) | Split documents.   `split_text`\(text\) |    `transform_documents`\(documents, \*\*kwargs\) | Transform sequence of documents by splitting them.      Parameters:     

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **buffer\_size** \(_int_\)

  * **add\_start\_index** \(_bool_\)

  * **breakpoint\_threshold\_type** \(_Literal_ _\[__'percentile'__,__'standard\_deviation'__,__'interquartile'__,__'gradient'__\]_\)

  * **breakpoint\_threshold\_amount** \(_float_ _|__None_\)

  * **number\_of\_chunks** \(_int_ _|__None_\)

  * **sentence\_split\_regex** \(_str_\)

  * **min\_chunk\_size** \(_int_ _|__None_\)

\_\_init\_\_\(

    _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _buffer\_size : int = 1_,     _add\_start\_index : bool = False_,     _breakpoint\_threshold\_type : Literal\['percentile', 'standard\_deviation', 'interquartile', 'gradient'\] = 'percentile'_,     _breakpoint\_threshold\_amount : float | None = None_,     _number\_of\_chunks : int | None = None_,     _sentence\_split\_regex : str = '\(?<=\[.?\!\]\)\\\s+'_,     _min\_chunk\_size : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/text_splitter.html#SemanticChunker.__init__)\#     

Parameters:     

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\)

  * **buffer\_size** \(_int_\)

  * **add\_start\_index** \(_bool_\)

  * **breakpoint\_threshold\_type** \(_Literal_ _\[__'percentile'__,__'standard\_deviation'__,__'interquartile'__,__'gradient'__\]_\)

  * **breakpoint\_threshold\_amount** \(_float_ _|__None_\)

  * **number\_of\_chunks** \(_int_ _|__None_\)

  * **sentence\_split\_regex** \(_str_\)

  * **min\_chunk\_size** \(_int_ _|__None_\)

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

    _texts : List\[str\]_,     _metadatas : List\[dict\] | None = None_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/text_splitter.html#SemanticChunker.create_documents)\#     

Create documents from a list of texts.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\)

  * **metadatas** \(_List_ _\[__dict_ _\]__|__None_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_documents\(

    _documents : Iterable\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/text_splitter.html#SemanticChunker.split_documents)\#     

Split documents.

Parameters:     

**documents** \(_Iterable_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

split\_text\(_text : str_\) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/text_splitter.html#SemanticChunker.split_text)\#     

Parameters:     

**text** \(_str_\)

Return type:     

_List_\[str\]

transform\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*\* kwargs: Any_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/text_splitter.html#SemanticChunker.transform_documents)\#     

Transform sequence of documents by splitting them.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using SemanticChunker

  * [How to split text based on semantic similarity](https://python.langchain.com/docs/how_to/semantic-chunker/)

__On this page