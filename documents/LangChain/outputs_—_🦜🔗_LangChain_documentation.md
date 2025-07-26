# outputs — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/outputs.html
**Word Count:** 197
**Links Count:** 110
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# `outputs`\#

Output classes.

**Output** classes are used to represent the output of a language model call and the output of a chat.

The top container for information is the LLMResult object. LLMResult is used by both chat models and LLMs. This object contains the output of the language model and any additional information that the model provider wants to return.

When invoking models via the standard runnable methods \(e.g. invoke, batch, etc.\): \- Chat models will return AIMessage objects. \- LLMs will return regular text strings.

In addition, users can access the raw output of either LLMs or chat models via callbacks. The on\_chat\_model\_end and on\_llm\_end callbacks will return an LLMResult object containing the generated outputs and any additional information returned by the model provider.

In general, if information is already available in the AIMessage object, it is recommended to access it from there rather than from the LLMResult object.

**Classes**

[`outputs.chat_generation.ChatGeneration`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGeneration.html#langchain_core.outputs.chat_generation.ChatGeneration "langchain_core.outputs.chat_generation.ChatGeneration") | A single chat generation output.   ---|---   [`outputs.chat_generation.ChatGenerationChunk`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGenerationChunk.html#langchain_core.outputs.chat_generation.ChatGenerationChunk "langchain_core.outputs.chat_generation.ChatGenerationChunk") | ChatGeneration chunk.   [`outputs.chat_result.ChatResult`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_result.ChatResult.html#langchain_core.outputs.chat_result.ChatResult "langchain_core.outputs.chat_result.ChatResult") | Use to represent the result of a chat model call with a single prompt.   [`outputs.generation.Generation`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation") | A single text generation output.   [`outputs.generation.GenerationChunk`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html#langchain_core.outputs.generation.GenerationChunk "langchain_core.outputs.generation.GenerationChunk") | Generation chunk, which can be concatenated with other Generation chunks.   [`outputs.llm_result.LLMResult`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.llm_result.LLMResult.html#langchain_core.outputs.llm_result.LLMResult "langchain_core.outputs.llm_result.LLMResult") | A container for results of an LLM call.   [`outputs.run_info.RunInfo`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.run_info.RunInfo.html#langchain_core.outputs.run_info.RunInfo "langchain_core.outputs.run_info.RunInfo") | Class that contains metadata for a single execution of a Chain or model.      **Functions**

[`outputs.chat_generation.merge_chat_generation_chunks`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.merge_chat_generation_chunks.html#langchain_core.outputs.chat_generation.merge_chat_generation_chunks "langchain_core.outputs.chat_generation.merge_chat_generation_chunks")\(chunks\) | Merge a list of ChatGenerationChunks into a single ChatGenerationChunk.   ---|---