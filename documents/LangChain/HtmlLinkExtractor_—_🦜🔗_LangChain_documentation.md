# HtmlLinkExtractor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.html_link_extractor.HtmlLinkExtractor.html
**Word Count:** 519
**Links Count:** 168
**Scraped:** 2025-07-21 08:17:20
**Status:** completed

---

# HtmlLinkExtractor\#

_class _langchain\_community.graph\_vectorstores.extractors.html\_link\_extractor.HtmlLinkExtractor\(

    _\*_ ,     _kind : str = 'hyperlink'_,     _drop\_fragments : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/html_link_extractor.html#HtmlLinkExtractor)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Extract hyperlinks from HTML content.

Expects the input to be an HTML string or a BeautifulSoup object.

Example:               extractor = HtmlLinkExtractor()     results = extractor.extract_one(HtmlInput(html, url))     

See also

  * [`How to use a graph vector store`](https://python.langchain.com/api_reference/community/graph_vectorstores.html#module-langchain_community.graph_vectorstores "langchain_community.graph_vectorstores")

  * [`How to create links between documents`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")

## How to link Documents on hyperlinks in HTML\#

### Preliminaries\#

Install the `beautifulsoup4` package:               pip install -q langchain_community beautifulsoup4     

### Usage\#

For this example, we’ll scrape 2 HTML pages that have an hyperlink from one page to the other using an `AsyncHtmlLoader`. Then we use the `HtmlLinkExtractor` to create the links in the documents.

#### Using extract\_one\(\)\#

We can use `extract_one()` on a document to get the links and add the links to the document metadata with [`add_links()`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.add_links.html#langchain_community.graph_vectorstores.links.add_links "langchain_community.graph_vectorstores.links.add_links"):               from langchain_community.document_loaders import AsyncHtmlLoader     from langchain_community.graph_vectorstores.extractors import (         HtmlInput,         HtmlLinkExtractor,     )     from langchain_community.graph_vectorstores.links import add_links     from langchain_core.documents import Document          loader = AsyncHtmlLoader(         [             "https://python.langchain.com/docs/integrations/providers/astradb/",             "https://docs.datastax.com/en/astra/home/astra.html",         ]     )          documents = loader.load()          html_extractor = HtmlLinkExtractor()          for doc in documents:         links = html_extractor.extract_one(HtmlInput(doc.page_content, url))         add_links(doc, links)          documents[0].metadata["links"][:5]                    [Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/spreedly/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/nvidia/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/ray_serve/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/bageldb/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/introduction/')]     

#### Using as\_document\_extractor\(\)\#

If you use a document loader that returns the raw HTML and that sets the source key in the document metadata such as `AsyncHtmlLoader`, you can simplify by using `as_document_extractor()` that takes directly a `Document` as input:               from langchain_community.document_loaders import AsyncHtmlLoader     from langchain_community.graph_vectorstores.extractors import HtmlLinkExtractor     from langchain_community.graph_vectorstores.links import add_links          loader = AsyncHtmlLoader(         [             "https://python.langchain.com/docs/integrations/providers/astradb/",             "https://docs.datastax.com/en/astra/home/astra.html",         ]     )     documents = loader.load()     html_extractor = HtmlLinkExtractor().as_document_extractor()          for document in documents:         links = html_extractor.extract_one(document)         add_links(document, links)          documents[0].metadata["links"][:5]                    [Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/spreedly/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/nvidia/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/ray_serve/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/bageldb/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/introduction/')]     

#### Using LinkExtractorTransformer\#

Using the [`LinkExtractorTransformer`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer.html#langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer "langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer"), we can simplify the link extraction:               from langchain_community.document_loaders import AsyncHtmlLoader     from langchain_community.graph_vectorstores.extractors import (         HtmlLinkExtractor,         LinkExtractorTransformer,     )     from langchain_community.graph_vectorstores.links import add_links          loader = AsyncHtmlLoader(         [             "https://python.langchain.com/docs/integrations/providers/astradb/",             "https://docs.datastax.com/en/astra/home/astra.html",         ]     )          documents = loader.load()     transformer = LinkExtractorTransformer([HtmlLinkExtractor().as_document_extractor()])     documents = transformer.transform_documents(documents)          documents[0].metadata["links"][:5]                    [Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/spreedly/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/nvidia/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/ray_serve/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/bageldb/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/introduction/')]     

We can check that there is a link from the first document to the second:               for doc_to in documents:         for link_to in doc_to.metadata["links"]:             if link_to.direction == "in":                 for doc_from in documents:                     for link_from in doc_from.metadata["links"]:                         if (                             link_to.direction == "in"                             and link_from.direction == "out"                             and link_to.tag == link_from.tag                         ):                             print(                                 f"Found link from {doc_from.metadata['source']} to {doc_to.metadata['source']}."                             )                    Found link from https://python.langchain.com/docs/integrations/providers/astradb/ to https://docs.datastax.com/en/astra/home/astra.html.     

The documents with URL links can then be added to a [`GraphVectorStore`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.GraphVectorStore.html#langchain_community.graph_vectorstores.base.GraphVectorStore "langchain_community.graph_vectorstores.base.GraphVectorStore"):               from langchain_community.graph_vectorstores import CassandraGraphVectorStore          store = CassandraGraphVectorStore.from_documents(documents=documents, embedding=...)     

param kind:     

The kind of edge to extract. Defaults to `hyperlink`.

param drop\_fragments:     

Whether fragments in URLs and links should be dropped. Defaults to `True`.

Methods

`__init__`\(\*\[, kind, drop\_fragments\]\) | Extract hyperlinks from HTML content.   ---|---   `as_document_extractor`\(\[url\_metadata\_key\]\) | Return a LinkExtractor that applies to documents.   `extract_many`\(inputs\) | Add edges from each input to the corresponding documents.   `extract_one`\(input\) | Add edges from each input to the corresponding documents.      \_\_init\_\_\(

    _\*_ ,     _kind : str = 'hyperlink'_,     _drop\_fragments : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/html_link_extractor.html#HtmlLinkExtractor.__init__)\#     

Extract hyperlinks from HTML content.

Expects the input to be an HTML string or a BeautifulSoup object.

Example:               extractor = HtmlLinkExtractor()     results = extractor.extract_one(HtmlInput(html, url))     

See also

  * [`How to use a graph vector store`](https://python.langchain.com/api_reference/community/graph_vectorstores.html#module-langchain_community.graph_vectorstores "langchain_community.graph_vectorstores")

  * [`How to create links between documents`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")

##### How to link Documents on hyperlinks in HTML\#

###### Preliminaries\#

Install the `beautifulsoup4` package:               pip install -q langchain_community beautifulsoup4     

###### Usage\#

For this example, we’ll scrape 2 HTML pages that have an hyperlink from one page to the other using an `AsyncHtmlLoader`. Then we use the `HtmlLinkExtractor` to create the links in the documents.

###### Using extract\_one\(\)\#

We can use `extract_one()` on a document to get the links and add the links to the document metadata with [`add_links()`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.add_links.html#langchain_community.graph_vectorstores.links.add_links "langchain_community.graph_vectorstores.links.add_links"):               from langchain_community.document_loaders import AsyncHtmlLoader     from langchain_community.graph_vectorstores.extractors import (         HtmlInput,         HtmlLinkExtractor,     )     from langchain_community.graph_vectorstores.links import add_links     from langchain_core.documents import Document          loader = AsyncHtmlLoader(         [             "https://python.langchain.com/docs/integrations/providers/astradb/",             "https://docs.datastax.com/en/astra/home/astra.html",         ]     )          documents = loader.load()          html_extractor = HtmlLinkExtractor()          for doc in documents:         links = html_extractor.extract_one(HtmlInput(doc.page_content, url))         add_links(doc, links)          documents[0].metadata["links"][:5]                    [Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/spreedly/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/nvidia/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/ray_serve/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/bageldb/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/introduction/')]     

###### Using as\_document\_extractor\(\)\#

If you use a document loader that returns the raw HTML and that sets the source key in the document metadata such as `AsyncHtmlLoader`, you can simplify by using `as_document_extractor()` that takes directly a `Document` as input:               from langchain_community.document_loaders import AsyncHtmlLoader     from langchain_community.graph_vectorstores.extractors import HtmlLinkExtractor     from langchain_community.graph_vectorstores.links import add_links          loader = AsyncHtmlLoader(         [             "https://python.langchain.com/docs/integrations/providers/astradb/",             "https://docs.datastax.com/en/astra/home/astra.html",         ]     )     documents = loader.load()     html_extractor = HtmlLinkExtractor().as_document_extractor()          for document in documents:         links = html_extractor.extract_one(document)         add_links(document, links)          documents[0].metadata["links"][:5]                    [Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/spreedly/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/nvidia/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/ray_serve/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/bageldb/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/introduction/')]     

###### Using LinkExtractorTransformer\#

Using the [`LinkExtractorTransformer`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer.html#langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer "langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer"), we can simplify the link extraction:               from langchain_community.document_loaders import AsyncHtmlLoader     from langchain_community.graph_vectorstores.extractors import (         HtmlLinkExtractor,         LinkExtractorTransformer,     )     from langchain_community.graph_vectorstores.links import add_links          loader = AsyncHtmlLoader(         [             "https://python.langchain.com/docs/integrations/providers/astradb/",             "https://docs.datastax.com/en/astra/home/astra.html",         ]     )          documents = loader.load()     transformer = LinkExtractorTransformer([HtmlLinkExtractor().as_document_extractor()])     documents = transformer.transform_documents(documents)          documents[0].metadata["links"][:5]                    [Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/spreedly/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/nvidia/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/ray_serve/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/integrations/providers/bageldb/'),      Link(kind='hyperlink', direction='out', tag='https://python.langchain.com/docs/introduction/')]     

We can check that there is a link from the first document to the second:               for doc_to in documents:         for link_to in doc_to.metadata["links"]:             if link_to.direction == "in":                 for doc_from in documents:                     for link_from in doc_from.metadata["links"]:                         if (                             link_to.direction == "in"                             and link_from.direction == "out"                             and link_to.tag == link_from.tag                         ):                             print(                                 f"Found link from {doc_from.metadata['source']} to {doc_to.metadata['source']}."                             )                    Found link from https://python.langchain.com/docs/integrations/providers/astradb/ to https://docs.datastax.com/en/astra/home/astra.html.     

The documents with URL links can then be added to a [`GraphVectorStore`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.GraphVectorStore.html#langchain_community.graph_vectorstores.base.GraphVectorStore "langchain_community.graph_vectorstores.base.GraphVectorStore"):               from langchain_community.graph_vectorstores import CassandraGraphVectorStore          store = CassandraGraphVectorStore.from_documents(documents=documents, embedding=...)     

param kind:     

The kind of edge to extract. Defaults to `hyperlink`.

param drop\_fragments:     

Whether fragments in URLs and links should be dropped. Defaults to `True`.

Parameters:     

  * **kind** \(_str_\)

  * **drop\_fragments** \(_bool_\)

as\_document\_extractor\(

    _url\_metadata\_key : str = 'source'_, \) → [LinkExtractor](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor.html#langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor "langchain_community.graph_vectorstores.extractors.link_extractor.LinkExtractor")\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/html_link_extractor.html#HtmlLinkExtractor.as_document_extractor)\#     

Return a LinkExtractor that applies to documents.

Note

Since the HtmlLinkExtractor parses HTML, if you use with other similar link extractors it may be more efficient to call the link extractors directly on the parsed BeautifulSoup object.

Parameters:     

**url\_metadata\_key** \(_str_\) – The name of the filed in document metadata with the URL of the document.

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

    _input : [HtmlInput](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.html_link_extractor.HtmlInput.html#langchain_community.graph_vectorstores.extractors.html_link_extractor.HtmlInput "langchain_community.graph_vectorstores.extractors.html_link_extractor.HtmlInput")_, \) → Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/html_link_extractor.html#HtmlLinkExtractor.extract_one)\#     

Add edges from each input to the corresponding documents.

Parameters:     

**input** \([_HtmlInput_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.html_link_extractor.HtmlInput.html#langchain_community.graph_vectorstores.extractors.html_link_extractor.HtmlInput "langchain_community.graph_vectorstores.extractors.html_link_extractor.HtmlInput")\) – The input content to extract edges from.

Returns:     

Set of links extracted from the input.

Return type:     

_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]

Parameters:     

  * **kind** \(_str_\)

  * **drop\_fragments** \(_bool_\)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)