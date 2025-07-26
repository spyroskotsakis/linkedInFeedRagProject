# ChainStringRunMapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.string_run_evaluator.ChainStringRunMapper.html
**Word Count:** 95
**Links Count:** 112
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# ChainStringRunMapper\#

_class _langchain.smith.evaluation.string\_run\_evaluator.ChainStringRunMapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#ChainStringRunMapper)\#     

Bases: [`StringRunMapper`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.string_run_evaluator.StringRunMapper.html#langchain.smith.evaluation.string_run_evaluator.StringRunMapper "langchain.smith.evaluation.string_run_evaluator.StringRunMapper")

Extract items to evaluate from the run object from a chain.

_param _input\_key _: str | None_ _ = None_\#     

The key from the model Run’s inputs to use as the eval input. If not provided, will use the only input key or raise an error if there are multiple.

_param _prediction\_key _: str | None_ _ = None_\#     

The key from the model Run’s outputs to use as the eval prediction. If not provided, will use the only output key or raise an error if there are multiple.

\_\_call\_\_\(

    _run : Run_, \) → dict\[str, str\]\#     

Maps the Run to a dictionary.

Parameters:     

**run** \(_Run_\)

Return type:     

dict\[str, str\]

map\(

    _run : Run_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#ChainStringRunMapper.map)\#     

Maps the Run to a dictionary.

Parameters:     

**run** \(_Run_\)

Return type:     

dict\[str, str\]

_property _output\_keys _: list\[str\]_\#     

The keys to extract from the run.

__On this page