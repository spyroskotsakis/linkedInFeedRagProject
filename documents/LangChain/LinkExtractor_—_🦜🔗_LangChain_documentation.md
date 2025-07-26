# LinkExtractor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html
**Word Count:** 87
**Links Count:** 132
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# LinkExtractor\#

_class _langchain\_community.graph\_vectorstores.extractors.link\_extractor.LinkExtractor\(_\* args: Any_, _\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/link_extractor.html#LinkExtractor)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Interface for extracting links \(incoming, outgoing, bidirectional\).

Methods

`__init__`\(\*args, \*\*kwargs\) |    ---|---   `extract_many`\(inputs\) | Add edges from each input to the corresponding documents.   `extract_one`\(input\) | Add edges from each input to the corresponding documents.      \_\_init\_\_\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → Any\#     

Parameters:     

  * **self** \(_Any_\)

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

_Any_

extract\_many\(

    _inputs : Iterable\[InputT\]_, \) → Iterable\[Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/link_extractor.html#LinkExtractor.extract_many)\#     

Add edges from each input to the corresponding documents.

Parameters:     

**inputs** \(_Iterable_ _\[__InputT_ _\]_\) – The input content to extract edges from.

Returns:     

Iterable over the set of links extracted from the input.

Return type:     

_Iterable_\[_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]\]

_abstractmethod _extract\_one\(

    _input : InputT_, \) → Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/link_extractor.html#LinkExtractor.extract_one)\#     

Add edges from each input to the corresponding documents.

Parameters:     

**input** \(_InputT_\) – The input content to extract edges from.

Returns:     

Set of links extracted from the input.

Return type:     

_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]

__On this page