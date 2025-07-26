# CassandraDatabaseToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.cassandra_database.toolkit.CassandraDatabaseToolkit.html
**Word Count:** 63
**Links Count:** 170
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# CassandraDatabaseToolkit\#

_class _langchain\_community.agent\_toolkits.cassandra\_database.toolkit.CassandraDatabaseToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/cassandra_database/toolkit.html#CassandraDatabaseToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Toolkit for interacting with an Apache Cassandra database.

Parameters:     

**db** – CassandraDatabase. The Cassandra database to interact with.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _db _: [CassandraDatabase](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.cassandra_database.CassandraDatabase.html#langchain_community.utilities.cassandra_database.CassandraDatabase "langchain_community.utilities.cassandra_database.CassandraDatabase")_ _\[Required\]_\#     

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/cassandra_database/toolkit.html#CassandraDatabaseToolkit.get_tools)\#     

Get the tools in the toolkit.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using CassandraDatabaseToolkit

  * [Cassandra](https://python.langchain.com/docs/integrations/providers/cassandra/)

  * [Cassandra Database Toolkit](https://python.langchain.com/docs/integrations/tools/cassandra_database/)

__On this page