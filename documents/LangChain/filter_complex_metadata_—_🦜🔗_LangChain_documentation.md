# filter_complex_metadata — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/utilities/langchain_aws.utilities.utils.filter_complex_metadata.html
**Word Count:** 19
**Links Count:** 90
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# filter\_complex\_metadata\#

langchain\_aws.utilities.utils.filter\_complex\_metadata\(_documents: ~typing.List\[~langchain\_core.documents.base.Document\], \*, allowed\_types: ~typing.Tuple\[~typing.Type, ...\] = \(<class 'str'>, <class 'bool'>, <class 'int'>, <class 'float'>\)_\) → List\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/utilities/utils.html#filter_complex_metadata)\#     

Filter out metadata types that are not supported for a vector store.

Parameters:     

  * **documents** \(_List_ _\[_[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document") _\]_\)

  * **allowed\_types** \(_Tuple_ _\[__Type_ _,__...__\]_\)

Return type:     

_List_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

__On this page