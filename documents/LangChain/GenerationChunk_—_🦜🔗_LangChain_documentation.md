# GenerationChunk — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.GenerationChunk.html
**Word Count:** 53
**Links Count:** 114
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# GenerationChunk\#

_class _langchain\_core.outputs.generation.GenerationChunk[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/outputs/generation.html#GenerationChunk)\#     

Bases: [`Generation`](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html#langchain_core.outputs.generation.Generation "langchain_core.outputs.generation.Generation")

Generation chunk, which can be concatenated with other Generation chunks.

_param _generation\_info _: dict\[str, Any\] | None_ _ = None_\#     

Raw response from the provider.

May include things like the reason for finishing or token log probabilities.

_param _text _: str_ _\[Required\]_\#     

Generated text output.

_param _type _: Literal\['Generation'\]__ = 'Generation'_\#     

Type is used exclusively for serialization purposes. Set to “Generation” for this class.

Examples using GenerationChunk

  * [How to create a custom LLM class](https://python.langchain.com/docs/how_to/custom_llm/)

__On this page