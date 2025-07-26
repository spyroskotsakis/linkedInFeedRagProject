# StringExampleMapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.string_run_evaluator.StringExampleMapper.html
**Word Count:** 52
**Links Count:** 114
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# StringExampleMapper\#

_class _langchain.smith.evaluation.string\_run\_evaluator.StringExampleMapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#StringExampleMapper)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Map an example, or row in the dataset, to the inputs of an evaluation.

_param _reference\_key _: str | None_ _ = None_\#     

\_\_call\_\_\(

    _example : Example_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#StringExampleMapper.__call__)\#     

Maps the Run and Example to a dictionary.

Parameters:     

**example** \(_Example_\)

Return type:     

dict\[str, str\]

map\(

    _example : Example_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#StringExampleMapper.map)\#     

Maps the Example, or dataset row to a dictionary.

Parameters:     

**example** \(_Example_\)

Return type:     

dict\[str, str\]

serialize\_chat\_messages\(

    _messages : list\[dict\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#StringExampleMapper.serialize_chat_messages)\#     

Extract the input messages from the run.

Parameters:     

**messages** \(_list_ _\[__dict_ _\]_\)

Return type:     

str

_property _output\_keys _: list\[str\]_\#     

The keys to extract from the run.

__On this page