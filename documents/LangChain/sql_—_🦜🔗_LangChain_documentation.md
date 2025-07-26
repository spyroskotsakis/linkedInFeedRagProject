# sql — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/sql.html
**Word Count:** 39
**Links Count:** 102
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# `sql`\#

**SQL Chain** interacts with SQL Database.

**Classes**

[`sql.base.SQLDatabaseChain`](https://python.langchain.com/api_reference/experimental/sql/langchain_experimental.sql.base.SQLDatabaseChain.html#langchain_experimental.sql.base.SQLDatabaseChain "langchain_experimental.sql.base.SQLDatabaseChain") | Chain for interacting with SQL Database.   ---|---   [`sql.base.SQLDatabaseSequentialChain`](https://python.langchain.com/api_reference/experimental/sql/langchain_experimental.sql.base.SQLDatabaseSequentialChain.html#langchain_experimental.sql.base.SQLDatabaseSequentialChain "langchain_experimental.sql.base.SQLDatabaseSequentialChain") | Chain for querying SQL database that is a sequential chain.   [`sql.vector_sql.VectorSQLDatabaseChain`](https://python.langchain.com/api_reference/experimental/sql/langchain_experimental.sql.vector_sql.VectorSQLDatabaseChain.html#langchain_experimental.sql.vector_sql.VectorSQLDatabaseChain "langchain_experimental.sql.vector_sql.VectorSQLDatabaseChain") | Chain for interacting with Vector SQL Database.   [`sql.vector_sql.VectorSQLOutputParser`](https://python.langchain.com/api_reference/experimental/sql/langchain_experimental.sql.vector_sql.VectorSQLOutputParser.html#langchain_experimental.sql.vector_sql.VectorSQLOutputParser "langchain_experimental.sql.vector_sql.VectorSQLOutputParser") | Output Parser for Vector SQL.   [`sql.vector_sql.VectorSQLRetrieveAllOutputParser`](https://python.langchain.com/api_reference/experimental/sql/langchain_experimental.sql.vector_sql.VectorSQLRetrieveAllOutputParser.html#langchain_experimental.sql.vector_sql.VectorSQLRetrieveAllOutputParser "langchain_experimental.sql.vector_sql.VectorSQLRetrieveAllOutputParser") | Parser based on VectorSQLOutputParser.      **Functions**

[`sql.vector_sql.get_result_from_sqldb`](https://python.langchain.com/api_reference/experimental/sql/langchain_experimental.sql.vector_sql.get_result_from_sqldb.html#langchain_experimental.sql.vector_sql.get_result_from_sqldb "langchain_experimental.sql.vector_sql.get_result_from_sqldb")\(db, cmd\) | Get result from SQL Database.   ---|---