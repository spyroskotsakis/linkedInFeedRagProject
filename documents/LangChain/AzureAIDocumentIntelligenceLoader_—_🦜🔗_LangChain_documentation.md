# AzureAIDocumentIntelligenceLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.doc_intelligence.AzureAIDocumentIntelligenceLoader.html
**Word Count:** 518
**Links Count:** 426
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# AzureAIDocumentIntelligenceLoader\#

_class _langchain\_community.document\_loaders.doc\_intelligence.AzureAIDocumentIntelligenceLoader\(

    _api\_endpoint : str_,     _api\_key : str | None = None_,     _file\_path : str | None = None_,     _url\_path : str | None = None_,     _bytes\_source : bytes | None = None_,     _api\_version : str | None = None_,     _api\_model : str = 'prebuilt-layout'_,     _mode : str = 'markdown'_,     _\*_ ,     _analysis\_features : List\[str\] | None = None_,     _azure\_credential : 'TokenCredential' | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/doc_intelligence.html#AzureAIDocumentIntelligenceLoader)\#     

Load a PDF with Azure Document Intelligence.

Initialize the object for file processing with Azure Document Intelligence \(formerly Form Recognizer\).

This constructor initializes a AzureAIDocumentIntelligenceParser object to be used for parsing files using the Azure Document Intelligence API. The load method generates Documents whose content representations are determined by the mode parameter.

## Parameters:\#

api\_endpoint: str     

The API endpoint to use for DocumentIntelligenceClient construction.

api\_key: str     

The API key to use for DocumentIntelligenceClient construction.

file\_pathOptional\[str\]     

The path to the file that needs to be loaded. Either file\_path, url\_path or bytes\_source must be specified.

url\_pathOptional\[str\]     

The URL to the file that needs to be loaded. Either file\_path, url\_path or bytes\_source must be specified.

bytes\_sourceOptional\[bytes\]     

The bytes array of the file that needs to be loaded. Either file\_path, url\_path or bytes\_source must be specified.

api\_version: Optional\[str\]     

The API version for DocumentIntelligenceClient. Setting None to use the default value from azure-ai-documentintelligence package.

api\_model: str     

Unique document model name. Default value is “prebuilt-layout”. Note that overriding this default value may result in unsupported behavior.

mode: Optional\[str\]     

The type of content representation of the generated Documents. Use either “single”, “page”, or “markdown”. Default value is “markdown”.

analysis\_features: Optional\[List\[str\]\]     

List of optional analysis features, each feature should be passed as a str that conforms to the enum DocumentAnalysisFeature in azure-ai-documentintelligence package. Default value is None.

azure\_credential: Optional\[TokenCredential\]     

The credentials to use for DocumentIntelligenceClient construction, when using credentials other than api\_key \(like AD\).

## Examples:\#               >>> obj = AzureAIDocumentIntelligenceLoader(     ...     file_path="path/to/file",     ...     api_endpoint="https://endpoint.azure.com",     ...     api_key="APIKEY",     ...     api_version="2023-10-31-preview",     ...     api_model="prebuilt-layout",     ...     mode="markdown"     ... )     

Methods

`__init__`\(api\_endpoint\[, api\_key, file\_path, ...\]\) | Initialize the object for file processing with Azure Document Intelligence \(formerly Form Recognizer\).   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | Lazy load the document as pages.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _api\_endpoint : str_,     _api\_key : str | None = None_,     _file\_path : str | None = None_,     _url\_path : str | None = None_,     _bytes\_source : bytes | None = None_,     _api\_version : str | None = None_,     _api\_model : str = 'prebuilt-layout'_,     _mode : str = 'markdown'_,     _\*_ ,     _analysis\_features : List\[str\] | None = None_,     _azure\_credential : 'TokenCredential' | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/doc_intelligence.html#AzureAIDocumentIntelligenceLoader.__init__)\#     

Initialize the object for file processing with Azure Document Intelligence \(formerly Form Recognizer\).

This constructor initializes a AzureAIDocumentIntelligenceParser object to be used for parsing files using the Azure Document Intelligence API. The load method generates Documents whose content representations are determined by the mode parameter.

### Parameters:\#

api\_endpoint: str     

The API endpoint to use for DocumentIntelligenceClient construction.

api\_key: str     

The API key to use for DocumentIntelligenceClient construction.

file\_pathOptional\[str\]     

The path to the file that needs to be loaded. Either file\_path, url\_path or bytes\_source must be specified.

url\_pathOptional\[str\]     

The URL to the file that needs to be loaded. Either file\_path, url\_path or bytes\_source must be specified.

bytes\_sourceOptional\[bytes\]     

The bytes array of the file that needs to be loaded. Either file\_path, url\_path or bytes\_source must be specified.

api\_version: Optional\[str\]     

The API version for DocumentIntelligenceClient. Setting None to use the default value from azure-ai-documentintelligence package.

api\_model: str     

Unique document model name. Default value is “prebuilt-layout”. Note that overriding this default value may result in unsupported behavior.

mode: Optional\[str\]     

The type of content representation of the generated Documents. Use either “single”, “page”, or “markdown”. Default value is “markdown”.

analysis\_features: Optional\[List\[str\]\]     

List of optional analysis features, each feature should be passed as a str that conforms to the enum DocumentAnalysisFeature in azure-ai-documentintelligence package. Default value is None.

azure\_credential: Optional\[TokenCredential\]     

The credentials to use for DocumentIntelligenceClient construction, when using credentials other than api\_key \(like AD\).

### Examples:\#               >>> obj = AzureAIDocumentIntelligenceLoader(     ...     file_path="path/to/file",     ...     api_endpoint="https://endpoint.azure.com",     ...     api_key="APIKEY",     ...     api_version="2023-10-31-preview",     ...     api_model="prebuilt-layout",     ...     mode="markdown"     ... )     

Parameters:     

  * **api\_endpoint** \(_str_\)

  * **api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **file\_path** \(_Optional_ _\[__str_ _\]_\)

  * **url\_path** \(_Optional_ _\[__str_ _\]_\)

  * **bytes\_source** \(_Optional_ _\[__bytes_ _\]_\)

  * **api\_version** \(_Optional_ _\[__str_ _\]_\)

  * **api\_model** \(_str_\)

  * **mode** \(_str_\)

  * **analysis\_features** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **azure\_credential** \(_Optional_ _\[__'TokenCredential'__\]_\)

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

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/doc_intelligence.html#AzureAIDocumentIntelligenceLoader.lazy_load)\#     

Lazy load the document as pages.

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

Parameters:     

  * **api\_endpoint** \(_str_\)

  * **api\_key** \(_Optional_ _\[__str_ _\]_\)

  * **file\_path** \(_Optional_ _\[__str_ _\]_\)

  * **url\_path** \(_Optional_ _\[__str_ _\]_\)

  * **bytes\_source** \(_Optional_ _\[__bytes_ _\]_\)

  * **api\_version** \(_Optional_ _\[__str_ _\]_\)

  * **api\_model** \(_str_\)

  * **mode** \(_str_\)

  * **analysis\_features** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\)

  * **azure\_credential** \(_Optional_ _\[__'TokenCredential'__\]_\)

Examples using AzureAIDocumentIntelligenceLoader

  * [Azure AI Document Intelligence](https://python.langchain.com/docs/integrations/document_loaders/azure_document_intelligence/)

  * [How to load Microsoft Office files](https://python.langchain.com/docs/how_to/document_loader_office_file/)

  * [Microsoft Excel](https://python.langchain.com/docs/integrations/document_loaders/microsoft_excel/)

  * [Microsoft PowerPoint](https://python.langchain.com/docs/integrations/document_loaders/microsoft_powerpoint/)

  * [Microsoft Word](https://python.langchain.com/docs/integrations/document_loaders/microsoft_word/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)