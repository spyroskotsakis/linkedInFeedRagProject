# Doc — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.pebblo.Doc.html
**Word Count:** 88
**Links Count:** 269
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# Doc\#

_class _langchain\_community.utilities.pebblo.Doc[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/pebblo.html#Doc)\#     

Bases: `BaseModel`

Pebblo document.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _anonymize\_snippets _: bool_ _\[Required\]_\#     

Whether to anonymize snippets going into VectorDB and the generated reports

_param _classifier\_location _: str_ _\[Required\]_\#     

Location of the classifier.

_param _docs _: list_ _\[Required\]_\#     

List of documents with its metadata.

_param _load\_id _: str_ _\[Required\]_\#     

Unique load\_id of the app instance.

_param _loader\_details _: dict_ _\[Required\]_\#     

Loader details with its metadata.

_param _loading\_end _: bool_ _\[Required\]_\#     

Boolean, specifying end of loading of source.

_param _name _: str_ _\[Required\]_\#     

Name of app originating this document.

_param _owner _: str_ _\[Required\]_\#     

Owner of app.

_param _plugin\_version _: str_ _\[Required\]_\#     

Pebblo plugin Version

_param _source\_owner _: str_ _\[Required\]_\#     

Owner of the source of the loader.

__On this page