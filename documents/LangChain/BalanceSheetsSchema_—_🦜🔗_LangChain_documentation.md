# BalanceSheetsSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.financial_datasets.balance_sheets.BalanceSheetsSchema.html
**Word Count:** 71
**Links Count:** 413
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# BalanceSheetsSchema\#

_class _langchain\_community.tools.financial\_datasets.balance\_sheets.BalanceSheetsSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/financial_datasets/balance_sheets.html#BalanceSheetsSchema)\#     

Bases: `BaseModel`

Input for BalanceSheets.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _limit _: int_ _\[Required\]_\#     

The number of balance sheets to return. Default is 10.

_param _period _: str_ _\[Required\]_\#     

The period of the balance sheets. Possible values are: annual, quarterly, ttm. Default is ‘annual’.

_param _ticker _: str_ _\[Required\]_\#     

The ticker symbol to fetch balance sheets for.

__On this page