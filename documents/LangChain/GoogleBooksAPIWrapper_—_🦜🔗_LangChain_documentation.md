# GoogleBooksAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.google_books.GoogleBooksAPIWrapper.html
**Word Count:** 101
**Links Count:** 256
**Scraped:** 2025-07-21 08:05:00
**Status:** completed

---

# GoogleBooksAPIWrapper\#

_class _langchain\_community.utilities.google\_books.GoogleBooksAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_books.html#GoogleBooksAPIWrapper)\#     

Bases: `BaseModel`

Wrapper around Google Books API.

To use, you should have a Google Books API key available. This wrapper will use the Google Books API to conduct searches and fetch books based on a query passed in by the agents. By default, it will return the top-k results.

The response for each book will contain the book title, author name, summary, and a source link.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _google\_books\_api\_key _: str | None_ _ = None_\#     

_param _top\_k\_results _: int_ _ = 5_\#     

run\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/google_books.html#GoogleBooksAPIWrapper.run)\#     

Parameters:     

**query** \(_str_\)

Return type:     

str

__On this page