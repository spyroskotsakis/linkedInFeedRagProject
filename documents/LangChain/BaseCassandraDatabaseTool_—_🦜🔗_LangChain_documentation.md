# BaseCassandraDatabaseTool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.cassandra_database.tool.BaseCassandraDatabaseTool.html
**Word Count:** 47
**Links Count:** 410
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# BaseCassandraDatabaseTool\#

_class _langchain\_community.tools.cassandra\_database.tool.BaseCassandraDatabaseTool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/cassandra_database/tool.html#BaseCassandraDatabaseTool)\#     

Bases: `BaseModel`

Base tool for interacting with an Apache Cassandra database.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _db _: [CassandraDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase "langchain_community.utilities.cassandra_database.CassandraDatabase")_ _\[Required\]_\#     

__On this page