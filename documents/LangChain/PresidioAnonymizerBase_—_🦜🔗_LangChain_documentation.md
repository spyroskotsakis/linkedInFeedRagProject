# PresidioAnonymizerBase — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/data_anonymizer/langchain_experimental.data_anonymizer.presidio.PresidioAnonymizerBase.html
**Word Count:** 215
**Links Count:** 128
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# PresidioAnonymizerBase\#

_class _langchain\_experimental.data\_anonymizer.presidio.PresidioAnonymizerBase\(

    _analyzed\_fields : List\[str\] | None = None_,     _operators : Dict\[str, OperatorConfig\] | None = None_,     _languages\_config : Dict | None = None_,     _add\_default\_faker\_operators : bool = True_,     _faker\_seed : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/presidio.html#PresidioAnonymizerBase)\#     

Base Anonymizer using Microsoft Presidio.

See more: <https://microsoft.github.io/presidio/>

Parameters:     

  * **analyzed\_fields** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of fields to detect and then anonymize. Defaults to all entities supported by Microsoft Presidio.

  * **operators** \(_Optional_ _\[__Dict_ _\[__str_ _,__OperatorConfig_ _\]__\]_\) – Operators to use for anonymization. Operators allow for custom anonymization of detected PII. Learn more: <https://microsoft.github.io/presidio/tutorial/10_simple_anonymization/>

  * **languages\_config** \(_Optional_ _\[__Dict_ _\]_\) – Configuration for the NLP engine. First language in the list will be used as the main language in self.anonymize\(…\) when no language is specified. Learn more: <https://microsoft.github.io/presidio/analyzer/customizing_nlp_models/>

  * **faker\_seed** \(_Optional_ _\[__int_ _\]_\) – Seed used to initialize faker. Defaults to None, in which case faker will be seeded randomly and provide random values.

  * **add\_default\_faker\_operators** \(_bool_\)

Methods

`__init__`\(\[analyzed\_fields, operators, ...\]\) |    ---|---   `add_operators`\(operators\) | Add operators to the anonymizer   `add_recognizer`\(recognizer\) | Add a recognizer to the analyzer   `anonymize`\(text\[, language, allow\_list\]\) | Anonymize text.      \_\_init\_\_\(

    _analyzed\_fields : List\[str\] | None = None_,     _operators : Dict\[str, OperatorConfig\] | None = None_,     _languages\_config : Dict | None = None_,     _add\_default\_faker\_operators : bool = True_,     _faker\_seed : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/presidio.html#PresidioAnonymizerBase.__init__)\#     

Parameters:     

  * **analyzed\_fields** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of fields to detect and then anonymize. Defaults to all entities supported by Microsoft Presidio.

  * **operators** \(_Optional_ _\[__Dict_ _\[__str_ _,__OperatorConfig_ _\]__\]_\) – Operators to use for anonymization. Operators allow for custom anonymization of detected PII. Learn more: <https://microsoft.github.io/presidio/tutorial/10_simple_anonymization/>

  * **languages\_config** \(_Optional_ _\[__Dict_ _\]_\) – Configuration for the NLP engine. First language in the list will be used as the main language in self.anonymize\(…\) when no language is specified. Learn more: <https://microsoft.github.io/presidio/analyzer/customizing_nlp_models/>

  * **faker\_seed** \(_Optional_ _\[__int_ _\]_\) – Seed used to initialize faker. Defaults to None, in which case faker will be seeded randomly and provide random values.

  * **add\_default\_faker\_operators** \(_bool_\)

add\_operators\(

    _operators : Dict\[str, OperatorConfig\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/presidio.html#PresidioAnonymizerBase.add_operators)\#     

Add operators to the anonymizer

Parameters:     

**operators** \(_Dict_ _\[__str_ _,__OperatorConfig_ _\]_\) – Operators to add to the anonymizer.

Return type:     

None

add\_recognizer\(

    _recognizer : EntityRecognizer_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/presidio.html#PresidioAnonymizerBase.add_recognizer)\#     

Add a recognizer to the analyzer

Parameters:     

**recognizer** \(_EntityRecognizer_\) – Recognizer to add to the analyzer.

Return type:     

None

anonymize\(

    _text : str_,     _language : str | None = None_,     _allow\_list : List\[str\] | None = None_, \) → str\#     

Anonymize text.

Parameters:     

  * **text** \(_str_\)

  * **language** \(_str_ _|__None_\)

  * **allow\_list** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

str

__On this page