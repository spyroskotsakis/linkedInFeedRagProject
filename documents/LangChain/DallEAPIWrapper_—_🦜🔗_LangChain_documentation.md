# DallEAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.dalle_image_generator.DallEAPIWrapper.html
**Word Count:** 121
**Links Count:** 285
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# DallEAPIWrapper\#

_class _langchain\_community.utilities.dalle\_image\_generator.DallEAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dalle_image_generator.html#DallEAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for OpenAI’s DALL-E Image Generator.

<https://platform.openai.com/docs/guides/images/generations?context=node>

Usage instructions:

  1. pip install openai

  2. save your OPENAI\_API\_KEY in an environment variable

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _default\_headers _: Mapping\[str, str\] | None_ _ = None_\#     

_param _default\_query _: Mapping\[str, object\] | None_ _ = None_\#     

_param _http\_client _: Any | None_ _ = None_\#     

Optional httpx.Client.

_param _max\_retries _: int_ _ = 2_\#     

Maximum number of retries to make when generating.

_param _model\_kwargs _: Dict\[str, Any\]__\[Optional\]_\#     

_param _model\_name _: str_ _ = 'dall-e-2'__\(alias 'model'\)_\#     

_param _n _: int_ _ = 1_\#     

Number of images to generate

_param _openai\_api\_base _: str | None_ _\[Optional\]__\(alias 'base\_url'\)_\#     

Base URL path for API requests, leave blank if not using a proxy or service emulator.

_param _openai\_api\_key _: SecretStr | None_ _\[Optional\]__\(alias 'api\_key'\)_\#     

Automatically inferred from env var OPENAI\_API\_KEY if not provided.

_param _openai\_organization _: str | None_ _\[Optional\]__\(alias 'organization'\)_\#     

Automatically inferred from env var OPENAI\_ORG\_ID if not provided.

_param _openai\_proxy _: str_ _\[Optional\]_\#     

_param _quality _: str | None_ _ = 'standard'_\#     

Quality of the image that will be generated

_param _request\_timeout _: float | Tuple\[float, float\] | Any | None_ _ = None_ _\(alias 'timeout'\)_\#     

_param _separator _: str_ _ = '\n'_\#     

Separator to use when multiple URLs are returned.

_param _size _: str_ _ = '1024x1024'_\#     

Size of image to generate

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dalle_image_generator.html#DallEAPIWrapper.run)\#     

Run query through OpenAI and parse result.

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using DallEAPIWrapper

  * [Dall-E Image Generator](https://python.langchain.com/docs/integrations/tools/dalle_image_generator/)

  * [OpenAI](https://python.langchain.com/docs/integrations/providers/openai/)

__On this page