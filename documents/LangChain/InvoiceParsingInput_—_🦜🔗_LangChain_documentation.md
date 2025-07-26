# InvoiceParsingInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.edenai.ocr_invoiceparser.InvoiceParsingInput.html
**Word Count:** 44
**Links Count:** 409
**Scraped:** 2025-07-21 08:15:47
**Status:** completed

---

# InvoiceParsingInput\#

_class _langchain\_community.tools.edenai.ocr\_invoiceparser.InvoiceParsingInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/edenai/ocr_invoiceparser.html#InvoiceParsingInput)\#     

Bases: `BaseModel`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _query _: HttpUrl_ _\[Required\]_\#     

url of the document to parse

__On this page