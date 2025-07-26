# BlockchainDocumentLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blockchain.BlockchainDocumentLoader.html
**Word Count:** 287
**Links Count:** 424
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# BlockchainDocumentLoader\#

_class _langchain\_community.document\_loaders.blockchain.BlockchainDocumentLoader\(

    _contract\_address : str_,     _blockchainType : [BlockchainType](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blockchain.BlockchainType.html#langchain_community.document_loaders.blockchain.BlockchainType "langchain_community.document_loaders.blockchain.BlockchainType") = BlockchainType.ETH\_MAINNET_,     _api\_key : str = 'docs-demo'_,     _startToken : str = ''_,     _get\_all\_tokens : bool = False_,     _max\_execution\_time : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blockchain.html#BlockchainDocumentLoader)\#     

Load elements from a blockchain smart contract.

See supported blockchains here: <https://python.langchain.com/v0.2/api_reference/community/document_loaders/langchain_community.document_loaders.blockchain.BlockchainType.html>

If no BlockchainType is specified, the default is Ethereum mainnet.

The Loader uses the Alchemy API to interact with the blockchain. ALCHEMY\_API\_KEY environment variable must be set to use this loader.

The API returns 100 NFTs per request and can be paginated using the startToken parameter.

If get\_all\_tokens is set to True, the loader will get all tokens on the contract. Note that for contracts with a large number of tokens, this may take a long time \(e.g. 10k tokens is 100 requests\). Default value is false for this reason.

The max\_execution\_time \(sec\) can be set to limit the execution time of the loader.

Future versions of this loader can:     

  * Support additional Alchemy APIs \(e.g. getTransactions, etc.\)

  * Support additional blockchain APIs \(e.g. Infura, Opensea, etc.\)

Parameters:     

  * **contract\_address** \(_str_\) – The address of the smart contract.

  * **blockchainType** \([_BlockchainType_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blockchain.BlockchainType.html#langchain_community.document_loaders.blockchain.BlockchainType "langchain_community.document_loaders.blockchain.BlockchainType")\) – The blockchain type.

  * **api\_key** \(_str_\) – The Alchemy API key.

  * **startToken** \(_str_\) – The start token for pagination.

  * **get\_all\_tokens** \(_bool_\) – Whether to get all tokens on the contract.

  * **max\_execution\_time** \(_int_ _|__None_\) – The maximum execution time \(sec\).

Methods

`__init__`\(contract\_address\[, blockchainType, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `lazy_load`\(\) | A lazy loader for Documents.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      \_\_init\_\_\(

    _contract\_address : str_,     _blockchainType : [BlockchainType](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blockchain.BlockchainType.html#langchain_community.document_loaders.blockchain.BlockchainType "langchain_community.document_loaders.blockchain.BlockchainType") = BlockchainType.ETH\_MAINNET_,     _api\_key : str = 'docs-demo'_,     _startToken : str = ''_,     _get\_all\_tokens : bool = False_,     _max\_execution\_time : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blockchain.html#BlockchainDocumentLoader.__init__)\#     

Parameters:     

  * **contract\_address** \(_str_\) – The address of the smart contract.

  * **blockchainType** \([_BlockchainType_](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.blockchain.BlockchainType.html#langchain_community.document_loaders.blockchain.BlockchainType "langchain_community.document_loaders.blockchain.BlockchainType")\) – The blockchain type.

  * **api\_key** \(_str_\) – The Alchemy API key.

  * **startToken** \(_str_\) – The start token for pagination.

  * **get\_all\_tokens** \(_bool_\) – Whether to get all tokens on the contract.

  * **max\_execution\_time** \(_int_ _|__None_\) – The maximum execution time \(sec\).

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

load\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/blockchain.html#BlockchainDocumentLoader.load)\#     

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

Examples using BlockchainDocumentLoader

  * [Alchemy](https://python.langchain.com/docs/integrations/providers/alchemy/)

  * [Blockchain](https://python.langchain.com/docs/integrations/document_loaders/blockchain/)

__On this page