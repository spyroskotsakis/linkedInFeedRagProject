# ToolStringRunMapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.string_run_evaluator.ToolStringRunMapper.html
**Word Count:** 32
**Links Count:** 108
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# ToolStringRunMapper\#

_class _langchain.smith.evaluation.string\_run\_evaluator.ToolStringRunMapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#ToolStringRunMapper)\#     

Bases: [`StringRunMapper`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.string_run_evaluator.StringRunMapper.html#langchain.smith.evaluation.string_run_evaluator.StringRunMapper "langchain.smith.evaluation.string_run_evaluator.StringRunMapper")

Map an input to the tool.

\_\_call\_\_\(

    _run : Run_, \) → dict\[str, str\]\#     

Maps the Run to a dictionary.

Parameters:     

**run** \(_Run_\)

Return type:     

dict\[str, str\]

map\(

    _run : Run_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#ToolStringRunMapper.map)\#     

Maps the Run to a dictionary.

Parameters:     

**run** \(_Run_\)

Return type:     

dict\[str, str\]

_property _output\_keys _: list\[str\]_\#     

The keys to extract from the run.

__On this page