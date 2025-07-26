# RivaAuthMixin — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.nvidia_riva.RivaAuthMixin.html
**Word Count:** 74
**Links Count:** 255
**Scraped:** 2025-07-21 08:10:17
**Status:** completed

---

# RivaAuthMixin\#

_class _langchain\_community.utilities.nvidia\_riva.RivaAuthMixin[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/nvidia_riva.html#RivaAuthMixin)\#     

Bases: `BaseModel`

Configuration for the authentication to a Riva service connection.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _ssl\_cert _: str | None_ _ = None_\#     

A full path to the file where Riva’s public ssl key can be read.

_param _url _: AnyHttpUrl | str_ _ = AnyHttpUrl\('http://localhost:50051/'\)_\#     

The full URL where the Riva service can be found.

_property _auth _: riva.client.Auth_\#     

Return a riva client auth object.

__On this page