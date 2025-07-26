# LLMResult — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html
**Word Count:** 270
**Links Count:** 129
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# LLMResult\#

_class _langchain\_core.outputs.llm\_result.LLMResult[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/outputs/llm_result.html#LLMResult)\#     

Bases: `BaseModel`

A container for results of an LLM call.

Both chat models and LLMs generate an LLMResult object. This object contains the generated outputs and any additional information that the model provider wants to return.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _generations _: list\[list\[[Generation](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") | [ChatGeneration](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGeneration.html#langchain_core.outputs.chat_generation.ChatGeneration "langchain_core.outputs.chat_generation.ChatGeneration") | [GenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") | [ChatGenerationChunk](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk")\]\]__\[Required\]_\#     

Generated outputs.

The first dimension of the list represents completions for different input prompts.

The second dimension of the list represents different candidate generations for a given prompt.

When returned from an LLM the type is list\[list\[Generation\]\]. When returned from a chat model the type is list\[list\[ChatGeneration\]\].

ChatGeneration is a subclass of Generation that has a field for a structured chat message.

_param _llm\_output _: dict | None_ _ = None_\#     

For arbitrary LLM provider specific output.

This dictionary is a free-form dictionary that can contain any information that the provider wants to return. It is not standardized and is provider-specific.

Users should generally avoid relying on this field and instead rely on accessing relevant information from standardized fields present in AIMessage.

_param _run _: list\[[RunInfo](https://python.langchain.com/api_reference/core/tracers/langchain_core.tracers.event_stream.RunInfo.html#langchain_core.tracers.event_stream.RunInfo "langchain_core.tracers.event_stream.RunInfo")\] | None_ _ = None_\#     

List of metadata info for model call for each input.

_param _type _: Literal\['LLMResult'\]__ = 'LLMResult'_\#     

Type is used exclusively for serialization purposes.

flatten\(\) → list\[LLMResult\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/outputs/llm_result.html#LLMResult.flatten)\#     

Flatten generations into a single list.

Unpack list\[list\[Generation\]\] -> list\[LLMResult\] where each returned LLMResult contains only a single Generation. If token usage information is available, it is kept only for the LLMResult corresponding to the top-choice Generation, to avoid over-counting of token usage downstream.

Returns:     

List of LLMResults where each returned LLMResult contains a single     

Generation.

Return type:     

list\[_LLMResult_\]

Examples using LLMResult

  * [Google Cloud Vertex AI](https://python.langchain.com/docs/integrations/llms/google_vertex_ai_palm/)

  * [How to attach callbacks to a runnable](https://python.langchain.com/docs/how_to/callbacks_attach/)

  * [How to pass callbacks in at runtime](https://python.langchain.com/docs/how_to/callbacks_runtime/)

  * [How to propagate callbacks constructor](https://python.langchain.com/docs/how_to/callbacks_constructor/)

  * [How to use callbacks in async environments](https://python.langchain.com/docs/how_to/callbacks_async/)

__On this page