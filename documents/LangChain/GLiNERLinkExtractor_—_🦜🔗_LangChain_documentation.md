# GLiNERLinkExtractor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.gliner_link_extractor.GLiNERLinkExtractor.html
**Word Count:** 231
**Links Count:** 150
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# GLiNERLinkExtractor\#

_class _langchain\_community.graph\_vectorstores.extractors.gliner\_link\_extractor.GLiNERLinkExtractor\(

    _labels : List\[str\]_,     _\*_ ,     _kind : str = 'entity'_,     _model : str = 'urchade/gliner\_mediumv2.1'_,     _extract\_kwargs : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/gliner_link_extractor.html#GLiNERLinkExtractor)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Link documents with common named entities using [GLiNER](https://github.com/urchade/GLiNER).

[GLiNER](https://github.com/urchade/GLiNER) is a Named Entity Recognition \(NER\) model capable of identifying any entity type using a bidirectional transformer encoder \(BERT-like\).

The `GLiNERLinkExtractor` uses GLiNER to create links between documents that have named entities in common.

Example:               extractor = GLiNERLinkExtractor(         labels=["Person", "Award", "Date", "Competitions", "Teams"]     )     results = extractor.extract_one("some long text...")     

See also

  * [`How to use a graph vector store`](https://python.langchain.com/api_reference/community/graph_vectorstores.html#module-langchain_community.graph_vectorstores "langchain_community.graph_vectorstores")

  * [`How to create links between documents`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")

## How to link Documents on common named entities\#

### Preliminaries\#

Install the `gliner` package:               pip install -q langchain_community gliner     

### Usage\#

We load the `state_of_the_union.txt` file, chunk it, then for each chunk we extract named entity links and add them to the chunk.

#### Using extract\_one\(\)\#

We can use `extract_one()` on a document to get the links and add the links to the document metadata with [`add_links()`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.add_links.html#langchain_community.graph_vectorstores.links.add_links "langchain_community.graph_vectorstores.links.add_links"):               from langchain_community.document_loaders import TextLoader     from langchain_community.graph_vectorstores import CassandraGraphVectorStore     from langchain_community.graph_vectorstores.extractors import GLiNERLinkExtractor     from langchain_community.graph_vectorstores.links import add_links     from langchain_text_splitters import CharacterTextSplitter          loader = TextLoader("state_of_the_union.txt")     raw_documents = loader.load()          text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)     documents = text_splitter.split_documents(raw_documents)          ner_extractor = GLiNERLinkExtractor(["Person", "Topic"])     for document in documents:         links = ner_extractor.extract_one(document)         add_links(document, links)          print(documents[0].metadata)                    {'source': 'state_of_the_union.txt', 'links': [Link(kind='entity:Person', direction='bidir', tag='President Zelenskyy'), Link(kind='entity:Person', direction='bidir', tag='Vladimir Putin')]}     

#### Using LinkExtractorTransformer\#

Using the [`LinkExtractorTransformer`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer.html#langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer "langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer"), we can simplify the link extraction:               from langchain_community.document_loaders import TextLoader     from langchain_community.graph_vectorstores.extractors import (         GLiNERLinkExtractor,         LinkExtractorTransformer,     )     from langchain_text_splitters import CharacterTextSplitter          loader = TextLoader("state_of_the_union.txt")     raw_documents = loader.load()          text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)     documents = text_splitter.split_documents(raw_documents)          ner_extractor = GLiNERLinkExtractor(["Person", "Topic"])     transformer = LinkExtractorTransformer([ner_extractor])     documents = transformer.transform_documents(documents)          print(documents[0].metadata)                    {'source': 'state_of_the_union.txt', 'links': [Link(kind='entity:Person', direction='bidir', tag='President Zelenskyy'), Link(kind='entity:Person', direction='bidir', tag='Vladimir Putin')]}     

The documents with named entity links can then be added to a [`GraphVectorStore`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.GraphVectorStore.html#langchain_community.graph_vectorstores.base.GraphVectorStore "langchain_community.graph_vectorstores.base.GraphVectorStore"):               from langchain_community.graph_vectorstores import CassandraGraphVectorStore          store = CassandraGraphVectorStore.from_documents(documents=documents, embedding=...)     

param labels:     

List of kinds of entities to extract.

param kind:     

Kind of links to produce with this extractor.

param model:     

GLiNER model to use.

param extract\_kwargs:     

Keyword arguments to pass to GLiNER.

Methods

`__init__`\(labels, \*\[, kind, model, ...\]\) |    ---|---   `extract_many`\(inputs\) | Add edges from each input to the corresponding documents.   `extract_one`\(input\) | Add edges from each input to the corresponding documents.      \_\_init\_\_\(

    _labels : List\[str\]_,     _\*_ ,     _kind : str = 'entity'_,     _model : str = 'urchade/gliner\_mediumv2.1'_,     _extract\_kwargs : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/gliner_link_extractor.html#GLiNERLinkExtractor.__init__)\#     

Parameters:     

  * **labels** \(_List_ _\[__str_ _\]_\)

  * **kind** \(_str_\)

  * **model** \(_str_\)

  * **extract\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

extract\_many\(

    _inputs : Iterable\[str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → Iterable\[Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/gliner_link_extractor.html#GLiNERLinkExtractor.extract_many)\#     

Add edges from each input to the corresponding documents.

Parameters:     

**inputs** \(_Iterable_ _\[__str_ _|_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The input content to extract edges from.

Returns:     

Iterable over the set of links extracted from the input.

Return type:     

_Iterable_\[_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]\]

extract\_one\(

    _input : str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_, \) → Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/gliner_link_extractor.html#GLiNERLinkExtractor.extract_one)\#     

Add edges from each input to the corresponding documents.

Parameters:     

**input** \(_str_ _|_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\) – The input content to extract edges from.

Returns:     

Set of links extracted from the input.

Return type:     

_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]

Parameters:     

  * **labels** \(_List_ _\[__str_ _\]_\)

  * **kind** \(_str_\)

  * **model** \(_str_\)

  * **extract\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)