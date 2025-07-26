# MoonshotCommon — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.moonshot.MoonshotCommon.html
**Word Count:** 76
**Links Count:** 299
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# MoonshotCommon\#

_class _langchain\_community.llms.moonshot.MoonshotCommon[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/moonshot.html#MoonshotCommon)\#     

Bases: `BaseModel`

Common parameters for Moonshot LLMs.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _base\_url _: str_ _ = 'https://api.moonshot.cn/v1'_\#     

_param _client _: Any_ _\[Required\]_\#     

_param _max\_tokens _: int_ _ = 1024_\#     

Maximum number of tokens to generate.

_param _model\_name _: str_ _ = 'moonshot-v1-8k'__\(alias 'model'\)_\#     

Model name. Available models listed here: <https://platform.moonshot.cn/pricing>

_param _moonshot\_api\_key _: SecretStr | None_ _ = None_ _\(alias 'api\_key'\)_\#     

Moonshot API key. Get it here: <https://platform.moonshot.cn/console/api-keys>

_param _temperature _: float_ _ = 0.3_\#     

Temperature parameter \(higher values make the model more creative\).

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/moonshot.html#MoonshotCommon.validate_environment)\#     

Validate that api key and python package exists in environment.

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

__On this page