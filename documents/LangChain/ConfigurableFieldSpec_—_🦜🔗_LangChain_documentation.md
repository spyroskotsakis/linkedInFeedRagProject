# ConfigurableFieldSpec — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableFieldSpec.html
**Word Count:** 152
**Links Count:** 197
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# ConfigurableFieldSpec\#

_class _langchain\_core.runnables.utils.ConfigurableFieldSpec\(

    _id : str_,     _annotation : Any_,     _name : str | None = None_,     _description : str | None = None_,     _default : Any = None_,     _is\_shared : bool = False_,     _dependencies : list\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#ConfigurableFieldSpec)\#     

Field that can be configured by the user. It is a specification of a field.

Parameters:     

  * **id** \(_str_\) – The unique identifier of the field.

  * **annotation** \(_Any_\) – The annotation of the field.

  * **name** \(_str_ _|__None_\) – The name of the field. Defaults to None.

  * **description** \(_str_ _|__None_\) – The description of the field. Defaults to None.

  * **default** \(_Any_\) – The default value for the field. Defaults to None.

  * **is\_shared** \(_bool_\) – Whether the field is shared. Defaults to False.

  * **dependencies** \(_list_ _\[__str_ _\]__|__None_\) – The dependencies of the field. Defaults to None.

Create new instance of ConfigurableFieldSpec\(id, annotation, name, description, default, is\_shared, dependencies\)

Attributes

`annotation` | Alias for field number 1   ---|---   `default` | Alias for field number 4   `dependencies` | Alias for field number 6   `description` | Alias for field number 3   `id` | Alias for field number 0   `is_shared` | Alias for field number 5   `name` | Alias for field number 2      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(

    _value_ ,     _start =0_,     _stop =9223372036854775807_,     _/_ , \)\#     

Return first index of value.

Raises ValueError if the value is not present.

Examples using ConfigurableFieldSpec

  * [How to add message history](https://python.langchain.com/docs/how_to/message_history/)

__On this page   *[/]: Positional-only parameter separator (PEP 570)