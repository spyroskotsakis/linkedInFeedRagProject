# FinancialDatasetsToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.financial_datasets.toolkit.FinancialDatasetsToolkit.html
**Word Count:** 56
**Links Count:** 169
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# FinancialDatasetsToolkit\#

_class _langchain\_community.agent\_toolkits.financial\_datasets.toolkit.FinancialDatasetsToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/financial_datasets/toolkit.html#FinancialDatasetsToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with financialdatasets.ai.

Parameters:     

**api\_wrapper** – The FinancialDatasets API Wrapper.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_wrapper _: [FinancialDatasetsAPIWrapper](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.financial_datasets.FinancialDatasetsAPIWrapper.html#langchain_community.utilities.financial_datasets.FinancialDatasetsAPIWrapper "langchain_community.utilities.financial_datasets.FinancialDatasetsAPIWrapper")_ _\[Optional\]_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/financial_datasets/toolkit.html#FinancialDatasetsToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using FinancialDatasetsToolkit

  * [FinancialDatasets Toolkit](https://python.langchain.com/docs/integrations/tools/financial_datasets/)

__On this page