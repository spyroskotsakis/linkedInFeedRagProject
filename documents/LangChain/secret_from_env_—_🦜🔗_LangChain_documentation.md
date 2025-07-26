# secret_from_env — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.utils.secret_from_env.html
**Word Count:** 63
**Links Count:** 166
**Scraped:** 2025-07-21 07:56:55
**Status:** completed

---

# secret\_from\_env\#

langchain\_core.utils.utils.secret\_from\_env\(

    _key : str | Sequence\[str\]_,     _/_ , \) → Callable\[\[\], SecretStr\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/utils.html#secret_from_env)\# langchain\_core.utils.utils.secret\_from\_env\(

    _key : str_,     _/_ ,     _\*_ ,     _default : str_, \) → Callable\[\[\], SecretStr\] langchain\_core.utils.utils.secret\_from\_env\(

    _key : str | Sequence\[str\]_,     _/_ ,     _\*_ ,     _default : None_, \) → Callable\[\[\], SecretStr | None\] langchain\_core.utils.utils.secret\_from\_env\(

    _key : str_,     _/_ ,     _\*_ ,     _error\_message : str_, \) → Callable\[\[\], SecretStr\]     

Secret from env.

Parameters:     

  * **key** – The environment variable to look up.

  * **default** – The default value to return if the environment variable is not set.

  * **error\_message** – the error message which will be raised if the key is not found and no default value is provided. This will be raised as a ValueError.

Returns:     

factory method that will look up the secret from the environment.

__On this page   *[/]: Positional-only parameter separator (PEP 570)   *[\*]: Keyword-only parameters separator (PEP 3102)