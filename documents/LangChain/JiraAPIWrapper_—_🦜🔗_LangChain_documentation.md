# JiraAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.jira.JiraAPIWrapper.html
**Word Count:** 141
**Links Count:** 287
**Scraped:** 2025-07-21 08:07:57
**Status:** completed

---

# JiraAPIWrapper\#

_class _langchain\_community.utilities.jira.JiraAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jira.html#JiraAPIWrapper)\#     

Bases: `BaseModel`

Wrapper for Jira API. You can connect to Jira with either an API token or OAuth2. \- with API token, you need to provide the JIRA\_USERNAME and JIRA\_API\_TOKEN

> environment variables or arguments.

ex: JIRA\_USERNAME=your\_username JIRA\_API\_TOKEN=your\_api\_token \- with OAuth2, you need to provide the JIRA\_OAUTH2 environment variable or

> argument as a dict having as fields “client\_id” and “token” which is a dict containing at least “access\_token” and “token\_type”.

ex: JIRA\_OAUTH2=’\{“client\_id”: “your\_client\_id”, “token”:     

\{“access\_token”: “your\_access\_token”,”token\_type”: “bearer”\}\}’

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _confluence _: Any_ _ = None_\#     

_param _jira\_api\_token _: str | None_ _ = None_\#     

Jira API token when you choose to connect to Jira with api token.

_param _jira\_cloud _: bool | None_ _ = None_\#     

_param _jira\_instance\_url _: str | None_ _ = None_\#     

_param _jira\_oauth2 _: [JiraOauth2](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.jira.JiraOauth2.html#langchain_community.utilities.jira.JiraOauth2 "langchain_community.utilities.jira.JiraOauth2") | str | None_ _ = None_\#     

Jira OAuth2 token when you choose to connect to Jira with oauth2.

_param _jira\_username _: str | None_ _ = None_\#     

issue\_create\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jira.html#JiraAPIWrapper.issue_create)\#     

Parameters:     

**query** \(_str_\)

Return type:     

str

other\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jira.html#JiraAPIWrapper.other)\#     

Parameters:     

**query** \(_str_\)

Return type:     

str

page\_create\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jira.html#JiraAPIWrapper.page_create)\#     

Parameters:     

**query** \(_str_\)

Return type:     

str

parse\_issues\(

    _issues : Dict_, \) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jira.html#JiraAPIWrapper.parse_issues)\#     

Parameters:     

**issues** \(_Dict_\)

Return type:     

_List_\[dict\]

parse\_projects\(

    _projects : List\[dict\]_, \) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jira.html#JiraAPIWrapper.parse_projects)\#     

Parameters:     

**projects** \(_List_ _\[__dict_ _\]_\)

Return type:     

_List_\[dict\]

project\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jira.html#JiraAPIWrapper.project)\#     

Return type:     

str

run\(_mode : str_, _query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jira.html#JiraAPIWrapper.run)\#     

Parameters:     

  * **mode** \(_str_\)

  * **query** \(_str_\)

Return type:     

str

search\(_query : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/jira.html#JiraAPIWrapper.search)\#     

Parameters:     

**query** \(_str_\)

Return type:     

str

Examples using JiraAPIWrapper

  * [Jira Toolkit](https://python.langchain.com/docs/integrations/tools/jira/)

__On this page