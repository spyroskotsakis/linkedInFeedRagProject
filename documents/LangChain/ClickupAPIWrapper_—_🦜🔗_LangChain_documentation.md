# ClickupAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.clickup.ClickupAPIWrapper.html
**Word Count:** 147
**Links Count:** 314
**Scraped:** 2025-07-21 08:18:46
**Status:** completed

---

# ClickupAPIWrapper\#

_class _langchain\_community.utilities.clickup.ClickupAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Clickup API.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _access\_token _: str | None_ _ = None_\#     

_param _folder\_id _: str | None_ _ = None_\#     

_param _list\_id _: str | None_ _ = None_\#     

_param _space\_id _: str | None_ _ = None_\#     

_param _team\_id _: str | None_ _ = None_\#     

_classmethod _get\_access\_code\_url\(

    _oauth\_client\_id : str_,     _redirect\_uri : str = 'https://google.com'_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.get_access_code_url)\#     

Get the URL to get an access code.

Parameters:     

  * **oauth\_client\_id** \(_str_\)

  * **redirect\_uri** \(_str_\)

Return type:     

str

_classmethod _get\_access\_token\(

    _oauth\_client\_id : str_,     _oauth\_client\_secret : str_,     _code : str_, \) → str | None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.get_access_token)\#     

Get the access token.

Parameters:     

  * **oauth\_client\_id** \(_str_\)

  * **oauth\_client\_secret** \(_str_\)

  * **code** \(_str_\)

Return type:     

str | None

attempt\_parse\_teams\(

    _input\_dict : dict_, \) → Dict\[str, List\[dict\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.attempt_parse_teams)\#     

Parse appropriate content from the list of teams.

Parameters:     

**input\_dict** \(_dict_\)

Return type:     

_Dict_\[str, _List_\[dict\]\]

create\_folder\(_query : str_\) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.create_folder)\#     

Creates a new folder.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_

create\_list\(_query : str_\) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.create_list)\#     

Creates a new list.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_

create\_task\(_query : str_\) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.create_task)\#     

Creates a new task.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_

get\_authorized\_teams\(\) → Dict\[Any, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.get_authorized_teams)\#     

Get all teams for the user.

Return type:     

_Dict_\[_Any_ , _Any_\]

get\_default\_params\(\) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.get_default_params)\#     

Return type:     

_Dict_

get\_folders\(\) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.get_folders)\#     

Get all the folders for the team.

Return type:     

_Dict_

get\_headers\(\) → Mapping\[str, str | bytes\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.get_headers)\#     

Get the headers for the request.

Return type:     

_Mapping_\[str, str | bytes\]

get\_lists\(\) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.get_lists)\#     

Get all available lists.

Return type:     

_Dict_

get\_spaces\(\) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.get_spaces)\#     

Get all spaces for the team.

Return type:     

_Dict_

get\_task\(

    _query : str_,     _fault\_tolerant : bool = True_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.get_task)\#     

Retrieve a specific task.

Parameters:     

  * **query** \(_str_\)

  * **fault\_tolerant** \(_bool_\)

Return type:     

_Dict_

get\_task\_attribute\(

    _query : str_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.get_task_attribute)\#     

Update an attribute of a specified task.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_

query\_tasks\(_query : str_\) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.query_tasks)\#     

Query tasks that match certain fields

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_

run\(_mode : str_, _query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.run)\#     

Run the API.

Parameters:     

  * **mode** \(_str_\)

  * **query** \(_str_\)

Return type:     

str

update\_task\(_query : str_\) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.update_task)\#     

Update an attribute of a specified task.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_

update\_task\_assignees\(

    _query : str_, \) → Dict[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/clickup.html#ClickupAPIWrapper.update_task_assignees)\#     

Add or remove assignees of a specified task.

Parameters:     

**query** \(_str_\)

Return type:     

_Dict_

Examples using ClickupAPIWrapper

  * [ClickUp Toolkit](https://python.langchain.com/docs/integrations/tools/clickup/)

__On this page