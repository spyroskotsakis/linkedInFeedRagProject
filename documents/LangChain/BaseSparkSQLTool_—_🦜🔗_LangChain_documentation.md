# BaseSparkSQLTool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.spark_sql.tool.BaseSparkSQLTool.html
**Word Count:** 45
**Links Count:** 410
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# BaseSparkSQLTool\#

_class _langchain\_community.tools.spark\_sql.tool.BaseSparkSQLTool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/spark_sql/tool.html#BaseSparkSQLTool)\#     

Bases: `BaseModel`

Base tool for interacting with Spark SQL.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _db _: [SparkSQL](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.spark_sql.SparkSQL.html#langchain_community.utilities.spark_sql.SparkSQL "langchain_community.utilities.spark_sql.SparkSQL")_ _\[Required\]_\#     

__On this page