# PythonREPL — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/utilities/langchain_experimental.utilities.python.PythonREPL.html
**Word Count:** 87
**Links Count:** 109
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# PythonREPL\#

_class _langchain\_experimental.utilities.python.PythonREPL[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/utilities/python.html#PythonREPL)\#     

Bases: `BaseModel`

Simulates a standalone Python REPL.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _globals _: Dict | None_ _\[Optional\]__\(alias '\_globals'\)_\#     

_param _locals _: Dict | None_ _\[Optional\]__\(alias '\_locals'\)_\#     

_classmethod _worker\(

    _command : str_,     _globals : Dict | None_,     _locals : Dict | None_,     _queue : Queue_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/utilities/python.html#PythonREPL.worker)\#     

Parameters:     

  * **command** \(_str_\)

  * **globals** \(_Dict_ _|__None_\)

  * **locals** \(_Dict_ _|__None_\)

  * **queue** \(_Queue_\)

Return type:     

None

_static _sanitize\_input\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/utilities/python.html#PythonREPL.sanitize_input)\#     

Sanitize input to the python REPL.

Remove whitespace, backtick & python \(if llm mistakes python console as terminal\)

Parameters:     

**query** \(_str_\) – The query to sanitize

Returns:     

The sanitized query

Return type:     

str

run\(

    _command : str_,     _timeout : int | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/utilities/python.html#PythonREPL.run)\#     

Run command with own globals/locals and returns anything printed. Timeout after the specified number of seconds.

Parameters:     

  * **command** \(_str_\)

  * **timeout** \(_int_ _|__None_\)

Return type:     

str

Examples using PythonREPL

  * [Python REPL](https://python.langchain.com/docs/integrations/tools/python/)

__On this page