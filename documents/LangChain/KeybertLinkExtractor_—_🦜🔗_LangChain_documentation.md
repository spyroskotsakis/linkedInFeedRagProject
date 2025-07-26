# KeybertLinkExtractor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.keybert_link_extractor.KeybertLinkExtractor.html
**Word Count:** 408
**Links Count:** 161
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# KeybertLinkExtractor\#

_class _langchain\_community.graph\_vectorstores.extractors.keybert\_link\_extractor.KeybertLinkExtractor\(

    _\*_ ,     _kind : str = 'kw'_,     _embedding\_model : str = 'all-MiniLM-L6-v2'_,     _extract\_keywords\_kwargs : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/keybert_link_extractor.html#KeybertLinkExtractor)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

Extract keywords using [KeyBERT](https://maartengr.github.io/KeyBERT/).

KeyBERT is a minimal and easy-to-use keyword extraction technique that leverages BERT embeddings to create keywords and keyphrases that are most similar to a document.

The KeybertLinkExtractor uses KeyBERT to create links between documents that have keywords in common.

Example:               extractor = KeybertLinkExtractor()     results = extractor.extract_one("lorem ipsum...")     

See also

  * [`How to use a graph vector store`](https://python.langchain.com/api_reference/community/graph_vectorstores.html#module-langchain_community.graph_vectorstores "langchain_community.graph_vectorstores")

  * [`How to create links between documents`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")

## How to link Documents on common keywords using Keybert\#

### Preliminaries\#

Install the keybert package:               pip install -q langchain_community keybert     

### Usage\#

We load the `state_of_the_union.txt` file, chunk it, then for each chunk we extract keyword links and add them to the chunk.

#### Using extract\_one\(\)\#

We can use `extract_one()` on a document to get the links and add the links to the document metadata with [`add_links()`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.add_links.html#langchain_community.graph_vectorstores.links.add_links "langchain_community.graph_vectorstores.links.add_links"):               from langchain_community.document_loaders import TextLoader     from langchain_community.graph_vectorstores import CassandraGraphVectorStore     from langchain_community.graph_vectorstores.extractors import KeybertLinkExtractor     from langchain_community.graph_vectorstores.links import add_links     from langchain_text_splitters import CharacterTextSplitter          loader = TextLoader("state_of_the_union.txt")          raw_documents = loader.load()     text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)          documents = text_splitter.split_documents(raw_documents)     keyword_extractor = KeybertLinkExtractor()          for document in documents:         links = keyword_extractor.extract_one(document)         add_links(document, links)          print(documents[0].metadata)                    {'source': 'state_of_the_union.txt', 'links': [Link(kind='kw', direction='bidir', tag='ukraine'), Link(kind='kw', direction='bidir', tag='ukrainian'), Link(kind='kw', direction='bidir', tag='putin'), Link(kind='kw', direction='bidir', tag='vladimir'), Link(kind='kw', direction='bidir', tag='russia')]}     

#### Using LinkExtractorTransformer\#

Using the [`LinkExtractorTransformer`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer.html#langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer "langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer"), we can simplify the link extraction:               from langchain_community.document_loaders import TextLoader     from langchain_community.graph_vectorstores.extractors import (         KeybertLinkExtractor,         LinkExtractorTransformer,     )     from langchain_text_splitters import CharacterTextSplitter          loader = TextLoader("state_of_the_union.txt")     raw_documents = loader.load()          text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)     documents = text_splitter.split_documents(raw_documents)          transformer = LinkExtractorTransformer([KeybertLinkExtractor()])     documents = transformer.transform_documents(documents)          print(documents[0].metadata)                    {'source': 'state_of_the_union.txt', 'links': [Link(kind='kw', direction='bidir', tag='ukraine'), Link(kind='kw', direction='bidir', tag='ukrainian'), Link(kind='kw', direction='bidir', tag='putin'), Link(kind='kw', direction='bidir', tag='vladimir'), Link(kind='kw', direction='bidir', tag='russia')]}     

The documents with keyword links can then be added to a [`GraphVectorStore`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.GraphVectorStore.html#langchain_community.graph_vectorstores.base.GraphVectorStore "langchain_community.graph_vectorstores.base.GraphVectorStore"):               from langchain_community.graph_vectorstores import CassandraGraphVectorStore          store = CassandraGraphVectorStore.from_documents(documents=documents, embedding=...)     

param kind:     

Kind of links to produce with this extractor.

param embedding\_model:     

Name of the embedding model to use with KeyBERT.

param extract\_keywords\_kwargs:     

Keyword arguments to pass to KeyBERT’s `extract_keywords` method.

Methods

`__init__`\(\*\[, kind, embedding\_model, ...\]\) |    ---|---   `extract_many`\(inputs\) | Add edges from each input to the corresponding documents.   `extract_one`\(input\) | Add edges from each input to the corresponding documents.      \_\_init\_\_\(

    _\*_ ,     _kind : str = 'kw'_,     _embedding\_model : str = 'all-MiniLM-L6-v2'_,     _extract\_keywords\_kwargs : Dict\[str, Any\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/keybert_link_extractor.html#KeybertLinkExtractor.__init__)\#     

Extract keywords using [KeyBERT](https://maartengr.github.io/KeyBERT/).

KeyBERT is a minimal and easy-to-use keyword extraction technique that leverages BERT embeddings to create keywords and keyphrases that are most similar to a document.

The KeybertLinkExtractor uses KeyBERT to create links between documents that have keywords in common.

Example:               extractor = KeybertLinkExtractor()     results = extractor.extract_one("lorem ipsum...")     

See also

  * [`How to use a graph vector store`](https://python.langchain.com/api_reference/community/graph_vectorstores.html#module-langchain_community.graph_vectorstores "langchain_community.graph_vectorstores")

  * [`How to create links between documents`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")

##### How to link Documents on common keywords using Keybert\#

###### Preliminaries\#

Install the keybert package:               pip install -q langchain_community keybert     

###### Usage\#

We load the `state_of_the_union.txt` file, chunk it, then for each chunk we extract keyword links and add them to the chunk.

###### Using extract\_one\(\)\#

We can use `extract_one()` on a document to get the links and add the links to the document metadata with [`add_links()`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.add_links.html#langchain_community.graph_vectorstores.links.add_links "langchain_community.graph_vectorstores.links.add_links"):               from langchain_community.document_loaders import TextLoader     from langchain_community.graph_vectorstores import CassandraGraphVectorStore     from langchain_community.graph_vectorstores.extractors import KeybertLinkExtractor     from langchain_community.graph_vectorstores.links import add_links     from langchain_text_splitters import CharacterTextSplitter          loader = TextLoader("state_of_the_union.txt")          raw_documents = loader.load()     text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)          documents = text_splitter.split_documents(raw_documents)     keyword_extractor = KeybertLinkExtractor()          for document in documents:         links = keyword_extractor.extract_one(document)         add_links(document, links)          print(documents[0].metadata)                    {'source': 'state_of_the_union.txt', 'links': [Link(kind='kw', direction='bidir', tag='ukraine'), Link(kind='kw', direction='bidir', tag='ukrainian'), Link(kind='kw', direction='bidir', tag='putin'), Link(kind='kw', direction='bidir', tag='vladimir'), Link(kind='kw', direction='bidir', tag='russia')]}     

###### Using LinkExtractorTransformer\#

Using the [`LinkExtractorTransformer`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer.html#langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer "langchain_community.graph_vectorstores.extractors.link_extractor_transformer.LinkExtractorTransformer"), we can simplify the link extraction:               from langchain_community.document_loaders import TextLoader     from langchain_community.graph_vectorstores.extractors import (         KeybertLinkExtractor,         LinkExtractorTransformer,     )     from langchain_text_splitters import CharacterTextSplitter          loader = TextLoader("state_of_the_union.txt")     raw_documents = loader.load()          text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)     documents = text_splitter.split_documents(raw_documents)          transformer = LinkExtractorTransformer([KeybertLinkExtractor()])     documents = transformer.transform_documents(documents)          print(documents[0].metadata)                    {'source': 'state_of_the_union.txt', 'links': [Link(kind='kw', direction='bidir', tag='ukraine'), Link(kind='kw', direction='bidir', tag='ukrainian'), Link(kind='kw', direction='bidir', tag='putin'), Link(kind='kw', direction='bidir', tag='vladimir'), Link(kind='kw', direction='bidir', tag='russia')]}     

The documents with keyword links can then be added to a [`GraphVectorStore`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.GraphVectorStore.html#langchain_community.graph_vectorstores.base.GraphVectorStore "langchain_community.graph_vectorstores.base.GraphVectorStore"):               from langchain_community.graph_vectorstores import CassandraGraphVectorStore          store = CassandraGraphVectorStore.from_documents(documents=documents, embedding=...)     

param kind:     

Kind of links to produce with this extractor.

param embedding\_model:     

Name of the embedding model to use with KeyBERT.

param extract\_keywords\_kwargs:     

Keyword arguments to pass to KeyBERT’s `extract_keywords` method.

Parameters:     

  * **kind** \(_str_\)

  * **embedding\_model** \(_str_\)

  * **extract\_keywords\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

extract\_many\(

    _inputs : Iterable\[str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → Iterable\[Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/keybert_link_extractor.html#KeybertLinkExtractor.extract_many)\#     

Add edges from each input to the corresponding documents.

Parameters:     

**inputs** \(_Iterable_ _\[__str_ _|_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The input content to extract edges from.

Returns:     

Iterable over the set of links extracted from the input.

Return type:     

_Iterable_\[_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]\]

extract\_one\(

    _input : str | [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_, \) → Set\[[Link](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/extractors/keybert_link_extractor.html#KeybertLinkExtractor.extract_one)\#     

Add edges from each input to the corresponding documents.

Parameters:     

**input** \(_str_ _|_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\) – The input content to extract edges from.

Returns:     

Set of links extracted from the input.

Return type:     

_Set_\[[_Link_](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html#langchain_community.graph_vectorstores.links.Link "langchain_community.graph_vectorstores.links.Link")\]

Parameters:     

  * **kind** \(_str_\)

  * **embedding\_model** \(_str_\)

  * **extract\_keywords\_kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]__|__None_\)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)