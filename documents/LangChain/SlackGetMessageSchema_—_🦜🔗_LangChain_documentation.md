# SlackGetMessageSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.slack.get_message.SlackGetMessageSchema.html
**Word Count:** 53
**Links Count:** 409
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# SlackGetMessageSchema\#

_class _langchain\_community.tools.slack.get\_message.SlackGetMessageSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/slack/get_message.html#SlackGetMessageSchema)\#     

Bases: `BaseModel`

Input schema for SlackGetMessages.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _channel\_id _: str_ _\[Required\]_\#     

The channel id, private group, or IM channel to send message to.

__On this page