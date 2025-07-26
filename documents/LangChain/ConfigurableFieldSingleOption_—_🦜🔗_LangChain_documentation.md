# ConfigurableFieldSingleOption — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSingleOption.html
**Word Count:** 126
**Links Count:** 196
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# ConfigurableFieldSingleOption\#

_class _langchain\_core.runnables.utils.ConfigurableFieldSingleOption\(

    _id : str_,     _options : Mapping\[str, Any\]_,     _default : str_,     _name : str | None = None_,     _description : str | None = None_,     _is\_shared : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#ConfigurableFieldSingleOption)\#     

Field that can be configured by the user with a default value.

Parameters:     

  * **id** \(_str_\) – The unique identifier of the field.

  * **options** \(_Mapping_ _\[__str_ _,__Any_ _\]_\) – The options for the field.

  * **default** \(_str_\) – The default value for the field.

  * **name** \(_str_ _|__None_\) – The name of the field. Defaults to None.

  * **description** \(_str_ _|__None_\) – The description of the field. Defaults to None.

  * **is\_shared** \(_bool_\) – Whether the field is shared. Defaults to False.

Create new instance of ConfigurableFieldSingleOption\(id, options, default, name, description, is\_shared\)

Attributes

`default` | Alias for field number 2   ---|---   `description` | Alias for field number 4   `id` | Alias for field number 0   `is_shared` | Alias for field number 5   `name` | Alias for field number 3   `options` | Alias for field number 1      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(

    _value_ ,     _start =0_,     _stop =9223372036854775807_,     _/_ , \)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[/]: Positional-only parameter separator (PEP 570)