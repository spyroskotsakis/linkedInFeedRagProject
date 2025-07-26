# tokenize — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.mustache.tokenize.html
**Word Count:** 101
**Links Count:** 166
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# tokenize\#

langchain\_core.utils.mustache.tokenize\(

    _template : str_,     _def\_ldel : str = '\{\{'_,     _def\_rdel : str = '\}\}'_, \) → Iterator\[tuple\[str, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/mustache.html#tokenize)\#     

Tokenize a mustache template.

Tokenizes a mustache template in a generator fashion, using file-like objects. It also accepts a string containing the template.

Parameters:     

  * **template** \(_str_\) – a file-like object, or a string of a mustache template

  * **def\_ldel** \(_str_\) – The default left delimiter \(“\{\{” by default, as in spec compliant mustache\)

  * **def\_rdel** \(_str_\) – The default right delimiter \(“\}\}” by default, as in spec compliant mustache\)

Returns:     

A generator of mustache tags in the form of a tuple \(tag\_type, tag\_key\)     

Where tag\_type is one of:     

  * literal

  * section

  * inverted section

  * end

  * partial

  * no escape

And tag\_key is either the key or in the case of a literal tag, the literal itself.

Return type:     

_Iterator_\[tuple\[str, str\]\]

__On this page