# CombineProcessor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.services.combine_service.CombineProcessor.html
**Word Count:** 12
**Links Count:** 124
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# CombineProcessor\#

_class _langchain\_experimental.video\_captioning.services.combine\_service.CombineProcessor\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _verbose : bool = True_,     _char\_limit : int = 20_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/combine_service.html#CombineProcessor)\#     

Methods

`__init__`\(llm\[, verbose, char\_limit\]\) |    ---|---   `process`\(video\_models, audio\_models\[, ...\]\) |       Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **verbose** \(_bool_\)

  * **char\_limit** \(_int_\)

\_\_init\_\_\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _verbose : bool = True_,     _char\_limit : int = 20_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/combine_service.html#CombineProcessor.__init__)\#     

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **verbose** \(_bool_\)

  * **char\_limit** \(_int_\)

process\(

    _video\_models : List\[[VideoModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.VideoModel.html#langchain_experimental.video_captioning.models.VideoModel "langchain_experimental.video_captioning.models.VideoModel")\]_,     _audio\_models : List\[[AudioModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.AudioModel.html#langchain_experimental.video_captioning.models.AudioModel "langchain_experimental.video_captioning.models.AudioModel")\]_,     _run\_manager : [CallbackManagerForChainRun](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") | None = None_, \) → List\[[CaptionModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.CaptionModel.html#langchain_experimental.video_captioning.models.CaptionModel "langchain_experimental.video_captioning.models.CaptionModel")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/video_captioning/services/combine_service.html#CombineProcessor.process)\#     

Parameters:     

  * **video\_models** \(_List_ _\[_[_VideoModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.VideoModel.html#langchain_experimental.video_captioning.models.VideoModel "langchain_experimental.video_captioning.models.VideoModel") _\]_\)

  * **audio\_models** \(_List_ _\[_[_AudioModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.AudioModel.html#langchain_experimental.video_captioning.models.AudioModel "langchain_experimental.video_captioning.models.AudioModel") _\]_\)

  * **run\_manager** \([_CallbackManagerForChainRun_](https://python.langchain.com/api_reference/core/callbacks/langchain_core.callbacks.manager.CallbackManagerForChainRun.html#langchain_core.callbacks.manager.CallbackManagerForChainRun "langchain_core.callbacks.manager.CallbackManagerForChainRun") _|__None_\)

Return type:     

_List_\[[_CaptionModel_](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.CaptionModel.html#langchain_experimental.video_captioning.models.CaptionModel "langchain_experimental.video_captioning.models.CaptionModel")\]

__On this page