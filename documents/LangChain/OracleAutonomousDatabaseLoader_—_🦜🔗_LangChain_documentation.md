# OracleAutonomousDatabaseLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.oracleadb_loader.OracleAutonomousDatabaseLoader.html
**Word Count:** 345
**Links Count:** 418
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# OracleAutonomousDatabaseLoader\#

_class _langchain\_community.document\_loaders.oracleadb\_loader.OracleAutonomousDatabaseLoader\(

    _query : str_,     _user : str_,     _password : str_,     _\*_ ,     _schema : str | None = None_,     _tns\_name : str | None = None_,     _config\_dir : str | None = None_,     _wallet\_location : str | None = None_,     _wallet\_password : str | None = None_,     _connection\_string : str | None = None_,     _metadata : List\[str\] | None = None_,     _parameters : list | tuple | dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleadb_loader.html#OracleAutonomousDatabaseLoader)\#     

Load from oracle adb

Autonomous Database connection can be made by either connection\_string or tns name. wallet\_location and wallet\_password are required for TLS connection. Each document will represent one row of the query result. Columns are written into the page\_content and ‘metadata’ in constructor is written into ‘metadata’ of document, by default, the ‘metadata’ is None.

init method :param query: sql query to execute :param user: username :param password: user password :param schema: schema to run in database :param tns\_name: tns name in tnsname.ora :param config\_dir: directory of config files\(tnsname.ora, wallet\) :param wallet\_location: location of wallet :param wallet\_password: password of wallet :param connection\_string: connection string to connect to adb instance :param metadata: metadata used in document :param parameters: bind variable to use in query

Methods

`__init__`\(query, user, password, \*\[, schema, ...\]\) | init method :param query: sql query to execute :param user: username :param password: user password :param schema: schema to run in database :param tns\_name: tns name in tnsname.ora :param config\_dir: directory of config files\(tnsname.ora, wallet\) :param wallet\_location: location of wallet :param wallet\_password: password of wallet :param connection\_string: connection string to connect to adb instance :param metadata: metadata used in document :param parameters: bind variable to use in query   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **query** \(_str_\)

  * **user** \(_str_\)

  * **password** \(_str_\)

  * **schema** \(_str_ _|__None_\)

  * **tns\_name** \(_str_ _|__None_\)

  * **config\_dir** \(_str_ _|__None_\)

  * **wallet\_location** \(_str_ _|__None_\)

  * **wallet\_password** \(_str_ _|__None_\)

  * **connection\_string** \(_str_ _|__None_\)

  * **metadata** \(_List_ _\[__str_ _\]__|__None_\)

  * **parameters** \(_list_ _|__tuple_ _|__dict_ _|__None_\)

\_\_init\_\_\(

    _query : str_,     _user : str_,     _password : str_,     _\*_ ,     _schema : str | None = None_,     _tns\_name : str | None = None_,     _config\_dir : str | None = None_,     _wallet\_location : str | None = None_,     _wallet\_password : str | None = None_,     _connection\_string : str | None = None_,     _metadata : List\[str\] | None = None_,     _parameters : list | tuple | dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleadb_loader.html#OracleAutonomousDatabaseLoader.__init__)\#     

init method :param query: sql query to execute :param user: username :param password: user password :param schema: schema to run in database :param tns\_name: tns name in tnsname.ora :param config\_dir: directory of config files\(tnsname.ora, wallet\) :param wallet\_location: location of wallet :param wallet\_password: password of wallet :param connection\_string: connection string to connect to adb instance :param metadata: metadata used in document :param parameters: bind variable to use in query

Parameters:     

  * **query** \(_str_\)

  * **user** \(_str_\)

  * **password** \(_str_\)

  * **schema** \(_str_ _|__None_\)

  * **tns\_name** \(_str_ _|__None_\)

  * **config\_dir** \(_str_ _|__None_\)

  * **wallet\_location** \(_str_ _|__None_\)

  * **wallet\_password** \(_str_ _|__None_\)

  * **connection\_string** \(_str_ _|__None_\)

  * **metadata** \(_List_ _\[__str_ _\]__|__None_\)

  * **parameters** \(_list_ _|__tuple_ _|__dict_ _|__None_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleadb_loader.html#OracleAutonomousDatabaseLoader.load)\#     

Load data into Document objects.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

Examples using OracleAutonomousDatabaseLoader

  * [Oracle Autonomous Database](https://python.langchain.com/docs/integrations/document_loaders/oracleadb_loader/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)