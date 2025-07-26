# Link — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.links.Link.html
**Word Count:** 393
**Links Count:** 149
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# Link\#

_class _langchain\_community.graph\_vectorstores.links.Link\(

    _kind : str_,     _direction : Literal\['in', 'out', 'bidir'\]_,     _tag : str_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/links.html#Link)\#     

Beta

This feature is in beta. It is actively being worked on, so the API may change.

A link to/from a tag of a given kind.

Documents in a [`graph vector store`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.base.GraphVectorStore.html#langchain_community.graph_vectorstores.base.GraphVectorStore "langchain_community.graph_vectorstores.base.GraphVectorStore") are connected via “links”. Links form a bipartite graph between documents and tags: documents are connected to tags, and tags are connected to other documents. When documents are retrieved from a graph vector store, a pair of documents are connected with a depth of one if both documents are connected to the same tag.

Links have a `kind` property, used to namespace different tag identifiers. For example a link to a keyword might use kind `kw`, while a link to a URL might use kind `url`. This allows the same tag value to be used in different contexts without causing name collisions.

Links are directed. The directionality of links controls how the graph is traversed at retrieval time. For example, given documents `A` and `B`, connected by links to tag `T`:

A to T | B to T | Result   ---|---|---   outgoing | incoming | Retrieval traverses from A to B   incoming | incoming | No traversal from A to B   outgoing | incoming | No traversal from A to B   bidir | incoming | Retrieval traverses from A to B   bidir | outgoing | No traversal from A to B   outgoing | bidir | Retrieval traverses from A to B   incoming | bidir | No traversal from A to B      Directed links make it possible to describe relationships such as term references / definitions: term definitions are generally relevant to any documents that use the term, but the full set of documents using a term generally aren’t relevant to the term’s definition.

See also

  * [`How to use a graph vector store`](https://python.langchain.com/api_reference/community/graph_vectorstores.html#module-langchain_community.graph_vectorstores "langchain_community.graph_vectorstores")

  * [`How to link Documents on hyperlinks in HTML`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.html_link_extractor.HtmlLinkExtractor.html#langchain_community.graph_vectorstores.extractors.html_link_extractor.HtmlLinkExtractor "langchain_community.graph_vectorstores.extractors.html_link_extractor.HtmlLinkExtractor")

  * [`How to link Documents on common keywords (using KeyBERT)`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.keybert_link_extractor.KeybertLinkExtractor.html#langchain_community.graph_vectorstores.extractors.keybert_link_extractor.KeybertLinkExtractor "langchain_community.graph_vectorstores.extractors.keybert_link_extractor.KeybertLinkExtractor")

  * [`How to link Documents on common named entities (using GliNER)`](https://python.langchain.com/api_reference/community/graph_vectorstores/langchain_community.graph_vectorstores.extractors.gliner_link_extractor.GLiNERLinkExtractor.html#langchain_community.graph_vectorstores.extractors.gliner_link_extractor.GLiNERLinkExtractor "langchain_community.graph_vectorstores.extractors.gliner_link_extractor.GLiNERLinkExtractor")

## How to add links to a Document\#

### How to create links\#

You can create links using the Link class’s constructors `incoming()`, `outgoing()`, and `bidir()`:               from langchain_community.graph_vectorstores.links import Link          print(Link.bidir(kind="location", tag="Paris"))                    Link(kind='location', direction='bidir', tag='Paris')     

### Extending documents with links\#

Now that we know how to create links, let’s associate them with some documents. These edges will strengthen the connection between documents that share a keyword when using a graph vector store to retrieve documents.

First, we’ll load some text and chunk it into smaller pieces. Then we’ll add a link to each document to link them all together:               from langchain_community.document_loaders import TextLoader     from langchain_community.graph_vectorstores.links import add_links     from langchain_text_splitters import CharacterTextSplitter          loader = TextLoader("state_of_the_union.txt")          raw_documents = loader.load()     text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)     documents = text_splitter.split_documents(raw_documents)          for doc in documents:         add_links(doc, Link.bidir(kind="genre", tag="oratory"))          print(documents[0].metadata)                    {'source': 'state_of_the_union.txt', 'links': [Link(kind='genre', direction='bidir', tag='oratory')]}     

As we can see, each document’s metadata now includes a bidirectional link to the genre `oratory`.

The documents can then be added to a graph vector store:               from langchain_community.graph_vectorstores import CassandraGraphVectorStore          graph_vectorstore = CassandraGraphVectorStore.from_documents(         documents=documents, embeddings=...     )     

Attributes

Methods

`__init__`\(kind, direction, tag\) |    ---|---   `bidir`\(kind, tag\) | Create a bidirectional link.   `incoming`\(kind, tag\) | Create an incoming link.   `outgoing`\(kind, tag\) | Create an outgoing link.      \_\_init\_\_\(

    _kind : str_,     _direction : Literal\['in', 'out', 'bidir'\]_,     _tag : str_, \) → None\#     

Parameters:     

  * **kind** \(_str_\)

  * **direction** \(_Literal_ _\[__'in'__,__'out'__,__'bidir'__\]_\)

  * **tag** \(_str_\)

Return type:     

None

_static _bidir\(

    _kind : str_,     _tag : str_, \) → Link[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/links.html#Link.bidir)\#     

Create a bidirectional link.

Parameters:     

  * **kind** \(_str_\) – the link kind.

  * **tag** \(_str_\) – the link tag.

Return type:     

_Link_

_static _incoming\(

    _kind : str_,     _tag : str_, \) → Link[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/links.html#Link.incoming)\#     

Create an incoming link.

Parameters:     

  * **kind** \(_str_\) – the link kind.

  * **tag** \(_str_\) – the link tag.

Return type:     

_Link_

_static _outgoing\(

    _kind : str_,     _tag : str_, \) → Link[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/graph_vectorstores/links.html#Link.outgoing)\#     

Create an outgoing link.

Parameters:     

  * **kind** \(_str_\) – the link kind.

  * **tag** \(_str_\) – the link tag.

Return type:     

_Link_

Parameters:     

  * **kind** \(_str_\)

  * **direction** \(_Literal_ _\[__'in'__,__'out'__,__'bidir'__\]_\)

  * **tag** \(_str_\)

__On this page