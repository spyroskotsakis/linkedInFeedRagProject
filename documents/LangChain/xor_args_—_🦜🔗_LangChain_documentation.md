# xor_args — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.utils.xor_args.html
**Word Count:** 39
**Links Count:** 166
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# xor\_args\#

langchain\_core.utils.utils.xor\_args\(_\* arg\_groups: tuple\[str, ...\]_\) → Callable[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/utils.html#xor_args)\#     

Validate specified keyword args are mutually exclusive.”.

Parameters:     

**\*arg\_groups** \(_tuple_ _\[__str_ _,__...__\]_\) – Groups of mutually exclusive keyword args.

Returns:     

Decorator that validates the specified keyword args     

are mutually exclusive

Return type:     

Callable

Raises:     

**ValueError** – If more than one arg in a group is defined.

__On this page