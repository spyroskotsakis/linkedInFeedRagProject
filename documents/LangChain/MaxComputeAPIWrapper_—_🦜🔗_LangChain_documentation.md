# MaxComputeAPIWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.max_compute.MaxComputeAPIWrapper.html
**Word Count:** 105
**Links Count:** 267
**Scraped:** 2025-07-21 08:21:41
**Status:** completed

---

# MaxComputeAPIWrapper\#

_class _langchain\_community.utilities.max\_compute.MaxComputeAPIWrapper\(_client : ODPS_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/max_compute.html#MaxComputeAPIWrapper)\#     

Interface for querying Alibaba Cloud MaxCompute tables.

Initialize MaxCompute document loader.

Parameters:     

**client** \(_ODPS_\) – odps.ODPS MaxCompute client object.

Methods

`__init__`\(client\) | Initialize MaxCompute document loader.   ---|---   `from_params`\(endpoint, project, \*\[, ...\]\) | Convenience constructor that builds the odsp.ODPS MaxCompute client from   `lazy_query`\(query\) |    `query`\(query\) |       \_\_init\_\_\(_client : ODPS_\)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/max_compute.html#MaxComputeAPIWrapper.__init__)\#     

Initialize MaxCompute document loader.

Parameters:     

**client** \(_ODPS_\) – odps.ODPS MaxCompute client object.

_classmethod _from\_params\(

    _endpoint : str_,     _project : str_,     _\*_ ,     _access\_id : str | None = None_,     _secret\_access\_key : str | None = None_, \) → MaxComputeAPIWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/max_compute.html#MaxComputeAPIWrapper.from_params)\#     

Convenience constructor that builds the odsp.ODPS MaxCompute client from     

given parameters.

Parameters:     

  * **endpoint** \(_str_\) – MaxCompute endpoint.

  * **project** \(_str_\) – A project is a basic organizational unit of MaxCompute, which is similar to a database.

  * **access\_id** \(_str_ _|__None_\) – MaxCompute access ID. Should be passed in directly or set as the environment variable MAX\_COMPUTE\_ACCESS\_ID.

  * **secret\_access\_key** \(_str_ _|__None_\) – MaxCompute secret access key. Should be passed in directly or set as the environment variable MAX\_COMPUTE\_SECRET\_ACCESS\_KEY.

Return type:     

_MaxComputeAPIWrapper_

lazy\_query\(

    _query : str_, \) → Iterator\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/max_compute.html#MaxComputeAPIWrapper.lazy_query)\#     

Parameters:     

**query** \(_str_\)

Return type:     

_Iterator_\[dict\]

query\(_query : str_\) → List\[dict\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/max_compute.html#MaxComputeAPIWrapper.query)\#     

Parameters:     

**query** \(_str_\)

Return type:     

_List_\[dict\]

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)