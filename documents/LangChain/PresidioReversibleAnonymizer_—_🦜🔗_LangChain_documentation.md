# PresidioReversibleAnonymizer — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/data_anonymizer/langchain_experimental.data_anonymizer.presidio.PresidioReversibleAnonymizer.html
**Word Count:** 305
**Links Count:** 141
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# PresidioReversibleAnonymizer\#

_class _langchain\_experimental.data\_anonymizer.presidio.PresidioReversibleAnonymizer\(

    _analyzed\_fields : List\[str\] | None = None_,     _operators : Dict\[str, OperatorConfig\] | None = None_,     _languages\_config : Dict | None = None_,     _add\_default\_faker\_operators : bool = True_,     _faker\_seed : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/presidio.html#PresidioReversibleAnonymizer)\#     

Reversible Anonymizer using Microsoft Presidio.

Parameters:     

  * **analyzed\_fields** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of fields to detect and then anonymize. Defaults to all entities supported by Microsoft Presidio.

  * **operators** \(_Optional_ _\[__Dict_ _\[__str_ _,__OperatorConfig_ _\]__\]_\) – Operators to use for anonymization. Operators allow for custom anonymization of detected PII. Learn more: <https://microsoft.github.io/presidio/tutorial/10_simple_anonymization/>

  * **languages\_config** \(_Optional_ _\[__Dict_ _\]_\) – Configuration for the NLP engine. First language in the list will be used as the main language in self.anonymize\(…\) when no language is specified. Learn more: <https://microsoft.github.io/presidio/analyzer/customizing_nlp_models/>

  * **faker\_seed** \(_Optional_ _\[__int_ _\]_\) – Seed used to initialize faker. Defaults to None, in which case faker will be seeded randomly and provide random values.

  * **add\_default\_faker\_operators** \(_bool_\)

Attributes

`anonymizer_mapping` | Return the anonymizer mapping This is just the reverse version of the deanonymizer mapping.   ---|---   `deanonymizer_mapping` | Return the deanonymizer mapping      Methods

`__init__`\(\[analyzed\_fields, operators, ...\]\) |    ---|---   `add_operators`\(operators\) | Add operators to the anonymizer   `add_recognizer`\(recognizer\) | Add a recognizer to the analyzer   `anonymize`\(text\[, language, allow\_list\]\) | Anonymize text.   `deanonymize`\(text\_to\_deanonymize\[, ...\]\) | Deanonymize text   `load_deanonymizer_mapping`\(file\_path\) | Load the deanonymizer mapping from a JSON or YAML file.   `reset_deanonymizer_mapping`\(\) | Reset the deanonymizer mapping   `save_deanonymizer_mapping`\(file\_path\) | Save the deanonymizer mapping to a JSON or YAML file.      \_\_init\_\_\(

    _analyzed\_fields : List\[str\] | None = None_,     _operators : Dict\[str, OperatorConfig\] | None = None_,     _languages\_config : Dict | None = None_,     _add\_default\_faker\_operators : bool = True_,     _faker\_seed : int | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/presidio.html#PresidioReversibleAnonymizer.__init__)\#     

Parameters:     

  * **analyzed\_fields** \(_Optional_ _\[__List_ _\[__str_ _\]__\]_\) – List of fields to detect and then anonymize. Defaults to all entities supported by Microsoft Presidio.

  * **operators** \(_Optional_ _\[__Dict_ _\[__str_ _,__OperatorConfig_ _\]__\]_\) – Operators to use for anonymization. Operators allow for custom anonymization of detected PII. Learn more: <https://microsoft.github.io/presidio/tutorial/10_simple_anonymization/>

  * **languages\_config** \(_Optional_ _\[__Dict_ _\]_\) – Configuration for the NLP engine. First language in the list will be used as the main language in self.anonymize\(…\) when no language is specified. Learn more: <https://microsoft.github.io/presidio/analyzer/customizing_nlp_models/>

  * **faker\_seed** \(_Optional_ _\[__int_ _\]_\) – Seed used to initialize faker. Defaults to None, in which case faker will be seeded randomly and provide random values.

  * **add\_default\_faker\_operators** \(_bool_\)

add\_operators\(

    _operators : Dict\[str, OperatorConfig\]_, \) → None\#     

Add operators to the anonymizer

Parameters:     

**operators** \(_Dict_ _\[__str_ _,__OperatorConfig_ _\]_\) – Operators to add to the anonymizer.

Return type:     

None

add\_recognizer\(

    _recognizer : EntityRecognizer_, \) → None\#     

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

deanonymize\(_text\_to\_deanonymize: str, deanonymizer\_matching\_strategy: ~typing.Callable\[\[str, ~typing.Dict\[str, ~typing.Dict\[str, str\]\]\], str\] = <function exact\_matching\_strategy>_\) → str\#     

Deanonymize text

Parameters:     

  * **text\_to\_deanonymize** \(_str_\)

  * **deanonymizer\_matching\_strategy** \(_Callable_ _\[__\[__str_ _,__Dict_ _\[__str_ _,__Dict_ _\[__str_ _,__str_ _\]__\]__\]__,__str_ _\]_\)

Return type:     

str

load\_deanonymizer\_mapping\(

    _file\_path : Path | str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/presidio.html#PresidioReversibleAnonymizer.load_deanonymizer_mapping)\#     

Load the deanonymizer mapping from a JSON or YAML file.

Parameters:     

**file\_path** \(_Path_ _|__str_\) – Path to file to load the mapping from.

Return type:     

None

Example: .. code-block:: python

> anonymizer.load\_deanonymizer\_mapping\(file\_path=”path/mapping.json”\)

reset\_deanonymizer\_mapping\(\) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/presidio.html#PresidioReversibleAnonymizer.reset_deanonymizer_mapping)\#     

Reset the deanonymizer mapping

Return type:     

None

save\_deanonymizer\_mapping\(

    _file\_path : Path | str_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/presidio.html#PresidioReversibleAnonymizer.save_deanonymizer_mapping)\#     

Save the deanonymizer mapping to a JSON or YAML file.

Parameters:     

**file\_path** \(_Path_ _|__str_\) – Path to file to save the mapping to.

Return type:     

None

Example: .. code-block:: python

> anonymizer.save\_deanonymizer\_mapping\(file\_path=”path/mapping.json”\)

Examples using PresidioReversibleAnonymizer

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

__On this page