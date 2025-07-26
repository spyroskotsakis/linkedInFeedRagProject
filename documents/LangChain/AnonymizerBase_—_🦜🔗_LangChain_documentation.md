# AnonymizerBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/data_anonymizer/langchain_experimental.data_anonymizer.base.AnonymizerBase.html
**Word Count:** 32
**Links Count:** 112
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# AnonymizerBase\#

_class _langchain\_experimental.data\_anonymizer.base.AnonymizerBase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/base.html#AnonymizerBase)\#     

Base abstract class for anonymizers.

It is public and non-virtual because it allows     

wrapping the behavior for all methods in a base class.

Methods

`anonymize`\(text\[, language, allow\_list\]\) | Anonymize text.   ---|---      anonymize\(

    _text : str_,     _language : str | None = None_,     _allow\_list : List\[str\] | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/base.html#AnonymizerBase.anonymize)\#     

Anonymize text.

Parameters:     

  * **text** \(_str_\)

  * **language** \(_str_ _|__None_\)

  * **allow\_list** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

str

__On this page