# sanitize — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.opaqueprompts.sanitize.html
**Word Count:** 125
**Links Count:** 249
**Scraped:** 2025-07-21 08:02:42
**Status:** completed

---

# sanitize\#

langchain\_community.utilities.opaqueprompts.sanitize\(

    _input : str | Dict\[str, str\]_, \) → Dict\[str, str | Dict\[str, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/opaqueprompts.html#sanitize)\#     

Sanitize input string or dict of strings by replacing sensitive data with placeholders.

It returns the sanitized input string or dict of strings and the secure context as a dict following the format: \{

> “sanitized\_input”: <sanitized input string or dict of strings>, “secure\_context”: <secure context>

\}

The secure context is a bytes object that is needed to de-sanitize the response from the LLM.

Parameters:     

**input** \(_str_ _|__Dict_ _\[__str_ _,__str_ _\]_\) – Input string or dict of strings.

Returns:     

Sanitized input string or dict of strings and the secure context as a dict following the format: \{

> ”sanitized\_input”: <sanitized input string or dict of strings>, “secure\_context”: <secure context>

\}

The secure\_context needs to be passed to the desanitize function.

Raises:     

  * **ValueError** – If the input is not a string or dict of strings.

  * **ImportError** – If the opaqueprompts Python package is not installed.

Return type:     

_Dict_\[str, str | _Dict_\[str, str\]\]

__On this page