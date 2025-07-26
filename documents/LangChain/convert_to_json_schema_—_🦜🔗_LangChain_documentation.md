# convert_to_json_schema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.function_calling.convert_to_json_schema.html
**Word Count:** 16
**Links Count:** 170
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# convert\_to\_json\_schema\#

langchain\_core.utils.function\_calling.convert\_to\_json\_schema\(

    _schema : dict\[str, Any\] | type\[[BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\] | Callable | [BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")_,     _\*_ ,     _strict : bool | None = None_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/function_calling.html#convert_to_json_schema)\#     

Convert a schema representation to a JSON schema.

Parameters:     

  * **schema** \(_Union_ _\[__dict_ _\[__str_ _,__Any_ _\]__,__type_ _\[_[_BaseModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel") _\]__,__Callable_ _,_[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool") _\]_\)

  * **strict** \(_Optional_ _\[__bool_ _\]_\)

Return type:     

dict\[str, Any\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)