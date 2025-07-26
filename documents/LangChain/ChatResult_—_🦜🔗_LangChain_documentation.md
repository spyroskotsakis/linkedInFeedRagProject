# ChatResult — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_result.ChatResult.html
**Word Count:** 174
**Links Count:** 112
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# ChatResult\#

_class _langchain\_core.outputs.chat\_result.ChatResult[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/outputs/chat_result.html#ChatResult)\#     

Bases: `BaseModel`

Use to represent the result of a chat model call with a single prompt.

This container is used internally by some implementations of chat model, it will eventually be mapped to a more general LLMResult object, and then projected into an AIMessage object.

LangChain users working with chat models will usually access information via AIMessage \(returned from runnable interfaces\) or LLMResult \(available via callbacks\). Please refer the AIMessage and LLMResult schema documentation for more information.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _generations _: list\[[ChatGeneration](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.chat_generation.ChatGeneration.html#langchain_core.outputs.chat_generation.ChatGeneration "langchain_core.outputs.chat_generation.ChatGeneration")\]__\[Required\]_\#     

List of the chat generations.

Generations is a list to allow for multiple candidate generations for a single input prompt.

_param _llm\_output _: dict | None_ _ = None_\#     

For arbitrary LLM provider specific output.

This dictionary is a free-form dictionary that can contain any information that the provider wants to return. It is not standardized and is provider-specific.

Users should generally avoid relying on this field and instead rely on accessing relevant information from standardized fields present in AIMessage.

Examples using ChatResult

  * [How to create a custom chat model class](https://python.langchain.com/docs/how_to/custom_chat_model/)

__On this page