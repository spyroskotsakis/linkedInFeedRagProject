# OracleSummary — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.oracleai.OracleSummary.html
**Word Count:** 80
**Links Count:** 259
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# OracleSummary\#

_class _langchain\_community.utilities.oracleai.OracleSummary\(

    _conn : Connection_,     _params : Dict\[str, Any\]_,     _proxy : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/oracleai.html#OracleSummary)\#     

Get Summary :param conn: Oracle Connection, :param params: Summary parameters, :param proxy: Proxy

Methods

`__init__`\(conn, params\[, proxy\]\) |    ---|---   `get_summary`\(docs\) | Get the summary of the input docs. :param docs: The documents to generate summary for. Allowed input types: str, Document, List\[str\], List\[Document\].      Parameters:     

  * **conn** \(_Connection_\)

  * **params** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **proxy** \(_Optional_ _\[__str_ _\]_\)

\_\_init\_\_\(

    _conn : Connection_,     _params : Dict\[str, Any\]_,     _proxy : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/oracleai.html#OracleSummary.__init__)\#     

Parameters:     

  * **conn** \(_Connection_\)

  * **params** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **proxy** \(_Optional_ _\[__str_ _\]_\)

get\_summary\(

    _docs : Any_, \) → List\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/oracleai.html#OracleSummary.get_summary)\#     

Get the summary of the input docs. :param docs: The documents to generate summary for.

> Allowed input types: str, Document, List\[str\], List\[Document\]

Returns:     

List of summary text, one for each input doc.

Parameters:     

**docs** \(_Any_\)

Return type:     

_List_\[str\]

Examples using OracleSummary

  * [Oracle AI Vector Search: Generate Summary](https://python.langchain.com/docs/integrations/tools/oracleai/)

  * [OracleAI Vector Search](https://python.langchain.com/docs/integrations/providers/oracleai/)

__On this page