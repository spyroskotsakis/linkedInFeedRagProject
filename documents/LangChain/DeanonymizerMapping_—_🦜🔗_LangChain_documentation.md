# DeanonymizerMapping — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/data_anonymizer/langchain_experimental.data_anonymizer.deanonymizer_mapping.DeanonymizerMapping.html
**Word Count:** 66
**Links Count:** 115
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# DeanonymizerMapping\#

_class _langchain\_experimental.data\_anonymizer.deanonymizer\_mapping.DeanonymizerMapping\(

    _mapping: ~typing.Dict\[str_,     _~typing.Dict\[str_ ,     _str\]\] = <factory>_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/deanonymizer_mapping.html#DeanonymizerMapping)\#     

Deanonymizer mapping.

Attributes

`data` | Return the deanonymizer mapping.   ---|---      Methods

`__init__`\(\[mapping\]\) |    ---|---   `update`\(new\_mapping\) | Update the deanonymizer mapping with new values.      Parameters:     

**mapping** \(_Dict_ _\[__str_ _,__Dict_ _\[__str_ _,__str_ _\]__\]_\)

\_\_init\_\_\(

    _mapping: ~typing.Dict\[str_,     _~typing.Dict\[str_ ,     _str\]\] = <factory>_, \) → None\#     

Parameters:     

**mapping** \(_Dict_ _\[__str_ _,__Dict_ _\[__str_ _,__str_ _\]__\]_\)

Return type:     

None

update\(

    _new\_mapping : Dict\[str, Dict\[str, str\]\]_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/data_anonymizer/deanonymizer_mapping.html#DeanonymizerMapping.update)\#     

Update the deanonymizer mapping with new values.

Duplicated values will not be added If there are multiple entities of the same type, the mapping will include a count to differentiate them. For example, if there are two names in the input text, the mapping will include NAME\_1 and NAME\_2.

Parameters:     

**new\_mapping** \(_Dict_ _\[__str_ _,__Dict_ _\[__str_ _,__str_ _\]__\]_\)

Return type:     

None

__On this page