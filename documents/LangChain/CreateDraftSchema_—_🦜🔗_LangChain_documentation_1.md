# CreateDraftSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/google_community/gmail/langchain_google_community.gmail.create_draft.CreateDraftSchema.html
**Word Count:** 62
**Links Count:** 114
**Scraped:** 2025-07-21 07:59:27
**Status:** completed

---

# CreateDraftSchema\#

_class _langchain\_google\_community.gmail.create\_draft.CreateDraftSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_google_community/gmail/create_draft.html#CreateDraftSchema)\#     

Bases: `BaseModel`

Input for CreateDraftTool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _bcc _: List\[str\] | None_ _ = None_\#     

The list of BCC recipients.

_param _cc _: List\[str\] | None_ _ = None_\#     

The list of CC recipients.

_param _message _: str_ _\[Required\]_\#     

The message to include in the draft.

_param _subject _: str_ _\[Required\]_\#     

The subject of the message.

_param _to _: List\[str\]__\[Required\]_\#     

The list of recipients.

__On this page