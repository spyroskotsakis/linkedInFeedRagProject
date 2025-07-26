# OBSFileLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.obs_file.OBSFileLoader.html
**Word Count:** 598
**Links Count:** 431
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# OBSFileLoader\#

_class _langchain\_community.document\_loaders.obs\_file.OBSFileLoader\(

    _bucket : str_,     _key : str_,     _client : Any = None_,     _endpoint : str = ''_,     _config : dict | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/obs_file.html#OBSFileLoader)\#     

Load from the Huawei OBS file.

Initialize the OBSFileLoader with the specified settings.

Parameters:     

  * **bucket** \(_str_\) – The name of the OBS bucket to be used.

  * **key** \(_str_\) – The name of the object in the OBS bucket.

  * **client** \(_ObsClient_ _,__optional_\) – An instance of the ObsClient to connect to OBS.

  * **endpoint** \(_str_ _,__optional_\) – The endpoint URL of your OBS bucket. This parameter is mandatory if client is not provided.

  * **config** \(_dict_ _,__optional_\) – The parameters for connecting to OBS, provided as a dictionary. This parameter is ignored if client is provided. The dictionary could have the following keys: \- “ak” \(str, optional\): Your OBS access key \(required if get\_token\_from\_ecs is False and bucket policy is not public read\). \- “sk” \(str, optional\): Your OBS secret key \(required if get\_token\_from\_ecs is False and bucket policy is not public read\). \- “token” \(str, optional\): Your security token \(required if using temporary credentials\). \- “get\_token\_from\_ecs” \(bool, optional\): Whether to retrieve the security token from ECS. Defaults to False if not provided. If set to True, ak, sk, and token will be ignored.

Raises:     

  * **ValueError** – If the esdk-obs-python package is not installed.

  * **TypeError** – If the provided client is not an instance of ObsClient.

  * **ValueError** – If client is not provided, but endpoint is missing.

Note

Before using this class, make sure you have registered with OBS and have the necessary credentials. The ak, sk, and endpoint values are mandatory unless get\_token\_from\_ecs is True or the bucket policy is public read. token is required when using temporary credentials.

Example

To create a new OBSFileLoader with a new client: \`\`\` config = \{

> “ak”: “your-access-key”, “sk”: “your-secret-key”

\} obs\_loader = OBSFileLoader\(“your-bucket-name”, “your-object-key”, config=config\) \`\`\`

To create a new OBSFileLoader with an existing client: \`\`\` from obs import ObsClient

\# Assuming you have an existing ObsClient object ‘obs\_client’ obs\_loader = OBSFileLoader\(“your-bucket-name”, “your-object-key”, client=obs\_client\) \`\`\`

To create a new OBSFileLoader without an existing client: `` obs_loader = OBSFileLoader("your-bucket-name", "your-object-key", endpoint="your-endpoint-url") ``

Methods

`__init__`\(bucket, key\[, client, endpoint, config\]\) | Initialize the OBSFileLoader with the specified settings.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\[mode\]\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _bucket : str_,     _key : str_,     _client : Any = None_,     _endpoint : str = ''_,     _config : dict | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/obs_file.html#OBSFileLoader.__init__)\#     

Initialize the OBSFileLoader with the specified settings.

Parameters:     

  * **bucket** \(_str_\) – The name of the OBS bucket to be used.

  * **key** \(_str_\) – The name of the object in the OBS bucket.

  * **client** \(_ObsClient_ _,__optional_\) – An instance of the ObsClient to connect to OBS.

  * **endpoint** \(_str_ _,__optional_\) – The endpoint URL of your OBS bucket. This parameter is mandatory if client is not provided.

  * **config** \(_dict_ _,__optional_\) – The parameters for connecting to OBS, provided as a dictionary. This parameter is ignored if client is provided. The dictionary could have the following keys: \- “ak” \(str, optional\): Your OBS access key \(required if get\_token\_from\_ecs is False and bucket policy is not public read\). \- “sk” \(str, optional\): Your OBS secret key \(required if get\_token\_from\_ecs is False and bucket policy is not public read\). \- “token” \(str, optional\): Your security token \(required if using temporary credentials\). \- “get\_token\_from\_ecs” \(bool, optional\): Whether to retrieve the security token from ECS. Defaults to False if not provided. If set to True, ak, sk, and token will be ignored.

Raises:     

  * **ValueError** – If the esdk-obs-python package is not installed.

  * **TypeError** – If the provided client is not an instance of ObsClient.

  * **ValueError** – If client is not provided, but endpoint is missing.

Return type:     

None

Note

Before using this class, make sure you have registered with OBS and have the necessary credentials. The ak, sk, and endpoint values are mandatory unless get\_token\_from\_ecs is True or the bucket policy is public read. token is required when using temporary credentials.

Example

To create a new OBSFileLoader with a new client: \`\`\` config = \{

> “ak”: “your-access-key”, “sk”: “your-secret-key”

\} obs\_loader = OBSFileLoader\(“your-bucket-name”, “your-object-key”, config=config\) \`\`\`

To create a new OBSFileLoader with an existing client: \`\`\` from obs import ObsClient

\# Assuming you have an existing ObsClient object ‘obs\_client’ obs\_loader = OBSFileLoader\(“your-bucket-name”, “your-object-key”, client=obs\_client\) \`\`\`

To create a new OBSFileLoader without an existing client: `` obs_loader = OBSFileLoader("your-bucket-name", "your-object-key", endpoint="your-endpoint-url") ``

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

load\(

    _mode : str = 'single'_, \) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/obs_file.html#OBSFileLoader.load)\#     

Load documents.

Parameters:     

**mode** \(_str_\)

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

Examples using OBSFileLoader

  * [Huawei](https://python.langchain.com/docs/integrations/providers/huawei/)

  * [Huawei OBS File](https://python.langchain.com/docs/integrations/document_loaders/huawei_obs_file/)

__On this page