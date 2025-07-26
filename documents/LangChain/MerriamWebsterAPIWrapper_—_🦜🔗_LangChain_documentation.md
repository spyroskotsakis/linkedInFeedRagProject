# MerriamWebsterAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.merriam_webster.MerriamWebsterAPIWrapper.html
**Word Count:** 76
**Links Count:** 256
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# MerriamWebsterAPIWrapper\#

_class _langchain\_community.utilities.merriam\_webster.MerriamWebsterAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/merriam_webster.html#MerriamWebsterAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Merriam-Webster.

Docs for using:

  1. Go to <https://www.dictionaryapi.com/register/index> and register an developer account with a key for the Collegiate Dictionary

  2. Get your API Key from <https://www.dictionaryapi.com/account/my-keys>

  3. Save your API Key into MERRIAM\_WEBSTER\_API\_KEY env variable

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _merriam\_webster\_api\_key _: str | None_ _ = None_\#     

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/merriam_webster.html#MerriamWebsterAPIWrapper.run)\#     

Run query through Merriam-Webster API and return a formatted result.

Parameters:     

**query** \(_str_\)

Return type:     

str

__On this page