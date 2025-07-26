# SemanticScholarAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.semanticscholar.SemanticScholarAPIWrapper.html
**Word Count:** 108
**Links Count:** 263
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# SemanticScholarAPIWrapper\#

_class _langchain\_community.utilities.semanticscholar.SemanticScholarAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/semanticscholar.html#SemanticScholarAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around semanticscholar.org API. [danielnsilva/semanticscholar](https://github.com/danielnsilva/semanticscholar)

You should have this library installed.

pip install semanticscholar

Semantic Scholar API can conduct searches and fetch document metadata like title, abstract, authors, etc.

Attributes: top\_k\_results: number of the top-scored document used for the Semantic Scholar tool load\_max\_docs: a limit to the number of loaded documents

Example: .. code-block:: python

from langchain\_community.utilities.semanticscholar import SemanticScholarAPIWrapper ss = SemanticScholarAPIWrapper\(

> top\_k\_results = 3, load\_max\_docs = 3

\) ss.run\(“biases in large language models”\)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _S2\_MAX\_QUERY\_LENGTH _: int_ _ = 300_\#     

_param _doc\_content\_chars\_max _: int | None_ _ = 4000_\#     

_param _load\_max\_docs _: int_ _ = 100_\#     

_param _returned\_fields _: List\[str\]__ = \['title', 'abstract', 'venue', 'year', 'paperId', 'citationCount', 'openAccessPdf', 'authors', 'externalIds'\]_\#     

_param _top\_k\_results _: int_ _ = 5_\#     

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/semanticscholar.html#SemanticScholarAPIWrapper.run)\#     

Run the Semantic Scholar API.

Parameters:     

**query** \(_str_\)

Return type:     

str

__On this page