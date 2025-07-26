# MintbaseDocumentLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.mintbase.MintbaseDocumentLoader.html
**Word Count:** 307
**Links Count:** 418
**Scraped:** 2025-07-21 08:20:44
**Status:** completed

---

# MintbaseDocumentLoader\#

_class _langchain\_community.document\_loaders.mintbase.MintbaseDocumentLoader\(

    _contract\_address : str_,     _\*_ ,     _blockchain\_type : Literal\['mainnet', 'testnet'\]_,     _api\_key : str = ''_,     _table : str = ''_,     _select : str = ''_,     _fields : List\[str\] | None = None_,     _get\_all\_tokens : bool = False_,     _max\_execution\_time : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mintbase.html#MintbaseDocumentLoader)\#     

Load elements from a blockchain smart contract.

The supported blockchains are: Near mainnet, Near testnet.

If no BlockchainType is specified, the default is Near mainnet.

The Loader uses the Mintbase API to interact with the blockchain. MB\_API\_KEY environment variable must be set to use this loader.

The API returns 100 NFTs per request and can be paginated using the startToken parameter.

If get\_all\_tokens is set to True, the loader will get all tokens on the contract. Note that for contracts with a large number of tokens, this may take a long time \(e.g. 10k tokens is 100 requests\). Default value is false for this reason.

The max\_execution\_time \(sec\) can be set to limit the execution time of the loader.

Future versions of this loader can:     

  * Support additional Mintbase APIs \(e.g. getTokens, etc.\)

Example               contractAddress = "nft.yearofchef.near"  # Year of chef contract address     blockchainLoader = MintbaseDocumentLoader(         contract_address=contractAddress, blockchain_type="mainnet",api_key="omni-site"     )     

Parameters:     

  * **contract\_address** \(_str_\) – The address of the smart contract.

  * **blockchainType** – The blockchain type.

  * **api\_key** \(_str_\) – The Mintbase API key.

  * **table** \(_str_\) – name of the table to query

  * **select** \(_str_\) – Conditions for querying

  * **fields** \(_List_ _\[__str_ _\]__|__None_\) – Information to display after query

  * **get\_all\_tokens** \(_bool_\) – Whether to get all tokens on the contract.

  * **max\_execution\_time** \(_int_ _|__None_\) – The maximum execution time \(sec\).

  * **blockchain\_type** \(_Literal_ _\[__'mainnet'__,__'testnet'__\]_\)

Methods

`__init__`\(contract\_address, \*, blockchain\_type\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _contract\_address : str_,     _\*_ ,     _blockchain\_type : Literal\['mainnet', 'testnet'\]_,     _api\_key : str = ''_,     _table : str = ''_,     _select : str = ''_,     _fields : List\[str\] | None = None_,     _get\_all\_tokens : bool = False_,     _max\_execution\_time : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mintbase.html#MintbaseDocumentLoader.__init__)\#     

Parameters:     

  * **contract\_address** \(_str_\) – The address of the smart contract.

  * **blockchainType** – The blockchain type.

  * **api\_key** \(_str_\) – The Mintbase API key.

  * **table** \(_str_\) – name of the table to query

  * **select** \(_str_\) – Conditions for querying

  * **fields** \(_List_ _\[__str_ _\]__|__None_\) – Information to display after query

  * **get\_all\_tokens** \(_bool_\) – Whether to get all tokens on the contract.

  * **max\_execution\_time** \(_int_ _|__None_\) – The maximum execution time \(sec\).

  * **blockchain\_type** \(_Literal_ _\[__'mainnet'__,__'testnet'__\]_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mintbase.html#MintbaseDocumentLoader.lazy_load)\#     

A lazy loader for Documents.

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/mintbase.html#MintbaseDocumentLoader.load)\#     

Load data into Document objects.

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

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)