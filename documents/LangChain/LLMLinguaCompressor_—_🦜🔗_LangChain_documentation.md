# LLMLinguaCompressor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_compressors/langchain_community.document_compressors.llmlingua_filter.LLMLinguaCompressor.html
**Word Count:** 267
**Links Count:** 147
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# LLMLinguaCompressor\#

_class _langchain\_community.document\_compressors.llmlingua\_filter.LLMLinguaCompressor[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_compressors/llmlingua_filter.html#LLMLinguaCompressor)\#     

Bases: [`BaseDocumentCompressor`](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.compressor.BaseDocumentCompressor.html#langchain_core.documents.compressor.BaseDocumentCompressor "langchain_core.documents.compressor.BaseDocumentCompressor")

Compress using LLMLingua Project.

[microsoft/LLMLingua](https://github.com/microsoft/LLMLingua)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _additional\_compress\_kwargs _: dict_ _ = \{'condition\_compare': True, 'condition\_in\_question': 'after', 'context\_budget': '+100', 'dynamic\_context\_compression\_ratio': 0.4, 'reorder\_context': 'sort'\}_\#     

Extra compression arguments

_param _device\_map _: str_ _ = 'cuda'_\#     

The device to use for llm lingua

_param _instruction _: str_ _ = 'Given this documents, please answer the final question'_\#     

The instruction for the LLM

_param _lingua _: Any_ _ = None_\#     

The instance of the llm linqua

_param _model\_configuration _: dict_ _\[Optional\]__\(alias 'model\_config'\)_\#     

Custom configuration for the model

_param _model\_name _: str_ _ = 'NousResearch/Llama-2-7b-hf'_\#     

The hugging face model to use

_param _open\_api\_config _: dict_ _\[Optional\]_\#     

open\_api configuration

_param _rank\_method _: str_ _ = 'longllmlingua'_\#     

The ranking method to use

_param _target\_token _: int_ _ = 300_\#     

The target number of compressed tokens

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

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _query : str_,     _callbacks : list\[[BaseCallbackHandler](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler")\] | [BaseCallbackManager](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") | None = None_, \) → Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_compressors/llmlingua_filter.html#LLMLinguaCompressor.compress_documents)\#     

Compress documents using BAAI/bge-reranker models.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – A sequence of documents to compress.

  * **query** \(_str_\) – The query to use for compressing the documents.

  * **callbacks** \(_list_ _\[_[_BaseCallbackHandler_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackHandler.html#langchain_core.callbacks.base.BaseCallbackHandler "langchain_core.callbacks.base.BaseCallbackHandler") _\]__|_[_BaseCallbackManager_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.base.BaseCallbackManager.html#langchain_core.callbacks.base.BaseCallbackManager "langchain_core.callbacks.base.BaseCallbackManager") _|__None_\) – Callbacks to run during the compression process.

Returns:     

A sequence of compressed documents.

Return type:     

_Sequence_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

extract\_ref\_id\_tuples\_and\_clean\(

    _contents : List\[str\]_, \) → List\[Tuple\[str, int\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_compressors/llmlingua_filter.html#LLMLinguaCompressor.extract_ref_id_tuples_and_clean)\#     

Extracts reference IDs from the contents and cleans up the ref tags.

This function processes a list of strings, searching for reference ID tags at the beginning and end of each string. When a ref tag is found, it is removed from the string, and its ID is recorded. If no ref ID is found, a generic ID of “-1” is assigned.

The search for ref tags is performed only at the beginning and end of the string, with the assumption that there will be at most one ref ID per string. Malformed ref tags are handled gracefully.

Parameters:     

**contents** \(_List_ _\[__str_ _\]_\) – A list of contents to be processed.

Returns:     

The cleaned string and the associated ref ID.

Return type:     

List\[Tuple\[str, int\]\]

Examples               >>> strings_list = [             '<#ref0#> Example content <#ref0#>',             'Content with no ref ID.'         ]     >>> extract_ref_id_tuples_and_clean(strings_list)     [('Example content', 0), ('Content with no ref ID.', -1)]     

Examples using LLMLinguaCompressor

  * [LLMLingua Document Compressor](https://python.langchain.com/docs/integrations/retrievers/llmlingua/)

__On this page