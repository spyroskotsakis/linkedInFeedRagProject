# GoldenQueryAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.golden_query.GoldenQueryAPIWrapper.html
**Word Count:** 75
**Links Count:** 258
**Scraped:** 2025-07-21 08:17:49
**Status:** completed

---

# GoldenQueryAPIWrapper\#

_class _langchain\_community.utilities.golden\_query.GoldenQueryAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/golden_query.html#GoldenQueryAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Golden.

Docs for using:

  1. Go to <https://golden.com> and sign up for an account

  2. Get your API Key from <https://golden.com/settings/api>

  3. Save your API Key into GOLDEN\_API\_KEY env variable

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _golden\_api\_key _: str | None_ _ = None_\#     

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/golden_query.html#GoldenQueryAPIWrapper.run)\#     

Run query through Golden Query API and return the JSON raw result.

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using GoldenQueryAPIWrapper

  * [Golden](https://python.langchain.com/docs/integrations/providers/golden/)

  * [Golden Query](https://python.langchain.com/docs/integrations/tools/golden_query/)

__On this page