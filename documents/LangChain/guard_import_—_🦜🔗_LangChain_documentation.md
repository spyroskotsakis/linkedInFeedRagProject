# guard_import — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.utils.guard_import.html
**Word Count:** 59
**Links Count:** 166
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# guard\_import\#

langchain\_core.utils.utils.guard\_import\(

    _module\_name : str_,     _\*_ ,     _pip\_name : str | None = None_,     _package : str | None = None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/utils.html#guard_import)\#     

Dynamically import a module.

Raise an exception if the module is not installed.

Parameters:     

  * **module\_name** \(_str_\) – The name of the module to import.

  * **pip\_name** \(_str_ _,__optional_\) – The name of the module to install with pip. Defaults to None.

  * **package** \(_str_ _,__optional_\) – The package to import the module from. Defaults to None.

Returns:     

The imported module.

Return type:     

Any

Raises:     

**ImportError** – If the module is not installed.

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)