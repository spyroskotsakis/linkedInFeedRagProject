# BaseVectorStoreTool — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.vectorstore.tool.BaseVectorStoreTool.html
**Word Count:** 46
**Links Count:** 413
**Scraped:** 2025-07-21 08:06:11
**Status:** completed

---

# BaseVectorStoreTool\#

_class _langchain\_community.tools.vectorstore.tool.BaseVectorStoreTool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/vectorstore/tool.html#BaseVectorStoreTool)\#     

Bases: `BaseModel`

Base class for tools that use a VectorStore.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _llm _: [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_ _\[Optional\]_\#     

_param _vectorstore _: [VectorStore](https://python.langchain.com/api_reference/core/vectorstores/langchain_core.vectorstores.base.VectorStore.html#langchain_core.vectorstores.base.VectorStore "langchain_core.vectorstores.base.VectorStore")_ _\[Required\]_\#     

__On this page