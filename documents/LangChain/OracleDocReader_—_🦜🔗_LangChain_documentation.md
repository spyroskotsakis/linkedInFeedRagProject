# OracleDocReader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.oracleai.OracleDocReader.html
**Word Count:** 54
**Links Count:** 395
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# OracleDocReader\#

_class _langchain\_community.document\_loaders.oracleai.OracleDocReader[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleai.html#OracleDocReader)\#     

Read a file

Methods

`generate_object_id`\(\[input\_string\]\) |    ---|---   `read_file`\(conn, file\_path, params\) | Read a file using OracleReader :param conn: Oracle Connection, :param file\_path: Oracle Directory, :param params: ONNX file name.      _static _generate\_object\_id\(

    _input\_string : str | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleai.html#OracleDocReader.generate_object_id)\#     

Parameters:     

**input\_string** \(_str_ _|__None_\)

Return type:     

str

_static _read\_file\(

    _conn : Connection_,     _file\_path : str_,     _params : dict_, \) → [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/oracleai.html#OracleDocReader.read_file)\#     

Read a file using OracleReader :param conn: Oracle Connection, :param file\_path: Oracle Directory, :param params: ONNX file name.

Returns:     

Plain text and metadata as Langchain Document.

Parameters:     

  * **conn** \(_Connection_\)

  * **file\_path** \(_str_\)

  * **params** \(_dict_\)

Return type:     

Union\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document"), None\]

__On this page