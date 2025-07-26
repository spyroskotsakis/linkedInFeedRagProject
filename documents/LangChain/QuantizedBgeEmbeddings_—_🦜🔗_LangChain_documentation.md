# QuantizedBgeEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.itrex.QuantizedBgeEmbeddings.html
**Word Count:** 223
**Links Count:** 223
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# QuantizedBgeEmbeddings\#

_class _langchain\_community.embeddings.itrex.QuantizedBgeEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/itrex.html#QuantizedBgeEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Leverage Itrex runtime to unlock the performance of compressed NLP models.

Please ensure that you have installed intel-extension-for-transformers.

Input:     

model\_name: str = Model name. max\_seq\_len: int = The maximum sequence length for tokenization. \(default 512\) pooling\_strategy: str =

> “mean” or “cls”, pooling strategy for the final layer. \(default “mean”\)

query\_instruction: Optional\[str\] =     

An instruction to add to the query before embedding. \(default None\)

document\_instruction: Optional\[str\] =     

An instruction to add to each document before embedding. \(default None\)

padding: Optional\[bool\] =     

Whether to add padding during tokenization or not. \(default True\)

model\_kwargs: Optional\[Dict\] =     

Parameters to add to the model during initialization. \(default \{\}\)

encode\_kwargs: Optional\[Dict\] =     

Parameters to add during the embedding forward pass. \(default \{\}\)

onnx\_file\_name: Optional\[str\] =     

File name of onnx optimized model which is exported by itrex. \(default “int8-model.onnx”\)

Example               from langchain_community.embeddings import QuantizedBgeEmbeddings          model_name = "Intel/bge-small-en-v1.5-sts-int8-static-inc"     encode_kwargs = {'normalize_embeddings': True}     hf = QuantizedBgeEmbeddings(         model_name,         encode_kwargs=encode_kwargs,         query_instruction="Represent this sentence for searching relevant passages: "     )     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\]\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(

    _text : str_, \) → list\[float\]\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\_documents\(

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/itrex.html#QuantizedBgeEmbeddings.embed_documents)\#     

Embed a list of text documents using the Optimized Embedder model.

Input:     

texts: List\[str\] = List of text documents to embed.

Output:     

List\[List\[float\]\] = The embeddings of each text document.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\)

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/itrex.html#QuantizedBgeEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

load\_model\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/itrex.html#QuantizedBgeEmbeddings.load_model)\#     

Return type:     

None

Examples using QuantizedBgeEmbeddings

  * [Intel](https://python.langchain.com/docs/integrations/providers/intel/)

  * [Intel® Extension for Transformers Quantized Text Embeddings](https://python.langchain.com/docs/integrations/text_embedding/itrex/)

__On this page