# get_navigable_strings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_transformers/langchain_community.document_transformers.beautiful_soup_transformer.get_navigable_strings.html
**Word Count:** 32
**Links Count:** 111
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# get\_navigable\_strings\#

langchain\_community.document\_transformers.beautiful\_soup\_transformer.get\_navigable\_strings\(

    _element : Any_,     _\*_ ,     _remove\_comments : bool = False_, \) → Iterator\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_transformers/beautiful_soup_transformer.html#get_navigable_strings)\#     

Get all navigable strings from a BeautifulSoup element.

Parameters:     

  * **element** \(_Any_\) – A BeautifulSoup element.

  * **remove\_comments** \(_bool_\) – If set to True, the comments will be removed.

Returns:     

A generator of strings.

Return type:     

_Iterator_\[str\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)