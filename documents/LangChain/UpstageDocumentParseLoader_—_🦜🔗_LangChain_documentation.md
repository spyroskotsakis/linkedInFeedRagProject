# UpstageDocumentParseLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/upstage/document_parse/langchain_upstage.document_parse.UpstageDocumentParseLoader.html
**Word Count:** 593
**Links Count:** 114
**Scraped:** 2025-07-21 08:45:22
**Status:** completed

---

# UpstageDocumentParseLoader\#

_class _langchain\_upstage.document\_parse.UpstageDocumentParseLoader\(

    _file\_path : str | Path | List\[str\] | List\[Path\]_,     _split : Literal\['none', 'page', 'element'\] = 'none'_,     _api\_key : str | None = None_,     _base\_url : str = 'https://api.upstage.ai/v1/document-ai/document-parse'_,     _model : str = 'document-parse'_,     _ocr : Literal\['auto', 'force'\] = 'auto'_,     _output\_format : Literal\['text', 'html', 'markdown'\] = 'html'_,     _coordinates : bool = True_,     _base64\_encoding : List\[Literal\['paragraph', 'table', 'figure', 'header', 'footer', 'caption', 'equation', 'heading1', 'list', 'index', 'footnote', 'chart'\]\] = \[\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/document_parse.html#UpstageDocumentParseLoader)\#     

Upstage Document Parse Loader.

To use, you should have the environment variable UPSTAGE\_API\_KEY set with your API key or pass it as a named parameter to the constructor.

Example               from langchain_upstage import UpstageDocumentParseLoader          file_path = "/PATH/TO/YOUR/FILE.pdf"     loader = UpstageDocumentParseLoader(                 file_path, split="page", output_format="text"              )     

Initializes an instance of the Upstage document parse loader.

Parameters:     

  * **file\_path** \(_Union_ _\[__str_ _,__Path_ _,__List_ _\[__str_ _\]__,__List_ _\[__Path_ _\]__\]_\) – The path to the document to be loaded.

  * **split** \(_SplitType_ _,__optional_\) – The type of splitting to be applied. Defaults to “none” \(no splitting\).

  * **api\_key** \(_str_ _,__optional_\) – The API key for accessing the Upstage API. Defaults to None, in which case it will be fetched from the environment variable UPSTAGE\_API\_KEY.

  * **base\_url** \(_str_ _,__optional_\) – The base URL for accessing the Upstage API.

  * **model** \(_str_\) – The model to be used for the document parse. Defaults to “document-parse”.

  * **ocr** \(_OCRMode_ _,__optional_\) – Extract text from images in the document using OCR. If the value is “force”, OCR is used to extract text from an image. If the value is “auto”, text is extracted from a PDF. \(An error will occur if the value is “auto” and the input is NOT in PDF format\)

  * **output\_format** \(_OutputFormat_ _,__optional_\) – Format of the inference results.

  * **coordinates** \(_bool_ _,__optional_\) – Whether to include the coordinates of the OCR in the output.

  * **base64\_encoding** \(_List_ _\[__Category_ _\]__,__optional_\) – The category of the elements to be encoded in base64.

Methods

`__init__`\(file\_path\[, split, api\_key, ...\]\) | Initializes an instance of the Upstage document parse loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazily loads and parses the document using the UpstageDocumentParseParser.   `load`\(\) | Loads and parses the document using the UpstageDocumentParseParser.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `merge_and_split`\(documents\[, splitter\]\) | Merges the page content and metadata of multiple documents into a single document, or splits the documents using a custom splitter.      \_\_init\_\_\(

    _file\_path : str | Path | List\[str\] | List\[Path\]_,     _split : Literal\['none', 'page', 'element'\] = 'none'_,     _api\_key : str | None = None_,     _base\_url : str = 'https://api.upstage.ai/v1/document-ai/document-parse'_,     _model : str = 'document-parse'_,     _ocr : Literal\['auto', 'force'\] = 'auto'_,     _output\_format : Literal\['text', 'html', 'markdown'\] = 'html'_,     _coordinates : bool = True_,     _base64\_encoding : List\[Literal\['paragraph', 'table', 'figure', 'header', 'footer', 'caption', 'equation', 'heading1', 'list', 'index', 'footnote', 'chart'\]\] = \[\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/document_parse.html#UpstageDocumentParseLoader.__init__)\#     

Initializes an instance of the Upstage document parse loader.

Parameters:     

  * **file\_path** \(_Union_ _\[__str_ _,__Path_ _,__List_ _\[__str_ _\]__,__List_ _\[__Path_ _\]__\]_\) – The path to the document to be loaded.

  * **split** \(_SplitType_ _,__optional_\) – The type of splitting to be applied. Defaults to “none” \(no splitting\).

  * **api\_key** \(_str_ _,__optional_\) – The API key for accessing the Upstage API. Defaults to None, in which case it will be fetched from the environment variable UPSTAGE\_API\_KEY.

  * **base\_url** \(_str_ _,__optional_\) – The base URL for accessing the Upstage API.

  * **model** \(_str_\) – The model to be used for the document parse. Defaults to “document-parse”.

  * **ocr** \(_OCRMode_ _,__optional_\) – Extract text from images in the document using OCR. If the value is “force”, OCR is used to extract text from an image. If the value is “auto”, text is extracted from a PDF. \(An error will occur if the value is “auto” and the input is NOT in PDF format\)

  * **output\_format** \(_OutputFormat_ _,__optional_\) – Format of the inference results.

  * **coordinates** \(_bool_ _,__optional_\) – Whether to include the coordinates of the OCR in the output.

  * **base64\_encoding** \(_List_ _\[__Category_ _\]__,__optional_\) – The category of the elements to be encoded in base64.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/document_parse.html#UpstageDocumentParseLoader.lazy_load)\#     

Lazily loads and parses the document using the UpstageDocumentParseParser.

Returns:     

An iterator of Document objects representing the parsed layout analysis.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/document_parse.html#UpstageDocumentParseLoader.load)\#     

Loads and parses the document using the UpstageDocumentParseParser.

Returns:     

A list of Document objects representing the parsed layout analysis.

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

merge\_and\_split\(

    _documents : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _splitter : object | None = None_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_upstage/document_parse.html#UpstageDocumentParseLoader.merge_and_split)\#     

Merges the page content and metadata of multiple documents into a single document, or splits the documents using a custom splitter.

Parameters:     

  * **documents** \(_list_\) – A list of Document objects to be merged and split.

  * **splitter** \(_object_ _,__optional_\) – An optional splitter object that implements the split\_documents method. If provided, the documents will be split using this splitter. Defaults to None, in which case the documents are merged.

Returns:     

A list of Document objects. If no splitter is provided, a single Document object is returned with the merged content and combined metadata. If a splitter is provided, the documents are split and a list of Document objects is returned.

Return type:     

list

Raises:     

  * **AssertionError** – If a splitter is provided but it does not implement the

  * **split\_documents** – 

__On this page