# Generation — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.generation.Generation.html
**Word Count:** 106
**Links Count:** 114
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# Generation\#

_class _langchain\_core.outputs.generation.Generation[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/outputs/generation.html#Generation)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

A single text generation output.

Generation represents the response from an “old-fashioned” LLM that generates regular text \(not chat messages\).

This model is used internally by chat model and will eventually be mapped to a more general LLMResult object, and then projected into an AIMessage object.

LangChain users working with chat models will usually access information via AIMessage \(returned from runnable interfaces\) or LLMResult \(available via callbacks\). Please refer the AIMessage and LLMResult schema documentation for more information.

_param _generation\_info _: dict\[str, Any\] | None_ _ = None_\#     

Raw response from the provider.

May include things like the reason for finishing or token log probabilities.

_param _text _: str_ _\[Required\]_\#     

Generated text output.

_param _type _: Literal\['Generation'\]__ = 'Generation'_\#     

Type is used exclusively for serialization purposes. Set to “Generation” for this class.

Examples using Generation

  * [How to create a custom Output Parser](https://python.langchain.com/docs/how_to/output_parser_custom/)

__On this page