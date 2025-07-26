# QuantizedBiEncoderEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.optimum_intel.QuantizedBiEncoderEmbeddings.html
**Word Count:** 218
**Links Count:** 223
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# QuantizedBiEncoderEmbeddings\#

_class _langchain\_community.embeddings.optimum\_intel.QuantizedBiEncoderEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/optimum_intel.html#QuantizedBiEncoderEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

Quantized bi-encoders embedding models.

Please ensure that you have installed optimum-intel and ipex.

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

Example:

from langchain\_community.embeddings import QuantizedBiEncoderEmbeddings

model\_name = “Intel/bge-small-en-v1.5-rag-int8-static” encode\_kwargs = \{‘normalize\_embeddings’: True\} hf = QuantizedBiEncoderEmbeddings\(

> model\_name, encode\_kwargs=encode\_kwargs, query\_instruction=”Represent this sentence for searching relevant passages: “

\)

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/optimum_intel.html#QuantizedBiEncoderEmbeddings.embed_documents)\#     

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

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/optimum_intel.html#QuantizedBiEncoderEmbeddings.embed_query)\#     

Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

_List_\[float\]

load\_model\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/optimum_intel.html#QuantizedBiEncoderEmbeddings.load_model)\#     

Return type:     

None

Examples using QuantizedBiEncoderEmbeddings

  * [Embedding Documents using Optimized and Quantized Embedders](https://python.langchain.com/docs/integrations/text_embedding/optimum_intel/)

  * [Intel](https://python.langchain.com/docs/integrations/providers/intel/)

__On this page