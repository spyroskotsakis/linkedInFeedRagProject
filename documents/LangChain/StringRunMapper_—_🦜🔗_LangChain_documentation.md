# StringRunMapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.string_run_evaluator.StringRunMapper.html
**Word Count:** 34
**Links Count:** 109
**Scraped:** 2025-07-21 07:51:08
**Status:** completed

---

# StringRunMapper\#

_class _langchain.smith.evaluation.string\_run\_evaluator.StringRunMapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#StringRunMapper)\#     

Bases: [`Serializable`](https://python.langchain.com/api_reference/core/load/langchain_core.load.serializable.Serializable.html#langchain_core.load.serializable.Serializable "langchain_core.load.serializable.Serializable")

Extract items to evaluate from the run object.

\_\_call\_\_\(

    _run : Run_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#StringRunMapper.__call__)\#     

Maps the Run to a dictionary.

Parameters:     

**run** \(_Run_\)

Return type:     

dict\[str, str\]

_abstractmethod _map\(

    _run : Run_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#StringRunMapper.map)\#     

Maps the Run to a dictionary.

Parameters:     

**run** \(_Run_\)

Return type:     

dict\[str, str\]

_property _output\_keys _: list\[str\]_\#     

The keys to extract from the run.

__On this page