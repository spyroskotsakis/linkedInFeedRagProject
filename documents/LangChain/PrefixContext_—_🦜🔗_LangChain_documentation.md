# PrefixContext — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.PrefixContext.html
**Word Count:** 69
**Links Count:** 124
**Scraped:** 2025-07-21 07:53:06
**Status:** completed

---

# PrefixContext\#

_class _langchain\_core.beta.runnables.context.PrefixContext\(_prefix : str = ''_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/beta/runnables/context.html#PrefixContext)\#     

Context for a runnable with a prefix.

Create a prefix context.

Parameters:     

**prefix** \(_str_\) – The prefix.

Attributes

`prefix` |    ---|---      Methods

`__init__`\(\[prefix\]\) | Create a prefix context.   ---|---   `getter`\(key, /\) | Return a prefixed context getter.   `setter`\(\[\_key, \_value\]\) | Return a prefixed context setter.      \_\_init\_\_\(_prefix : str = ''_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/beta/runnables/context.html#PrefixContext.__init__)\#     

Create a prefix context.

Parameters:     

**prefix** \(_str_\) – The prefix.

getter\(

    _key : str | list\[str\]_,     _/_ , \) → [ContextGet](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.ContextGet.html#langchain_core.beta.runnables.context.ContextGet "langchain_core.beta.runnables.context.ContextGet")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/beta/runnables/context.html#PrefixContext.getter)\#     

Return a prefixed context getter.

Parameters:     

**key** \(_str_ _|__list_ _\[__str_ _\]_\) – The context getter key.

Return type:     

[_ContextGet_](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.ContextGet.html#langchain_core.beta.runnables.context.ContextGet "langchain_core.beta.runnables.context.ContextGet")

setter\(

    _\_key : str | None = None_,     _\_value : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\] | Callable\[\[Input\], Output\] | Callable\[\[Input\], Awaitable\[Output\]\] | Any | None = None_,     _/_ ,     _\*\* kwargs: [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\] | Callable\[\[Input\], Output\] | Callable\[\[Input\], Awaitable\[Output\]\] | Any_, \) → [ContextSet](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.ContextSet.html#langchain_core.beta.runnables.context.ContextSet "langchain_core.beta.runnables.context.ContextSet")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/beta/runnables/context.html#PrefixContext.setter)\#     

Return a prefixed context setter.

Parameters:     

  * **\_key** \(_str_ _|__None_\) – The context setter key.

  * **\_value** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__|__Callable_ _\[__\[__Input_ _\]__,__Output_ _\]__|__Callable_ _\[__\[__Input_ _\]__,__Awaitable_ _\[__Output_ _\]__\]__|__Any_ _|__None_\) – The context setter value.

  * **\*\*kwargs** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__|__Callable_ _\[__\[__Input_ _\]__,__Output_ _\]__|__Callable_ _\[__\[__Input_ _\]__,__Awaitable_ _\[__Output_ _\]__\]__|__Any_\) – Additional context setter key-value pairs.

Return type:     

[_ContextSet_](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.ContextSet.html#langchain_core.beta.runnables.context.ContextSet "langchain_core.beta.runnables.context.ContextSet")

__On this page   *[/]: Positional-only parameter separator (PEP 570)