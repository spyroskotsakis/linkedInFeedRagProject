# GoogleJobsAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_jobs.GoogleJobsAPIWrapper.html
**Word Count:** 95
**Links Count:** 259
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# GoogleJobsAPIWrapper\#

_class _langchain\_community.utilities.google\_jobs.GoogleJobsAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_jobs.html#GoogleJobsAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for SerpApi’s Google Scholar API

You can create SerpApi.com key by signing up at: <https://serpapi.com/users/sign_up>. The wrapper uses the SerpApi.com python package: <https://serpapi.com/integrations/python> To use, you should have the environment variable `SERPAPI_API_KEY` set with your API key, or pass serp\_api\_key as a named parameter to the constructor.

> Example: >      >      >      >      >  > from langchain\_community.utilities import GoogleJobsAPIWrapper google\_Jobs = GoogleJobsAPIWrapper\(\) google\_Jobs.run\(‘langchain’\)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _serp\_api\_key _: SecretStr | None_ _ = None_\#     

_param _serp\_search\_engine _: Any_ _ = None_\#     

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_jobs.html#GoogleJobsAPIWrapper.run)\#     

Run query through Google Trends with Serpapi

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using GoogleJobsAPIWrapper

  * [Google Jobs](https://python.langchain.com/docs/integrations/tools/google_jobs/)

__On this page