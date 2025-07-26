# DistanceStrategy — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.indexes.DistanceStrategy.html
**Word Count:** 24
**Links Count:** 107
**Scraped:** 2025-07-21 08:26:03
**Status:** completed

---

# DistanceStrategy\#

_class _langchain\_postgres.v2.indexes.DistanceStrategy\(_value_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/indexes.html#DistanceStrategy)\#     

Enumerator of the Distance strategies.

EUCLIDEAN _ = StrategyMixin\(operator='<->', search\_function='l2\_distance', index\_function='vector\_l2\_ops'\)_\#     

COSINE\_DISTANCE _ = StrategyMixin\(operator='<=>', search\_function='cosine\_distance', index\_function='vector\_cosine\_ops'\)_\#     

INNER\_PRODUCT _ = StrategyMixin\(operator='<\#>', search\_function='inner\_product', index\_function='vector\_ip\_ops'\)_\#     

operator _: str_\#     

search\_function _: str_\#     

index\_function _: str_\#     

Examples using DistanceStrategy

  * [Kinetica Vectorstore API](https://python.langchain.com/docs/integrations/vectorstores/kinetica/)

  * [Oracle AI Vector Search: Vector Store](https://python.langchain.com/docs/integrations/vectorstores/oracle/)

  * [SAP HANA Cloud Vector Engine](https://python.langchain.com/docs/integrations/vectorstores/sap_hanavector/)

  * [SemaDB](https://python.langchain.com/docs/integrations/vectorstores/semadb/)

  * [SingleStoreDB](https://python.langchain.com/docs/integrations/vectorstores/singlestoredb/)

__On this page