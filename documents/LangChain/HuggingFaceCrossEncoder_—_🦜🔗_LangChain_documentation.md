# HuggingFaceCrossEncoder — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.huggingface.HuggingFaceCrossEncoder.html
**Word Count:** 49
**Links Count:** 109
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# HuggingFaceCrossEncoder\#

_class _langchain\_community.cross\_encoders.huggingface.HuggingFaceCrossEncoder[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cross_encoders/huggingface.html#HuggingFaceCrossEncoder)\#     

Bases: `BaseModel`, [`BaseCrossEncoder`](https://python.langchain.com/api_reference/langchain/retrievers/langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder.html#langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder "langchain.retrievers.document_compressors.cross_encoder.BaseCrossEncoder")

HuggingFace cross encoder models.

Example               from langchain_community.cross_encoders import HuggingFaceCrossEncoder          model_name = "BAAI/bge-reranker-base"     model_kwargs = {'device': 'cpu'}     hf = HuggingFaceCrossEncoder(         model_name=model_name,         model_kwargs=model_kwargs     )     

Initialize the sentence\_transformer.

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments to pass to the model.

_param _model\_name _: str_ _ = 'BAAI/bge-reranker-base'_\#     

Model name to use.

score\(

    _text\_pairs : List\[Tuple\[str, str\]\]_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/cross_encoders/huggingface.html#HuggingFaceCrossEncoder.score)\#     

Compute similarity scores using a HuggingFace transformer model.

Parameters:     

**text\_pairs** \(_List_ _\[__Tuple_ _\[__str_ _,__str_ _\]__\]_\) – The list of text text\_pairs to score the similarity.

Returns:     

List of scores, one for each pair.

Return type:     

_List_\[float\]

Examples using HuggingFaceCrossEncoder

  * [Cross Encoder Reranker](https://python.langchain.com/docs/integrations/document_transformers/cross_encoder_reranker/)

__On this page