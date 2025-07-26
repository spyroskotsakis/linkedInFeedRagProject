# generate_size_based_batches — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.generate_size_based_batches.html
**Word Count:** 39
**Links Count:** 253
**Scraped:** 2025-07-21 08:02:07
**Status:** completed

---

# generate\_size\_based\_batches\#

langchain\_community.utilities.pebblo.generate\_size\_based\_batches\(

    _docs : List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _max\_batch\_size : int = 102400_, \) → List\[List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#generate_size_based_batches)\#     

Generate batches of documents based on page\_content size. :param docs: List of documents to be batched. :param max\_batch\_size: Maximum size of each batch in bytes. Defaults to 100\*1024\(100KB\)

Returns:     

List of batches of documents

Return type:     

List\[List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\]

Parameters:     

  * **docs** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **max\_batch\_size** \(_int_\)

__On this page