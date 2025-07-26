# YouAPIOutput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouAPIOutput.html
**Word Count:** 48
**Links Count:** 252
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# YouAPIOutput\#

_class _langchain\_community.utilities.you.YouAPIOutput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/you.html#YouAPIOutput)\#     

Bases: `BaseModel`

Output from you.com API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _hits _: List\[[YouHit](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.you.YouHit.html#langchain_community.utilities.you.YouHit "langchain_community.utilities.you.YouHit")\]__\[Required\]_\#     

A list of dictionaries containing the results

__On this page