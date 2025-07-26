# S3DirectoryLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.s3_directory.S3DirectoryLoader.html
**Word Count:** 810
**Links Count:** 419
**Scraped:** 2025-07-21 08:19:43
**Status:** completed

---

# S3DirectoryLoader\#

_class _langchain\_community.document\_loaders.s3\_directory.S3DirectoryLoader\(

    _bucket : str_,     _prefix : str = ''_,     _\*_ ,     _region\_name : str | None = None_,     _api\_version : str | None = None_,     _use\_ssl : bool | None = True_,     _verify : str | bool | None = None_,     _endpoint\_url : str | None = None_,     _aws\_access\_key\_id : str | None = None_,     _aws\_secret\_access\_key : str | None = None_,     _aws\_session\_token : str | None = None_,     _boto\_config : botocore.client.Config | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/s3_directory.html#S3DirectoryLoader)\#     

Load from Amazon AWS S3 directory.

Initialize with bucket and key name.

Parameters:     

  * **bucket** \(_str_\) – The name of the S3 bucket.

  * **prefix** \(_str_\) – The prefix of the S3 key. Defaults to “”.

  * **region\_name** \(_Optional_ _\[__str_ _\]_\) – The name of the region associated with the client. A client is associated with a single region.

  * **api\_version** \(_Optional_ _\[__str_ _\]_\) – The API version to use. By default, botocore will use the latest API version when creating a client. You only need to specify this parameter if you want to use a previous API version of the client.

  * **use\_ssl** \(_Optional_ _\[__bool_ _\]_\) – Whether to use SSL. By default, SSL is used. Note that not all services support non-ssl connections.

  * **verify** \(_Union_ _\[__str_ _,__bool_ _,__None_ _\]_\) – 

Whether to verify SSL certificates. By default SSL certificates are verified. You can provide the following values:

    * False - do not validate SSL certificates. SSL will still be used \(unless use\_ssl is False\), but SSL certificates will not be verified.

    * path/to/cert/bundle.pem - A filename of the CA cert bundle to uses. You can specify this argument if you want to use a different CA cert bundle than the one used by botocore.

  * **endpoint\_url** \(_Optional_ _\[__str_ _\]_\) – The complete URL to use for the constructed client. Normally, botocore will automatically construct the appropriate URL to use when communicating with a service. You can specify a complete URL \(including the “http/https” scheme\) to override this behavior. If this value is provided, then `use_ssl` is ignored.

  * **aws\_access\_key\_id** \(_Optional_ _\[__str_ _\]_\) – The access key to use when creating the client. This is entirely optional, and if not provided, the credentials configured for the session will automatically be used. You only need to provide this argument if you want to override the credentials used for this specific client.

  * **aws\_secret\_access\_key** \(_Optional_ _\[__str_ _\]_\) – The secret key to use when creating the client. Same semantics as aws\_access\_key\_id above.

  * **aws\_session\_token** \(_Optional_ _\[__str_ _\]_\) – The session token to use when creating the client. Same semantics as aws\_access\_key\_id above.

  * **boto\_config** \(_botocore.client.Config_\) – Advanced boto3 client configuration options. If a value is specified in the client config, its value will take precedence over environment variables and configuration values, but not over a value passed explicitly to the method. If a default config object is set on the session, the config object used when creating the client will be the result of calling `merge()` on the default config with the config provided to this call.

Methods

`__init__`\(bucket\[, prefix, region\_name, ...\]\) | Initialize with bucket and key name.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _bucket : str_,     _prefix : str = ''_,     _\*_ ,     _region\_name : str | None = None_,     _api\_version : str | None = None_,     _use\_ssl : bool | None = True_,     _verify : str | bool | None = None_,     _endpoint\_url : str | None = None_,     _aws\_access\_key\_id : str | None = None_,     _aws\_secret\_access\_key : str | None = None_,     _aws\_session\_token : str | None = None_,     _boto\_config : botocore.client.Config | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/s3_directory.html#S3DirectoryLoader.__init__)\#     

Initialize with bucket and key name.

Parameters:     

  * **bucket** \(_str_\) – The name of the S3 bucket.

  * **prefix** \(_str_\) – The prefix of the S3 key. Defaults to “”.

  * **region\_name** \(_Optional_ _\[__str_ _\]_\) – The name of the region associated with the client. A client is associated with a single region.

  * **api\_version** \(_Optional_ _\[__str_ _\]_\) – The API version to use. By default, botocore will use the latest API version when creating a client. You only need to specify this parameter if you want to use a previous API version of the client.

  * **use\_ssl** \(_Optional_ _\[__bool_ _\]_\) – Whether to use SSL. By default, SSL is used. Note that not all services support non-ssl connections.

  * **verify** \(_Union_ _\[__str_ _,__bool_ _,__None_ _\]_\) – 

Whether to verify SSL certificates. By default SSL certificates are verified. You can provide the following values:

    * False - do not validate SSL certificates. SSL will still be used \(unless use\_ssl is False\), but SSL certificates will not be verified.

    * path/to/cert/bundle.pem - A filename of the CA cert bundle to uses. You can specify this argument if you want to use a different CA cert bundle than the one used by botocore.

  * **endpoint\_url** \(_Optional_ _\[__str_ _\]_\) – The complete URL to use for the constructed client. Normally, botocore will automatically construct the appropriate URL to use when communicating with a service. You can specify a complete URL \(including the “http/https” scheme\) to override this behavior. If this value is provided, then `use_ssl` is ignored.

  * **aws\_access\_key\_id** \(_Optional_ _\[__str_ _\]_\) – The access key to use when creating the client. This is entirely optional, and if not provided, the credentials configured for the session will automatically be used. You only need to provide this argument if you want to override the credentials used for this specific client.

  * **aws\_secret\_access\_key** \(_Optional_ _\[__str_ _\]_\) – The secret key to use when creating the client. Same semantics as aws\_access\_key\_id above.

  * **aws\_session\_token** \(_Optional_ _\[__str_ _\]_\) – The session token to use when creating the client. Same semantics as aws\_access\_key\_id above.

  * **boto\_config** \(_botocore.client.Config_\) – Advanced boto3 client configuration options. If a value is specified in the client config, its value will take precedence over environment variables and configuration values, but not over a value passed explicitly to the method. If a default config object is set on the session, the config object used when creating the client will be the result of calling `merge()` on the default config with the config provided to this call.

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/s3_directory.html#S3DirectoryLoader.load)\#     

Load documents.

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

Examples using S3DirectoryLoader

  * [AWS](https://python.langchain.com/docs/integrations/providers/aws/)

  * [AWS S3 Directory](https://python.langchain.com/docs/integrations/document_loaders/aws_s3_directory/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)