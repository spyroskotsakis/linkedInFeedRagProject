# get_default_label_configs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.labelstudio_callback.get_default_label_configs.html
**Word Count:** 30
**Links Count:** 185
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# get\_default\_label\_configs\#

langchain\_community.callbacks.labelstudio\_callback.get\_default\_label\_configs\(

    _mode : str | [LabelStudioMode](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.labelstudio_callback.LabelStudioMode.html#langchain_community.callbacks.labelstudio_callback.LabelStudioMode "langchain_community.callbacks.labelstudio_callback.LabelStudioMode")_, \) → Tuple\[str, [LabelStudioMode](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.labelstudio_callback.LabelStudioMode.html#langchain_community.callbacks.labelstudio_callback.LabelStudioMode "langchain_community.callbacks.labelstudio_callback.LabelStudioMode")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/labelstudio_callback.html#get_default_label_configs)\#     

Get default Label Studio configs for the given mode.

Parameters:     

**mode** \(_str_ _|_[_LabelStudioMode_](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.labelstudio_callback.LabelStudioMode.html#langchain_community.callbacks.labelstudio_callback.LabelStudioMode "langchain_community.callbacks.labelstudio_callback.LabelStudioMode")\) – Label Studio mode \(“prompt” or “chat”\)

Return type:     

_Tuple_\[str, [_LabelStudioMode_](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.labelstudio_callback.LabelStudioMode.html#langchain_community.callbacks.labelstudio_callback.LabelStudioMode "langchain_community.callbacks.labelstudio_callback.LabelStudioMode")\]

Returns: Tuple of Label Studio config and mode

__On this page