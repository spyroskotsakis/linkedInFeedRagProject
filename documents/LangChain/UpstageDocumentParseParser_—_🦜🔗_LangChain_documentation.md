# UpstageDocumentParseParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/upstage/document_parse_parsers/langchain_upstage.document_parse_parsers.UpstageDocumentParseParser.html
**Word Count:** 435
**Links Count:** 94
**Scraped:** 2025-07-21 08:45:22
**Status:** completed

---

# UpstageDocumentParseParser\#

_class _langchain\_upstage.document\_parse\_parsers.UpstageDocumentParseParser\(

    _api\_key : str | None = None_,     _base\_url : str = 'https://api.upstage.ai/v1/document-ai/document-parse'_,     _model : str = 'document-parse'_,     _split : Literal\['none', 'page', 'element'\] = 'none'_,     _ocr : Literal\['auto', 'force'\] = 'auto'_,     _output\_format : Literal\['text', 'html', 'markdown'\] = 'html'_,     _coordinates : bool = True_,     _base64\_encoding : List\[Literal\['paragraph', 'table', 'figure', 'header', 'footer', 'caption', 'equation', 'heading1', 'list', 'index', 'footnote', 'chart'\]\] = \[\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/document_parse_parsers.html#UpstageDocumentParseParser)\#     

Upstage Document Parse Parser.

To use, you should have the environment variable UPSTAGE\_API\_KEY set with your API key or pass it as a named parameter to the constructor.

Example               from langchain_upstage import UpstageDocumentParseParser          loader = UpstageDocumentParseParser(split="page", output_format="text")     

Initializes an instance of the Upstage class.

Parameters:     

  * **api\_key** \(_str_ _,__optional_\) – The API key for accessing the Upstage API. Defaults to None, in which case it will be fetched from the environment variable UPSTAGE\_API\_KEY.

  * **base\_url** \(_str_ _,__optional_\) – The base URL for accessing the Upstage API.

  * **model** \(_str_\) – The model to be used for the document parse. Defaults to “document-parse”.

  * **split** \(_SplitType_ _,__optional_\) – The type of splitting to be applied. Defaults to “none” \(no splitting\).

  * **ocr** \(_OCRMode_ _,__optional_\) – Extract text from images in the document using OCR. If the value is “force”, OCR is used to extract text from an image. If the value is “auto”, text is extracted from a PDF. \(An error will occur if the value is “auto” and the input is NOT in PDF format\)

  * **output\_format** \(_OutputFormat_ _,__optional_\) – Format of the inference results.

  * **coordinates** \(_bool_ _,__optional_\) – Whether to include the coordinates of the OCR in the output.

  * **base64\_encoding** \(_List_ _\[__Category_ _\]__,__optional_\) – The category of the elements to be encoded in base64.

Methods

`__init__`\(\[api\_key, base\_url, model, split, ...\]\) | Initializes an instance of the Upstage class.   ---|---   `lazy_parse`\(blob\[, is\_batch\]\) | Lazily parses a document and yields Document objects based on the specified split type.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _api\_key : str | None = None_,     _base\_url : str = 'https://api.upstage.ai/v1/document-ai/document-parse'_,     _model : str = 'document-parse'_,     _split : Literal\['none', 'page', 'element'\] = 'none'_,     _ocr : Literal\['auto', 'force'\] = 'auto'_,     _output\_format : Literal\['text', 'html', 'markdown'\] = 'html'_,     _coordinates : bool = True_,     _base64\_encoding : List\[Literal\['paragraph', 'table', 'figure', 'header', 'footer', 'caption', 'equation', 'heading1', 'list', 'index', 'footnote', 'chart'\]\] = \[\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/document_parse_parsers.html#UpstageDocumentParseParser.__init__)\#     

Initializes an instance of the Upstage class.

Parameters:     

  * **api\_key** \(_str_ _,__optional_\) – The API key for accessing the Upstage API. Defaults to None, in which case it will be fetched from the environment variable UPSTAGE\_API\_KEY.

  * **base\_url** \(_str_ _,__optional_\) – The base URL for accessing the Upstage API.

  * **model** \(_str_\) – The model to be used for the document parse. Defaults to “document-parse”.

  * **split** \(_SplitType_ _,__optional_\) – The type of splitting to be applied. Defaults to “none” \(no splitting\).

  * **ocr** \(_OCRMode_ _,__optional_\) – Extract text from images in the document using OCR. If the value is “force”, OCR is used to extract text from an image. If the value is “auto”, text is extracted from a PDF. \(An error will occur if the value is “auto” and the input is NOT in PDF format\)

  * **output\_format** \(_OutputFormat_ _,__optional_\) – Format of the inference results.

  * **coordinates** \(_bool_ _,__optional_\) – Whether to include the coordinates of the OCR in the output.

  * **base64\_encoding** \(_List_ _\[__Category_ _\]__,__optional_\) – The category of the elements to be encoded in base64.

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_,     _is\_batch : bool = False_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/document_parse_parsers.html#UpstageDocumentParseParser.lazy_parse)\#     

Lazily parses a document and yields Document objects based on the specified split type.

Parameters:     

  * **blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – The input document blob to parse.

  * **is\_batch** \(_bool_ _,__optional_\) – Whether to parse the document in batches. Defaults to False \(single page parsing\)

Yields:     

_Document_ – The parsed document object.

Raises:     

**ValueError** – If an invalid split type is provided.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Eagerly parse the blob into a document or documents.

This is a convenience method for interactive development environment.

Production applications should favor the lazy\_parse method instead.

Subclasses should generally not over-ride this parse method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

List of documents

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page