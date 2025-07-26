# InputType — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.conversational_retrieval.base.InputType.html
**Word Count:** 51
**Links Count:** 192
**Scraped:** 2025-07-21 07:49:32
**Status:** completed

---

# InputType\#

_class _langchain.chains.conversational\_retrieval.base.InputType[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/conversational_retrieval/base.html#InputType)\#     

Bases: `BaseModel`

Input type for ConversationalRetrievalChain.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _chat\_history _: list\[CHAT\_TURN\_TYPE\]__\[Optional\]_\#     

The chat history to use for retrieval.

_param _question _: str_ _\[Required\]_\#     

The question to answer.

__On this page