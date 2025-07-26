# WikipediaAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.wikipedia.WikipediaAPIWrapper.html
**Word Count:** 135
**Links Count:** 274
**Scraped:** 2025-07-21 08:18:47
**Status:** completed

---

# WikipediaAPIWrapper\#

_class _langchain\_community.utilities.wikipedia.WikipediaAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/wikipedia.html#WikipediaAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around WikipediaAPI.

To use, you should have the `wikipedia` python package installed. This wrapper will use the Wikipedia API to conduct searches and fetch page summaries. By default, it will return the page summaries of the top-k results. It limits the Document content by doc\_content\_chars\_max.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _doc\_content\_chars\_max _: int_ _ = 4000_\#     

_param _lang _: str_ _ = 'en'_\#     

_param _load\_all\_available\_meta _: bool_ _ = False_\#     

_param _top\_k\_results _: int_ _ = 3_\#     

lazy\_load\(

    _query : str_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/wikipedia.html#WikipediaAPIWrapper.lazy_load)\#     

Run Wikipedia search and get the article text plus the meta information. See

Returns: a list of documents.

Parameters:     

**query** \(_str_\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(

    _query : str_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/wikipedia.html#WikipediaAPIWrapper.load)\#     

Run Wikipedia search and get the article text plus the meta information. See

Returns: a list of documents.

Parameters:     

**query** \(_str_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/wikipedia.html#WikipediaAPIWrapper.run)\#     

Run Wikipedia search and get page summaries.

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using WikipediaAPIWrapper

  * [How to use built-in tools and toolkits](https://python.langchain.com/docs/how_to/tools_builtin/)

  * [Wikipedia](https://python.langchain.com/docs/integrations/tools/wikipedia/)

  * [Zep Cloud Memory](https://python.langchain.com/docs/integrations/memory/zep_memory_cloud/)

  * [Zep Open Source Memory](https://python.langchain.com/docs/integrations/memory/zep_memory/)

__On this page