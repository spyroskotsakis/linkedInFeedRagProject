# CashFlowStatementsSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.financial_datasets.cash_flow_statements.CashFlowStatementsSchema.html
**Word Count:** 74
**Links Count:** 413
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# CashFlowStatementsSchema\#

_class _langchain\_community.tools.financial\_datasets.cash\_flow\_statements.CashFlowStatementsSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/financial_datasets/cash_flow_statements.html#CashFlowStatementsSchema)\#     

Bases: `BaseModel`

Input for CashFlowStatements.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _limit _: int_ _\[Required\]_\#     

The number of cash flow statements to return. Default is 10.

_param _period _: str_ _\[Required\]_\#     

The period of the cash flow statement. Possible values are: annual, quarterly, ttm. Default is ‘annual’.

_param _ticker _: str_ _\[Required\]_\#     

The ticker symbol to fetch cash flow statements for.

__On this page