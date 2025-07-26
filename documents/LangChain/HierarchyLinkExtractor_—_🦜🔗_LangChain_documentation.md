# HierarchyLinkExtractor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.hierarchy_link_extractor.HierarchyLinkExtractor.html
**Word Count:** 263
**Links Count:** 142
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# HierarchyLinkExtractor\#

_class _langchain\_community.graph\_vectorstores.extractors.hierarchy\_link\_extractor.HierarchyLinkExtractor\(

    _\*_ ,     _kind : str = 'hierarchy'_,     _parent\_links : bool = True_,     _child\_links : bool = False_,     _sibling\_links : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/hierarchy_link_extractor.html#HierarchyLinkExtractor)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Extract links from a document hierarchy.

Example               # Given three paths (in this case, within the "Root" document):     h1 = ["Root", "H1"]     h1a = ["Root", "H1", "a"]     h1b = ["Root", "H1", "b"]          # Parent links `h1a` and `h1b` to `h1`.     # Child links `h1` to `h1a` and `h1b`.     # Sibling links `h1a` and `h1b` together (both directions).     

Example use with documents:     

Parameters:     

  * **kind** \(_str_\) – Kind of links to produce with this extractor.

  * **parent\_links** \(_bool_\) – Link from a section to its parent.

  * **child\_links** \(_bool_\) – Link from a section to its children.

  * **sibling\_links** \(_bool_\) – Link from a section to other sections with the same parent.

Methods

`__init__`\(\*\[, kind, parent\_links, ...\]\) | Extract links from a document hierarchy.   ---|---   `as_document_extractor`\(hierarchy\) | Create a LinkExtractor from Document.   `extract_many`\(inputs\) | Add edges from each input to the corresponding documents.   `extract_one`\(input\) | Add edges from each input to the corresponding documents.      \_\_init\_\_\(

    _\*_ ,     _kind : str = 'hierarchy'_,     _parent\_links : bool = True_,     _child\_links : bool = False_,     _sibling\_links : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/hierarchy_link_extractor.html#HierarchyLinkExtractor.__init__)\#     

Extract links from a document hierarchy.

Example               # Given three paths (in this case, within the "Root" document):     h1 = ["Root", "H1"]     h1a = ["Root", "H1", "a"]     h1b = ["Root", "H1", "b"]          # Parent links `h1a` and `h1b` to `h1`.     # Child links `h1` to `h1a` and `h1b`.     # Sibling links `h1a` and `h1b` together (both directions).     

Example use with documents:     

Parameters:     

  * **kind** \(_str_\) – Kind of links to produce with this extractor.

  * **parent\_links** \(_bool_\) – Link from a section to its parent.

  * **child\_links** \(_bool_\) – Link from a section to its children.

  * **sibling\_links** \(_bool_\) – Link from a section to other sections with the same parent.

as\_document\_extractor\(

    _hierarchy : Callable\[\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\], List\[str\]\]_, \) → [LinkExtractor](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor")\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/hierarchy_link_extractor.html#HierarchyLinkExtractor.as_document_extractor)\#     

Create a LinkExtractor from Document.

Parameters:     

**hierarchy** \(_Callable_ _\[__\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]__,__List_ _\[__str_ _\]__\]_\) – Function that returns the path for the given document.

Returns:     

A LinkExtractor\[Document\] suitable for application to Documents directly or with LinkExtractorTransformer.

Return type:     

[_LinkExtractor_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor")\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

extract\_many\(

    _inputs : Iterable\[InputT\]_, \) → Iterable\[Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]\]\#     

Add edges from each input to the corresponding documents.

Parameters:     

**inputs** \(_Iterable_ _\[__InputT_ _\]_\) – The input content to extract edges from.

Returns:     

Iterable over the set of links extracted from the input.

Return type:     

_Iterable_\[_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]\]

extract\_one\(

    _input : List\[str\]_, \) → Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/hierarchy_link_extractor.html#HierarchyLinkExtractor.extract_one)\#     

Add edges from each input to the corresponding documents.

Parameters:     

**input** \(_List_ _\[__str_ _\]_\) – The input content to extract edges from.

Returns:     

Set of links extracted from the input.

Return type:     

_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)