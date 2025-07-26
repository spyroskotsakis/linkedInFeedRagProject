# ZapierNLAWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.zapier.ZapierNLAWrapper.html
**Word Count:** 541
**Links Count:** 299
**Scraped:** 2025-07-21 08:12:36
**Status:** completed

---

# ZapierNLAWrapper\#

_class _langchain\_community.utilities.zapier.ZapierNLAWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper)\#     

Bases: `BaseModel`

Wrapper for Zapier NLA.

Full docs here: <https://nla.zapier.com/start/>

This wrapper supports both API Key and OAuth Credential auth methods. API Key is the fastest way to get started using this wrapper.

Call this wrapper with either zapier\_nla\_api\_key or zapier\_nla\_oauth\_access\_token arguments, or set the ZAPIER\_NLA\_API\_KEY environment variable. If both arguments are set, the Access Token will take precedence.

For use-cases where LangChain + Zapier NLA is powering a user-facing application, and LangChain needs access to the end-user’s connected accounts on Zapier.com, you’ll need to use OAuth. Review the full docs above to learn how to create your own provider and generate credentials.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _zapier\_nla\_api\_base _: str_ _ = 'https://nla.zapier.com/api/v1/'_\#     

_param _zapier\_nla\_api\_key _: str_ _\[Required\]_\#     

_param _zapier\_nla\_oauth\_access\_token _: str_ _\[Required\]_\#     

_async _alist\(\) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.alist)\#     

Returns a list of all exposed \(enabled\) actions associated with current user \(associated with the set api\_key\). Change your exposed actions here: <https://nla.zapier.com/demo/start/>

The return list can be empty if no actions exposed. Else will contain a list of action objects:

\[\{     

“id”: str, “description”: str, “params”: Dict\[str, str\]

\}\]

params will always contain an instructions key, the only required param. All others optional and if provided will override any AI guesses \(see “understanding the AI guessing flow” here: <https://nla.zapier.com/api/v1/docs>\)

Return type:     

_List_\[_Dict_\]

_async _alist\_as\_str\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.alist_as_str)\#     

Same as list, but returns a stringified version of the JSON for insertting back into an LLM.

Return type:     

str

_async _apreview\(

    _action\_id : str_,     _instructions : str_,     _params : Dict | None = None_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.apreview)\#     

Same as run, but instead of actually executing the action, will instead return a preview of params that have been guessed by the AI in case you need to explicitly review before executing.

Parameters:     

  * **action\_id** \(_str_\)

  * **instructions** \(_str_\)

  * **params** \(_Dict_ _|__None_\)

Return type:     

_Dict_

_async _apreview\_as\_str\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.apreview_as_str)\#     

Same as preview, but returns a stringified version of the JSON for insertting back into an LLM.

Parameters:     

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

str

_async _arun\(

    _action\_id : str_,     _instructions : str_,     _params : Dict | None = None_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.arun)\#     

Executes an action that is identified by action\_id, must be exposed \(enabled\) by the current user \(associated with the set api\_key\). Change your exposed actions here: <https://nla.zapier.com/demo/start/>

The return JSON is guaranteed to be less than ~500 words \(350 tokens\) making it safe to inject into the prompt of another LLM call.

Parameters:     

  * **action\_id** \(_str_\)

  * **instructions** \(_str_\)

  * **params** \(_Dict_ _|__None_\)

Return type:     

_Dict_

_async _arun\_as\_str\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.arun_as_str)\#     

Same as run, but returns a stringified version of the JSON for insertting back into an LLM.

Parameters:     

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

str

list\(\) → List\[Dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.list)\#     

Returns a list of all exposed \(enabled\) actions associated with current user \(associated with the set api\_key\). Change your exposed actions here: <https://nla.zapier.com/demo/start/>

The return list can be empty if no actions exposed. Else will contain a list of action objects:

\[\{     

“id”: str, “description”: str, “params”: Dict\[str, str\]

\}\]

params will always contain an instructions key, the only required param. All others optional and if provided will override any AI guesses \(see “understanding the AI guessing flow” here: <https://nla.zapier.com/docs/using-the-api#ai-guessing>\)

Return type:     

_List_\[_Dict_\]

list\_as\_str\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.list_as_str)\#     

Same as list, but returns a stringified version of the JSON for insertting back into an LLM.

Return type:     

str

preview\(

    _action\_id : str_,     _instructions : str_,     _params : Dict | None = None_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.preview)\#     

Same as run, but instead of actually executing the action, will instead return a preview of params that have been guessed by the AI in case you need to explicitly review before executing.

Parameters:     

  * **action\_id** \(_str_\)

  * **instructions** \(_str_\)

  * **params** \(_Dict_ _|__None_\)

Return type:     

_Dict_

preview\_as\_str\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.preview_as_str)\#     

Same as preview, but returns a stringified version of the JSON for insertting back into an LLM.

Parameters:     

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

str

run\(

    _action\_id : str_,     _instructions : str_,     _params : Dict | None = None_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.run)\#     

Executes an action that is identified by action\_id, must be exposed \(enabled\) by the current user \(associated with the set api\_key\). Change your exposed actions here: <https://nla.zapier.com/demo/start/>

The return JSON is guaranteed to be less than ~500 words \(350 tokens\) making it safe to inject into the prompt of another LLM call.

Parameters:     

  * **action\_id** \(_str_\)

  * **instructions** \(_str_\)

  * **params** \(_Dict_ _|__None_\)

Return type:     

_Dict_

run\_as\_str\(

    _\* args: Any_,     _\*\* kwargs: Any_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/zapier.html#ZapierNLAWrapper.run_as_str)\#     

Same as run, but returns a stringified version of the JSON for insertting back into an LLM.

Parameters:     

  * **args** \(_Any_\)

  * **kwargs** \(_Any_\)

Return type:     

str

Examples using ZapierNLAWrapper

  * [Zapier Natural Language Actions](https://python.langchain.com/docs/integrations/tools/zapier/)

__On this page