# YouSearchAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouSearchAPIWrapper.html
**Word Count:** 233
**Links Count:** 313
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# YouSearchAPIWrapper\#

_class _langchain\_community.utilities.you.YouSearchAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/you.html#YouSearchAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for you.com Search and News API.

To connect to the You.com api requires an API key which you can get at <https://api.you.com>. You can check out the docs at <https://documentation.you.com/api-reference/>.

You need to set the environment variable YDC\_API\_KEY for retriever to operate.

ydc\_api\_key\#     

you.com api key, if YDC\_API\_KEY is not set in the environment

Type:     

str, optional

endpoint\_type\#     

you.com endpoints: search, news, rag; web and snippet alias search rag returns \{‘message’: ‘Forbidden’\} @todo news endpoint

Type:     

str, optional

num\_web\_results\#     

The max number of web results to return, must be under 20. This is mapped to the count query parameter for the News API.

Type:     

int, optional

safesearch\#     

Safesearch settings, one of off, moderate, strict, defaults to moderate

Type:     

str, optional

country\#     

Country code, ex: ‘US’ for United States, see api docs for list

Type:     

str, optional

search\_lang\#     

\(News API\) Language codes, ex: ‘en’ for English, see api docs for list

Type:     

str, optional

ui\_lang\#     

\(News API\) User interface language for the response, ex: ‘en’ for English,     

see api docs for list

Type:     

str, optional

spellcheck\#     

\(News API\) Whether to spell check query or not, defaults to True

Type:     

bool, optional

k\#     

max number of Documents to return using results\(\)

Type:     

int, optional

n\_hits\#     

Alias for num\_web\_results

Type:     

int, optional, deprecated

n\_snippets\_per\_hit\#     

limit the number of snippets returned per hit

Type:     

int, optional

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _country _: str | None_ _ = None_\#     

_param _endpoint\_type _: Literal\['search', 'news', 'rag', 'snippet'\]__ = 'search'_\#     

_param _k _: int | None_ _ = None_\#     

_param _n\_hits _: int | None_ _ = None_\#     

_param _n\_snippets\_per\_hit _: int | None_ _ = None_\#     

_param _num\_web\_results _: int | None_ _ = None_\#     

_param _safesearch _: Literal\['off', 'moderate', 'strict'\] | None_ _ = None_\#     

_param _search\_lang _: str | None_ _ = None_\#     

_param _spellcheck _: bool | None_ _ = None_\#     

_param _ui\_lang _: str | None_ _ = None_\#     

_param _ydc\_api\_key _: str | None_ _ = None_\#     

raw\_results\(

    _query : str_,     _\*\* kwargs: Any_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/you.html#YouSearchAPIWrapper.raw_results)\#     

Run query through you.com Search and return hits.

Parameters:     

  * **query** \(_str_\) – The query to search for.

  * **kwargs** \(_Any_\)

Return type:     

_Dict_

Returns: YouAPIOutput

_async _raw\_results\_async\(

    _query : str_,     _\*\* kwargs: Any_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/you.html#YouSearchAPIWrapper.raw_results_async)\#     

Get results from the you.com Search API asynchronously.

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_Dict_

results\(

    _query : str_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/you.html#YouSearchAPIWrapper.results)\#     

Run query through you.com Search and parses results into Documents.

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _results\_async\(

    _query : str_,     _\*\* kwargs: Any_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/you.html#YouSearchAPIWrapper.results_async)\#     

Parameters:     

  * **query** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using YouSearchAPIWrapper

  * [You.com](https://python.langchain.com/docs/integrations/retrievers/you-retriever/)

  * [You.com Search](https://python.langchain.com/docs/integrations/tools/you/)

__On this page