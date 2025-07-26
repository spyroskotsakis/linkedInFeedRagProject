# AmazonTextractPDFParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.pdf.AmazonTextractPDFParser.html
**Word Count:** 419
**Links Count:** 410
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# AmazonTextractPDFParser\#

_class _langchain\_community.document\_loaders.parsers.pdf.AmazonTextractPDFParser\(

    _textract\_features : Sequence\[int\] | None = None_,     _client : Any | None = None_,     _\*_ ,     _linearization\_config : TextLinearizationConfig | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#AmazonTextractPDFParser)\#     

Send PDF files to Amazon Textract and parse them.

For parsing multi-page PDFs, they have to reside on S3.

The AmazonTextractPDFLoader calls the \[Amazon Textract Service\]\(<https://aws.amazon.com/textract/>\) to convert PDFs into a Document structure. Single and multi-page documents are supported with up to 3000 pages and 512 MB of size.

For the call to be successful an AWS account is required, similar to the \[AWS CLI\]\(<https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html>\) requirements.

Besides the AWS configuration, it is very similar to the other PDF loaders, while also supporting JPEG, PNG and TIFF and non-native PDF formats.

``python from langchain_community.document_loaders import AmazonTextractPDFLoader loader=AmazonTextractPDFLoader("example_data/alejandro_rosalez_sample-small.jpeg") documents = loader.load() ``

One feature is the linearization of the output. When using the features LAYOUT, FORMS or TABLES together with Textract

\`\`\`python from langchain\_community.document\_loaders import AmazonTextractPDFLoader \# you can mix and match each of the features loader=AmazonTextractPDFLoader\(

> “example\_data/alejandro\_rosalez\_sample-small.jpeg”, textract\_features=\[“TABLES”, “LAYOUT”\]\)

documents = loader.load\(\) \`\`\`

it will generate output that formats the text in reading order and try to output the information in a tabular structure or output the key/value pairs with a colon \(key: value\). This helps most LLMs to achieve better accuracy when processing these texts.

`Document` objects are returned with metadata that includes the `source` and a 1-based index of the page number in `page`. Note that `page` represents the index of the result returned from Textract, not necessarily the as-written page number in the document.

Initializes the parser.

Parameters:     

  * **textract\_features** \(_Optional_ _\[__Sequence_ _\[__int_ _\]__\]_\) – Features to be used for extraction, each feature should be passed as an int that conforms to the enum Textract\_Features, see amazon-textract-caller pkg

  * **client** \(_Optional_ _\[__Any_ _\]_\) – boto3 textract client

  * **linearization\_config** \(_Optional_ _\[__TextLinearizationConfig_ _\]_\) – Config to be used for linearization of the output should be an instance of TextLinearizationConfig from the textractor pkg

Methods

`__init__`\(\[textract\_features, client, ...\]\) | Initializes the parser.   ---|---   `lazy_parse`\(blob\) | Iterates over the Blob pages and returns an Iterator with a Document for each page, like the other parsers If multi-page document, blob.path has to be set to the S3 URI and for single page docs the blob.data is taken   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _textract\_features : Sequence\[int\] | None = None_,     _client : Any | None = None_,     _\*_ ,     _linearization\_config : TextLinearizationConfig | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#AmazonTextractPDFParser.__init__)\#     

Initializes the parser.

Parameters:     

  * **textract\_features** \(_Optional_ _\[__Sequence_ _\[__int_ _\]__\]_\) – Features to be used for extraction, each feature should be passed as an int that conforms to the enum Textract\_Features, see amazon-textract-caller pkg

  * **client** \(_Optional_ _\[__Any_ _\]_\) – boto3 textract client

  * **linearization\_config** \(_Optional_ _\[__TextLinearizationConfig_ _\]_\) – Config to be used for linearization of the output should be an instance of TextLinearizationConfig from the textractor pkg

Return type:     

None

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/pdf.html#AmazonTextractPDFParser.lazy_parse)\#     

Iterates over the Blob pages and returns an Iterator with a Document for each page, like the other parsers If multi-page document, blob.path has to be set to the S3 URI and for single page docs the blob.data is taken

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\)

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\(_blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)