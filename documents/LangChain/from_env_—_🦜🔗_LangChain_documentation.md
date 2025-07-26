# from_env — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.utils.from_env.html
**Word Count:** 98
**Links Count:** 166
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# from\_env\#

langchain\_core.utils.utils.from\_env\(_key : str_, _/_\) → Callable\[\[\], str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/utils.html#from_env)\# langchain\_core.utils.utils.from\_env\(

    _key : str_,     _/_ ,     _\*_ ,     _default : str_, \) → Callable\[\[\], str\] langchain\_core.utils.utils.from\_env\(

    _key : Sequence\[str\]_,     _/_ ,     _\*_ ,     _default : str_, \) → Callable\[\[\], str\] langchain\_core.utils.utils.from\_env\(

    _key : str_,     _/_ ,     _\*_ ,     _error\_message : str_, \) → Callable\[\[\], str\] langchain\_core.utils.utils.from\_env\(

    _key : str | Sequence\[str\]_,     _/_ ,     _\*_ ,     _default : str_,     _error\_message : str | None_, \) → Callable\[\[\], str\] langchain\_core.utils.utils.from\_env\(

    _key : str_,     _/_ ,     _\*_ ,     _default : None_,     _error\_message : str | None_, \) → Callable\[\[\], str | None\] langchain\_core.utils.utils.from\_env\(

    _key : str | Sequence\[str\]_,     _/_ ,     _\*_ ,     _default : None_, \) → Callable\[\[\], str | None\]     

Create a factory method that gets a value from an environment variable.

Parameters:     

  * **key** – The environment variable to look up. If a list of keys is provided, the first key found in the environment will be used. If no key is found, the default value will be used if set, otherwise an error will be raised.

  * **default** – The default value to return if the environment variable is not set.

  * **error\_message** – the error message which will be raised if the key is not found and no default value is provided. This will be raised as a ValueError.

__On this page   *[/]: Positional-only parameter separator (PEP 570)   *[\*]: Keyword-only parameters separator (PEP 3102)