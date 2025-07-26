# CaptionProcessor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.services.caption_service.CaptionProcessor.html
**Word Count:** 12
**Links Count:** 122
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# CaptionProcessor\#

_class _langchain\_experimental.video\_captioning.services.caption\_service.CaptionProcessor\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _verbose : bool = True_,     _similarity\_threshold : int = 80_,     _use\_unclustered\_models : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/caption_service.html#CaptionProcessor)\#     

Methods

`__init__`\(llm\[, verbose, ...\]\) |    ---|---   `process`\(video\_models\[, run\_manager\]\) |       Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **verbose** \(_bool_\)

  * **similarity\_threshold** \(_int_\)

  * **use\_unclustered\_models** \(_bool_\)

\_\_init\_\_\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _verbose : bool = True_,     _similarity\_threshold : int = 80_,     _use\_unclustered\_models : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/caption_service.html#CaptionProcessor.__init__)\#     

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **verbose** \(_bool_\)

  * **similarity\_threshold** \(_int_\)

  * **use\_unclustered\_models** \(_bool_\)

Return type:     

None

process\(

    _video\_models : List\[[VideoModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.VideoModel.html#langchain_experimental.video_captioning.models.VideoModel "langchain_experimental.video_captioning.models.VideoModel")\]_,     _run\_manager : [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") | None = None_, \) → List\[[VideoModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.VideoModel.html#langchain_experimental.video_captioning.models.VideoModel "langchain_experimental.video_captioning.models.VideoModel")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/caption_service.html#CaptionProcessor.process)\#     

Parameters:     

  * **video\_models** \(_List_ _\[_[_VideoModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.VideoModel.html#langchain_experimental.video_captioning.models.VideoModel "langchain_experimental.video_captioning.models.VideoModel") _\]_\)

  * **run\_manager** \([_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") _|__None_\)

Return type:     

_List_\[[_VideoModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.VideoModel.html#langchain_experimental.video_captioning.models.VideoModel "langchain_experimental.video_captioning.models.VideoModel")\]

__On this page