# load_dataset — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.loading.load_dataset.html
**Word Count:** 32
**Links Count:** 124
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# load\_dataset\#

langchain.evaluation.loading.load\_dataset\(_uri : str_\) → list\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/evaluation/loading.html#load_dataset)\#     

Load a dataset from the [LangChainDatasets on HuggingFace](https://huggingface.co/LangChainDatasets).

Parameters:     

**uri** \(_str_\) – The uri of the dataset to load.

Returns:     

A list of dictionaries, each representing a row in the dataset.

Return type:     

list\[dict\]

**Prerequisites**               pip install datasets     

Examples               from langchain.evaluation import load_dataset     ds = load_dataset("llm-math")     

__On this page