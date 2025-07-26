# DALMFilter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.DALMFilter.html
**Word Count:** 185
**Links Count:** 256
**Scraped:** 2025-07-21 08:11:12
**Status:** completed

---

# DALMFilter\#

_class _langchain\_community.utilities.arcee.DALMFilter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/arcee.html#DALMFilter)\#     

Bases: `BaseModel`

Filters available for a DALM retrieval and generation.

Parameters:     

  * **field\_name** – The field to filter on. Can be ‘document’ or ‘name’ to filter on your document’s raw text or title. Any other field will be presumed to be a metadata field you included when uploading your context data

  * **filter\_type** – Currently ‘fuzzy\_search’ and ‘strict\_search’ are supported. ‘fuzzy\_search’ means a fuzzy search on the provided field is performed. The exact strict doesn’t need to exist in the document for this to find a match. Very useful for scanning a document for some keyword terms. ‘strict\_search’ means that the exact string must appear in the provided field. This is NOT an exact eq filter. ie a document with content “the happy dog crossed the street” will match on a strict\_search of “dog” but won’t match on “the dog”. Python equivalent of return search\_string in full\_string.

  * **value** – The actual value to search for in the context data/metadata

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _field\_name _: str_ _\[Required\]_\#     

_param _filter\_type _: [DALMFilterType](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.arcee.DALMFilterType.html#langchain_community.utilities.arcee.DALMFilterType "langchain_community.utilities.arcee.DALMFilterType")_ _\[Required\]_\#     

_param _value _: str_ _\[Required\]_\#     

__On this page