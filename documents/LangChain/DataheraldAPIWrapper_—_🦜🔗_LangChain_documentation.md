# DataheraldAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.dataherald.DataheraldAPIWrapper.html
**Word Count:** 71
**Links Count:** 257
**Scraped:** 2025-07-21 08:03:18
**Status:** completed

---

# DataheraldAPIWrapper\#

_class _langchain\_community.utilities.dataherald.DataheraldAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dataherald.html#DataheraldAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Dataherald.

Docs for using:

  1. Go to dataherald and sign up

  2. Create an API key

  3. Save your API key into DATAHERALD\_API\_KEY env variable

  4. pip install dataherald

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _dataherald\_api\_key _: str | None_ _ = None_\#     

_param _db\_connection\_id _: str_ _\[Required\]_\#     

run\(_prompt : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/dataherald.html#DataheraldAPIWrapper.run)\#     

Generate a sql query through Dataherald and parse result.

Parameters:     

**prompt** \(_str_\)

Return type:     

str

Examples using DataheraldAPIWrapper

  * [Dataherald](https://python.langchain.com/docs/integrations/providers/dataherald/)

__On this page