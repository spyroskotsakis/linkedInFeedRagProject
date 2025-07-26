# VectorStoreIndexWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/indexes/langchain.indexes.vectorstore.VectorStoreIndexWrapper.html
**Word Count:** 235
**Links Count:** 108
**Scraped:** 2025-07-21 07:49:01
**Status:** completed

---

# VectorStoreIndexWrapper\#

_class _langchain.indexes.vectorstore.VectorStoreIndexWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/indexes/vectorstore.html#VectorStoreIndexWrapper)\#     

Bases: `BaseModel`

Wrapper around a vectorstore for easy access.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _vectorstore _: [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_ _\[Required\]_\#     

_async _aquery\(

    _question : str_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None = None_,     _retriever\_kwargs : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/indexes/vectorstore.html#VectorStoreIndexWrapper.aquery)\#     

Asynchronously query the vectorstore using the provided LLM.

Parameters:     

  * **question** \(_str_\) – The question or prompt to query.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _|__None_\) – The language model to use. Must not be None.

  * **retriever\_kwargs** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional keyword arguments for the retriever.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments forwarded to the chain.

Returns:     

The asynchronous result string from the RetrievalQA chain.

Return type:     

str

_async _aquery\_with\_sources\(

    _question : str_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None = None_,     _retriever\_kwargs : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/indexes/vectorstore.html#VectorStoreIndexWrapper.aquery_with_sources)\#     

Asynchronously query the vectorstore and retrieve the answer and sources.

Parameters:     

  * **question** \(_str_\) – The question or prompt to query.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _|__None_\) – The language model to use. Must not be None.

  * **retriever\_kwargs** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional keyword arguments for the retriever.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments forwarded to the chain.

Returns:     

A dictionary containing the answer and source documents.

Return type:     

dict

query\(

    _question : str_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None = None_,     _retriever\_kwargs : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/indexes/vectorstore.html#VectorStoreIndexWrapper.query)\#     

Query the vectorstore using the provided LLM.

Parameters:     

  * **question** \(_str_\) – The question or prompt to query.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _|__None_\) – The language model to use. Must not be None.

  * **retriever\_kwargs** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional keyword arguments for the retriever.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments forwarded to the chain.

Returns:     

The result string from the RetrievalQA chain.

Return type:     

str

query\_with\_sources\(

    _question : str_,     _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") | None = None_,     _retriever\_kwargs : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/indexes/vectorstore.html#VectorStoreIndexWrapper.query_with_sources)\#     

Query the vectorstore and retrieve the answer along with sources.

Parameters:     

  * **question** \(_str_\) – The question or prompt to query.

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel") _|__None_\) – The language model to use. Must not be None.

  * **retriever\_kwargs** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional keyword arguments for the retriever.

  * **\*\*kwargs** \(_Any_\) – Additional keyword arguments forwarded to the chain.

Returns:     

A dictionary containing the answer and source documents.

Return type:     

dict

__On this page