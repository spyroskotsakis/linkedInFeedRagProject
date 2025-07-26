# JSONObjectEncoder — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/azure_ai/utils/langchain_azure_ai.utils.utils.JSONObjectEncoder.html
**Word Count:** 607
**Links Count:** 91
**Scraped:** 2025-07-21 07:52:07
**Status:** completed

---

# JSONObjectEncoder\#

_class _langchain\_azure\_ai.utils.utils.JSONObjectEncoder\(

    _\*_ ,     _skipkeys =False_,     _ensure\_ascii =True_,     _check\_circular =True_,     _allow\_nan =True_,     _sort\_keys =False_,     _indent =None_,     _separators =None_,     _default =None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/utils/utils.html#JSONObjectEncoder)\#     

Custom JSON encoder for objects in LangChain.

Constructor for JSONEncoder, with sensible defaults.

If skipkeys is false, then it is a TypeError to attempt encoding of keys that are not str, int, float or None. If skipkeys is True, such items are simply skipped.

If ensure\_ascii is true, the output is guaranteed to be str objects with all incoming non-ASCII characters escaped. If ensure\_ascii is false, the output can contain non-ASCII characters.

If check\_circular is true, then lists, dicts, and custom encoded objects will be checked for circular references during encoding to prevent an infinite recursion \(which would cause an RecursionError\). Otherwise, no such check takes place.

If allow\_nan is true, then NaN, Infinity, and -Infinity will be encoded as such. This behavior is not JSON specification compliant, but is consistent with most JavaScript based encoders and decoders. Otherwise, it will be a ValueError to encode such floats.

If sort\_keys is true, then the output of dictionaries will be sorted by key; this is useful for regression tests to ensure that JSON serializations can be compared on a day-to-day basis.

If indent is a non-negative integer, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0 will only insert newlines. None is the most compact representation.

If specified, separators should be an \(item\_separator, key\_separator\) tuple. The default is \(’, ‘, ‘: ‘\) if _indent_ is `None` and \(‘,’, ‘: ‘\) otherwise. To get the most compact JSON representation, you should specify \(‘,’, ‘:’\) to eliminate whitespace.

If specified, default is a function that gets called for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a `TypeError`.

Attributes

`item_separator` |    ---|---   `key_separator` |       Methods

`__init__`\(\*\[, skipkeys, ensure\_ascii, ...\]\) | Constructor for JSONEncoder, with sensible defaults.   ---|---   `default`\(o\) | Serialize the object to JSON string.   `encode`\(o\) | Return a JSON string representation of a Python data structure.   `iterencode`\(o\[, \_one\_shot\]\) | Encode the given object and yield each string representation as available.      \_\_init\_\_\(

    _\*_ ,     _skipkeys =False_,     _ensure\_ascii =True_,     _check\_circular =True_,     _allow\_nan =True_,     _sort\_keys =False_,     _indent =None_,     _separators =None_,     _default =None_, \)\#     

Constructor for JSONEncoder, with sensible defaults.

If skipkeys is false, then it is a TypeError to attempt encoding of keys that are not str, int, float or None. If skipkeys is True, such items are simply skipped.

If ensure\_ascii is true, the output is guaranteed to be str objects with all incoming non-ASCII characters escaped. If ensure\_ascii is false, the output can contain non-ASCII characters.

If check\_circular is true, then lists, dicts, and custom encoded objects will be checked for circular references during encoding to prevent an infinite recursion \(which would cause an RecursionError\). Otherwise, no such check takes place.

If allow\_nan is true, then NaN, Infinity, and -Infinity will be encoded as such. This behavior is not JSON specification compliant, but is consistent with most JavaScript based encoders and decoders. Otherwise, it will be a ValueError to encode such floats.

If sort\_keys is true, then the output of dictionaries will be sorted by key; this is useful for regression tests to ensure that JSON serializations can be compared on a day-to-day basis.

If indent is a non-negative integer, then JSON array elements and object members will be pretty-printed with that indent level. An indent level of 0 will only insert newlines. None is the most compact representation.

If specified, separators should be an \(item\_separator, key\_separator\) tuple. The default is \(’, ‘, ‘: ‘\) if _indent_ is `None` and \(‘,’, ‘: ‘\) otherwise. To get the most compact JSON representation, you should specify \(‘,’, ‘:’\) to eliminate whitespace.

If specified, default is a function that gets called for objects that can’t otherwise be serialized. It should return a JSON encodable version of the object or raise a `TypeError`.

default\(_o : Any_\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_azure_ai/utils/utils.html#JSONObjectEncoder.default)\#     

Serialize the object to JSON string.

Parameters:     

**o** \(_Any_\) – Object to be serialized.

Return type:     

_Any_

encode\(_o_\)\#     

Return a JSON string representation of a Python data structure.               >>> from json.encoder import JSONEncoder     >>> JSONEncoder().encode({"foo": ["bar", "baz"]})     '{"foo": ["bar", "baz"]}'     

iterencode\(_o_ , _\_one\_shot =False_\)\#     

Encode the given object and yield each string representation as available.

For example:               for chunk in JSONEncoder().iterencode(bigobject):         mysocket.write(chunk)     

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)