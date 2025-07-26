# parse_tag — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/utils/langchain_core.utils.mustache.parse_tag.html
**Word Count:** 42
**Links Count:** 168
**Scraped:** 2025-07-21 07:56:55
**Status:** completed

---

# parse\_tag\#

langchain\_core.utils.mustache.parse\_tag\(

    _template : str_,     _l\_del : str_,     _r\_del : str_, \) → tuple\[tuple\[str, str\], str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/utils/mustache.html#parse_tag)\#     

Parse a tag from a template.

Parameters:     

  * **template** \(_str_\) – The template.

  * **l\_del** \(_str_\) – The left delimiter.

  * **r\_del** \(_str_\) – The right delimiter.

Returns:     

The tag and the template.

Return type:     

tuple\[tuple\[str, str\], str\]

Raises:     

  * [**ChevronError**](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.mustache.ChevronError.html#langchain_core.utils.mustache.ChevronError "langchain_core.utils.mustache.ChevronError") – If the tag is unclosed.

  * [**ChevronError**](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.mustache.ChevronError.html#langchain_core.utils.mustache.ChevronError "langchain_core.utils.mustache.ChevronError") – If the set delimiter tag is unclosed.

__On this page