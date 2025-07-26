# GlinerGraphTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.gliner.GlinerGraphTransformer.html
**Word Count:** 201
**Links Count:** 133
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# GlinerGraphTransformer\#

_class _langchain\_experimental.graph\_transformers.gliner.GlinerGraphTransformer\(

    _allowed\_nodes : List\[str\]_,     _allowed\_relationships : List\[str\] | Dict\[str, Any\]_,     _gliner\_model : str = 'urchade/gliner\_mediumv2.1'_,     _glirel\_model : str = 'jackboyla/glirel\_beta'_,     _entity\_confidence\_threshold : float = 0.1_,     _relationship\_confidence\_threshold : float = 0.1_,     _device : str = 'cpu'_,     _ignore\_self\_loops : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/gliner.html#GlinerGraphTransformer)\#     

A transformer class for converting documents into graph structures using the GLiNER and GLiREL models.

This class leverages GLiNER for named entity recognition and GLiREL for relationship extraction from text documents, converting them into a graph format. The extracted entities and relationships are filtered based on specified confidence thresholds and allowed types.

For more details on GLiNER and GLiREL, visit their respective repositories:     

GLiNER: [urchade/GLiNER](https://github.com/urchade/GLiNER) GLiREL: [jackboyla/GLiREL](https://github.com/jackboyla/GLiREL/tree/main)

Parameters:     

  * **allowed\_nodes** \(_List_ _\[__str_ _\]_\) – A list of allowed node types for entity extraction.

  * **allowed\_relationships** \(_Union_ _\[__List_ _\[__str_ _\]__,__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – A list of allowed relationship types or a dictionary with additional configuration for relationship extraction.

  * **gliner\_model** \(_str_\) – The name of the pretrained GLiNER model to use. Default is “urchade/gliner\_mediumv2.1”.

  * **glirel\_model** \(_str_\) – The name of the pretrained GLiREL model to use. Default is “jackboyla/glirel\_beta”.

  * **entity\_confidence\_threshold** \(_float_\) – The confidence threshold for filtering extracted entities. Default is 0.1.

  * **relationship\_confidence\_threshold** \(_float_\) – The confidence threshold for filtering extracted relationships. Default is 0.1.

  * **device** \(_str_\) – The device to use for model inference \(‘cpu’ or ‘cuda’\). Default is “cpu”.

  * **ignore\_self\_loops** \(_bool_\) – Whether to ignore relationships where the source and target nodes are the same. Default is True.

Methods

`__init__`\(allowed\_nodes, allowed\_relationships\) |    ---|---   `convert_to_graph_documents`\(documents\) | Convert a sequence of documents into graph documents.   `process_document`\(document\) |       \_\_init\_\_\(

    _allowed\_nodes : List\[str\]_,     _allowed\_relationships : List\[str\] | Dict\[str, Any\]_,     _gliner\_model : str = 'urchade/gliner\_mediumv2.1'_,     _glirel\_model : str = 'jackboyla/glirel\_beta'_,     _entity\_confidence\_threshold : float = 0.1_,     _relationship\_confidence\_threshold : float = 0.1_,     _device : str = 'cpu'_,     _ignore\_self\_loops : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/gliner.html#GlinerGraphTransformer.__init__)\#     

Parameters:     

  * **allowed\_nodes** \(_List_ _\[__str_ _\]_\)

  * **allowed\_relationships** \(_List_ _\[__str_ _\]__|__Dict_ _\[__str_ _,__Any_ _\]_\)

  * **gliner\_model** \(_str_\)

  * **glirel\_model** \(_str_\)

  * **entity\_confidence\_threshold** \(_float_\)

  * **relationship\_confidence\_threshold** \(_float_\)

  * **device** \(_str_\)

  * **ignore\_self\_loops** \(_bool_\)

Return type:     

None

convert\_to\_graph\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/gliner.html#GlinerGraphTransformer.convert_to_graph_documents)\#     

Convert a sequence of documents into graph documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The original documents.

  * **kwargs** – Additional keyword arguments.

Returns:     

The transformed documents as graphs.

Return type:     

Sequence\[[GraphDocument](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument")\]

process\_document\(

    _document : [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_, \) → [GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/gliner.html#GlinerGraphTransformer.process_document)\#     

Parameters:     

**document** \([_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\)

Return type:     

[_GraphDocument_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")

__On this page