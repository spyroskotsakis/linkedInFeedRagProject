# BM25BuiltInFunction — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/milvus/function/langchain_milvus.function.BM25BuiltInFunction.html
**Word Count:** 117
**Links Count:** 84
**Scraped:** 2025-07-21 08:26:28
**Status:** completed

---

# BM25BuiltInFunction\#

_class _langchain\_milvus.function.BM25BuiltInFunction\(

    _\*_ ,     _input\_field\_names : str = 'text'_,     _output\_field\_names : str = 'sparse'_,     _analyzer\_params : Dict\[Any, Any\] | None = None_,     _enable\_match : bool = False_,     _function\_name : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/function.html#BM25BuiltInFunction)\#     

Milvus BM25 built-in function.

See: <https://milvus.io/docs/full-text-search.md>

Parameters:     

  * **input\_field\_names** \(_str_\) – The name of the input field, default is ‘text’.

  * **output\_field\_names** \(_str_\) – The name of the output field, default is ‘sparse’.

  * **analyzer\_params** \(_Optional_ _\[__Dict_ _\[__Any_ _,__Any_ _\]__\]_\) – The parameters for the analyzer. Default is None. See: <https://milvus.io/docs/analyzer-overview.md#Analyzer-Overview>

  * **enable\_match** \(_bool_\) – Whether to enable match.

  * **function\_name** \(_Optional_ _\[__str_ _\]_\) – The name of the function. Default is None, which means a random name will be generated.

Attributes

`function` |    ---|---   `input_field_names` |    `output_field_names` |    `type` |       Methods

`__init__`\(\*\[, input\_field\_names, ...\]\) |    ---|---   `get_input_field_schema_kwargs`\(\) |       \_\_init\_\_\(

    _\*_ ,     _input\_field\_names : str = 'text'_,     _output\_field\_names : str = 'sparse'_,     _analyzer\_params : Dict\[Any, Any\] | None = None_,     _enable\_match : bool = False_,     _function\_name : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/function.html#BM25BuiltInFunction.__init__)\#     

Parameters:     

  * **input\_field\_names** \(_str_\) – The name of the input field, default is ‘text’.

  * **output\_field\_names** \(_str_\) – The name of the output field, default is ‘sparse’.

  * **analyzer\_params** \(_Optional_ _\[__Dict_ _\[__Any_ _,__Any_ _\]__\]_\) – The parameters for the analyzer. Default is None. See: <https://milvus.io/docs/analyzer-overview.md#Analyzer-Overview>

  * **enable\_match** \(_bool_\) – Whether to enable match.

  * **function\_name** \(_Optional_ _\[__str_ _\]_\) – The name of the function. Default is None, which means a random name will be generated.

get\_input\_field\_schema\_kwargs\(\) → dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_milvus/function.html#BM25BuiltInFunction.get_input_field_schema_kwargs)\#     

Return type:     

dict

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)