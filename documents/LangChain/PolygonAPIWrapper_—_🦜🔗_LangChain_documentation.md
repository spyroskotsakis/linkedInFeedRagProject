# PolygonAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.polygon.PolygonAPIWrapper.html
**Word Count:** 133
**Links Count:** 268
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# PolygonAPIWrapper\#

_class _langchain\_community.utilities.polygon.PolygonAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/polygon.html#PolygonAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Polygon API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _polygon\_api\_key _: str | None_ _ = None_\#     

get\_aggregates\(

    _ticker : str_,     _\*\* kwargs: Any_, \) → dict | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/polygon.html#PolygonAPIWrapper.get_aggregates)\#     

Get aggregate bars for a stock over a given date range in custom time window sizes.

/v2/aggs/ticker/\{ticker\}/range/\{multiplier\}/\{timespan\}/\{from\_date\}/\{to\_date\}

Parameters:     

  * **ticker** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

dict | None

get\_financials\(_ticker : str_\) → dict | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/polygon.html#PolygonAPIWrapper.get_financials)\#     

Get fundamental financial data, which is found in balance sheets, income statements, and cash flow statements for a given ticker.

/vX/reference/financials

Parameters:     

**ticker** \(_str_\)

Return type:     

dict | None

get\_last\_quote\(_ticker : str_\) → dict | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/polygon.html#PolygonAPIWrapper.get_last_quote)\#     

Get the most recent National Best Bid and Offer \(Quote\) for a ticker.

/v2/last/nbbo/\{ticker\}

Parameters:     

**ticker** \(_str_\)

Return type:     

dict | None

get\_ticker\_news\(

    _ticker : str_, \) → dict | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/polygon.html#PolygonAPIWrapper.get_ticker_news)\#     

Get the most recent news articles relating to a stock ticker symbol, including a summary of the article and a link to the original source.

/v2/reference/news

Parameters:     

**ticker** \(_str_\)

Return type:     

dict | None

run\(

    _mode : str_,     _ticker : str_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/polygon.html#PolygonAPIWrapper.run)\#     

Parameters:     

  * **mode** \(_str_\)

  * **ticker** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

str

Examples using PolygonAPIWrapper

  * [Polygon IO Toolkit](https://python.langchain.com/docs/integrations/tools/polygon_toolkit/)

  * [Polygon IO Toolkit and Tools](https://python.langchain.com/docs/integrations/tools/polygon/)

__On this page