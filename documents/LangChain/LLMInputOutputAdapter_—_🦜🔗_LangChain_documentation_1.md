# LLMInputOutputAdapter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.bedrock.LLMInputOutputAdapter.html
**Word Count:** 45
**Links Count:** 302
**Scraped:** 2025-07-21 08:11:13
**Status:** completed

---

# LLMInputOutputAdapter\#

_class _langchain\_community.llms.bedrock.LLMInputOutputAdapter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/bedrock.html#LLMInputOutputAdapter)\#     

Adapter class to prepare the inputs from Langchain to a format that LLM model expects.

It also provides helper function to extract the generated text from the model response.

Attributes

`provider_to_output_key_map` |    ---|---      Methods

`aprepare_output_stream`\(provider, response\[, ...\]\) |    ---|---   `prepare_input`\(provider, model\_kwargs\[, ...\]\) |    `prepare_output`\(provider, response\) |    `prepare_output_stream`\(provider, response\[, ...\]\) |       _classmethod _aprepare\_output\_stream\(

    _provider : str_,     _response : Any_,     _stop : List\[str\] | None = None_, \) → AsyncIterator\[[GenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/bedrock.html#LLMInputOutputAdapter.aprepare_output_stream)\#     

Parameters:     

  * **provider** \(_str_\)

  * **response** \(_Any_\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

_AsyncIterator_\[[_GenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk")\]

_classmethod _prepare\_input\(

    _provider : str_,     _model\_kwargs : Dict\[str, Any\]_,     _prompt : str | None = None_,     _system : str | None = None_,     _messages : List\[Dict\] | None = None_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/bedrock.html#LLMInputOutputAdapter.prepare_input)\#     

Parameters:     

  * **provider** \(_str_\)

  * **model\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **prompt** \(_str_ _|__None_\)

  * **system** \(_str_ _|__None_\)

  * **messages** \(_List_ _\[__Dict_ _\]__|__None_\)

Return type:     

_Dict_\[str, _Any_\]

_classmethod _prepare\_output\(

    _provider : str_,     _response : Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/bedrock.html#LLMInputOutputAdapter.prepare_output)\#     

Parameters:     

  * **provider** \(_str_\)

  * **response** \(_Any_\)

Return type:     

dict

_classmethod _prepare\_output\_stream\(

    _provider : str_,     _response : Any_,     _stop : List\[str\] | None = None_,     _messages\_api : bool = False_, \) → Iterator\[[GenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/bedrock.html#LLMInputOutputAdapter.prepare_output_stream)\#     

Parameters:     

  * **provider** \(_str_\)

  * **response** \(_Any_\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

  * **messages\_api** \(_bool_\)

Return type:     

_Iterator_\[[_GenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk")\]

__On this page