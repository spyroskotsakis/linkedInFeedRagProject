# jinja2_formatter — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/prompts/langchain_core.prompts.string.jinja2_formatter.html
**Word Count:** 75
**Links Count:** 129
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# jinja2\_formatter\#

langchain\_core.prompts.string.jinja2\_formatter\(

    _template : str_,     _/_ ,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/prompts/string.html#jinja2_formatter)\#     

Format a template using jinja2.

_Security warning_ :     

As of LangChain 0.0.329, this method uses Jinja2’s SandboxedEnvironment by default. However, this sand-boxing should be treated as a best-effort approach rather than a guarantee of security. Do not accept jinja2 templates from untrusted sources as they may lead to arbitrary Python code execution.

<https://jinja.palletsprojects.com/en/3.1.x/sandbox/>

Parameters:     

  * **template** \(_str_\) – The template string.

  * **\*\*kwargs** \(_Any_\) – The variables to format the template with.

Returns:     

The formatted string.

Raises:     

**ImportError** – If jinja2 is not installed.

Return type:     

str

__On this page   *[/]: Positional-only parameter separator (PEP 570)