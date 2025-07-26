# ContextThreadPoolExecutor — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.config.ContextThreadPoolExecutor.html
**Word Count:** 263
**Links Count:** 204
**Scraped:** 2025-07-21 07:55:55
**Status:** completed

---

# ContextThreadPoolExecutor\#

_class _langchain\_core.runnables.config.ContextThreadPoolExecutor\(

    _max\_workers =None_,     _thread\_name\_prefix =''_,     _initializer =None_,     _initargs =\(\)_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/config.html#ContextThreadPoolExecutor)\#     

ThreadPoolExecutor that copies the context to the child thread.

Initializes a new ThreadPoolExecutor instance.

Parameters:     

  * **max\_workers** – The maximum number of threads that can be used to execute the given calls.

  * **thread\_name\_prefix** – An optional name prefix to give our threads.

  * **initializer** – A callable used to initialize worker threads.

  * **initargs** – A tuple of arguments to pass to the initializer.

Methods

`__init__`\(\[max\_workers, thread\_name\_prefix, ...\]\) | Initializes a new ThreadPoolExecutor instance.   ---|---   `map`\(fn, \*iterables\[, timeout, chunksize\]\) | Map a function to multiple iterables.   `shutdown`\(\[wait, cancel\_futures\]\) | Clean-up the resources associated with the Executor.   `submit`\(func, \*args, \*\*kwargs\) | Submit a function to the executor.      \_\_init\_\_\(

    _max\_workers =None_,     _thread\_name\_prefix =''_,     _initializer =None_,     _initargs =\(\)_, \)\#     

Initializes a new ThreadPoolExecutor instance.

Parameters:     

  * **max\_workers** – The maximum number of threads that can be used to execute the given calls.

  * **thread\_name\_prefix** – An optional name prefix to give our threads.

  * **initializer** – A callable used to initialize worker threads.

  * **initargs** – A tuple of arguments to pass to the initializer.

map\(

    _fn : Callable\[\[...\], T\]_,     _\* iterables: Iterable\[Any\]_,     _timeout : float | None = None_,     _chunksize : int = 1_, \) → Iterator\[T\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/config.html#ContextThreadPoolExecutor.map)\#     

Map a function to multiple iterables.

Parameters:     

  * **fn** \(_Callable_ _\[__...__,__T_ _\]_\) – The function to map.

  * **\*iterables** \(_Iterable_ _\[__Any_ _\]_\) – The iterables to map over.

  * **timeout** \(_float_ _|__None_ _,__optional_\) – The timeout for the map. Defaults to None.

  * **chunksize** \(_int_ _,__optional_\) – The chunksize for the map. Defaults to 1.

Returns:     

The iterator for the mapped function.

Return type:     

Iterator\[T\]

shutdown\(

    _wait =True_,     _\*_ ,     _cancel\_futures =False_, \)\#     

Clean-up the resources associated with the Executor.

It is safe to call this method several times. Otherwise, no other methods can be called after this one.

Parameters:     

  * **wait** – If True then shutdown will not return until all running futures have finished executing and the resources used by the executor have been reclaimed.

  * **cancel\_futures** – If True then shutdown will cancel all pending futures. Futures that are completed or running will not be cancelled.

submit\(_func: ~typing.Callable\[\[~P\], ~langchain\_core.runnables.config.T\], \*args: ~typing.~P, \*\*kwargs: ~typing.~P_\) → Future\[T\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/runnables/config.html#ContextThreadPoolExecutor.submit)\#     

Submit a function to the executor.

Parameters:     

  * **func** \(_Callable_ _\[__...__,__T_ _\]_\) – The function to submit.

  * **\*args** \(_Any_\) – The positional arguments to the function.

  * **\*\*kwargs** \(_Any_\) – The keyword arguments to the function.

Returns:     

The future for the function.

Return type:     

Future\[T\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)