# LLMInputOutputAdapter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.bedrock.LLMInputOutputAdapter.html
**Word Count:** 45
**Links Count:** 115
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# LLMInputOutputAdapter\#

_class _langchain\_aws.llms.bedrock.LLMInputOutputAdapter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/llms/bedrock.html#LLMInputOutputAdapter)\#     

Adapter class to prepare the inputs from Langchain to a format that LLM model expects.

It also provides helper function to extract the generated text from the model response.

Attributes

`provider_to_output_key_map` |    ---|---      Methods

`aprepare_output_stream`\(provider, response\[, ...\]\) |    ---|---   `prepare_input`\(provider, model\_kwargs\[, ...\]\) |    `prepare_output`\(provider, response\) |    `prepare_output_stream`\(provider, response\[, ...\]\) |       _classmethod _aprepare\_output\_stream\(

    _provider : str_,     _response : Any_,     _stop : List\[str\] | None = None_,     _messages\_api : bool = False_,     _coerce\_content\_to\_string : bool = False_, \) → AsyncIterator\[[GenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") | [AIMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessageChunk.html#langchain_core.messages.ai.AIMessageChunk "langchain_core.messages.ai.AIMessageChunk")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/llms/bedrock.html#LLMInputOutputAdapter.aprepare_output_stream)\#     

Parameters:     

  * **provider** \(_str_\)

  * **response** \(_Any_\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

  * **messages\_api** \(_bool_\)

  * **coerce\_content\_to\_string** \(_bool_\)

Return type:     

_AsyncIterator_\[[_GenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") | [_AIMessageChunk_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessageChunk.html#langchain_core.messages.ai.AIMessageChunk "langchain_core.messages.ai.AIMessageChunk")\]

_classmethod _prepare\_input\(

    _provider : str_,     _model\_kwargs : Dict\[str, Any\]_,     _prompt : str | None = None_,     _system : str | None = None_,     _messages : List\[Dict\] | None = None_,     _tools : List\[[AnthropicTool](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.bedrock.AnthropicTool.html#langchain_aws.llms.bedrock.AnthropicTool "langchain_aws.llms.bedrock.AnthropicTool")\] | None = None_,     _\*_ ,     _max\_tokens : int | None = None_,     _temperature : float | None = None_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/llms/bedrock.html#LLMInputOutputAdapter.prepare_input)\#     

Parameters:     

  * **provider** \(_str_\)

  * **model\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **prompt** \(_str_ _|__None_\)

  * **system** \(_str_ _|__None_\)

  * **messages** \(_List_ _\[__Dict_ _\]__|__None_\)

  * **tools** \(_List_ _\[_[_AnthropicTool_](https://python.langchain.com/api_reference/aws/llms/langchain_aws.llms.bedrock.AnthropicTool.html#langchain_aws.llms.bedrock.AnthropicTool "langchain_aws.llms.bedrock.AnthropicTool") _\]__|__None_\)

  * **max\_tokens** \(_int_ _|__None_\)

  * **temperature** \(_float_ _|__None_\)

Return type:     

_Dict_\[str, _Any_\]

_classmethod _prepare\_output\(

    _provider : str_,     _response : Any_, \) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/llms/bedrock.html#LLMInputOutputAdapter.prepare_output)\#     

Parameters:     

  * **provider** \(_str_\)

  * **response** \(_Any_\)

Return type:     

dict

_classmethod _prepare\_output\_stream\(

    _provider : str_,     _response : Any_,     _stop : List\[str\] | None = None_,     _messages\_api : bool = False_,     _coerce\_content\_to\_string : bool = False_, \) → Iterator\[[GenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") | [AIMessageChunk](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessageChunk.html#langchain_core.messages.ai.AIMessageChunk "langchain_core.messages.ai.AIMessageChunk")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/llms/bedrock.html#LLMInputOutputAdapter.prepare_output_stream)\#     

Parameters:     

  * **provider** \(_str_\)

  * **response** \(_Any_\)

  * **stop** \(_List_ _\[__str_ _\]__|__None_\)

  * **messages\_api** \(_bool_\)

  * **coerce\_content\_to\_string** \(_bool_\)

Return type:     

_Iterator_\[[_GenerationChunk_](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") | [_AIMessageChunk_](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.ai.AIMessageChunk.html#langchain_core.messages.ai.AIMessageChunk "langchain_core.messages.ai.AIMessageChunk")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)