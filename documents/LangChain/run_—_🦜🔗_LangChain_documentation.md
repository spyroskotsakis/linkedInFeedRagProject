# run — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/utils/langchain_prompty.utils.run.html
**Word Count:** 53
**Links Count:** 78
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# run\#

langchain\_prompty.utils.run\(

    _prompt : [Prompty](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")_,     _content : dict | list | str_,     _configuration : dict\[str, Any\] = \{\}_,     _parameters : dict\[str, Any\] = \{\}_,     _raw : bool = False_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/utils.html#run)\#     

Run the prompty.

Parameters:     

  * **prompt** \([_Prompty_](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty")\) – The Prompty object.

  * **content** \(_dict_ _|__list_ _|__str_\) – The content to run the prompty on.

  * **configuration** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The configuration to use. Defaults to \{\}.

  * **parameters** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The parameters to use. Defaults to \{\}.

  * **raw** \(_bool_\) – Whether to return the raw output. Defaults to False.

Returns:     

The result of running the prompty.

Return type:     

_Any_

__On this page