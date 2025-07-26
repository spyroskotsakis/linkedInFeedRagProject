# ConneryService — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.service.ConneryService.html
**Word Count:** 169
**Links Count:** 426
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# ConneryService\#

_class _langchain\_community.tools.connery.service.ConneryService[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/connery/service.html#ConneryService)\#     

Bases: `BaseModel`

Service for interacting with the Connery Runner API.

It gets the list of available actions from the Connery Runner, wraps them in ConneryAction Tools and returns them to the user. It also provides a method for running the actions.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _api\_key _: str | None_ _ = None_\#     

_param _runner\_url _: str | None_ _ = None_\#     

get\_action\(

    _action\_id : str_, \) → [ConneryAction](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.tool.ConneryAction.html#langchain_community.tools.connery.tool.ConneryAction "langchain_community.tools.connery.tool.ConneryAction")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/connery/service.html#ConneryService.get_action)\#     

Returns the specified action available in the Connery Runner. :param action\_id: The ID of the action to return. :type action\_id: str

Returns:     

The action with the specified ID.

Return type:     

[ConneryAction](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.tool.ConneryAction.html#langchain_community.tools.connery.tool.ConneryAction "langchain_community.tools.connery.tool.ConneryAction")

Parameters:     

**action\_id** \(_str_\)

list\_actions\(\) → List\[[ConneryAction](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.tool.ConneryAction.html#langchain_community.tools.connery.tool.ConneryAction "langchain_community.tools.connery.tool.ConneryAction")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/connery/service.html#ConneryService.list_actions)\#     

Returns the list of actions available in the Connery Runner. :returns: The list of actions available in the Connery Runner. :rtype: List\[ConneryAction\]

Return type:     

_List_\[[_ConneryAction_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.connery.tool.ConneryAction.html#langchain_community.tools.connery.tool.ConneryAction "langchain_community.tools.connery.tool.ConneryAction")\]

run\_action\(

    _action\_id : str_,     _input : Dict\[str, str\] = \{\}_, \) → Dict\[str, str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/connery/service.html#ConneryService.run_action)\#     

Runs the specified Connery Action with the provided input. :param action\_id: The ID of the action to run. :type action\_id: str :param input: The input object expected by the action. :type input: Dict\[str, str\]

Returns:     

The output of the action.

Return type:     

Dict\[str, str\]

Parameters:     

  * **action\_id** \(_str_\)

  * **input** \(_Dict_ _\[__str_ _,__str_ _\]_\)

Examples using ConneryService

  * [Connery Toolkit](https://python.langchain.com/docs/integrations/tools/connery_toolkit/)

  * [Connery Toolkit and Tools](https://python.langchain.com/docs/integrations/tools/connery/)

__On this page