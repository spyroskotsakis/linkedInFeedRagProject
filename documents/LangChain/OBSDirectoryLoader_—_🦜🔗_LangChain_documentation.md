# OBSDirectoryLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.obs_directory.OBSDirectoryLoader.html
**Word Count:** 445
**Links Count:** 423
**Scraped:** 2025-07-21 08:06:47
**Status:** completed

---

# OBSDirectoryLoader\#

_class _langchain\_community.document\_loaders.obs\_directory.OBSDirectoryLoader\(

    _bucket : str_,     _endpoint : str_,     _config : dict | None = None_,     _prefix : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/obs_directory.html#OBSDirectoryLoader)\#     

Load from Huawei OBS directory.

Initialize the OBSDirectoryLoader with the specified settings.

Parameters:     

  * **bucket** \(_str_\) – The name of the OBS bucket to be used.

  * **endpoint** \(_str_\) – The endpoint URL of your OBS bucket.

  * **config** \(_dict_\) – The parameters for connecting to OBS, provided as a dictionary. The dictionary could have the following keys: \- “ak” \(str, optional\): Your OBS access key \(required if get\_token\_from\_ecs is False and bucket policy is not public read\). \- “sk” \(str, optional\): Your OBS secret key \(required if get\_token\_from\_ecs is False and bucket policy is not public read\). \- “token” \(str, optional\): Your security token \(required if using temporary credentials\). \- “get\_token\_from\_ecs” \(bool, optional\): Whether to retrieve the security token from ECS. Defaults to False if not provided. If set to True, ak, sk, and token will be ignored.

  * **prefix** \(_str_ _,__optional_\) – The prefix to be added to the OBS key. Defaults to “”.

Note

Before using this class, make sure you have registered with OBS and have the necessary credentials. The ak, sk, and endpoint values are mandatory unless get\_token\_from\_ecs is True or the bucket policy is public read. token is required when using temporary credentials.

Example

To create a new OBSDirectoryLoader: \`\`\` config = \{

> “ak”: “your-access-key”, “sk”: “your-secret-key”

## \}\#

directory\_loader = OBSDirectoryLoader\(“your-bucket-name”, “your-end-endpoint”, config, “your-prefix”\)

Methods

`__init__`\(bucket, endpoint\[, config, prefix\]\) | Initialize the OBSDirectoryLoader with the specified settings.   ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load documents.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _bucket : str_,     _endpoint : str_,     _config : dict | None = None_,     _prefix : str = ''_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/obs_directory.html#OBSDirectoryLoader.__init__)\#     

Initialize the OBSDirectoryLoader with the specified settings.

Parameters:     

  * **bucket** \(_str_\) – The name of the OBS bucket to be used.

  * **endpoint** \(_str_\) – The endpoint URL of your OBS bucket.

  * **config** \(_dict_\) – The parameters for connecting to OBS, provided as a dictionary. The dictionary could have the following keys: \- “ak” \(str, optional\): Your OBS access key \(required if get\_token\_from\_ecs is False and bucket policy is not public read\). \- “sk” \(str, optional\): Your OBS secret key \(required if get\_token\_from\_ecs is False and bucket policy is not public read\). \- “token” \(str, optional\): Your security token \(required if using temporary credentials\). \- “get\_token\_from\_ecs” \(bool, optional\): Whether to retrieve the security token from ECS. Defaults to False if not provided. If set to True, ak, sk, and token will be ignored.

  * **prefix** \(_str_ _,__optional_\) – The prefix to be added to the OBS key. Defaults to “”.

Note

Before using this class, make sure you have registered with OBS and have the necessary credentials. The ak, sk, and endpoint values are mandatory unless get\_token\_from\_ecs is True or the bucket policy is public read. token is required when using temporary credentials.

Example

To create a new OBSDirectoryLoader: \`\`\` config = \{

> “ak”: “your-access-key”, “sk”: “your-secret-key”

### \}\#

directory\_loader = OBSDirectoryLoader\(“your-bucket-name”, “your-end-endpoint”, config, “your-prefix”\)

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/obs_directory.html#OBSDirectoryLoader.load)\#     

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

Examples using OBSDirectoryLoader

  * [Huawei](https://python.langchain.com/docs/integrations/providers/huawei/)

  * [Huawei OBS Directory](https://python.langchain.com/docs/integrations/document_loaders/huawei_obs_directory/)

__On this page