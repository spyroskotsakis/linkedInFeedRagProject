# RecursiveCharacterTextSplitter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html
**Word Count:** 424
**Links Count:** 190
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# RecursiveCharacterTextSplitter\#

_class _langchain\_text\_splitters.character.RecursiveCharacterTextSplitter\(

    _separators : list\[str\] | None = None_,     _keep\_separator : bool | Literal\['start', 'end'\] = True_,     _is\_separator\_regex : bool = False_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/character.html#RecursiveCharacterTextSplitter)\#     

Splitting text by recursively look at characters.

Recursively tries to split by different characters to find one that works.

Create a new TextSplitter.

Methods

`__init__`\(\[separators, keep\_separator, ...\]\) | Create a new TextSplitter.   ---|---   `atransform_documents`\(documents, \*\*kwargs\) | Asynchronously transform a list of documents.   `create_documents`\(texts\[, metadatas\]\) | Create documents from a list of texts.   `from_huggingface_tokenizer`\(tokenizer, \*\*kwargs\) | Text splitter that uses HuggingFace tokenizer to count length.   `from_language`\(language, \*\*kwargs\) | Return an instance of this class based on a specific language.   `from_tiktoken_encoder`\(\[encoding\_name, ...\]\) | Text splitter that uses tiktoken encoder to count length.   `get_separators_for_language`\(language\) | Retrieve a list of separators specific to the given language.   `split_documents`\(documents\) | Split documents.   `split_text`\(text\) | Split the input text into smaller chunks based on predefined separators.   `transform_documents`\(documents, \*\*kwargs\) | Transform sequence of documents by splitting them.      Parameters:     

  * **separators** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\)

  * **keep\_separator** \(_Union_ _\[__bool_ _,__Literal_ _\[__'start'__,__'end'__\]__\]_\)

  * **is\_separator\_regex** \(_bool_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _separators : list\[str\] | None = None_,     _keep\_separator : bool | Literal\['start', 'end'\] = True_,     _is\_separator\_regex : bool = False_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/character.html#RecursiveCharacterTextSplitter.__init__)\#     

Create a new TextSplitter.

Parameters:     

  * **separators** \(_list_ _\[__str_ _\]__|__None_\)

  * **keep\_separator** \(_bool_ _|__Literal_ _\[__'start'__,__'end'__\]_\)

  * **is\_separator\_regex** \(_bool_\)

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

_classmethod _from\_language\(

    _language : [Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")_,     _\*\* kwargs: Any_, \) → RecursiveCharacterTextSplitter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/character.html#RecursiveCharacterTextSplitter.from_language)\#     

Return an instance of this class based on a specific language.

This method initializes the text splitter with language-specific separators.

Parameters:     

  * **language** \([_Language_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")\) – The language to configure the text splitter for.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments to customize the splitter.

Returns:     

An instance of the text splitter configured for the specified language.

Return type:     

RecursiveCharacterTextSplitter

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

    _language : [Language](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/character.html#RecursiveCharacterTextSplitter.get_separators_for_language)\#     

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

split\_text\(

    _text : str_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/character.html#RecursiveCharacterTextSplitter.split_text)\#     

Split the input text into smaller chunks based on predefined separators.

Parameters:     

**text** \(_str_\) – The input text to be split.

Returns:     

A list of text chunks obtained after splitting.

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

Examples using RecursiveCharacterTextSplitter

  * [Activeloop Deep Memory](https://python.langchain.com/docs/integrations/retrievers/activeloop/)

  * [Apache Cassandra](https://python.langchain.com/docs/integrations/vectorstores/cassandra/)

  * [ApertureDB](https://python.langchain.com/docs/integrations/vectorstores/aperturedb/)

  * [Azure Cosmos DB No SQL](https://python.langchain.com/docs/integrations/vectorstores/azure_cosmos_db_no_sql/)

  * [Build a Local RAG Application](https://python.langchain.com/docs/tutorials/local_rag/)

  * [Build a PDF ingestion and Question/Answering system](https://python.langchain.com/docs/tutorials/pdf_qa/)

  * [Build a Query Analysis System](https://python.langchain.com/docs/tutorials/query_analysis/)

  * [Build a Retrieval Augmented Generation \(RAG\) App](https://python.langchain.com/docs/tutorials/rag/)

  * [Build an Agent with AgentExecutor \(Legacy\)](https://python.langchain.com/docs/how_to/agent_executor/)

  * [Cohere reranker](https://python.langchain.com/docs/integrations/retrievers/cohere-reranker/)

  * [Conversational RAG](https://python.langchain.com/docs/tutorials/qa_chat_history/)

  * [Cross Encoder Reranker](https://python.langchain.com/docs/integrations/document_transformers/cross_encoder_reranker/)

  * [DashScope Reranker](https://python.langchain.com/docs/integrations/document_transformers/dashscope_rerank/)

  * [FlashRank reranker](https://python.langchain.com/docs/integrations/retrievers/flashrank-reranker/)

  * [Google Cloud Vertex AI Reranker](https://python.langchain.com/docs/integrations/document_transformers/google_cloud_vertexai_rerank/)

  * [Google Vertex AI Vector Search](https://python.langchain.com/docs/integrations/vectorstores/google_vertex_ai_vector_search/)

  * [How to add chat history](https://python.langchain.com/docs/how_to/qa_chat_history_how_to/)

  * [How to add retrieval to chatbots](https://python.langchain.com/docs/how_to/chatbots_retrieval/)

  * [How to add scores to retriever results](https://python.langchain.com/docs/how_to/add_scores_retriever/)

  * [How to get a RAG application to add citations](https://python.langchain.com/docs/how_to/qa_citations/)

  * [How to get your RAG application to return sources](https://python.langchain.com/docs/how_to/qa_sources/)

  * [How to handle cases where no queries are generated](https://python.langchain.com/docs/how_to/query_no_queries/)

  * [How to handle multiple queries when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_queries/)

  * [How to handle multiple retrievers when doing query analysis](https://python.langchain.com/docs/how_to/query_multiple_retrievers/)

  * [How to recursively split text by characters](https://python.langchain.com/docs/how_to/recursive_text_splitter/)

  * [How to retrieve using multiple vectors per document](https://python.langchain.com/docs/how_to/multi_vector/)

  * [How to split Markdown by Headers](https://python.langchain.com/docs/how_to/markdown_header_metadata_splitter/)

  * [How to split by HTML header ](https://python.langchain.com/docs/how_to/HTML_header_metadata_splitter/)

  * [How to split by HTML sections](https://python.langchain.com/docs/how_to/HTML_section_aware_splitter/)

  * [How to split code](https://python.langchain.com/docs/how_to/code_splitter/)

  * [How to split text by tokens ](https://python.langchain.com/docs/how_to/split_by_token/)

  * [How to stream results from your RAG application](https://python.langchain.com/docs/how_to/qa_streaming/)

  * [How to use the MultiQueryRetriever](https://python.langchain.com/docs/how_to/MultiQueryRetriever/)

  * [How to use the Parent Document Retriever](https://python.langchain.com/docs/how_to/parent_document_retriever/)

  * [Image captions](https://python.langchain.com/docs/integrations/document_loaders/image_captions/)

  * [Jina Reranker](https://python.langchain.com/docs/integrations/document_transformers/jina_rerank/)

  * [LLMLingua Document Compressor](https://python.langchain.com/docs/integrations/retrievers/llmlingua/)

  * [Load docs](https://python.langchain.com/docs/versions/migrating_chains/retrieval_qa/)

  * [Maritalk](https://python.langchain.com/docs/integrations/chat/maritalk/)

  * [OpenVINO Reranker](https://python.langchain.com/docs/integrations/document_transformers/openvino_rerank/)

  * [RAGatouille](https://python.langchain.com/docs/integrations/providers/ragatouille/)

  * [RankLLM Reranker](https://python.langchain.com/docs/integrations/document_transformers/rankllm-reranker/)

  * [RePhraseQuery](https://python.langchain.com/docs/integrations/retrievers/re_phrase/)

  * [Source Code](https://python.langchain.com/docs/integrations/document_loaders/source_code/)

  * [UpTrain](https://python.langchain.com/docs/integrations/callbacks/uptrain/)

  * [Vearch](https://python.langchain.com/docs/integrations/vectorstores/vearch/)

  * [Volcengine Reranker](https://python.langchain.com/docs/integrations/document_transformers/volcengine_rerank/)

  * [VoyageAI Reranker](https://python.langchain.com/docs/integrations/document_transformers/voyageai-reranker/)

  * [Yellowbrick](https://python.langchain.com/docs/integrations/vectorstores/yellowbrick/)

  * [YouTube audio](https://python.langchain.com/docs/integrations/document_loaders/youtube_audio/)

  * [Zep](https://python.langchain.com/docs/integrations/vectorstores/zep/)

  * [Zep Cloud](https://python.langchain.com/docs/integrations/vectorstores/zep_cloud/)

  * [viking DB](https://python.langchain.com/docs/integrations/vectorstores/vikingdb/)

__On this page