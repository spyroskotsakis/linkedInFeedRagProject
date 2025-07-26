# ArceeWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.ArceeWrapper.html
**Word Count:** 168
**Links Count:** 268
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# ArceeWrapper\#

_class _langchain\_community.utilities.arcee.ArceeWrapper\(

    _arcee\_api\_key : str | SecretStr_,     _arcee\_api\_url : str_,     _arcee\_api\_version : str_,     _model\_kwargs : Dict\[str, Any\] | None_,     _model\_name : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arcee.html#ArceeWrapper)\#     

Wrapper for Arcee API.

For more details, see: <https://www.arcee.ai/>

Initialize ArceeWrapper.

Parameters:     

  * **arcee\_api\_key** \(_str_ _|__SecretStr_\) – API key for Arcee API.

  * **arcee\_api\_url** \(_str_\) – URL for Arcee API.

  * **arcee\_api\_version** \(_str_\) – Version of Arcee API.

  * **model\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Keyword arguments for Arcee API.

  * **model\_name** \(_str_\) – Name of an Arcee model.

Methods

`__init__`\(arcee\_api\_key, arcee\_api\_url, ...\) | Initialize ArceeWrapper.   ---|---   `generate`\(prompt, \*\*kwargs\) | Generate text from Arcee DALM.   `retrieve`\(query, \*\*kwargs\) | Retrieve \{size\} contexts with your retriever for a given query   `validate_model_training_status`\(\) |       \_\_init\_\_\(

    _arcee\_api\_key : str | SecretStr_,     _arcee\_api\_url : str_,     _arcee\_api\_version : str_,     _model\_kwargs : Dict\[str, Any\] | None_,     _model\_name : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arcee.html#ArceeWrapper.__init__)\#     

Initialize ArceeWrapper.

Parameters:     

  * **arcee\_api\_key** \(_str_ _|__SecretStr_\) – API key for Arcee API.

  * **arcee\_api\_url** \(_str_\) – URL for Arcee API.

  * **arcee\_api\_version** \(_str_\) – Version of Arcee API.

  * **model\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Keyword arguments for Arcee API.

  * **model\_name** \(_str_\) – Name of an Arcee model.

generate\(

    _prompt : str_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arcee.html#ArceeWrapper.generate)\#     

Generate text from Arcee DALM.

Parameters:     

  * **prompt** \(_str_\) – Prompt to generate text from.

  * **size** – The max number of context results to retrieve. Defaults to 3. \(Can be less if filters are provided\).

  * **filters** – Filters to apply to the context dataset.

  * **kwargs** \(_Any_\)

Return type:     

str

retrieve\(

    _query : str_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arcee.html#ArceeWrapper.retrieve)\#     

Retrieve \{size\} contexts with your retriever for a given query

Parameters:     

  * **query** \(_str_\) – Query to submit to the model

  * **size** – The max number of context results to retrieve. Defaults to 3. \(Can be less if filters are provided\).

  * **filters** – Filters to apply to the context dataset.

  * **kwargs** \(_Any_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

validate\_model\_training\_status\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arcee.html#ArceeWrapper.validate_model_training_status)\#     

Return type:     

None

__On this page