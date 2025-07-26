# check_valid_template — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.check_valid_template.html
**Word Count:** 45
**Links Count:** 128
**Scraped:** 2025-07-21 07:56:25
**Status:** completed

---

# check\_valid\_template\#

langchain\_core.prompts.string.check\_valid\_template\(

    _template : str_,     _template\_format : str_,     _input\_variables : list\[str\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/string.html#check_valid_template)\#     

Check that template string is valid.

Parameters:     

  * **template** \(_str_\) – The template string.

  * **template\_format** \(_str_\) – The template format. Should be one of “f-string” or “jinja2”.

  * **input\_variables** \(_list_ _\[__str_ _\]_\) – The input variables.

Raises:     

  * **ValueError** – If the template format is not supported.

  * **ValueError** – If the prompt schema is invalid.

Return type:     

None

__On this page