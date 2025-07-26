# SceneXplainAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.scenexplain.SceneXplainAPIWrapper.html
**Word Count:** 90
**Links Count:** 258
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# SceneXplainAPIWrapper\#

_class _langchain\_community.utilities.scenexplain.SceneXplainAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/scenexplain.html#SceneXplainAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for SceneXplain API.

In order to set this up, you need API key for the SceneXplain API. You can obtain a key by following the steps below. \- Sign up for a free account at <https://scenex.jina.ai/>. \- Navigate to the API Access page \(<https://scenex.jina.ai/api>\)

> and create a new API key.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _scenex\_api\_key _: str_ _\[Optional\]_\#     

_param _scenex\_api\_url _: str_ _ = 'https://api.scenex.jina.ai/v1/describe'_\#     

run\(_image : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/scenexplain.html#SceneXplainAPIWrapper.run)\#     

Run SceneXplain image explainer.

Parameters:     

**image** \(_str_\)

Return type:     

str

__On this page