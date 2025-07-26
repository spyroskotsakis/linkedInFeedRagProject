# RelikGraphTransformer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/graph_transformers/langchain_experimental.graph_transformers.relik.RelikGraphTransformer.html
**Word Count:** 142
**Links Count:** 132
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# RelikGraphTransformer\#

_class _langchain\_experimental.graph\_transformers.relik.RelikGraphTransformer\(

    _model : str = 'relik-ie/relik-relation-extraction-small'_,     _relationship\_confidence\_threshold : float = 0.1_,     _model\_config : Dict\[str, Any\] = \{\}_,     _ignore\_self\_loops : bool = True_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/relik.html#RelikGraphTransformer)\#     

A transformer class for converting documents into graph structures using the Relik library and models.

This class leverages relik models for extracting relationships and nodes from text documents and converting them into a graph format. The relationships are filtered based on a specified confidence threshold.

For more details on the Relik library, visit their GitHub repository:     

[SapienzaNLP/relik](https://github.com/SapienzaNLP/relik)

Parameters:     

  * **model** \(_str_\) – The name of the pretrained Relik model to use. Default is “relik-ie/relik-relation-extraction-small-wikipedia”.

  * **relationship\_confidence\_threshold** \(_float_\) – The confidence threshold for filtering relationships. Default is 0.1.

  * **model\_config** \(_Dict_ _\[__str_ _,__any_ _\]_\) – Additional configuration options for the Relik model. Default is an empty dictionary.

  * **ignore\_self\_loops** \(_bool_\) – Whether to ignore relationships where the source and target nodes are the same. Default is True.

Methods

`__init__`\(\[model, ...\]\) |    ---|---   `convert_to_graph_documents`\(documents\) | Convert a sequence of documents into graph documents.   `process_document`\(document\) |       \_\_init\_\_\(

    _model : str = 'relik-ie/relik-relation-extraction-small'_,     _relationship\_confidence\_threshold : float = 0.1_,     _model\_config : Dict\[str, Any\] = \{\}_,     _ignore\_self\_loops : bool = True_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/relik.html#RelikGraphTransformer.__init__)\#     

Parameters:     

  * **model** \(_str_\)

  * **relationship\_confidence\_threshold** \(_float_\)

  * **model\_config** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **ignore\_self\_loops** \(_bool_\)

Return type:     

None

convert\_to\_graph\_documents\(

    _documents : Sequence\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_, \) → List\[[GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/relik.html#RelikGraphTransformer.convert_to_graph_documents)\#     

Convert a sequence of documents into graph documents.

Parameters:     

  * **documents** \(_Sequence_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\) – The original documents.

  * **kwargs** – Additional keyword arguments.

Returns:     

The transformed documents as graphs.

Return type:     

Sequence\[[GraphDocument](https://python.langchain.com/api_reference/neo4j/graphs/langchain_neo4j.graphs.graph_document.GraphDocument.html#langchain_neo4j.graphs.graph_document.GraphDocument "langchain_neo4j.graphs.graph_document.GraphDocument")\]

process\_document\(

    _document : [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")_, \) → [GraphDocument](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/graph_transformers/relik.html#RelikGraphTransformer.process_document)\#     

Parameters:     

**document** \([_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\)

Return type:     

[_GraphDocument_](https://python.langchain.com/api_reference/community/graphs/langchain_community.graphs.graph_document.GraphDocument.html#langchain_community.graphs.graph_document.GraphDocument "langchain_community.graphs.graph_document.GraphDocument")

__On this page