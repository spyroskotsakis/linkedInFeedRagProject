# App — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.App.html
**Word Count:** 73
**Links Count:** 268
**Scraped:** 2025-07-21 08:05:36
**Status:** completed

---

# App\#

_class _langchain\_community.utilities.pebblo.App[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#App)\#     

Bases: `BaseModel`

Pebblo AI application.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _client\_version _: [Framework](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.Framework.html#langchain_community.utilities.pebblo.Framework "langchain_community.utilities.pebblo.Framework")_ _\[Required\]_\#     

Client version used for the app.

_param _description _: str | None_ _\[Required\]_\#     

Description of the app.

_param _framework _: [Framework](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.Framework.html#langchain_community.utilities.pebblo.Framework "langchain_community.utilities.pebblo.Framework")_ _\[Required\]_\#     

Framework details of the app.

_param _load\_id _: str_ _\[Required\]_\#     

Unique load\_id of the app instance.

_param _name _: str_ _\[Required\]_\#     

Name of the app.

_param _owner _: str_ _\[Required\]_\#     

Owner of the app.

_param _plugin\_version _: str_ _\[Required\]_\#     

Plugin version used for the app.

_param _runtime _: [Runtime](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.Runtime.html#langchain_community.utilities.pebblo.Runtime "langchain_community.utilities.pebblo.Runtime")_ _\[Required\]_\#     

Runtime details of the app.

__On this page