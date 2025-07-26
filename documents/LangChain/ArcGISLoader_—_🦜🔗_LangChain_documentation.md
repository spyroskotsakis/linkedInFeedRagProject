# ArcGISLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.arcgis_loader.ArcGISLoader.html
**Word Count:** 94
**Links Count:** 418
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# ArcGISLoader\#

_class _langchain\_community.document\_loaders.arcgis\_loader.ArcGISLoader\(

    _layer : str | arcgis.features.FeatureLayer_,     _gis : arcgis.gis.GIS | None = None_,     _where : str = '1=1'_,     _out\_fields : List\[str\] | str | None = None_,     _return\_geometry : bool = False_,     _result\_record\_count : int | None = None_,     _lyr\_desc : str | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/arcgis_loader.html#ArcGISLoader)\#     

Load records from an ArcGIS FeatureLayer.

Methods

`__init__`\(layer\[, gis, where, out\_fields, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load records from FeatureLayer.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **layer** \(_Union_ _\[__str_ _,__arcgis.features.FeatureLayer_ _\]_\)

  * **gis** \(_Optional_ _\[__arcgis.gis.GIS_ _\]_\)

  * **where** \(_str_\)

  * **out\_fields** \(_Optional_ _\[__Union_ _\[__List_ _\[__str_ _\]__,__str_ _\]__\]_\)

  * **return\_geometry** \(_bool_\)

  * **result\_record\_count** \(_Optional_ _\[__int_ _\]_\)

  * **lyr\_desc** \(_Optional_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _layer : str | arcgis.features.FeatureLayer_,     _gis : arcgis.gis.GIS | None = None_,     _where : str = '1=1'_,     _out\_fields : List\[str\] | str | None = None_,     _return\_geometry : bool = False_,     _result\_record\_count : int | None = None_,     _lyr\_desc : str | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/arcgis_loader.html#ArcGISLoader.__init__)\#     

Parameters:     

  * **layer** \(_Union_ _\[__str_ _,__arcgis.features.FeatureLayer_ _\]_\)

  * **gis** \(_Optional_ _\[__arcgis.gis.GIS_ _\]_\)

  * **where** \(_str_\)

  * **out\_fields** \(_Optional_ _\[__Union_ _\[__List_ _\[__str_ _\]__,__str_ _\]__\]_\)

  * **return\_geometry** \(_bool_\)

  * **result\_record\_count** \(_Optional_ _\[__int_ _\]_\)

  * **lyr\_desc** \(_Optional_ _\[__str_ _\]_\)

  * **kwargs** \(_Any_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/arcgis_loader.html#ArcGISLoader.lazy_load)\#     

Lazy load records from FeatureLayer.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\_and\_split\(

    _text\_splitter : [TextSplitter](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") | None = None_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load Documents and split into chunks. Chunks are returned as Documents.

Do not override this method. It should be considered to be deprecated\!

Parameters:     

**text\_splitter** \(_Optional_ _\[_[_TextSplitter_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter") _\]_\) – TextSplitter instance to use for splitting documents. Defaults to RecursiveCharacterTextSplitter.

Returns:     

List of Documents.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using ArcGISLoader

  * [ArcGIS](https://python.langchain.com/docs/integrations/document_loaders/arcgis/)

__On this page