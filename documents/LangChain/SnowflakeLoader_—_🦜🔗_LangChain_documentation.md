# SnowflakeLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.snowflake_loader.SnowflakeLoader.html
**Word Count:** 225
**Links Count:** 418
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# SnowflakeLoader\#

_class _langchain\_community.document\_loaders.snowflake\_loader.SnowflakeLoader\(

    _query : str_,     _user : str_,     _password : str_,     _account : str_,     _warehouse : str_,     _role : str_,     _database : str_,     _schema : str_,     _parameters : Dict\[str, Any\] | None = None_,     _page\_content\_columns : List\[str\] | None = None_,     _metadata\_columns : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/snowflake_loader.html#SnowflakeLoader)\#     

Load from Snowflake API.

Each document represents one row of the result. The page\_content\_columns are written into the page\_content of the document. The metadata\_columns are written into the metadata of the document. By default, all columns are written into the page\_content and none into the metadata.

Initialize Snowflake document loader.

Parameters:     

  * **query** \(_str_\) – The query to run in Snowflake.

  * **user** \(_str_\) – Snowflake user.

  * **password** \(_str_\) – Snowflake password.

  * **account** \(_str_\) – Snowflake account.

  * **warehouse** \(_str_\) – Snowflake warehouse.

  * **role** \(_str_\) – Snowflake role.

  * **database** \(_str_\) – Snowflake database

  * **schema** \(_str_\) – Snowflake schema

  * **parameters** \(_Optional_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – Optional. Parameters to pass to the query.

  * **page\_content\_columns** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. Columns written to Document page\_content.

  * **metadata\_columns** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – Optional. Columns written to Document metadata.

Methods

`__init__`\(query, user, password, account, ...\) | Initialize Snowflake document loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _query : str_,     _user : str_,     _password : str_,     _account : str_,     _warehouse : str_,     _role : str_,     _database : str_,     _schema : str_,     _parameters : Dict\[str, Any\] | None = None_,     _page\_content\_columns : List\[str\] | None = None_,     _metadata\_columns : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/snowflake_loader.html#SnowflakeLoader.__init__)\#     

Initialize Snowflake document loader.

Parameters:     

  * **query** \(_str_\) – The query to run in Snowflake.

  * **user** \(_str_\) – Snowflake user.

  * **password** \(_str_\) – Snowflake password.

  * **account** \(_str_\) – Snowflake account.

  * **warehouse** \(_str_\) – Snowflake warehouse.

  * **role** \(_str_\) – Snowflake role.

  * **database** \(_str_\) – Snowflake database

  * **schema** \(_str_\) – Snowflake schema

  * **parameters** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Optional. Parameters to pass to the query.

  * **page\_content\_columns** \(_List_ _\[__str_ _\]__|__None_\) – Optional. Columns written to Document page\_content.

  * **metadata\_columns** \(_List_ _\[__str_ _\]__|__None_\) – Optional. Columns written to Document metadata.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/snowflake_loader.html#SnowflakeLoader.lazy_load)\#     

A lazy loader for Documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load Documents and split into chunks. Chunks are returned as Documents.

Do not override this method. It should be considered to be deprecated\!

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using SnowflakeLoader

  * [Snowflake](https://python.langchain.com/docs/integrations/document_loaders/snowflake/)

__On this page