# cosine_similarity_top_k — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.math.cosine_similarity_top_k.html
**Word Count:** 53
**Links Count:** 87
**Scraped:** 2025-07-21 08:29:02
**Status:** completed

---

# cosine\_similarity\_top\_k\#

langchain\_aws.utilities.math.cosine\_similarity\_top\_k\(

    _X : List\[List\[float\]\] | List\[ndarray\] | ndarray_,     _Y : List\[List\[float\]\] | List\[ndarray\] | ndarray_,     _top\_k : int | None = 5_,     _score\_threshold : float | None = None_, \) → Tuple\[List\[Tuple\[int, int\]\], List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/utilities/math.html#cosine_similarity_top_k)\#     

Row-wise cosine similarity with optional top-k and score threshold filtering.

Parameters:     

  * **X** \(_List_ _\[__List_ _\[__float_ _\]__\]__|__List_ _\[__ndarray_ _\]__|__ndarray_\) – Matrix.

  * **Y** \(_List_ _\[__List_ _\[__float_ _\]__\]__|__List_ _\[__ndarray_ _\]__|__ndarray_\) – Matrix, same width as X.

  * **top\_k** \(_int_ _|__None_\) – Max number of results to return.

  * **score\_threshold** \(_float_ _|__None_\) – Minimum cosine similarity of results.

Returns:     

Tuple of two lists. First contains two-tuples of indices \(X\_idx, Y\_idx\),     

second contains corresponding cosine similarities.

Return type:     

_Tuple_\[_List_\[_Tuple_\[int, int\]\], _List_\[float\]\]

__On this page