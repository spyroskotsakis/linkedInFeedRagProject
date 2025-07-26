# ModelRepository — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.model_repository.ModelRepository.html
**Word Count:** 14
**Links Count:** 144
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# ModelRepository\#

_class _langchain\_experimental.rl\_chain.model\_repository.ModelRepository\(

    _folder : str | PathLike_,     _with\_history : bool = True_,     _reset : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/model_repository.html#ModelRepository)\#     

Model Repository.

Methods

`__init__`\(folder\[, with\_history, reset\]\) |    ---|---   `get_tag`\(\) |    `has_history`\(\) |    `load`\(commandline\) |    `save`\(workspace\) |       Parameters:     

  * **folder** \(_str_ _|__PathLike_\)

  * **with\_history** \(_bool_\)

  * **reset** \(_bool_\)

\_\_init\_\_\(

    _folder : str | PathLike_,     _with\_history : bool = True_,     _reset : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/model_repository.html#ModelRepository.__init__)\#     

Parameters:     

  * **folder** \(_str_ _|__PathLike_\)

  * **with\_history** \(_bool_\)

  * **reset** \(_bool_\)

get\_tag\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/model_repository.html#ModelRepository.get_tag)\#     

Return type:     

str

has\_history\(\) → bool[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/model_repository.html#ModelRepository.has_history)\#     

Return type:     

bool

load\(

    _commandline : List\[str\]_, \) → vw.Workspace[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/model_repository.html#ModelRepository.load)\#     

Parameters:     

**commandline** \(_List_ _\[__str_ _\]_\)

Return type:     

vw.Workspace

save\(_workspace : vw.Workspace_\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/model_repository.html#ModelRepository.save)\#     

Parameters:     

**workspace** \(_vw.Workspace_\)

Return type:     

None

__On this page