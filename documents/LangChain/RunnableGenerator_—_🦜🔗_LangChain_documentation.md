# RunnableGenerator — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.RunnableGenerator.html
**Word Count:** 279
**Links Count:** 199
**Scraped:** 2025-07-21 07:54:02
**Status:** completed

---

# RunnableGenerator\#

_class _langchain\_core.runnables.base.RunnableGenerator\(

    _transform : Callable\[\[Iterator\[Input\]\], Iterator\[Output\]\] | Callable\[\[AsyncIterator\[Input\]\], AsyncIterator\[Output\]\]_,     _atransform : Callable\[\[AsyncIterator\[Input\]\], AsyncIterator\[Output\]\] | None = None_,     _\*_ ,     _name : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/base.html#RunnableGenerator)\#     

Runnable that runs a generator function.

RunnableGenerators can be instantiated directly or by using a generator within a sequence.

RunnableGenerators can be used to implement custom behavior, such as custom output parsers, while preserving streaming capabilities. Given a generator function with a signature Iterator\[A\] -> Iterator\[B\], wrapping it in a RunnableGenerator allows it to emit output chunks as soon as they are streamed in from the previous step.

Note that if a generator function has a signature A -> Iterator\[B\], such that it requires its input from the previous step to be completed before emitting chunks \(e.g., most LLMs need the entire prompt available to start generating\), it can instead be wrapped in a RunnableLambda.

Here is an example to show the basic mechanics of a RunnableGenerator:

>  >     from typing import Any, AsyncIterator, Iterator >      >     from langchain_core.runnables import RunnableGenerator >      >      >     def gen(input: Iterator[Any]) -> Iterator[str]: >         for token in ["Have", " a", " nice", " day"]: >             yield token >      >      >     runnable = RunnableGenerator(gen) >     runnable.invoke(None)  # "Have a nice day" >     list(runnable.stream(None))  # ["Have", " a", " nice", " day"] >     runnable.batch([None, None])  # ["Have a nice day", "Have a nice day"] >      >      >     # Async version: >     async def agen(input: AsyncIterator[Any]) -> AsyncIterator[str]: >         for token in ["Have", " a", " nice", " day"]: >             yield token >      >     runnable = RunnableGenerator(agen) >     await runnable.ainvoke(None)  # "Have a nice day" >     [p async for p in runnable.astream(None)] # ["Have", " a", " nice", " day"] >     

RunnableGenerator makes it easy to implement custom behavior within a streaming context. Below we show an example:

>  >     from langchain_core.prompts import ChatPromptTemplate >     from langchain_core.runnables import RunnableGenerator, RunnableLambda >     from langchain_openai import ChatOpenAI >     from langchain_core.output_parsers import StrOutputParser >      >      >     model = ChatOpenAI() >     chant_chain = ( >         ChatPromptTemplate.from_template("Give me a 3 word chant about {topic}") >         | model >         | StrOutputParser() >     ) >      >     def character_generator(input: Iterator[str]) -> Iterator[str]: >         for token in input: >             if "," in token or "." in token: >                 yield "👏" + token >             else: >                 yield token >      >      >     runnable = chant_chain | character_generator >     assert type(runnable.last) is RunnableGenerator >     "".join(runnable.stream({"topic": "waste"})) # Reduce👏, Reuse👏, Recycle👏. >      >     # Note that RunnableLambda can be used to delay streaming of one step in a >     # sequence until the previous step is finished: >     def reverse_generator(input: str) -> Iterator[str]: >         # Yield characters of input in reverse order. >         for character in input[::-1]: >             yield character >      >     runnable = chant_chain | RunnableLambda(reverse_generator) >     "".join(runnable.stream({"topic": "waste"}))  # ".elcycer ,esuer ,ecudeR" >     

Initialize a RunnableGenerator.

Parameters:     

  * **transform** \(_Union_ _\[__Callable_ _\[__\[__Iterator_ _\[__Input_ _\]__\]__,__Iterator_ _\[__Output_ _\]__\]__,__Callable_ _\[__\[__AsyncIterator_ _\[__Input_ _\]__\]__,__AsyncIterator_ _\[__Output_ _\]__\]__\]_\) – The transform function.

  * **atransform** \(_Optional_ _\[__Callable_ _\[__\[__AsyncIterator_ _\[__Input_ _\]__\]__,__AsyncIterator_ _\[__Output_ _\]__\]__\]_\) – The async transform function. Defaults to None.

  * **name** \(_str_ _|__None_\) – The name of the Runnable. Defaults to None.

Raises:     

**TypeError** – If the transform is not a generator function.

Note

RunnableGenerator implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃

> The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more.

Attributes

Methods

`__init__`\(\*args, \*\*kwargs\) | Initialize self.   ---|---      Examples using RunnableGenerator

  * [How to create a custom Output Parser](https://python.langchain.com/docs/how_to/output_parser_custom/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)