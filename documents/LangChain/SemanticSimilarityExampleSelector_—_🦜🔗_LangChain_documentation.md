# SemanticSimilarityExampleSelector — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/example_selectors/langchain_core.example_selectors.semantic_similarity.SemanticSimilarityExampleSelector.html
**Word Count:** 403
**Links Count:** 148
**Scraped:** 2025-07-21 07:52:36
**Status:** completed

---

# SemanticSimilarityExampleSelector\#

_class _langchain\_core.example\_selectors.semantic\_similarity.SemanticSimilarityExampleSelector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/semantic_similarity.html#SemanticSimilarityExampleSelector)\#     

Bases: `_VectorStoreExampleSelector`

Select examples based on semantic similarity.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _example\_keys _: list\[str\] | None_ _ = None_\#     

Optional keys to filter examples to.

_param _input\_keys _: list\[str\] | None_ _ = None_\#     

Optional keys to filter input to. If provided, the search is based on the input variables instead of all variables.

_param _k _: int_ _ = 4_\#     

Number of examples to select.

_param _vectorstore _: [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_ _\[Required\]_\#     

VectorStore that contains information about examples.

_param _vectorstore\_kwargs _: dict\[str, Any\] | None_ _ = None_\#     

Extra arguments passed to similarity\_search function of the vectorstore.

_async classmethod _afrom\_examples\(

    _examples : list\[dict\]_,     _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _vectorstore\_cls : type\[[VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\]_,     _k : int = 4_,     _input\_keys : list\[str\] | None = None_,     _\*_ ,     _example\_keys : list\[str\] | None = None_,     _vectorstore\_kwargs : dict | None = None_,     _\*\* vectorstore\_cls\_kwargs: Any_, \) → SemanticSimilarityExampleSelector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/semantic_similarity.html#SemanticSimilarityExampleSelector.afrom_examples)\#     

Async create k-shot example selector using example list and embeddings.

Reshuffles examples dynamically based on query similarity.

Parameters:     

  * **examples** \(_list_ _\[__dict_ _\]_\) – List of examples to use in the prompt.

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – An initialized embedding API interface, e.g. OpenAIEmbeddings\(\).

  * **vectorstore\_cls** \(_type_ _\[_[_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore") _\]_\) – A vector store DB interface class, e.g. FAISS.

  * **k** \(_int_\) – Number of examples to select. Default is 4.

  * **input\_keys** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – If provided, the search is based on the input variables instead of all variables.

  * **example\_keys** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – If provided, keys to filter examples to.

  * **vectorstore\_kwargs** \(_Optional_ _\[__dict_ _\]_\) – Extra arguments passed to similarity\_search function of the vectorstore.

  * **vectorstore\_cls\_kwargs** \(_Any_\) – optional kwargs containing url for vector store

Returns:     

The ExampleSelector instantiated, backed by a vector store.

Return type:     

SemanticSimilarityExampleSelector

_classmethod _from\_examples\(

    _examples : list\[dict\]_,     _embeddings : [Embeddings](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")_,     _vectorstore\_cls : type\[[VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")\]_,     _k : int = 4_,     _input\_keys : list\[str\] | None = None_,     _\*_ ,     _example\_keys : list\[str\] | None = None_,     _vectorstore\_kwargs : dict | None = None_,     _\*\* vectorstore\_cls\_kwargs: Any_, \) → SemanticSimilarityExampleSelector[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/semantic_similarity.html#SemanticSimilarityExampleSelector.from_examples)\#     

Create k-shot example selector using example list and embeddings.

Reshuffles examples dynamically based on query similarity.

Parameters:     

  * **examples** \(_list_ _\[__dict_ _\]_\) – List of examples to use in the prompt.

  * **embeddings** \([_Embeddings_](https://python.langchain.com/api_reference/core/embeddings/langchain_core.embeddings.embeddings.Embeddings.html#langchain_core.embeddings.embeddings.Embeddings "langchain_core.embeddings.embeddings.Embeddings")\) – An initialized embedding API interface, e.g. OpenAIEmbeddings\(\).

  * **vectorstore\_cls** \(_type_ _\[_[_VectorStore_](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore") _\]_\) – A vector store DB interface class, e.g. FAISS.

  * **k** \(_int_\) – Number of examples to select. Default is 4.

  * **input\_keys** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – If provided, the search is based on the input variables instead of all variables.

  * **example\_keys** \(_Optional_ _\[__list_ _\[__str_ _\]__\]_\) – If provided, keys to filter examples to.

  * **vectorstore\_kwargs** \(_Optional_ _\[__dict_ _\]_\) – Extra arguments passed to similarity\_search function of the vectorstore.

  * **vectorstore\_cls\_kwargs** \(_Any_\) – optional kwargs containing url for vector store

Returns:     

The ExampleSelector instantiated, backed by a vector store.

Return type:     

SemanticSimilarityExampleSelector

_async _aadd\_example\(

    _example : dict\[str, str\]_, \) → str\#     

Async add new example to vectorstore.

Parameters:     

**example** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Returns:     

The ID of the added example.

Return type:     

str

add\_example\(

    _example : dict\[str, str\]_, \) → str\#     

Add a new example to vectorstore.

Parameters:     

**example** \(_dict_ _\[__str_ _,__str_ _\]_\) – A dictionary with keys as input variables and values as their values.

Returns:     

The ID of the added example.

Return type:     

str

_async _aselect\_examples\(

    _input\_variables : dict\[str, str\]_, \) → list\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/semantic_similarity.html#SemanticSimilarityExampleSelector.aselect_examples)\#     

Asynchronously select examples based on semantic similarity.

Parameters:     

**input\_variables** \(_dict_ _\[__str_ _,__str_ _\]_\) – The input variables to use for search.

Returns:     

The selected examples.

Return type:     

list\[dict\]

select\_examples\(

    _input\_variables : dict\[str, str\]_, \) → list\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/example_selectors/semantic_similarity.html#SemanticSimilarityExampleSelector.select_examples)\#     

Select examples based on semantic similarity.

Parameters:     

**input\_variables** \(_dict_ _\[__str_ _,__str_ _\]_\) – The input variables to use for search.

Returns:     

The selected examples.

Return type:     

list\[dict\]

Examples using SemanticSimilarityExampleSelector

  * [How to best prompt for Graph-RAG](https://python.langchain.com/docs/how_to/graph_prompting/)

  * [How to better prompt when doing SQL question-answering](https://python.langchain.com/docs/how_to/sql_prompting/)

  * [How to select examples by maximal marginal relevance \(MMR\)](https://python.langchain.com/docs/how_to/example_selectors_mmr/)

  * [How to select examples by similarity](https://python.langchain.com/docs/how_to/example_selectors_similarity/)

  * [How to use few shot examples](https://python.langchain.com/docs/how_to/few_shot_examples/)

  * [How to use few shot examples in chat models](https://python.langchain.com/docs/how_to/few_shot_examples_chat/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)