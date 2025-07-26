# OpenVINOBgeEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.openvino.OpenVINOBgeEmbeddings.html
**Word Count:** 174
**Links Count:** 239
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# OpenVINOBgeEmbeddings\#

_class _langchain\_community.embeddings.openvino.OpenVINOBgeEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/openvino.html#OpenVINOBgeEmbeddings)\#     

Bases: [`OpenVINOEmbeddings`](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.openvino.OpenVINOEmbeddings.html#langchain_community.embeddings.openvino.OpenVINOEmbeddings "langchain_community.embeddings.openvino.OpenVINOEmbeddings")

OpenVNO BGE embedding models.

Bge Example:                    from langchain_community.embeddings import OpenVINOBgeEmbeddings          model_name = "BAAI/bge-large-en-v1.5"     model_kwargs = {'device': 'CPU'}     encode_kwargs = {'normalize_embeddings': True}     ov = OpenVINOBgeEmbeddings(         model_name_or_path=model_name,         model_kwargs=model_kwargs,         encode_kwargs=encode_kwargs     )     

Initialize the sentence\_transformer.

_param _embed\_instruction _: str_ _ = ''_\#     

Instruction to use for embedding document.

_param _encode\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments to pass when calling the encode method of the model.

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

Keyword arguments to pass to the model.

_param _model\_name\_or\_path _: str_ _\[Required\]_\#     

HuggingFace model id.

_param _ov\_model _: Any_ _ = None_\#     

OpenVINO model object.

_param _query\_instruction _: str_ _ = 'Represent this question for searching relevant passages: '_\#     

Instruction to use for embedding query.

_param _show\_progress _: bool_ _ = False_\#     

Whether to show a progress bar.

_param _tokenizer _: Any_ _ = None_\#     

Tokenizer for embedding model.

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\]\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(_text : str_\) → list\[float\]\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/openvino.html#OpenVINOBgeEmbeddings.embed_documents)\#     

Compute doc embeddings using a HuggingFace transformer model.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – The list of texts to embed.

Returns:     

List of embeddings, one for each text.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/openvino.html#OpenVINOBgeEmbeddings.embed_query)\#     

Compute query embeddings using a HuggingFace transformer model.

Parameters:     

**text** \(_str_\) – The text to embed.

Returns:     

Embeddings for the text.

Return type:     

_List_\[float\]

encode\(

    _sentences : Any_,     _batch\_size : int = 4_,     _show\_progress\_bar : bool = False_,     _convert\_to\_numpy : bool = True_,     _convert\_to\_tensor : bool = False_,     _mean\_pooling : bool = False_,     _normalize\_embeddings : bool = True_, \) → Any\#     

Computes sentence embeddings.

Parameters:     

  * **sentences** \(_Any_\) – the sentences to embed.

  * **batch\_size** \(_int_\) – the batch size used for the computation.

  * **show\_progress\_bar** \(_bool_\) – Whether to output a progress bar.

  * **convert\_to\_numpy** \(_bool_\) – Whether the output should be a list of numpy vectors.

  * **convert\_to\_tensor** \(_bool_\) – Whether the output should be one large tensor.

  * **mean\_pooling** \(_bool_\) – Whether to pool returned vectors.

  * **normalize\_embeddings** \(_bool_\) – Whether to normalize returned vectors.

Returns:     

By default, a 2d numpy array with shape \[num\_inputs, output\_dimension\].

Return type:     

_Any_

save\_model\(_model\_path : str_\) → bool\#     

Parameters:     

**model\_path** \(_str_\)

Return type:     

bool

Examples using OpenVINOBgeEmbeddings

  * [OpenVINO](https://python.langchain.com/docs/integrations/text_embedding/openvino/)

__On this page