# IncomeStatementsSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.financial_datasets.income_statements.IncomeStatementsSchema.html
**Word Count:** 71
**Links Count:** 413
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# IncomeStatementsSchema\#

_class _langchain\_community.tools.financial\_datasets.income\_statements.IncomeStatementsSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/financial_datasets/income_statements.html#IncomeStatementsSchema)\#     

Bases: `BaseModel`

Input for IncomeStatements.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _limit _: int_ _\[Required\]_\#     

The number of income statements to return. Default is 10.

_param _period _: str_ _\[Required\]_\#     

The period of the income statement. Possible values are: annual, quarterly, ttm. Default is ‘annual’.

_param _ticker _: str_ _\[Required\]_\#     

The ticker symbol to fetch income statements for.

__On this page