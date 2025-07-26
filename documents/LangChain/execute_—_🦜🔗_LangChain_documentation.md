# execute — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/utils/langchain_prompty.utils.execute.html
**Word Count:** 75
**Links Count:** 78
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# execute\#

langchain\_prompty.utils.execute\(

    _prompt : str | [Prompty](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")_,     _configuration : dict\[str, Any\] = \{\}_,     _parameters : dict\[str, Any\] = \{\}_,     _inputs : dict\[str, Any\] = \{\}_,     _raw : bool = False_,     _connection : str = 'default'_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/utils.html#execute)\#     

Execute a prompty.

Parameters:     

  * **prompt** \(_str_ _|_[_Prompty_](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")\) – The prompt to execute. Can be a path to a prompty file or a Prompty object.

  * **configuration** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The configuration to use. Defaults to \{\}.

  * **parameters** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The parameters to use. Defaults to \{\}.

  * **inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The inputs to the prompty. Defaults to \{\}.

  * **raw** \(_bool_\) – Whether to return the raw output. Defaults to False.

  * **connection** \(_str_\) – The connection to use. Defaults to “default”.

Returns:     

The result of executing the prompty.

Return type:     

_Any_

__On this page