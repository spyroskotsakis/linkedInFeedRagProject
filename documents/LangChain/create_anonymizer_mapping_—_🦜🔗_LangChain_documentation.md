# create_anonymizer_mapping — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/data_anonymizer/langchain_experimental.data_anonymizer.deanonymizer_mapping.create_anonymizer_mapping.html
**Word Count:** 109
**Links Count:** 108
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# create\_anonymizer\_mapping\#

langchain\_experimental.data\_anonymizer.deanonymizer\_mapping.create\_anonymizer\_mapping\(

    _original\_text : str_,     _analyzer\_results : List\[RecognizerResult\]_,     _anonymizer\_results : EngineResult_,     _is\_reversed : bool = False_, \) → Dict\[str, Dict\[str, str\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/deanonymizer_mapping.html#create_anonymizer_mapping)\#     

Create or update the mapping used to anonymize and/or     

deanonymize a text.

This method exploits the results returned by the analysis and anonymization processes.

If is\_reversed is True, it constructs a mapping from each original entity to its anonymized value.

If is\_reversed is False, it constructs a mapping from each anonymized entity back to its original text value.

If there are multiple entities of the same type, the mapping will include a count to differentiate them. For example, if there are two names in the input text, the mapping will include NAME\_1 and NAME\_2.

Example of mapping: \{

> “PERSON”: \{ >      >  > “<original>”: “<anonymized>”, “John Doe”: “Slim Shady” >  > \}, “PHONE\_NUMBER”: \{ >
>> “111-111-1111”: “555-555-5555”

\}

Parameters:     

  * **original\_text** \(_str_\)

  * **analyzer\_results** \(_List_ _\[__RecognizerResult_ _\]_\)

  * **anonymizer\_results** \(_EngineResult_\)

  * **is\_reversed** \(_bool_\)

Return type:     

_Dict_\[str, _Dict_\[str, str\]\]

__On this page