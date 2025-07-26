# ComprehendToxicity — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.toxicity.ComprehendToxicity.html
**Word Count:** 97
**Links Count:** 115
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# ComprehendToxicity\#

_class _langchain\_experimental.comprehend\_moderation.toxicity.ComprehendToxicity\(

    _client : Any_,     _callback : Any | None = None_,     _unique\_id : str | None = None_,     _chain\_id : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/toxicity.html#ComprehendToxicity)\#     

Class to handle toxicity moderation.

Methods

`__init__`\(client\[, callback, unique\_id, chain\_id\]\) |    ---|---   `validate`\(prompt\_value\[, config\]\) | Check the toxicity of a given text prompt using AWS Comprehend service and apply actions based on configuration.      Parameters:     

  * **client** \(_Any_\)

  * **callback** \(_Any_ _|__None_\)

  * **unique\_id** \(_str_ _|__None_\)

  * **chain\_id** \(_str_ _|__None_\)

\_\_init\_\_\(

    _client : Any_,     _callback : Any | None = None_,     _unique\_id : str | None = None_,     _chain\_id : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/toxicity.html#ComprehendToxicity.__init__)\#     

Parameters:     

  * **client** \(_Any_\)

  * **callback** \(_Any_ _|__None_\)

  * **unique\_id** \(_str_ _|__None_\)

  * **chain\_id** \(_str_ _|__None_\)

Return type:     

None

validate\(

    _prompt\_value : str_,     _config : Any = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/toxicity.html#ComprehendToxicity.validate)\#     

Check the toxicity of a given text prompt using AWS Comprehend service and apply actions based on configuration. :param prompt\_value: The text content to be checked for toxicity. :type prompt\_value: str :param config: Configuration for toxicity checks and actions. :type config: Dict\[str, Any\]

Returns:     

The original prompt\_value if allowed or no toxicity found.

Return type:     

str

Raises:     

  * **ValueError** – If the prompt contains toxic labels and cannot be

  * **processed based on the configuration.** – 

Parameters:     

  * **prompt\_value** \(_str_\)

  * **config** \(_Any_\)

__On this page