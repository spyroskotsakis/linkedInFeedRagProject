# InMemoryDBModel — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBModel.html
**Word Count:** 46
**Links Count:** 146
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# InMemoryDBModel\#

_class _langchain\_aws.vectorstores.inmemorydb.schema.InMemoryDBModel[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#InMemoryDBModel)\#     

Bases: `BaseModel`

Schema for MemoryDB index.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _content\_key _: str_ _ = 'content'_\#     

_param _content\_vector\_key _: str_ _ = 'content\_vector'_\#     

_param _extra _: List\[[InMemoryDBField](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField")\] | None_ _ = None_\#     

_param _numeric _: List\[[NumericFieldSchema](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.NumericFieldSchema.html#langchain_aws.vectorstores.inmemorydb.schema.NumericFieldSchema "langchain_aws.vectorstores.inmemorydb.schema.NumericFieldSchema")\] | None_ _ = None_\#     

_param _tag _: List\[[TagFieldSchema](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.TagFieldSchema.html#langchain_aws.vectorstores.inmemorydb.schema.TagFieldSchema "langchain_aws.vectorstores.inmemorydb.schema.TagFieldSchema")\] | None_ _ = None_\#     

_param _text _: List\[[TextFieldSchema](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.TextFieldSchema.html#langchain_aws.vectorstores.inmemorydb.schema.TextFieldSchema "langchain_aws.vectorstores.inmemorydb.schema.TextFieldSchema")\]__ = \[TextFieldSchema\(name='content', weight=1, no\_stem=False, phonetic\_matcher=None, withsuffixtrie=False, no\_index=False, sortable=False\)\]_\#     

_param _vector _: List\[[FlatVectorField](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.FlatVectorField.html#langchain_aws.vectorstores.inmemorydb.schema.FlatVectorField "langchain_aws.vectorstores.inmemorydb.schema.FlatVectorField") | [HNSWVectorField](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.HNSWVectorField.html#langchain_aws.vectorstores.inmemorydb.schema.HNSWVectorField "langchain_aws.vectorstores.inmemorydb.schema.HNSWVectorField")\] | None_ _ = None_\#     

add\_content\_field\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#InMemoryDBModel.add_content_field)\#     

Return type:     

None

add\_vector\_field\(

    _vector\_field : Dict\[str, Any\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#InMemoryDBModel.add_vector_field)\#     

Parameters:     

**vector\_field** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

None

as\_dict\(\) → Dict\[str, List\[Any\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#InMemoryDBModel.as_dict)\#     

Return type:     

_Dict_\[str, _List_\[_Any_\]\]

get\_fields\(\) → List\[[InMemoryDBField](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/vectorstores/inmemorydb/schema.html#InMemoryDBModel.get_fields)\#     

Return type:     

_List_\[[_InMemoryDBField_](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField.html#langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField "langchain_aws.vectorstores.inmemorydb.schema.InMemoryDBField")\]

_property _content\_vector _: [FlatVectorField](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.FlatVectorField.html#langchain_aws.vectorstores.inmemorydb.schema.FlatVectorField "langchain_aws.vectorstores.inmemorydb.schema.FlatVectorField") | [HNSWVectorField](https://python.langchain.com/api_reference/aws/vectorstores/langchain_aws.vectorstores.inmemorydb.schema.HNSWVectorField.html#langchain_aws.vectorstores.inmemorydb.schema.HNSWVectorField "langchain_aws.vectorstores.inmemorydb.schema.HNSWVectorField")_\#     

_property _is\_empty _: bool_\#     

_property _metadata\_keys _: List\[str\]_\#     

_property _vector\_dtype _: dtype_\#     

__On this page