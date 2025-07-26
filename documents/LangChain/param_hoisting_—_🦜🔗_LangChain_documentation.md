# param_hoisting — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.param_hoisting.html
**Word Count:** 39
**Links Count:** 82
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# param\_hoisting\#

langchain\_prompty.core.param\_hoisting\(

    _top : dict\[str, Any\]_,     _bottom : dict\[str, Any\]_,     _top\_key : Any = None_, \) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#param_hoisting)\#     

Merge two dictionaries with hoisting of parameters from bottom to top.

Parameters:     

  * **top** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The top dictionary.

  * **bottom** \(_dict_ _\[__str_ _,__Any_ _\]_\) – The bottom dictionary.

  * **top\_key** \(_Any_\) – The key to hoist from the bottom to the top.

Returns:     

The merged dictionary.

Return type:     

dict\[str, _Any_\]

__On this page