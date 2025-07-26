# docstore — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/docstore.html
**Word Count:** 49
**Links Count:** 102
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# `docstore`\#

**Docstores** are classes to store and load Documents.

The **Docstore** is a simplified version of the Document Loader.

**Class hierarchy:**               Docstore --> <name> # Examples: InMemoryDocstore, Wikipedia     

**Main helpers:**               Document, AddableMixin     

**Classes**

[`docstore.arbitrary_fn.DocstoreFn`](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.arbitrary_fn.DocstoreFn.html#langchain_community.docstore.arbitrary_fn.DocstoreFn "langchain_community.docstore.arbitrary_fn.DocstoreFn")\(lookup\_fn\) | Docstore via arbitrary lookup function.   ---|---   [`docstore.base.AddableMixin`](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.AddableMixin.html#langchain_community.docstore.base.AddableMixin "langchain_community.docstore.base.AddableMixin")\(\) | Mixin class that supports adding texts.   [`docstore.base.Docstore`](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.base.Docstore.html#langchain_community.docstore.base.Docstore "langchain_community.docstore.base.Docstore")\(\) | Interface to access to place that stores documents.   [`docstore.in_memory.InMemoryDocstore`](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.in_memory.InMemoryDocstore.html#langchain_community.docstore.in_memory.InMemoryDocstore "langchain_community.docstore.in_memory.InMemoryDocstore")\(\[\_dict\]\) | Simple in memory docstore in the form of a dict.   [`docstore.wikipedia.Wikipedia`](https://python.langchain.com/api_reference/community/docstore/langchain_community.docstore.wikipedia.Wikipedia.html#langchain_community.docstore.wikipedia.Wikipedia "langchain_community.docstore.wikipedia.Wikipedia")\(\) | Wikipedia API.