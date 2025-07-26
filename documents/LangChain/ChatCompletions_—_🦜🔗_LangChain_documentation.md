# ChatCompletions — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.ChatCompletions.html
**Word Count:** 40
**Links Count:** 113
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# ChatCompletions\#

_class _langchain\_community.adapters.openai.ChatCompletions[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#ChatCompletions)\#     

Bases: [`IndexableBaseModel`](https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.IndexableBaseModel.html#langchain_community.adapters.openai.IndexableBaseModel "langchain_community.adapters.openai.IndexableBaseModel")

Chat completions.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _choices _: List\[[Choice](https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.Choice.html#langchain_community.adapters.openai.Choice "langchain_community.adapters.openai.Choice")\]__\[Required\]_\#     

__On this page