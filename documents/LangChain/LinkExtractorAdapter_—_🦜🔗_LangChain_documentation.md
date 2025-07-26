# LinkExtractorAdapter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor_adapter.LinkExtractorAdapter.html
**Word Count:** 81
**Links Count:** 137
**Scraped:** 2025-07-21 08:12:08
**Status:** completed

---

# LinkExtractorAdapter\#

_class _langchain\_community.graph\_vectorstores.extractors.link\_extractor\_adapter.LinkExtractorAdapter\(

    _underlying : [LinkExtractor](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor")\[UnderlyingInputT\]_,     _transform : Callable\[\[InputT\], UnderlyingInputT\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/link_extractor_adapter.html#LinkExtractorAdapter)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Methods

`__init__`\(underlying, transform\) |    ---|---   `extract_many`\(inputs\) | Add edges from each input to the corresponding documents.   `extract_one`\(input\) | Add edges from each input to the corresponding documents.      Parameters:     

  * **underlying** \([_LinkExtractor_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor") _\[__UnderlyingInputT_ _\]_\)

  * **transform** \(_Callable_ _\[__\[__InputT_ _\]__,__UnderlyingInputT_ _\]_\)

\_\_init\_\_\(

    _underlying : [LinkExtractor](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor")\[UnderlyingInputT\]_,     _transform : Callable\[\[InputT\], UnderlyingInputT\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/link_extractor_adapter.html#LinkExtractorAdapter.__init__)\#     

Parameters:     

  * **underlying** \([_LinkExtractor_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor") _\[__UnderlyingInputT_ _\]_\)

  * **transform** \(_Callable_ _\[__\[__InputT_ _\]__,__UnderlyingInputT_ _\]_\)

Return type:     

None

extract\_many\(

    _inputs : Iterable\[InputT\]_, \) → Iterable\[Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/link_extractor_adapter.html#LinkExtractorAdapter.extract_many)\#     

Add edges from each input to the corresponding documents.

Parameters:     

**inputs** \(_Iterable_ _\[__InputT_ _\]_\) – The input content to extract edges from.

Returns:     

Iterable over the set of links extracted from the input.

Return type:     

_Iterable_\[_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]\]

extract\_one\(

    _input : InputT_, \) → Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/link_extractor_adapter.html#LinkExtractorAdapter.extract_one)\#     

Add edges from each input to the corresponding documents.

Parameters:     

**input** \(_InputT_\) – The input content to extract edges from.

Returns:     

Set of links extracted from the input.

Return type:     

_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]

__On this page