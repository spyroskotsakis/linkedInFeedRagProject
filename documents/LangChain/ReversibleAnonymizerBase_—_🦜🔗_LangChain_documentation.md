# ReversibleAnonymizerBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/data_anonymizer/langchain_experimental.data_anonymizer.base.ReversibleAnonymizerBase.html
**Word Count:** 32
**Links Count:** 119
**Scraped:** 2025-07-21 08:24:51
**Status:** completed

---

# ReversibleAnonymizerBase\#

_class _langchain\_experimental.data\_anonymizer.base.ReversibleAnonymizerBase[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/base.html#ReversibleAnonymizerBase)\#     

Base abstract class for reversible anonymizers.

Methods

`anonymize`\(text\[, language, allow\_list\]\) | Anonymize text.   ---|---   `deanonymize`\(text\_to\_deanonymize\[, ...\]\) | Deanonymize text   `reset_deanonymizer_mapping`\(\) | Abstract method to reset deanonymizer mapping      anonymize\(

    _text : str_,     _language : str | None = None_,     _allow\_list : List\[str\] | None = None_, \) → str\#     

Anonymize text.

Parameters:     

  * **text** \(_str_\)

  * **language** \(_str_ _|__None_\)

  * **allow\_list** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

str

deanonymize\(_text\_to\_deanonymize: str, deanonymizer\_matching\_strategy: ~typing.Callable\[\[str, ~typing.Dict\[str, ~typing.Dict\[str, str\]\]\], str\] = <function exact\_matching\_strategy>_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/base.html#ReversibleAnonymizerBase.deanonymize)\#     

Deanonymize text

Parameters:     

  * **text\_to\_deanonymize** \(_str_\)

  * **deanonymizer\_matching\_strategy** \(_Callable_ _\[__\[__str_ _,__Dict_ _\[__str_ _,__Dict_ _\[__str_ _,__str_ _\]__\]__\]__,__str_ _\]_\)

Return type:     

str

_abstractmethod _reset\_deanonymizer\_mapping\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/base.html#ReversibleAnonymizerBase.reset_deanonymizer_mapping)\#     

Abstract method to reset deanonymizer mapping

Return type:     

None

__On this page