# get_template_variables — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.get_template_variables.html
**Word Count:** 39
**Links Count:** 128
**Scraped:** 2025-07-21 07:55:26
**Status:** completed

---

# get\_template\_variables\#

langchain\_core.prompts.string.get\_template\_variables\(

    _template : str_,     _template\_format : str_, \) → list\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/string.html#get_template_variables)\#     

Get the variables from the template.

Parameters:     

  * **template** \(_str_\) – The template string.

  * **template\_format** \(_str_\) – The template format. Should be one of “f-string” or “jinja2”.

Returns:     

The variables from the template.

Raises:     

**ValueError** – If the template format is not supported.

Return type:     

list\[str\]

__On this page