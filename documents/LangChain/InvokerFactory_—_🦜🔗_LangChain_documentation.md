# InvokerFactory — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.InvokerFactory.html
**Word Count:** 24
**Links Count:** 113
**Scraped:** 2025-07-21 08:26:51
**Status:** completed

---

# InvokerFactory\#

_class _langchain\_prompty.core.InvokerFactory[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#InvokerFactory)\#     

Factory for creating invokers.

Methods

`register`\(type, name, invoker\) |    ---|---   `register_executor`\(name, executor\_class\) |    `register_parser`\(name, parser\_class\) |    `register_processor`\(name, processor\_class\) |    `register_renderer`\(name, renderer\_class\) |    `to_dict`\(\) |    `to_json`\(\) |       Return type:     

InvokerFactory

register\(

    _type : Literal\['renderer', 'parser', 'executor', 'processor'\]_,     _name : str_,     _invoker : type\[[Invoker](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Invoker.html#langchain_prompty.core.Invoker "langchain_prompty.core.Invoker")\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#InvokerFactory.register)\#     

Parameters:     

  * **type** \(_Literal_ _\[__'renderer'__,__'parser'__,__'executor'__,__'processor'__\]_\)

  * **name** \(_str_\)

  * **invoker** \(_type_ _\[_[_Invoker_](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Invoker.html#langchain_prompty.core.Invoker "langchain_prompty.core.Invoker") _\]_\)

Return type:     

None

register\_executor\(

    _name : str_,     _executor\_class : Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#InvokerFactory.register_executor)\#     

Parameters:     

  * **name** \(_str_\)

  * **executor\_class** \(_Any_\)

Return type:     

None

register\_parser\(

    _name : str_,     _parser\_class : Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#InvokerFactory.register_parser)\#     

Parameters:     

  * **name** \(_str_\)

  * **parser\_class** \(_Any_\)

Return type:     

None

register\_processor\(

    _name : str_,     _processor\_class : Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#InvokerFactory.register_processor)\#     

Parameters:     

  * **name** \(_str_\)

  * **processor\_class** \(_Any_\)

Return type:     

None

register\_renderer\(

    _name : str_,     _renderer\_class : Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#InvokerFactory.register_renderer)\#     

Parameters:     

  * **name** \(_str_\)

  * **renderer\_class** \(_Any_\)

Return type:     

None

to\_dict\(\) → dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#InvokerFactory.to_dict)\#     

Return type:     

dict\[str, _Any_\]

to\_json\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_prompty/core.html#InvokerFactory.to_json)\#     

Return type:     

str

__On this page