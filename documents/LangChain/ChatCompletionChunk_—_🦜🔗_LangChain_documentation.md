# ChatCompletionChunk — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.ChatCompletionChunk.html
**Word Count:** 41
**Links Count:** 113
**Scraped:** 2025-07-21 08:11:39
**Status:** completed

---

# ChatCompletionChunk\#

_class _langchain\_community.adapters.openai.ChatCompletionChunk[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/adapters/openai.html#ChatCompletionChunk)\#     

Bases: [`IndexableBaseModel`](https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.IndexableBaseModel.html#langchain_community.adapters.openai.IndexableBaseModel "langchain_community.adapters.openai.IndexableBaseModel")

Chat completion chunk.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _choices _: List\[[ChoiceChunk](https://python.langchain.com/api_reference/community/adapters/langchain_community.adapters.openai.ChoiceChunk.html#langchain_community.adapters.openai.ChoiceChunk "langchain_community.adapters.openai.ChoiceChunk")\]__\[Required\]_\#     

__On this page