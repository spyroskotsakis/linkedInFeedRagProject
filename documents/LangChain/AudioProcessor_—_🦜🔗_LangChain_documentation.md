# AudioProcessor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.services.audio_service.AudioProcessor.html
**Word Count:** 10
**Links Count:** 114
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# AudioProcessor\#

_class _langchain\_experimental.video\_captioning.services.audio\_service.AudioProcessor\(

    _api\_key : str_,     _output\_audio\_path : str = 'output\_audio.mp3'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/audio_service.html#AudioProcessor)\#     

Methods

`__init__`\(api\_key\[, output\_audio\_path\]\) |    ---|---   `process`\(video\_file\_path\[, run\_manager\]\) |       Parameters:     

  * **api\_key** \(_str_\)

  * **output\_audio\_path** \(_str_\)

\_\_init\_\_\(

    _api\_key : str_,     _output\_audio\_path : str = 'output\_audio.mp3'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/audio_service.html#AudioProcessor.__init__)\#     

Parameters:     

  * **api\_key** \(_str_\)

  * **output\_audio\_path** \(_str_\)

process\(

    _video\_file\_path : str_,     _run\_manager : [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") | None = None_, \) → list[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/audio_service.html#AudioProcessor.process)\#     

Parameters:     

  * **video\_file\_path** \(_str_\)

  * **run\_manager** \([_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") _|__None_\)

Return type:     

list

__On this page