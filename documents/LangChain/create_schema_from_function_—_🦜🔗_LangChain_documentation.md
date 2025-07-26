# create_schema_from_function — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.create_schema_from_function.html
**Word Count:** 107
**Links Count:** 116
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# create\_schema\_from\_function\#

langchain\_core.tools.base.create\_schema\_from\_function\(

    _model\_name : str_,     _func : Callable_,     _\*_ ,     _filter\_args : Sequence\[str\] | None = None_,     _parse\_docstring : bool = False_,     _error\_on\_invalid\_docstring : bool = False_,     _include\_injected : bool = True_, \) → type\[[BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/tools/base.html#create_schema_from_function)\#     

Create a pydantic schema from a function’s signature.

Parameters:     

  * **model\_name** \(_str_\) – Name to assign to the generated pydantic schema.

  * **func** \(_Callable_\) – Function to generate the schema from.

  * **filter\_args** \(_Optional_ _\[__Sequence_ _\[__str_ _\]__\]_\) – Optional list of arguments to exclude from the schema. Defaults to FILTERED\_ARGS.

  * **parse\_docstring** \(_bool_\) – Whether to parse the function’s docstring for descriptions for each argument. Defaults to False.

  * **error\_on\_invalid\_docstring** \(_bool_\) – if `parse_docstring` is provided, configure whether to raise ValueError on invalid Google Style docstrings. Defaults to False.

  * **include\_injected** \(_bool_\) – Whether to include injected arguments in the schema. Defaults to True, since we want to include them in the schema when _validating_ tool inputs.

Returns:     

A pydantic model with the same arguments as the function.

Return type:     

type\[[BaseModel](https://python.langchain.com/api_reference/experimental/video_captioning/langchain_experimental.video_captioning.models.BaseModel.html#langchain_experimental.video_captioning.models.BaseModel "langchain_experimental.video_captioning.models.BaseModel")\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)