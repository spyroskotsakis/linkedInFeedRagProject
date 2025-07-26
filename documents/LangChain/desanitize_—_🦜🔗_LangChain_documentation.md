# desanitize — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.opaqueprompts.desanitize.html
**Word Count:** 26
**Links Count:** 249
**Scraped:** 2025-07-21 08:19:13
**Status:** completed

---

# desanitize\#

langchain\_community.utilities.opaqueprompts.desanitize\(

    _sanitized\_text : str_,     _secure\_context : bytes_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/opaqueprompts.html#desanitize)\#     

Restore the original sensitive data from the sanitized text.

Parameters:     

  * **sanitized\_text** \(_str_\) – Sanitized text.

  * **secure\_context** \(_bytes_\) – Secure context returned by the sanitize function.

Returns:     

De-sanitized text.

Return type:     

str

__On this page