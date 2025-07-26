# CaptionModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.CaptionModel.html
**Word Count:** 17
**Links Count:** 139
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# CaptionModel\#

_class _langchain\_experimental.video\_captioning.models.CaptionModel\(

    _start\_time : int_,     _end\_time : int_,     _closed\_caption : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#CaptionModel)\#     

Attributes

`closed_caption` |    ---|---   `end_time` |    `start_time` |       Methods

`__init__`\(start\_time, end\_time, closed\_caption\) |    ---|---   `add_subtitle_text`\(subtitle\_text\) |    `from_audio_model`\(audio\_model\) |    `from_srt`\(start\_time, end\_time, \*args\) |    `from_video_model`\(video\_model\) |    `to_srt_entry`\(index\) |       Parameters:     

  * **start\_time** \(_int_\)

  * **end\_time** \(_int_\)

  * **closed\_caption** \(_str_\)

\_\_init\_\_\(

    _start\_time : int_,     _end\_time : int_,     _closed\_caption : str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#CaptionModel.__init__)\#     

Parameters:     

  * **start\_time** \(_int_\)

  * **end\_time** \(_int_\)

  * **closed\_caption** \(_str_\)

Return type:     

None

add\_subtitle\_text\(

    _subtitle\_text : str_, \) → CaptionModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#CaptionModel.add_subtitle_text)\#     

Parameters:     

**subtitle\_text** \(_str_\)

Return type:     

_CaptionModel_

_classmethod _from\_audio\_model\(

    _audio\_model : [AudioModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.AudioModel.html#langchain_experimental.video_captioning.models.AudioModel "langchain_experimental.video_captioning.models.AudioModel")_, \) → CaptionModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#CaptionModel.from_audio_model)\#     

Parameters:     

**audio\_model** \([_AudioModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.AudioModel.html#langchain_experimental.video_captioning.models.AudioModel "langchain_experimental.video_captioning.models.AudioModel")\)

Return type:     

_CaptionModel_

_classmethod _from\_srt\(

    _start\_time : str_,     _end\_time : str_,     _\* args: Any_, \) → [BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\#     

Parameters:     

  * **start\_time** \(_str_\)

  * **end\_time** \(_str_\)

  * **args** \(_Any_\)

Return type:     

[_BaseModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")

_classmethod _from\_video\_model\(

    _video\_model : [VideoModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.VideoModel.html#langchain_experimental.video_captioning.models.VideoModel "langchain_experimental.video_captioning.models.VideoModel")_, \) → CaptionModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#CaptionModel.from_video_model)\#     

Parameters:     

**video\_model** \([_VideoModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.VideoModel.html#langchain_experimental.video_captioning.models.VideoModel "langchain_experimental.video_captioning.models.VideoModel")\)

Return type:     

_CaptionModel_

to\_srt\_entry\(_index : int_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/models.html#CaptionModel.to_srt_entry)\#     

Parameters:     

**index** \(_int_\)

Return type:     

str

__On this page