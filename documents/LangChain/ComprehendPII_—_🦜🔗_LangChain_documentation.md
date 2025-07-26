# ComprehendPII — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.pii.ComprehendPII.html
**Word Count:** 20
**Links Count:** 115
**Scraped:** 2025-07-21 08:24:27
**Status:** completed

---

# ComprehendPII\#

_class _langchain\_experimental.comprehend\_moderation.pii.ComprehendPII\(

    _client : Any_,     _callback : Any | None = None_,     _unique\_id : str | None = None_,     _chain\_id : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/pii.html#ComprehendPII)\#     

Class to handle Personally Identifiable Information \(PII\) moderation.

Methods

`__init__`\(client\[, callback, unique\_id, chain\_id\]\) |    ---|---   `validate`\(prompt\_value\[, config\]\) |       Parameters:     

  * **client** \(_Any_\)

  * **callback** \(_Any_ _|__None_\)

  * **unique\_id** \(_str_ _|__None_\)

  * **chain\_id** \(_str_ _|__None_\)

\_\_init\_\_\(

    _client : Any_,     _callback : Any | None = None_,     _unique\_id : str | None = None_,     _chain\_id : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/pii.html#ComprehendPII.__init__)\#     

Parameters:     

  * **client** \(_Any_\)

  * **callback** \(_Any_ _|__None_\)

  * **unique\_id** \(_str_ _|__None_\)

  * **chain\_id** \(_str_ _|__None_\)

Return type:     

None

validate\(

    _prompt\_value : str_,     _config : Any = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/pii.html#ComprehendPII.validate)\#     

Parameters:     

  * **prompt\_value** \(_str_\)

  * **config** \(_Any_\)

Return type:     

str

__On this page