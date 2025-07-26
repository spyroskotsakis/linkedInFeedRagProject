# AI21Base — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/ai21/ai21_base/langchain_ai21.ai21_base.AI21Base.html
**Word Count:** 77
**Links Count:** 81
**Scraped:** 2025-07-21 07:58:35
**Status:** completed

---

# AI21Base\#

_class _langchain\_ai21.ai21\_base.AI21Base[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_ai21/ai21_base.html#AI21Base)\#     

Bases: `BaseModel`

Base class for AI21 models.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_host _: str_ _\[Optional\]_\#     

Host URL

_param _api\_key _: SecretStr_ _\[Optional\]_\#     

API key for AI21 API.

_param _async\_client _: Any_ _ = None_\#     

Asynchronous client for API calls.

_param _num\_retries _: int | None_ _ = None_\#     

Maximum number of retries for API requests before giving up.

_param _timeout\_sec _: float_ _\[Optional\]_\#     

Timeout in seconds.

If not set, it will default to the value of the environment variable AI21\_TIMEOUT\_SEC or 300 seconds.

__On this page