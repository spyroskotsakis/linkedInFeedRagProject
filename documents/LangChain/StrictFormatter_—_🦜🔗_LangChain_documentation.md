# StrictFormatter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.formatting.StrictFormatter.html
**Word Count:** 95
**Links Count:** 195
**Scraped:** 2025-07-21 07:56:55
**Status:** completed

---

# StrictFormatter\#

_class _langchain\_core.utils.formatting.StrictFormatter[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/formatting.html#StrictFormatter)\#     

Formatter that checks for extra keys.

Methods

`check_unused_args`\(used\_args, args, kwargs\) |    ---|---   `convert_field`\(value, conversion\) |    `format`\(format\_string, /, \*args, \*\*kwargs\) |    `format_field`\(value, format\_spec\) |    `get_field`\(field\_name, args, kwargs\) |    `get_value`\(key, args, kwargs\) |    `parse`\(format\_string\) |    `validate_input_variables`\(format\_string, ...\) | Check that all input variables are used in the format string.   `vformat`\(format\_string, args, kwargs\) | Check that no arguments are provided.      check\_unused\_args\(_used\_args_ , _args_ , _kwargs_\)\#     

convert\_field\(_value_ , _conversion_\)\#     

format\(_format\_string_ , _/_ , _\* args_, _\*\* kwargs_\)\#     

format\_field\(_value_ , _format\_spec_\)\#     

get\_field\(_field\_name_ , _args_ , _kwargs_\)\#     

get\_value\(_key_ , _args_ , _kwargs_\)\#     

parse\(_format\_string_\)\#     

validate\_input\_variables\(

    _format\_string : str_,     _input\_variables : list\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/formatting.html#StrictFormatter.validate_input_variables)\#     

Check that all input variables are used in the format string.

Parameters:     

  * **format\_string** \(_str_\) – The format string.

  * **input\_variables** \(_list_ _\[__str_ _\]_\) – The input variables.

Raises:     

**ValueError** – If any input variables are not used in the format string.

Return type:     

None

vformat\(

    _format\_string : str_,     _args : Sequence_,     _kwargs : Mapping\[str, Any\]_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/formatting.html#StrictFormatter.vformat)\#     

Check that no arguments are provided.

Parameters:     

  * **format\_string** \(_str_\) – The format string.

  * **args** \(_Sequence_\) – The arguments.

  * **kwargs** \(_Mapping_ _\[__str_ _,__Any_ _\]_\) – The keyword arguments.

Returns:     

The formatted string.

Raises:     

**ValueError** – If any arguments are provided.

Return type:     

str

__On this page   *[/]: Positional-only parameter separator (PEP 570)