# ComprehendPromptSafety — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/comprehend_moderation/langchain_experimental.comprehend_moderation.prompt_safety.ComprehendPromptSafety.html
**Word Count:** 117
**Links Count:** 115
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# ComprehendPromptSafety\#

_class _langchain\_experimental.comprehend\_moderation.prompt\_safety.ComprehendPromptSafety\(

    _client : Any_,     _callback : Any | None = None_,     _unique\_id : str | None = None_,     _chain\_id : str | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/prompt_safety.html#ComprehendPromptSafety)\#     

Class to handle prompt safety moderation.

Methods

`__init__`\(client\[, callback, unique\_id, chain\_id\]\) |    ---|---   `validate`\(prompt\_value\[, config\]\) | Check and validate the safety of the given prompt text.      Parameters:     

  * **client** \(_Any_\)

  * **callback** \(_Any_ _|__None_\)

  * **unique\_id** \(_str_ _|__None_\)

  * **chain\_id** \(_str_ _|__None_\)

\_\_init\_\_\(

    _client : Any_,     _callback : Any | None = None_,     _unique\_id : str | None = None_,     _chain\_id : str | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/prompt_safety.html#ComprehendPromptSafety.__init__)\#     

Parameters:     

  * **client** \(_Any_\)

  * **callback** \(_Any_ _|__None_\)

  * **unique\_id** \(_str_ _|__None_\)

  * **chain\_id** \(_str_ _|__None_\)

Return type:     

None

validate\(

    _prompt\_value : str_,     _config : Any = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/comprehend_moderation/prompt_safety.html#ComprehendPromptSafety.validate)\#     

Check and validate the safety of the given prompt text.

Parameters:     

  * **prompt\_value** \(_str_\) – The input text to be checked for unsafe text.

  * **config** \(_Dict_ _\[__str_ _,__Any_ _\]_\) – Configuration settings for prompt safety checks.

Raises:     

  * **ValueError** – If unsafe prompt is found in the prompt text based

  * **on the specified threshold.** – 

Returns:     

The input prompt\_value.

Return type:     

str

Note

This function checks the safety of the provided prompt text using Comprehend’s classify\_document API and raises an error if unsafe text is detected with a score above the specified threshold.

Example

comprehend\_client = boto3.client\(‘comprehend’\) prompt\_text = “Please tell me your credit card information.” config = \{“threshold”: 0.7\} checked\_prompt = check\_prompt\_safety\(comprehend\_client, prompt\_text, config\)

__On this page