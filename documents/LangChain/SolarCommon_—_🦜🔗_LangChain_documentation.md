# SolarCommon — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/llms/langchain_community.llms.solar.SolarCommon.html
**Word Count:** 54
**Links Count:** 297
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# SolarCommon\#

_class _langchain\_community.llms.solar.SolarCommon[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/solar.html#SolarCommon)\#     

Bases: `BaseModel`

Common configuration for Solar LLMs.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _base\_url _: str_ _ = 'https://api.upstage.ai/v1/solar'_\#     

_param _max\_tokens _: int_ _ = 1024_\#     

_param _model\_name _: str_ _ = 'solar-mini'__\(alias 'model'\)_\#     

Model name. Available models listed here: <https://console.upstage.ai/services/solar>

_param _solar\_api\_key _: SecretStr | None_ _ = None_ _\(alias 'api\_key'\)_\#     

Solar API key. Get it here: <https://console.upstage.ai/services/solar>

_param _temperature _: float_ _ = 0.3_\#     

_classmethod _validate\_environment\(

    _values : Dict_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/llms/solar.html#SolarCommon.validate_environment)\#     

Parameters:     

**values** \(_Dict_\)

Return type:     

_Dict_

__On this page