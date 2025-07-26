# SearchEmailsInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.office365.messages_search.SearchEmailsInput.html
**Word Count:** 136
**Links Count:** 415
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# SearchEmailsInput\#

_class _langchain\_community.tools.office365.messages\_search.SearchEmailsInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/office365/messages_search.html#SearchEmailsInput)\#     

Bases: `BaseModel`

Input for SearchEmails Tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _folder _: str_ _ = ''_\#     

If the user wants to search in only one folder, the name of the folder. Default folders are “inbox”, “drafts”, “sent items”, “deleted ttems”, but users can search custom folders as well.

_param _max\_results _: int_ _ = 10_\#     

The maximum number of results to return.

_param _query _: str_ _\[Required\]_\#     

The Microsoift Graph v1.0 $search query. Example filters include from:sender, from:sender, to:recipient, subject:subject, recipients:list\_of\_recipients, body:excitement, importance:high, received>2022-12-01, received<2021-12-01, sent>2022-12-01, sent<2021-12-01, hasAttachments:true attachment:api-catalog.md, cc:samanthab@contoso.com, bcc:samanthab@contoso.com, body:excitement date range example: received:2023-06-08..2023-06-09 matching example: from:amy OR from:david.

_param _truncate _: bool_ _ = True_\#     

Whether the email body is truncated to meet token number limits. Set to False for searches that will retrieve small messages, otherwise, set to True

__On this page