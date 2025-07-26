# ConfigurableField — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.utils.ConfigurableField.html
**Word Count:** 134
**Links Count:** 201
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# ConfigurableField\#

_class _langchain\_core.runnables.utils.ConfigurableField\(

    _id : str_,     _name : str | None = None_,     _description : str | None = None_,     _annotation : Any | None = None_,     _is\_shared : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/utils.html#ConfigurableField)\#     

Field that can be configured by the user.

Parameters:     

  * **id** \(_str_\) – The unique identifier of the field.

  * **name** \(_str_ _|__None_\) – The name of the field. Defaults to None.

  * **description** \(_str_ _|__None_\) – The description of the field. Defaults to None.

  * **annotation** \(_Any_ _|__None_\) – The annotation of the field. Defaults to None.

  * **is\_shared** \(_bool_\) – Whether the field is shared. Defaults to False.

Create new instance of ConfigurableField\(id, name, description, annotation, is\_shared\)

Attributes

`annotation` | Alias for field number 3   ---|---   `description` | Alias for field number 2   `id` | Alias for field number 0   `is_shared` | Alias for field number 4   `name` | Alias for field number 1      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(

    _value_ ,     _start =0_,     _stop =9223372036854775807_,     _/_ , \)\#     

Return first index of value.

Raises ValueError if the value is not present.

Examples using ConfigurableField

  * [How to combine results from multiple retrievers](https://python.langchain.com/docs/how_to/ensemble_retriever/)

  * [How to configure runtime chain internals](https://python.langchain.com/docs/how_to/configure/)

  * [How to do per-user retrieval](https://python.langchain.com/docs/how_to/qa_per_user/)

  * [Hybrid Search](https://python.langchain.com/docs/how_to/hybrid/)

  * [LangChain Expression Language Cheatsheet](https://python.langchain.com/docs/how_to/lcel_cheatsheet/)

__On this page   *[/]: Positional-only parameter separator (PEP 570)