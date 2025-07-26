# SendMessageSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.slack.send_message.SendMessageSchema.html
**Word Count:** 55
**Links Count:** 411
**Scraped:** 2025-07-21 08:20:13
**Status:** completed

---

# SendMessageSchema\#

_class _langchain\_community.tools.slack.send\_message.SendMessageSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/slack/send_message.html#SendMessageSchema)\#     

Bases: `BaseModel`

Input for SendMessageTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _channel _: str_ _\[Required\]_\#     

The channel, private group, or IM channel to send message to.

_param _message _: str_ _\[Required\]_\#     

The message to be sent.

__On this page