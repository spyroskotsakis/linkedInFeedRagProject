# LLMListwiseRerank — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.document_compressors.listwise_rerank.LLMListwiseRerank.html
**Word Count:** 204
**Links Count:** 141
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# LLMListwiseRerank\#

_class _langchain.retrievers.document\_compressors.listwise\_rerank.LLMListwiseRerank[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/retrievers/document_compressors/listwise_rerank.html#LLMListwiseRerank)\#     

Bases: [`BaseDocumentCompressor`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.compressor.BaseDocumentCompressor.html#langchain_core.documents.compressor.BaseDocumentCompressor "langchain_core.documents.compressor.BaseDocumentCompressor")

Document compressor that uses Zero-Shot Listwise Document Reranking.

Adapted from: <https://arxiv.org/pdf/2305.02156.pdf>

`LLMListwiseRerank` uses a language model to rerank a list of documents based on their relevance to a query.

**NOTE** : requires that underlying model implement `with_structured_output`.

Example usage:                    from langchain.retrievers.document_compressors.listwise_rerank import (         LLMListwiseRerank,     )     from langchain_core.documents import Document     from langchain_openai import ChatOpenAI          documents = [         Document("Sally is my friend from school"),         Document("Steve is my friend from home"),         Document("I didn't always like yogurt"),         Document("I wonder why it's called football"),         Document("Where's waldo"),     ]          reranker = LLMListwiseRerank.from_llm(         llm=ChatOpenAI(model="gpt-3.5-turbo"), top_n=3     )     compressed_docs = reranker.compress_documents(documents, "Who is steve")     assert len(compressed_docs) == 3     assert "Steve" in compressed_docs[0].page_content     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _reranker _: [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[dict, list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\]__\[Required\]_\#     

LLM-based reranker to use for filtering documents. Expected to take in a dict with ‘documents: Sequence\[Document\]’ and ‘query: str’ keys and output a List\[Document\].

_param _top\_n _: int_ _ = 3_\#     

Number of documents to return.

_classmethod _from\_llm\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _\*_ ,     _prompt : [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") | None = None_,     _\*\* kwargs: Any_, \) → LLMListwiseRerank[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/retrievers/document_compressors/listwise_rerank.html#LLMListwiseRerank.from_llm)\#     

Create a LLMListwiseRerank document compressor from a language model.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use for filtering. **Must implement BaseLanguageModel.with\_structured\_output\(\).**

  * **prompt** \([_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate") _|__None_\) – The prompt to use for the filter.

  * **kwargs** \(_Any_\) – Additional arguments to pass to the constructor.

Returns:     

A LLMListwiseRerank document compressor that uses the given language model.

Return type:     

_LLMListwiseRerank_

_async _acompress\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : Callbacks | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Async compress retrieved documents given the query context.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The retrieved documents.

  * **query** \(_str_\) – The query context.

  * **callbacks** \(_Optional_ _\[__Callbacks_ _\]_\) – Optional callbacks to run during compression.

Returns:     

The compressed documents.

Return type:     

Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

compress\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/retrievers/document_compressors/listwise_rerank.html#LLMListwiseRerank.compress_documents)\#     

Filter down documents based on their relevance to the query.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **query** \(_str_\)

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\)

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using LLMListwiseRerank

  * [How to do retrieval with contextual compression](https://python.langchain.com/docs/how_to/contextual_compression/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)