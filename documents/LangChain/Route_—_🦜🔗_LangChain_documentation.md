# Route — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/chains/langchain.chains.router.base.Route.html
**Word Count:** 48
**Links Count:** 194
**Scraped:** 2025-07-21 07:49:02
**Status:** completed

---

# Route\#

_class _langchain.chains.router.base.Route\(_destination_ , _next\_inputs_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/chains/router/base.html#Route)\#     

Create new instance of Route\(destination, next\_inputs\)

Attributes

`destination` | Alias for field number 0   ---|---   `next_inputs` | Alias for field number 1      Methods

`count`\(value, /\) | Return number of occurrences of value.   ---|---   `index`\(value\[, start, stop\]\) | Return first index of value.      Parameters:     

  * **destination** \(_str_ _|__None_\)

  * **next\_inputs** \(_dict_ _\[__str_ _,__Any_ _\]_\)

count\(_value_ , _/_\)\#     

Return number of occurrences of value.

index\(_value_ , _start =0_, _stop =9223372036854775807_, _/_\)\#     

Return first index of value.

Raises ValueError if the value is not present.

__On this page   *[/]: Positional-only parameter separator (PEP 570)