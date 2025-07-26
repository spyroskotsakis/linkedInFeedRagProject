# ImageProcessor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.services.image_service.ImageProcessor.html
**Word Count:** 11
**Links Count:** 114
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# ImageProcessor\#

_class _langchain\_experimental.video\_captioning.services.image\_service.ImageProcessor\(

    _frame\_skip : int = -1_,     _threshold : int = 3000000_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/image_service.html#ImageProcessor)\#     

Methods

`__init__`\(\[frame\_skip, threshold\]\) |    ---|---   `process`\(video\_file\_path\[, run\_manager\]\) |       Parameters:     

  * **frame\_skip** \(_int_\)

  * **threshold** \(_int_\)

\_\_init\_\_\(

    _frame\_skip : int = -1_,     _threshold : int = 3000000_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/image_service.html#ImageProcessor.__init__)\#     

Parameters:     

  * **frame\_skip** \(_int_\)

  * **threshold** \(_int_\)

Return type:     

None

process\(

    _video\_file\_path : str_,     _run\_manager : [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") | None = None_, \) → list[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/image_service.html#ImageProcessor.process)\#     

Parameters:     

  * **video\_file\_path** \(_str_\)

  * **run\_manager** \([_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") _|__None_\)

Return type:     

list

__On this page