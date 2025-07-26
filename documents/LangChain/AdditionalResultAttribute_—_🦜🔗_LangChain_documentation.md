# AdditionalResultAttribute — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.AdditionalResultAttribute.html
**Word Count:** 54
**Links Count:** 108
**Scraped:** 2025-07-21 08:44:55
**Status:** completed

---

# AdditionalResultAttribute\#

_class _langchain\_aws.retrievers.kendra.AdditionalResultAttribute[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#AdditionalResultAttribute)\#     

Bases: `BaseModel`

Additional result attribute.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _Key _: str_ _\[Required\]_\#     

The key of the attribute.

_param _Value _: [AdditionalResultAttributeValue](https://python.langchain.com/api_reference/aws/retrievers/langchain_aws.retrievers.kendra.AdditionalResultAttributeValue.html#langchain_aws.retrievers.kendra.AdditionalResultAttributeValue "langchain_aws.retrievers.kendra.AdditionalResultAttributeValue")_ _\[Required\]_\#     

The value of the attribute.

_param _ValueType _: Literal\['TEXT\_WITH\_HIGHLIGHTS\_VALUE'\]__\[Required\]_\#     

The type of the value.

get\_value\_text\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/retrievers/kendra.html#AdditionalResultAttribute.get_value_text)\#     

Return type:     

str

__On this page