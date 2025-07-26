# ChildRecord — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.mutable_expander.ChildRecord.html
**Word Count:** 57
**Links Count:** 189
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# ChildRecord\#

_class _langchain\_community.callbacks.streamlit.mutable\_expander.ChildRecord\(

    _type : [ChildType](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.mutable_expander.ChildType.html#langchain_community.callbacks.streamlit.mutable_expander.ChildType "langchain_community.callbacks.streamlit.mutable_expander.ChildType")_,     _kwargs : Dict\[str, Any\]_,     _dg : DeltaGenerator_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/streamlit/mutable_expander.html#ChildRecord)\#     

Child record as a NamedTuple.

Create new instance of ChildRecord\(type, kwargs, dg\)

Attributes

`dg` | Alias for field number 2   ---|---   `kwargs` | Alias for field number 1   `type` | Alias for field number 0      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      Parameters:     

  * **type** \([_ChildType_](https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.streamlit.mutable_expander.ChildType.html#langchain_community.callbacks.streamlit.mutable_expander.ChildType "langchain_community.callbacks.streamlit.mutable_expander.ChildType")\)

  * **kwargs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

  * **dg** \(_DeltaGenerator_\)

count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(

    _value_ ,     _start =0_,     _stop =9223372036854775807_,     _/_ , \)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[/]: Positional-only parameter separator (PEP 570)