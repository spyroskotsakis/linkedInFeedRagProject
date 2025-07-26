# WolframAlphaAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.wolfram_alpha.WolframAlphaAPIWrapper.html
**Word Count:** 80
**Links Count:** 255
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# WolframAlphaAPIWrapper\#

_class _langchain\_community.utilities.wolfram\_alpha.WolframAlphaAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/wolfram_alpha.html#WolframAlphaAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Wolfram Alpha.

Docs for using:

  1. Go to wolfram alpha and sign up for a developer account

  2. Create an app and get your APP ID

  3. Save your APP ID into WOLFRAM\_ALPHA\_APPID env variable

  4. pip install wolframalpha

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _wolfram\_alpha\_appid _: str | None_ _ = None_\#     

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/wolfram_alpha.html#WolframAlphaAPIWrapper.run)\#     

Run query through WolframAlpha and parse result.

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using WolframAlphaAPIWrapper

  * [Wolfram Alpha](https://python.langchain.com/docs/integrations/providers/wolfram_alpha/)

__On this page