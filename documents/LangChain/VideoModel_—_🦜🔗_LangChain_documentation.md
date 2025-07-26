# VideoModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.VideoModel.html
**Word Count:** 14
**Links Count:** 119
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# VideoModel\#

_class _langchain\_experimental.video\_captioning.models.VideoModel\(

    _start\_time : int_,     _end\_time : int_,     _image\_description : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#VideoModel)\#     

Attributes

`end_time` |    ---|---   `image_description` |    `start_time` |       Methods

`__init__`\(start\_time, end\_time, image\_description\) |    ---|---   `from_srt`\(start\_time, end\_time, \*args\) |    `similarity_score`\(other\) |       Parameters:     

  * **start\_time** \(_int_\)

  * **end\_time** \(_int_\)

  * **image\_description** \(_str_\)

\_\_init\_\_\(

    _start\_time : int_,     _end\_time : int_,     _image\_description : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#VideoModel.__init__)\#     

Parameters:     

  * **start\_time** \(_int_\)

  * **end\_time** \(_int_\)

  * **image\_description** \(_str_\)

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

similarity\_score\(

    _other : VideoModel_, \) → float[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#VideoModel.similarity_score)\#     

Parameters:     

**other** \(_VideoModel_\)

Return type:     

float

__On this page