# AlphaVantageAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.alpha_vantage.AlphaVantageAPIWrapper.html
**Word Count:** 88
**Links Count:** 260
**Scraped:** 2025-07-21 08:07:22
**Status:** completed

---

# AlphaVantageAPIWrapper\#

_class _langchain\_community.utilities.alpha\_vantage.AlphaVantageAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/alpha_vantage.html#AlphaVantageAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for AlphaVantage API for Currency Exchange Rate.

Docs for using:

  1. Go to AlphaVantage and sign up for an API key

  2. Save your API KEY into ALPHAVANTAGE\_API\_KEY env variable

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _alphavantage\_api\_key _: str | None_ _ = None_\#     

run\(

    _from\_currency : str_,     _to\_currency : str_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/alpha_vantage.html#AlphaVantageAPIWrapper.run)\#     

Get the current exchange rate for a specified currency pair.

Parameters:     

  * **from\_currency** \(_str_\)

  * **to\_currency** \(_str_\)

Return type:     

str

search\_symbols\(

    _keywords : str_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/alpha_vantage.html#AlphaVantageAPIWrapper.search_symbols)\#     

Make a request to the AlphaVantage API to search for symbols.

Parameters:     

**keywords** \(_str_\)

Return type:     

_Dict_\[str, _Any_\]

_property _standard\_currencies _: List\[str\]_\#     

Examples using AlphaVantageAPIWrapper

  * [Alpha Vantage](https://python.langchain.com/docs/integrations/tools/alpha_vantage/)

__On this page