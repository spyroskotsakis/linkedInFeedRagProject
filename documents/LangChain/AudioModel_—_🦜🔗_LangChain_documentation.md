# AudioModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.AudioModel.html
**Word Count:** 13
**Links Count:** 113
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# AudioModel\#

_class _langchain\_experimental.video\_captioning.models.AudioModel\(

    _start\_time : int_,     _end\_time : int_,     _subtitle\_text : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#AudioModel)\#     

Attributes

`end_time` |    ---|---   `start_time` |    `subtitle_text` |       Methods

`__init__`\(start\_time, end\_time, subtitle\_text\) |    ---|---   `from_srt`\(start\_time, end\_time, \*args\) |       Parameters:     

  * **start\_time** \(_int_\)

  * **end\_time** \(_int_\)

  * **subtitle\_text** \(_str_\)

\_\_init\_\_\(

    _start\_time : int_,     _end\_time : int_,     _subtitle\_text : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#AudioModel.__init__)\#     

Parameters:     

  * **start\_time** \(_int_\)

  * **end\_time** \(_int_\)

  * **subtitle\_text** \(_str_\)

Return type:     

None

_classmethod _from\_srt\(

    _start\_time : str_,     _end\_time : str_,     _\* args: Any_, \) → [BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\#     

Parameters:     

  * **start\_time** \(_str_\)

  * **end\_time** \(_str_\)

  * **args** \(_Any_\)

Return type:     

[_BaseModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")

__On this page