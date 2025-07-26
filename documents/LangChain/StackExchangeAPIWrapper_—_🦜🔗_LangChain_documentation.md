# StackExchangeAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.stackexchange.StackExchangeAPIWrapper.html
**Word Count:** 84
**Links Count:** 262
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# StackExchangeAPIWrapper\#

_class _langchain\_community.utilities.stackexchange.StackExchangeAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/stackexchange.html#StackExchangeAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Stack Exchange API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _fetch\_params _: Dict\[str, Any\]__\[Optional\]_\#     

Additional params to pass to StackApi.fetch.

_param _max\_results _: int_ _ = 3_\#     

Max number of results to include in output.

_param _query\_type _: Literal\['all', 'title', 'body'\]__ = 'all'_\#     

Which part of StackOverflows items to match against. One of ‘all’, ‘title’, ‘body’. Defaults to ‘all’.

_param _result\_separator _: str_ _ = '\n\n'_\#     

Separator between question,answer pairs.

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/stackexchange.html#StackExchangeAPIWrapper.run)\#     

Run query through StackExchange API and parse results.

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using StackExchangeAPIWrapper

  * [Stack Exchange](https://python.langchain.com/docs/integrations/providers/stackexchange/)

  * [StackExchange](https://python.langchain.com/docs/integrations/tools/stackexchange/)

__On this page