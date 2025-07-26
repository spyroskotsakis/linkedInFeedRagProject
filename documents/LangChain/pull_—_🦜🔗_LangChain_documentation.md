# pull — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/hub/langchain.hub.pull.html
**Word Count:** 79
**Links Count:** 85
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# pull\#

langchain.hub.pull\(

    _owner\_repo\_commit : str_,     _\*_ ,     _include\_model : bool | None = None_,     _api\_url : str | None = None_,     _api\_key : str | None = None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/hub.html#pull)\#     

Pull an object from the hub and returns it as a LangChain object.

Parameters:     

  * **owner\_repo\_commit** \(_str_\) – The full name of the prompt to pull from in the format of owner/prompt\_name:commit\_hash or owner/prompt\_name or just prompt\_name if it’s your own prompt.

  * **api\_url** \(_str_ _|__None_\) – The URL of the LangChain Hub API. Defaults to the hosted API service if you have an api key set, or a localhost instance if not.

  * **api\_key** \(_str_ _|__None_\) – The API key to use to authenticate with the LangChain Hub API.

  * **include\_model** \(_bool_ _|__None_\)

Return type:     

_Any_

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)