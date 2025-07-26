# CreateDraftMessageSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.office365.create_draft_message.CreateDraftMessageSchema.html
**Word Count:** 63
**Links Count:** 417
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# CreateDraftMessageSchema\#

_class _langchain\_community.tools.office365.create\_draft\_message.CreateDraftMessageSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/office365/create_draft_message.html#CreateDraftMessageSchema)\#     

Bases: `BaseModel`

Input for SendMessageTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _bcc _: List\[str\] | None_ _ = None_\#     

The list of BCC recipients.

_param _body _: str_ _\[Required\]_\#     

The message body to include in the draft.

_param _cc _: List\[str\] | None_ _ = None_\#     

The list of CC recipients.

_param _subject _: str_ _\[Required\]_\#     

The subject of the message.

_param _to _: List\[str\]__\[Required\]_\#     

The list of recipients.

__On this page