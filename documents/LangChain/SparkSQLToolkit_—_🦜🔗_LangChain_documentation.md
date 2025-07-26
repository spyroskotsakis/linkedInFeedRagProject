# SparkSQLToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.spark_sql.toolkit.SparkSQLToolkit.html
**Word Count:** 63
**Links Count:** 172
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# SparkSQLToolkit\#

_class _langchain\_community.agent\_toolkits.spark\_sql.toolkit.SparkSQLToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/spark_sql/toolkit.html#SparkSQLToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with Spark SQL.

Parameters:     

  * **db** – SparkSQL. The Spark SQL database.

  * **llm** – BaseLanguageModel. The language model.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _db _: [SparkSQL](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.spark_sql.SparkSQL.html#langchain_community.utilities.spark_sql.SparkSQL "langchain_community.utilities.spark_sql.SparkSQL")_ _\[Required\]_\#     

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Required\]_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/spark_sql/toolkit.html#SparkSQLToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using SparkSQLToolkit

  * [Spark SQL Toolkit](https://python.langchain.com/docs/integrations/tools/spark_sql/)

__On this page