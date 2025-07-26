# AmazonTextractPDFLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.pdf.AmazonTextractPDFLoader.html
**Word Count:** 303
**Links Count:** 421
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# AmazonTextractPDFLoader\#

_class _langchain\_community.document\_loaders.pdf.AmazonTextractPDFLoader\(

    _file\_path : str | PurePath_,     _textract\_features : Sequence\[str\] | None = None_,     _client : Any | None = None_,     _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_,     _endpoint\_url : str | None = None_,     _headers : dict | None = None_,     _\*_ ,     _linearization\_config : TextLinearizationConfig | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#AmazonTextractPDFLoader)\#     

Load PDF files from a local file system, HTTP or S3.

To authenticate, the AWS client uses the following methods to automatically load credentials: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

If a specific credential profile should be used, you must pass the name of the profile from the ~/.aws/credentials file that is to be used.

Make sure the credentials / roles used have the required policies to access the Amazon Textract service.

Example

Initialize the loader.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\) – A file, url or s3 path for input file

  * **textract\_features** \(_Sequence_ _\[__str_ _\]__|__None_\) – Features to be used for extraction, each feature should be passed as a str that conforms to the enum Textract\_Features, see amazon-textract-caller pkg

  * **client** \(_Any_ _|__None_\) – boto3 textract client \(Optional\)

  * **credentials\_profile\_name** \(_str_ _|__None_\) – AWS profile name, if not default \(Optional\)

  * **region\_name** \(_str_ _|__None_\) – AWS region, eg us-east-1 \(Optional\)

  * **endpoint\_url** \(_str_ _|__None_\) – endpoint url for the textract service \(Optional\)

  * **linearization\_config** \(_TextLinearizationConfig_ _|__None_\) – Config to be used for linearization of the output should be an instance of TextLinearizationConfig from the textractor pkg

  * **headers** \(_dict_ _|__None_\)

Attributes

`source` |    ---|---      Methods

`__init__`\(file\_path\[, textract\_features, ...\]\) | Initialize the loader.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load documents   `load`\(\) | Load given path as pages.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _file\_path : str | PurePath_,     _textract\_features : Sequence\[str\] | None = None_,     _client : Any | None = None_,     _credentials\_profile\_name : str | None = None_,     _region\_name : str | None = None_,     _endpoint\_url : str | None = None_,     _headers : dict | None = None_,     _\*_ ,     _linearization\_config : TextLinearizationConfig | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#AmazonTextractPDFLoader.__init__)\#     

Initialize the loader.

Parameters:     

  * **file\_path** \(_str_ _|__PurePath_\) – A file, url or s3 path for input file

  * **textract\_features** \(_Sequence_ _\[__str_ _\]__|__None_\) – Features to be used for extraction, each feature should be passed as a str that conforms to the enum Textract\_Features, see amazon-textract-caller pkg

  * **client** \(_Any_ _|__None_\) – boto3 textract client \(Optional\)

  * **credentials\_profile\_name** \(_str_ _|__None_\) – AWS profile name, if not default \(Optional\)

  * **region\_name** \(_str_ _|__None_\) – AWS region, eg us-east-1 \(Optional\)

  * **endpoint\_url** \(_str_ _|__None_\) – endpoint url for the textract service \(Optional\)

  * **linearization\_config** \(_TextLinearizationConfig_ _|__None_\) – Config to be used for linearization of the output should be an instance of TextLinearizationConfig from the textractor pkg

  * **headers** \(_dict_ _|__None_\)

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#AmazonTextractPDFLoader.lazy_load)\#     

Lazy load documents

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/pdf.html#AmazonTextractPDFLoader.load)\#     

Load given path as pages.

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

Examples using AmazonTextractPDFLoader

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [Amazon Textract ](https://python.langchain.com/docs/integrations/document_loaders/amazon_textract/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)