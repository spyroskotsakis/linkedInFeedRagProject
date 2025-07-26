# create_model_v2 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.pydantic.create_model_v2.html
**Word Count:** 75
**Links Count:** 167
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# create\_model\_v2\#

langchain\_core.utils.pydantic.create\_model\_v2\(

    _model\_name : str_,     _\*_ ,     _module\_name : str | None = None_,     _field\_definitions : dict\[str, Any\] | None = None_,     _root : Any | None = None_, \) → type\[BaseModel\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/pydantic.html#create_model_v2)\#     

Create a pydantic model with the given field definitions.

Attention

Please do not use outside of langchain packages. This API is subject to change at any time.

Parameters:     

  * **model\_name** \(_str_\) – The name of the model.

  * **module\_name** \(_str_ _|__None_\) – The name of the module where the model is defined. This is used by Pydantic to resolve any forward references.

  * **field\_definitions** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – The field definitions for the model.

  * **root** \(_Any_ _|__None_\) – Type for a root model \(RootModel\)

Returns:     

The created model.

Return type:     

Type\[[BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)