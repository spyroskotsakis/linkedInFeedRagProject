# cosine_similarity — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/chroma/vectorstores/langchain_chroma.vectorstores.cosine_similarity.html
**Word Count:** 33
**Links Count:** 72
**Scraped:** 2025-07-21 07:57:21
**Status:** completed

---

# cosine\_similarity\#

langchain\_chroma.vectorstores.cosine\_similarity\(

    _X : list\[list\[float\]\] | list\[ndarray\] | ndarray_,     _Y : list\[list\[float\]\] | list\[ndarray\] | ndarray_, \) → ndarray[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_chroma/vectorstores.html#cosine_similarity)\#     

Row-wise cosine similarity between two equal-width matrices.

Raises:     

**ValueError** – If the number of columns in X and Y are not the same.

Parameters:     

  * **X** \(_list_ _\[__list_ _\[__float_ _\]__\]__|__list_ _\[__ndarray_ _\]__|__ndarray_\)

  * **Y** \(_list_ _\[__list_ _\[__float_ _\]__\]__|__list_ _\[__ndarray_ _\]__|__ndarray_\)

Return type:     

_ndarray_

Examples using cosine\_similarity

  * [How to route between sub-chains](https://python.langchain.com/docs/how_to/routing/)

__On this page