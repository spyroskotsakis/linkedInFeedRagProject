# KineticaSqlResponse — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chat_models/langchain_community.chat_models.kinetica.KineticaSqlResponse.html
**Word Count:** 80
**Links Count:** 232
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# KineticaSqlResponse\#

_class _langchain\_community.chat\_models.kinetica.KineticaSqlResponse[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chat_models/kinetica.html#KineticaSqlResponse)\#     

Bases: `BaseModel`

Response containing SQL and the fetched data.

This object is returned by a chain with `KineticaSqlOutputParser` and it contains the generated SQL and related Pandas Dataframe fetched from the database.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _dataframe _: Any_ _ = None_\#     

The Pandas dataframe containing the fetched data.

_param _sql _: str_ _ = ''_\#     

The generated SQL.

Examples using KineticaSqlResponse

  * [Kinetica Language To SQL Chat Model](https://python.langchain.com/docs/integrations/chat/kinetica/)

__On this page