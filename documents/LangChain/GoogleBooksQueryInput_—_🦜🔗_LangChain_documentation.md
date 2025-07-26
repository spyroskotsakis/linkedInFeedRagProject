# GoogleBooksQueryInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.google_books.GoogleBooksQueryInput.html
**Word Count:** 49
**Links Count:** 409
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# GoogleBooksQueryInput\#

_class _langchain\_community.tools.google\_books.GoogleBooksQueryInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/google_books.html#GoogleBooksQueryInput)\#     

Bases: `BaseModel`

Input for the GoogleBooksQuery tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: str_ _\[Required\]_\#     

query to look up on google books

__On this page