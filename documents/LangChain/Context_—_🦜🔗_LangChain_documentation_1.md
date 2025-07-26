# Context — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.Context.html
**Word Count:** 101
**Links Count:** 126
**Scraped:** 2025-07-21 07:54:58
**Status:** completed

---

# Context\#

_class _langchain\_core.beta.runnables.context.Context[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/beta/runnables/context.html#Context)\#     

Context for a runnable.

The Context class provides methods for creating context scopes, getters, and setters within a runnable. It allows for managing and accessing contextual information throughout the execution of a program.

Example               from langchain_core.beta.runnables.context import Context     from langchain_core.runnables.passthrough import RunnablePassthrough     from langchain_core.prompts.prompt import PromptTemplate     from langchain_core.output_parsers.string import StrOutputParser     from tests.unit_tests.fake.llm import FakeListLLM          chain = (         Context.setter("input")         | {             "context": RunnablePassthrough()                     | Context.setter("context"),             "question": RunnablePassthrough(),         }         | PromptTemplate.from_template("{context} {question}")         | FakeListLLM(responses=["hello"])         | StrOutputParser()         | {             "result": RunnablePassthrough(),             "context": Context.getter("context"),             "input": Context.getter("input"),         }     )          # Use the chain     output = chain.invoke("What's your name?")     print(output["result"])  # Output: "hello"     print(output["context"])  # Output: "What's your name?"     print(output["input"])  # Output: "What's your name?     

Methods

`create_scope`\(scope, /\) | Create a context scope.   ---|---   `getter`\(key, /\) | Return a context getter.   `setter`\(\[\_key, \_value\]\) | Return a context setter.      _static _create\_scope\(

    _scope : str_,     _/_ , \) → [PrefixContext](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.PrefixContext.html#langchain_core.beta.runnables.context.PrefixContext "langchain_core.beta.runnables.context.PrefixContext")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/beta/runnables/context.html#Context.create_scope)\#     

Create a context scope.

Parameters:     

**scope** \(_str_\) – The scope.

Returns:     

The context scope.

Return type:     

[_PrefixContext_](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.PrefixContext.html#langchain_core.beta.runnables.context.PrefixContext "langchain_core.beta.runnables.context.PrefixContext")

_static _getter\(

    _key : str | list\[str\]_,     _/_ , \) → [ContextGet](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.ContextGet.html#langchain_core.beta.runnables.context.ContextGet "langchain_core.beta.runnables.context.ContextGet")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/beta/runnables/context.html#Context.getter)\#     

Return a context getter.

Parameters:     

**key** \(_str_ _|__list_ _\[__str_ _\]_\) – The context getter key.

Return type:     

[_ContextGet_](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.ContextGet.html#langchain_core.beta.runnables.context.ContextGet "langchain_core.beta.runnables.context.ContextGet")

_static _setter\(

    _\_key : str | None = None_,     _\_value : [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\] | Callable\[\[Input\], Output\] | Callable\[\[Input\], Awaitable\[Output\]\] | Any | None = None_,     _/_ ,     _\*\* kwargs: [Runnable](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable")\[Input, Output\] | Callable\[\[Input\], Output\] | Callable\[\[Input\], Awaitable\[Output\]\] | Any_, \) → [ContextSet](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.ContextSet.html#langchain_core.beta.runnables.context.ContextSet "langchain_core.beta.runnables.context.ContextSet")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/beta/runnables/context.html#Context.setter)\#     

Return a context setter.

Parameters:     

  * **\_key** \(_str_ _|__None_\) – The context setter key.

  * **\_value** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__|__Callable_ _\[__\[__Input_ _\]__,__Output_ _\]__|__Callable_ _\[__\[__Input_ _\]__,__Awaitable_ _\[__Output_ _\]__\]__|__Any_ _|__None_\) – The context setter value.

  * **\*\*kwargs** \([_Runnable_](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") _\[__Input_ _,__Output_ _\]__|__Callable_ _\[__\[__Input_ _\]__,__Output_ _\]__|__Callable_ _\[__\[__Input_ _\]__,__Awaitable_ _\[__Output_ _\]__\]__|__Any_\) – Additional context setter key-value pairs.

Return type:     

[_ContextSet_](https://python.langchain.com/api_reference/core/beta/langchain_core.beta.runnables.context.ContextSet.html#langchain_core.beta.runnables.context.ContextSet "langchain_core.beta.runnables.context.ContextSet")

__On this page   *[/]: Positional-only parameter separator (PEP 570)