# EvalError — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/langchain/smith/langchain.smith.evaluation.runner_utils.EvalError.html
**Word Count:** 263
**Links Count:** 137
**Scraped:** 2025-07-21 07:49:02
**Status:** completed

---

# EvalError\#

_class _langchain.smith.evaluation.runner\_utils.EvalError\(_Error : BaseException_, _\*\* kwargs: Any_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/runner_utils.html#EvalError)\#     

Your architecture raised an error.

Methods

`__init__`\(Error, \*\*kwargs\) |    ---|---   `clear`\(\) |    `copy`\(\) |    `fromkeys`\(iterable\[, value\]\) | Create a new dictionary with keys from iterable and values set to value.   `get`\(key\[, default\]\) | Return the value for key if key is in the dictionary, else default.   `items`\(\) |    `keys`\(\) |    `pop`\(k\[,d\]\) | If the key is not found, return the default if given; otherwise, raise a KeyError.   `popitem`\(\) | Remove and return a \(key, value\) pair as a 2-tuple.   `setdefault`\(key\[, default\]\) | Insert key with a value of default if key is not in the dictionary.   `update`\(\[E, \]\*\*F\) | If E is present and has a .keys\(\) method, then does: for k in E: D\[k\] = E\[k\] If E is present and lacks a .keys\(\) method, then does: for k, v in E: D\[k\] = v In either case, this is followed by: for k in F: D\[k\] = F\[k\]   `values`\(\) |       Parameters:     

  * **Error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

\_\_init\_\_\(

    _Error : BaseException_,     _\*\* kwargs: Any_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain/smith/evaluation/runner_utils.html#EvalError.__init__)\#     

Parameters:     

  * **Error** \(_BaseException_\)

  * **kwargs** \(_Any_\)

Return type:     

None

clear\(\) → None. Remove all items from D.\#     

copy\(\) → a shallow copy of D\#     

_classmethod _fromkeys\(_iterable_ , _value =None_, _/_\)\#     

Create a new dictionary with keys from iterable and values set to value.

get\(_key_ , _default =None_, _/_\)\#     

Return the value for key if key is in the dictionary, else default.

items\(\) → a set-like object providing a view on D's items\#     

keys\(\) → a set-like object providing a view on D's keys\#     

pop\(

    _k_\[,     _d_ ,\] \) → v, remove specified key and return the corresponding value.\#     

If the key is not found, return the default if given; otherwise, raise a KeyError.

popitem\(\)\#     

Remove and return a \(key, value\) pair as a 2-tuple.

Pairs are returned in LIFO \(last-in, first-out\) order. Raises KeyError if the dict is empty.

setdefault\(_key_ , _default =None_, _/_\)\#     

Insert key with a value of default if key is not in the dictionary.

Return the value for key if key is in the dictionary, else default.

update\(

    \[_E_ ,\]     _\*\*F_ , \) → None. Update D from dict/iterable E and F.\#     

If E is present and has a .keys\(\) method, then does: for k in E: D\[k\] = E\[k\] If E is present and lacks a .keys\(\) method, then does: for k, v in E: D\[k\] = v In either case, this is followed by: for k in F: D\[k\] = F\[k\]

values\(\) → an object providing a view on D's values\#     

__On this page   *[/]: Positional-only parameter separator (PEP 570)