# UpTrainDataSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.uptrain_callback.UpTrainDataSchema.html
**Word Count:** 103
**Links Count:** 209
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# UpTrainDataSchema\#

_class _langchain\_community.callbacks.uptrain\_callback.UpTrainDataSchema\(_project\_name : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/uptrain_callback.html#UpTrainDataSchema)\#     

The UpTrain data schema for tracking evaluation results.

Parameters:     

**project\_name** \(_str_\) – The project name to be shown in UpTrain dashboard.

project\_name\#     

The project name to be shown in UpTrain dashboard.

Type:     

str

uptrain\_results\#     

Dictionary to store evaluation results.

Type:     

DefaultDict\[str, Any\]

eval\_types\#     

Set to store the types of evaluations.

Type:     

Set\[str\]

query\#     

Query for the RAG evaluation.

Type:     

str

context\#     

Context for the RAG evaluation.

Type:     

str

response\#     

Response for the RAG evaluation.

Type:     

str

old\_context\#     

Old context nodes for Context Conciseness evaluation.

Type:     

List\[str\]

new\_context\#     

New context nodes for Context Conciseness evaluation.

Type:     

List\[str\]

context\_conciseness\_run\_id\#     

Run ID for Context Conciseness evaluation.

Type:     

str

multi\_queries\#     

List of multi queries for Multi Query evaluation.

Type:     

List\[str\]

multi\_query\_run\_id\#     

Run ID for Multi Query evaluation.

Type:     

str

multi\_query\_daugher\_run\_id\#     

Run ID for Multi Query daughter evaluation.

Type:     

str

Initialize the UpTrain data schema.

Methods

`__init__`\(project\_name\) | Initialize the UpTrain data schema.   ---|---      \_\_init\_\_\(_project\_name : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/uptrain_callback.html#UpTrainDataSchema.__init__)\#     

Initialize the UpTrain data schema.

Parameters:     

**project\_name** \(_str_\)

Return type:     

None

__On this page