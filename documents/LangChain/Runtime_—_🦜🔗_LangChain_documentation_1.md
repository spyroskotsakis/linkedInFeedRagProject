# Runtime — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.Runtime.html
**Word Count:** 74
**Links Count:** 269
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# Runtime\#

_class _langchain\_community.utilities.pebblo.Runtime[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#Runtime)\#     

Bases: `BaseModel`

Pebblo Runtime.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _host _: str_ _\[Required\]_\#     

Host name of the runtime.

_param _ip _: str | None_ _ = ''_\#     

IP address of the runtime. Defaults to ‘’.

_param _language _: str_ _\[Required\]_\#     

Runtime kernel.

_param _language\_version _: str_ _\[Required\]_\#     

Version of the runtime kernel.

_param _os _: str_ _\[Required\]_\#     

OS name.

_param _os\_version _: str_ _\[Required\]_\#     

OS version.

_param _path _: str_ _\[Required\]_\#     

Current working directory path.

_param _platform _: str_ _\[Required\]_\#     

Platform details of the runtime.

_param _runtime _: str_ _ = 'local'_\#     

More runtime details. Defaults to ‘local’.

_param _type _: str_ _ = 'local'_\#     

Runtime type. Defaults to ‘local’.

__On this page