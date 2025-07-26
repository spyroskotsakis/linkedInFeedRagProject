# push — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/hub/langchain.hub.push.html
**Word Count:** 130
**Links Count:** 85
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# push\#

langchain.hub.push\(

    _repo\_full\_name : str_,     _object : Any_,     _\*_ ,     _api\_url : str | None = None_,     _api\_key : str | None = None_,     _parent\_commit\_hash : str | None = None_,     _new\_repo\_is\_public : bool = False_,     _new\_repo\_description : str | None = None_,     _readme : str | None = None_,     _tags : Sequence\[str\] | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/hub.html#push)\#     

Push an object to the hub and returns the URL it can be viewed at in a browser.

Parameters:     

  * **repo\_full\_name** \(_str_\) – The full name of the prompt to push to in the format of owner/prompt\_name or prompt\_name.

  * **object** \(_Any_\) – The LangChain to serialize and push to the hub.

  * **api\_url** \(_str_ _|__None_\) – The URL of the LangChain Hub API. Defaults to the hosted API service if you have an api key set, or a localhost instance if not.

  * **api\_key** \(_str_ _|__None_\) – The API key to use to authenticate with the LangChain Hub API.

  * **parent\_commit\_hash** \(_str_ _|__None_\) – The commit hash of the parent commit to push to. Defaults to the latest commit automatically.

  * **new\_repo\_is\_public** \(_bool_\) – Whether the prompt should be public. Defaults to False \(Private by default\).

  * **new\_repo\_description** \(_str_ _|__None_\) – The description of the prompt. Defaults to an empty string.

  * **readme** \(_str_ _|__None_\)

  * **tags** \(_Sequence_ _\[__str_ _\]__|__None_\)

Return type:     

str

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)