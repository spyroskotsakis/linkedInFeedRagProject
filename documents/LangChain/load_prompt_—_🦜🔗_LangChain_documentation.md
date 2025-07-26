# load_prompt — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.loading.load_prompt.html
**Word Count:** 43
**Links Count:** 130
**Scraped:** 2025-07-21 07:54:29
**Status:** completed

---

# load\_prompt\#

langchain\_core.prompts.loading.load\_prompt\(

    _path : str | Path_,     _encoding : str | None = None_, \) → [BasePromptTemplate](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/loading.html#load_prompt)\#     

Unified method for loading a prompt from LangChainHub or local fs.

Parameters:     

  * **path** \(_str_ _|__Path_\) – Path to the prompt file.

  * **encoding** \(_str_ _|__None_\) – Encoding of the file. Defaults to None.

Returns:     

A PromptTemplate object.

Raises:     

**RuntimeError** – If the path is a Lang Chain Hub path.

Return type:     

[_BasePromptTemplate_](https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.base.BasePromptTemplate.html#langchain_core.prompts.base.BasePromptTemplate "langchain_core.prompts.base.BasePromptTemplate")

__On this page