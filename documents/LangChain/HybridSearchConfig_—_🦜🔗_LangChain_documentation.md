# HybridSearchConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/postgres/v2/langchain_postgres.v2.hybrid_search_config.HybridSearchConfig.html
**Word Count:** 132
**Links Count:** 96
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# HybridSearchConfig\#

_class _langchain\_postgres.v2.hybrid\_search\_config.HybridSearchConfig\(_tsv\_column: str | None = '', tsv\_lang: str | None = 'pg\_catalog.english', fts\_query: str | None = '', fusion\_function: ~typing.Callable\[\[~typing.Sequence\[~sqlalchemy.engine.row.RowMapping\], ~typing.Sequence\[~sqlalchemy.engine.row.RowMapping\], ~typing.Any\], ~typing.Sequence\[~typing.Any\]\] = <function weighted\_sum\_ranking>, fusion\_function\_parameters: dict\[str, ~typing.Any\] = <factory>, primary\_top\_k: int = 4, secondary\_top\_k: int = 4, index\_name: str = 'langchain\_tsv\_index', index\_type: str = 'GIN'_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_postgres/v2/hybrid_search_config.html#HybridSearchConfig)\#     

AlloyDB Vector Store Hybrid Search Config.

Queries might be slow if the hybrid search column does not exist. For best hybrid search performance, consider creating a TSV column and adding GIN index.

Attributes

`fts_query` |    ---|---   `index_name` |    `index_type` |    `primary_top_k` |    `secondary_top_k` |    `tsv_column` |    `tsv_lang` |       Methods

`__init__`\(\[tsv\_column, tsv\_lang, fts\_query, ...\]\) |    ---|---   `fusion_function`\(secondary\_search\_results\[, ...\]\) | Ranks documents using a weighted sum of scores from two sources.      Parameters:     

  * **tsv\_column** \(_str_ _|__None_\)

  * **tsv\_lang** \(_str_ _|__None_\)

  * **fts\_query** \(_str_ _|__None_\)

  * **fusion\_function** \(_Callable_ _\[__\[__Sequence_ _\[__RowMapping_ _\]__,__Sequence_ _\[__RowMapping_ _\]__,__Any_ _\]__,__Sequence_ _\[__Any_ _\]__\]_\)

  * **fusion\_function\_parameters** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **primary\_top\_k** \(_int_\)

  * **secondary\_top\_k** \(_int_\)

  * **index\_name** \(_str_\)

  * **index\_type** \(_str_\)

\_\_init\_\_\(_tsv\_column: str | None = '', tsv\_lang: str | None = 'pg\_catalog.english', fts\_query: str | None = '', fusion\_function: ~typing.Callable\[\[~typing.Sequence\[~sqlalchemy.engine.row.RowMapping\], ~typing.Sequence\[~sqlalchemy.engine.row.RowMapping\], ~typing.Any\], ~typing.Sequence\[~typing.Any\]\] = <function weighted\_sum\_ranking>, fusion\_function\_parameters: dict\[str, ~typing.Any\] = <factory>, primary\_top\_k: int = 4, secondary\_top\_k: int = 4, index\_name: str = 'langchain\_tsv\_index', index\_type: str = 'GIN'_\) → None\#     

Parameters:     

  * **tsv\_column** \(_str_ _|__None_\)

  * **tsv\_lang** \(_str_ _|__None_\)

  * **fts\_query** \(_str_ _|__None_\)

  * **fusion\_function** \(_Callable_ _\[__\[__Sequence_ _\[__RowMapping_ _\]__,__Sequence_ _\[__RowMapping_ _\]__,__Any_ _\]__,__Sequence_ _\[__Any_ _\]__\]_\)

  * **fusion\_function\_parameters** \(_dict_ _\[__str_ _,__Any_ _\]_\)

  * **primary\_top\_k** \(_int_\)

  * **secondary\_top\_k** \(_int_\)

  * **index\_name** \(_str_\)

  * **index\_type** \(_str_\)

Return type:     

None

fusion\_function\(

    _secondary\_search\_results : Sequence\[RowMapping\]_,     _primary\_results\_weight : float = 0.5_,     _secondary\_results\_weight : float = 0.5_,     _fetch\_top\_k : int = 4_, \) → Sequence\[dict\[str, Any\]\]\#     

Ranks documents using a weighted sum of scores from two sources.

Parameters:     

  * **primary\_search\_results** \(_Sequence_ _\[__RowMapping_ _\]_\) – A list of \(document, distance\) tuples from the primary search.

  * **secondary\_search\_results** \(_Sequence_ _\[__RowMapping_ _\]_\) – A list of \(document, distance\) tuples from the secondary search.

  * **primary\_results\_weight** \(_float_\) – The weight for the primary source’s scores. Defaults to 0.5.

  * **secondary\_results\_weight** \(_float_\) – The weight for the secondary source’s scores. Defaults to 0.5.

  * **fetch\_top\_k** \(_int_\) – The number of documents to fetch after merging the results. Defaults to 4.

Returns:     

A list of \(document, distance\) tuples, sorted by weighted\_score in descending order.

Return type:     

_Sequence_\[dict\[str, _Any_\]\]

__On this page