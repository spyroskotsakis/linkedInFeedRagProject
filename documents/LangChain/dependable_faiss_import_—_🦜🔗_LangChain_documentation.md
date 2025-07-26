# dependable_faiss_import — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.faiss.dependable_faiss_import.html
**Word Count:** 50
**Links Count:** 316
**Scraped:** 2025-07-21 08:16:18
**Status:** completed

---

# dependable\_faiss\_import\#

langchain\_community.vectorstores.faiss.dependable\_faiss\_import\(

    _no\_avx2 : bool | None = None_, \) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/faiss.html#dependable_faiss_import)\#     

Import faiss if available, otherwise raise error. If FAISS\_NO\_AVX2 environment variable is set, it will be considered to load FAISS with no AVX2 optimization.

Parameters:     

**no\_avx2** \(_bool_ _|__None_\) – Load FAISS strictly with no AVX2 optimization so that the vectorstore is portable and compatible with other devices.

Return type:     

_Any_

__On this page