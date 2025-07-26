# Tokenizer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Tokenizer.html
**Word Count:** 12
**Links Count:** 87
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# Tokenizer\#

_class _langchain\_text\_splitters.base.Tokenizer\(

    _chunk\_overlap : int_,     _tokens\_per\_chunk : int_,     _decode : Callable\[\[list\[int\]\], str\]_,     _encode : Callable\[\[str\], list\[int\]\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_text_splitters/base.html#Tokenizer)\#     

Tokenizer data class.

Attributes

Methods

`__init__`\(chunk\_overlap, tokens\_per\_chunk, ...\) |    ---|---      Parameters:     

  * **chunk\_overlap** \(_int_\)

  * **tokens\_per\_chunk** \(_int_\)

  * **decode** \(_Callable_ _\[__\[__list_ _\[__int_ _\]__\]__,__str_ _\]_\)

  * **encode** \(_Callable_ _\[__\[__str_ _\]__,__list_ _\[__int_ _\]__\]_\)

\_\_init\_\_\(

    _chunk\_overlap : int_,     _tokens\_per\_chunk : int_,     _decode : Callable\[\[list\[int\]\], str\]_,     _encode : Callable\[\[str\], list\[int\]\]_, \) → None\#     

Parameters:     

  * **chunk\_overlap** \(_int_\)

  * **tokens\_per\_chunk** \(_int_\)

  * **decode** \(_Callable_ _\[__\[__list_ _\[__int_ _\]__\]__,__str_ _\]_\)

  * **encode** \(_Callable_ _\[__\[__str_ _\]__,__list_ _\[__int_ _\]__\]_\)

Return type:     

None

__On this page