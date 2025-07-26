# OpenWeatherMapAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openweathermap.OpenWeatherMapAPIWrapper.html
**Word Count:** 75
**Links Count:** 257
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# OpenWeatherMapAPIWrapper\#

_class _langchain\_community.utilities.openweathermap.OpenWeatherMapAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openweathermap.html#OpenWeatherMapAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for OpenWeatherMap API using PyOWM.

Docs for using:

  1. Go to OpenWeatherMap and sign up for an API key

  2. Save your API KEY into OPENWEATHERMAP\_API\_KEY env variable

  3. pip install pyowm

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _openweathermap\_api\_key _: str | None_ _ = None_\#     

_param _owm _: Any_ _ = None_\#     

run\(_location : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/openweathermap.html#OpenWeatherMapAPIWrapper.run)\#     

Get the current weather information for a specified location.

Parameters:     

**location** \(_str_\)

Return type:     

str

Examples using OpenWeatherMapAPIWrapper

  * [OpenWeatherMap](https://python.langchain.com/docs/integrations/providers/openweathermap/)

__On this page