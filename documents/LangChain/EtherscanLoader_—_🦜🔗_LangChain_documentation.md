# EtherscanLoader — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.etherscan.EtherscanLoader.html
**Word Count:** 113
**Links Count:** 454
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# EtherscanLoader\#

_class _langchain\_community.document\_loaders.etherscan.EtherscanLoader\(

    _account\_address : str_,     _api\_key : str = 'docs-demo'_,     _filter : str = 'normal\_transaction'_,     _page : int = 1_,     _offset : int = 10_,     _start\_block : int = 0_,     _end\_block : int = 99999999_,     _sort : str = 'desc'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/etherscan.html#EtherscanLoader)\#     

Load transactions from Ethereum mainnet.

The Loader use Etherscan API to interact with Ethereum mainnet.

ETHERSCAN\_API\_KEY environment variable must be set use this loader.

Methods

`__init__`\(account\_address\[, api\_key, filter, ...\]\) |    ---|---   `alazy_load`\(\) | A lazy loader for Documents.   `aload`\(\) | Load data into Document objects.   `getERC1155Tx`\(\) |    `getERC20Tx`\(\) |    `getERC721Tx`\(\) |    `getEthBalance`\(\) |    `getInternalTx`\(\) |    `getNormTx`\(\) |    `lazy_load`\(\) | Lazy load Documents from table.   `load`\(\) | Load data into Document objects.   `load_and_split`\(\[text\_splitter\]\) | Load Documents and split into chunks.      Parameters:     

  * **account\_address** \(_str_\)

  * **api\_key** \(_str_\)

  * **filter** \(_str_\)

  * **page** \(_int_\)

  * **offset** \(_int_\)

  * **start\_block** \(_int_\)

  * **end\_block** \(_int_\)

  * **sort** \(_str_\)

\_\_init\_\_\(

    _account\_address : str_,     _api\_key : str = 'docs-demo'_,     _filter : str = 'normal\_transaction'_,     _page : int = 1_,     _offset : int = 10_,     _start\_block : int = 0_,     _end\_block : int = 99999999_,     _sort : str = 'desc'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/etherscan.html#EtherscanLoader.__init__)\#     

Parameters:     

  * **account\_address** \(_str_\)

  * **api\_key** \(_str_\)

  * **filter** \(_str_\)

  * **page** \(_int_\)

  * **offset** \(_int_\)

  * **start\_block** \(_int_\)

  * **end\_block** \(_int_\)

  * **sort** \(_str_\)

_async _alazy\_load\(\) → AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

A lazy loader for Documents.

Return type:     

AsyncIterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

_async _aload\(\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Load data into Document objects.

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

getERC1155Tx\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/etherscan.html#EtherscanLoader.getERC1155Tx)\#     

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

getERC20Tx\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/etherscan.html#EtherscanLoader.getERC20Tx)\#     

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

getERC721Tx\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/etherscan.html#EtherscanLoader.getERC721Tx)\#     

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

getEthBalance\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/etherscan.html#EtherscanLoader.getEthBalance)\#     

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

getInternalTx\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/etherscan.html#EtherscanLoader.getInternalTx)\#     

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

getNormTx\(\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/etherscan.html#EtherscanLoader.getNormTx)\#     

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

lazy\_load\(\) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/etherscan.html#EtherscanLoader.lazy_load)\#     

Lazy load Documents from table.

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

Examples using EtherscanLoader

  * [Etherscan](https://python.langchain.com/docs/integrations/document_loaders/etherscan/)

__On this page