# DiffbotGraphTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.diffbot.DiffbotGraphTransformer.html
**Word Count:** 317
**Links Count:** 141
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# DiffbotGraphTransformer\#

_class _langchain\_experimental.graph\_transformers.diffbot.DiffbotGraphTransformer\(

    _diffbot\_api\_key : str | None = None_,     _fact\_confidence\_threshold : float = 0.7_,     _include\_qualifiers : bool = True_,     _include\_evidence : bool = True_,     _simplified\_schema : bool = True_,     _extract\_types : List\[[TypeOption](https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.diffbot.TypeOption.html#langchain_experimental.graph_transformers.diffbot.TypeOption "langchain_experimental.graph_transformers.diffbot.TypeOption")\] = \[TypeOption.FACTS\]_,     _\*_ ,     _include\_confidence : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#DiffbotGraphTransformer)\#     

Transform documents into graph documents using Diffbot NLP API.

A graph document transformation system takes a sequence of Documents and returns a sequence of Graph Documents.

Example

Initialize the graph transformer with various options.

Parameters:     

  * **diffbot\_api\_key** \(_str_\) – The API key for Diffbot’s NLP services.

  * **fact\_confidence\_threshold** \(_float_\) – Minimum confidence level for facts to be included.

  * **include\_qualifiers** \(_bool_\) – Whether to include qualifiers in the relationships.

  * **include\_evidence** \(_bool_\) – Whether to include evidence for the relationships.

  * **simplified\_schema** \(_bool_\) – Whether to use a simplified schema for relationships.

  * **extract\_types** \(_List_ _\[_[_TypeOption_](https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.diffbot.TypeOption.html#langchain_experimental.graph_transformers.diffbot.TypeOption "langchain_experimental.graph_transformers.diffbot.TypeOption") _\]_\) – A list of data types to extract. Facts, entities, and sentiment are supported. By default, the option is set to facts. A fact represents a combination of source and target nodes with a relationship type.

  * **include\_confidence** \(_bool_\) – Whether to include confidence scores on nodes and rels

Methods

`__init__`\(\[diffbot\_api\_key, ...\]\) | Initialize the graph transformer with various options.   ---|---   `convert_to_graph_documents`\(documents\) | Convert a sequence of documents into graph documents.   `nlp_request`\(text\) | Make an API request to the Diffbot NLP endpoint.   `process_response`\(payload, document\) | Transform the Diffbot NLP response into a GraphDocument.      \_\_init\_\_\(

    _diffbot\_api\_key : str | None = None_,     _fact\_confidence\_threshold : float = 0.7_,     _include\_qualifiers : bool = True_,     _include\_evidence : bool = True_,     _simplified\_schema : bool = True_,     _extract\_types : List\[[TypeOption](https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.diffbot.TypeOption.html#langchain_experimental.graph_transformers.diffbot.TypeOption "langchain_experimental.graph_transformers.diffbot.TypeOption")\] = \[TypeOption.FACTS\]_,     _\*_ ,     _include\_confidence : bool = False_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#DiffbotGraphTransformer.__init__)\#     

Initialize the graph transformer with various options.

Parameters:     

  * **diffbot\_api\_key** \(_str_\) – The API key for Diffbot’s NLP services.

  * **fact\_confidence\_threshold** \(_float_\) – Minimum confidence level for facts to be included.

  * **include\_qualifiers** \(_bool_\) – Whether to include qualifiers in the relationships.

  * **include\_evidence** \(_bool_\) – Whether to include evidence for the relationships.

  * **simplified\_schema** \(_bool_\) – Whether to use a simplified schema for relationships.

  * **extract\_types** \(_List_ _\[_[_TypeOption_](https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.diffbot.TypeOption.html#langchain_experimental.graph_transformers.diffbot.TypeOption "langchain_experimental.graph_transformers.diffbot.TypeOption") _\]_\) – A list of data types to extract. Facts, entities, and sentiment are supported. By default, the option is set to facts. A fact represents a combination of source and target nodes with a relationship type.

  * **include\_confidence** \(_bool_\) – Whether to include confidence scores on nodes and rels

Return type:     

None

convert\_to\_graph\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#DiffbotGraphTransformer.convert_to_graph_documents)\#     

Convert a sequence of documents into graph documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The original documents.

  * **kwargs** – Additional keyword arguments.

Returns:     

The transformed documents as graphs.

Return type:     

Sequence\[[GraphDocument](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument")\]

nlp\_request\(

    _text : str_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#DiffbotGraphTransformer.nlp_request)\#     

Make an API request to the Diffbot NLP endpoint.

Parameters:     

**text** \(_str_\) – The text to be processed.

Returns:     

The JSON response from the API.

Return type:     

Dict\[str, Any\]

process\_response\(

    _payload : Dict\[str, Any\]_,     _document : [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_, \) → [GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/diffbot.html#DiffbotGraphTransformer.process_response)\#     

Transform the Diffbot NLP response into a GraphDocument.

Parameters:     

  * **payload** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – The JSON response from Diffbot’s NLP API.

  * **document** \([_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\) – The original document.

Returns:     

The transformed document as a graph.

Return type:     

[GraphDocument](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument")

Examples using DiffbotGraphTransformer

  * [Diffbot](https://python.langchain.com/docs/integrations/graphs/diffbot/)

  * [Neo4j](https://python.langchain.com/docs/integrations/providers/neo4j/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)