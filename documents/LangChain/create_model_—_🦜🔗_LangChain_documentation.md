# create_model — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.pydantic.create_model.html
**Word Count:** 58
**Links Count:** 167
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# create\_model\#

langchain\_core.utils.pydantic.create\_model\(

    _model\_name : str_,     _module\_name : str | None = None_,     _/_ ,     _\*\* field\_definitions: Any_, \) → type\[BaseModel\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/pydantic.html#create_model)\#     

Create a pydantic model with the given field definitions.

Please use create\_model\_v2 instead of this function.

Parameters:     

  * **model\_name** \(_str_\) – The name of the model.

  * **module\_name** \(_str_ _|__None_\) – The name of the module where the model is defined. This is used by Pydantic to resolve any forward references.

  * **\*\*field\_definitions** \(_Any_\) – The field definitions for the model.

Returns:     

The created model.

Return type:     

Type\[[BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\]

__On this page   *[/]: Positional-only parameter separator (PEP 570)