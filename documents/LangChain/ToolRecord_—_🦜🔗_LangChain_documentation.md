# ToolRecord — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.streamlit_callback_handler.ToolRecord.html
**Word Count:** 52
**Links Count:** 187
**Scraped:** 2025-07-21 08:09:49
**Status:** completed

---

# ToolRecord\#

_class _langchain\_community.callbacks.streamlit.streamlit\_callback\_handler.ToolRecord\(_name : str_, _input\_str : str_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/streamlit_callback_handler.html#ToolRecord)\#     

Tool record as a NamedTuple.

Create new instance of ToolRecord\(name, input\_str\)

Attributes

`input_str` | Alias for field number 1   ---|---   `name` | Alias for field number 0      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      Parameters:     

  * **name** \(_str_\)

  * **input\_str** \(_str_\)

count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(

    _value_ ,     _start =0_,     _stop =9223372036854775807_,     _/_ , \)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[/]: Positional-only parameter separator (PEP 570)