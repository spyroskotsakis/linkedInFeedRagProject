# ZhipuAIEmbeddings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.zhipuai.ZhipuAIEmbeddings.html
**Word Count:** 208
**Links Count:** 225
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# ZhipuAIEmbeddings\#

_class _langchain\_community.embeddings.zhipuai.ZhipuAIEmbeddings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/zhipuai.html#ZhipuAIEmbeddings)\#     

Bases: `BaseModel`, [`Embeddings`](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")

ZhipuAI embedding model integration.

Setup:

> To use, you should have the `zhipuai` python package installed, and the environment variable `ZHIPU_API_KEY` set with your API KEY. >  > More instructions about ZhipuAi Embeddings, you can get it from <https://open.bigmodel.cn/dev/api#vector> >      >      >     pip install -U zhipuai >     export ZHIPU_API_KEY="your-api-key" >     

Key init args — completion params:     

model: Optional\[str\]     

Name of ZhipuAI model to use.

api\_key: str     

Automatically inferred from env var ZHIPU\_API\_KEY if not provided.

See full list of supported init args and their descriptions in the params section.

Instantiate:

>  >     from langchain_community.embeddings import ZhipuAIEmbeddings >      >     embed = ZhipuAIEmbeddings( >         model="embedding-2", >         # api_key="...", >     ) >     

Embed single text:                    input_text = "The meaning of life is 42"     embed.embed_query(input_text)                    [-0.003832892, 0.049372625, -0.035413884, -0.019301128, 0.0068899863, 0.01248398, -0.022153955, 0.006623926, 0.00778216, 0.009558191, ...]     

Embed multiple text:                    input_texts = ["This is a test query1.", "This is a test query2."]     embed.embed_documents(input_texts)                    [         [0.0083934665, 0.037985895, -0.06684559, -0.039616987, 0.015481004, -0.023952313, ...],         [-0.02713102, -0.005470169, 0.032321047, 0.042484466, 0.023290444, 0.02170547, ...]     ]     

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_key _: str_ _\[Required\]_\#     

Automatically inferred from env var ZHIPU\_API\_KEY if not provided.

_param _dimensions _: int | None_ _ = None_\#     

The number of dimensions the resulting output embeddings should have.

Only supported in embedding-3 and later models.

_param _model _: str_ _ = 'embedding-2'_\#     

Model name

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

    _texts : List\[str\]_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/zhipuai.html#ZhipuAIEmbeddings.embed_documents)\#     

Embeds a list of text documents using the AutoVOT algorithm.

Parameters:     

**texts** \(_List_ _\[__str_ _\]_\) – A list of text documents to embed.

Returns:     

A list of embeddings for each document in the input list. Each embedding is represented as a list of float values.

Return type:     

_List_\[_List_\[float\]\]

embed\_query\(

    _text : str_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/zhipuai.html#ZhipuAIEmbeddings.embed_query)\#     

Embeds a text using the AutoVOT algorithm.

Parameters:     

**text** \(_str_\) – A text to embed.

Returns:     

Input document’s embedded list.

Return type:     

_List_\[float\]

__On this page