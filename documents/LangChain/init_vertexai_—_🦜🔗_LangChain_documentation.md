# init_vertexai — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.vertexai.init_vertexai.html
**Word Count:** 60
**Links Count:** 249
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# init\_vertexai\#

langchain\_community.utilities.vertexai.init\_vertexai\(

    _project : str | None = None_,     _location : str | None = None_,     _credentials : Credentials | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/vertexai.html#init_vertexai)\#     

Init Vertex AI.

Parameters:     

  * **project** \(_str_ _|__None_\) – The default GCP project to use when making Vertex API calls.

  * **location** \(_str_ _|__None_\) – The default location to use when making API calls.

  * **credentials** \(_Credentials_ _|__None_\) – The default custom credentials to use when making API calls. If not provided credentials will be ascertained from the environment.

Raises:     

**ImportError** – If importing vertexai SDK did not succeed.

Return type:     

None

__On this page