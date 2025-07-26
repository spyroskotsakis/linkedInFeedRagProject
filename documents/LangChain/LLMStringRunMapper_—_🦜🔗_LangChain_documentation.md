# LLMStringRunMapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.string_run_evaluator.LLMStringRunMapper.html
**Word Count:** 43
**Links Count:** 117
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# LLMStringRunMapper\#

_class _langchain.smith.evaluation.string\_run\_evaluator.LLMStringRunMapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#LLMStringRunMapper)\#     

Bases: [`StringRunMapper`](https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.string_run_evaluator.StringRunMapper.html#langchain.smith.evaluation.string_run_evaluator.StringRunMapper "langchain.smith.evaluation.string_run_evaluator.StringRunMapper")

Extract items to evaluate from the run object.

\_\_call\_\_\(

    _run : Run_, \) → dict\[str, str\]\#     

Maps the Run to a dictionary.

Parameters:     

**run** \(_Run_\)

Return type:     

dict\[str, str\]

map\(

    _run : Run_, \) → dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#LLMStringRunMapper.map)\#     

Maps the Run to a dictionary.

Parameters:     

**run** \(_Run_\)

Return type:     

dict\[str, str\]

serialize\_chat\_messages\(

    _messages : list\[dict\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#LLMStringRunMapper.serialize_chat_messages)\#     

Extract the input messages from the run.

Parameters:     

**messages** \(_list_ _\[__dict_ _\]_\)

Return type:     

str

serialize\_inputs\(_inputs : dict_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#LLMStringRunMapper.serialize_inputs)\#     

Parameters:     

**inputs** \(_dict_\)

Return type:     

str

serialize\_outputs\(_outputs : dict_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/string_run_evaluator.html#LLMStringRunMapper.serialize_outputs)\#     

Parameters:     

**outputs** \(_dict_\)

Return type:     

str

_property _output\_keys _: list\[str\]_\#     

The keys to extract from the run.

__On this page