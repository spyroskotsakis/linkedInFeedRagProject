# MathpixPDFLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.MathpixPDFLoader.html
**Word Count:** 227
**Links Count:** 434
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# MathpixPDFLoader\#

_class _langchain\_community.document\_loaders.pdf.MathpixPDFLoader\(

    _file\_path : str | PurePath_,     _processed\_file\_format : str = 'md'_,     _max\_wait\_time\_seconds : int = 500_,     _should\_clean\_pdf : bool = False_,     _extra\_request\_data : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#MathpixPDFLoader)\#     

Load PDF files using Mathpix service.

Initialize with a file path.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\) – a file for loading.

  * **processed\_file\_format** \(_str_\) – a format of the processed file. Default is “md”.

  * **max\_wait\_time\_seconds** \(_int_\) – a maximum time to wait for the response from the server. Default is 500.

  * **should\_clean\_pdf** \(_bool_\) – a flag to clean the PDF file. Default is False.

  * **extra\_request\_data** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Additional request data.

  * **\*\*kwargs** \(_Any_\) – additional keyword arguments.

Attributes

`data` |    ---|---   `source` |    `url` |       Methods

`__init__`\(file\_path\[, processed\_file\_format, ...\]\) | Initialize with a file path.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `clean_pdf`\(contents\) | Clean the PDF file.   `get_processed_pdf`\(pdf\_id\) |    `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.   `send_pdf`\(\) |    `wait_for_processing`\(pdf\_id\) | Wait for processing to complete.      \_\_init\_\_\(

    _file\_path : str | PurePath_,     _processed\_file\_format : str = 'md'_,     _max\_wait\_time\_seconds : int = 500_,     _should\_clean\_pdf : bool = False_,     _extra\_request\_data : dict\[str, Any\] | None = None_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#MathpixPDFLoader.__init__)\#     

Initialize with a file path.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\) – a file for loading.

  * **processed\_file\_format** \(_str_\) – a format of the processed file. Default is “md”.

  * **max\_wait\_time\_seconds** \(_int_\) – a maximum time to wait for the response from the server. Default is 500.

  * **should\_clean\_pdf** \(_bool_\) – a flag to clean the PDF file. Default is False.

  * **extra\_request\_data** \(_dict_ _\[__str_ _,__Any_ _\]__|__None_\) – Additional request data.

  * **\*\*kwargs** \(_Any_\) – additional keyword arguments.

Return type:     

None

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

clean\_pdf\(_contents : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#MathpixPDFLoader.clean_pdf)\#     

Clean the PDF file.

Parameters:     

**contents** \(_str_\) – a PDF file contents.

Return type:     

str

Returns:

get\_processed\_pdf\(_pdf\_id : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#MathpixPDFLoader.get_processed_pdf)\#     

Parameters:     

**pdf\_id** \(_str_\)

Return type:     

str

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#MathpixPDFLoader.load)\#     

Load data into Document objects.

Return type:     

list\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

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

send\_pdf\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#MathpixPDFLoader.send_pdf)\#     

Return type:     

str

wait\_for\_processing\(_pdf\_id : str_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#MathpixPDFLoader.wait_for_processing)\#     

Wait for processing to complete.

Parameters:     

**pdf\_id** \(_str_\) – a PDF id.

Return type:     

None

Returns: None

Examples using MathpixPDFLoader

  * [MathPixPDFLoader](https://python.langchain.com/docs/integrations/document_loaders/mathpix/)

__On this page