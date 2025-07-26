# PowerBIDataset — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.powerbi.PowerBIDataset.html
**Word Count:** 146
**Links Count:** 293
**Scraped:** 2025-07-21 08:09:13
**Status:** completed

---

# PowerBIDataset\#

_class _langchain\_community.utilities.powerbi.PowerBIDataset[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/powerbi.html#PowerBIDataset)\#     

Bases: `BaseModel`

Create PowerBI engine from dataset ID and credential or token.

Use either the credential or a supplied token to authenticate. If both are supplied the credential is used to generate a token. The impersonated\_user\_name is the UPN of a user to be impersonated. If the model is not RLS enabled, this will be ignored.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _aiosession _: aiohttp.ClientSession | None_ _ = None_\#     

_param _credential _: TokenCredential | None_ _ = None_\#     

_param _dataset\_id _: str_ _\[Required\]_\#     

_param _group\_id _: str | None_ _ = None_\#     

_param _impersonated\_user\_name _: str | None_ _ = None_\#     

_param _sample\_rows\_in\_table\_info _: int_ _ = 1_\#     

Constraints:     

  * **gt** = 0

  * **le** = 10

_param _schemas _: Dict\[str, str\]__\[Optional\]_\#     

_param _table\_names _: List\[str\]__\[Required\]_\#     

_param _token _: str | None_ _ = None_\#     

_async _aget\_table\_info\(

    _table\_names : List\[str\] | str | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/powerbi.html#PowerBIDataset.aget_table_info)\#     

Get information about specified tables.

Parameters:     

**table\_names** \(_List_ _\[__str_ _\]__|__str_ _|__None_\)

Return type:     

str

_async _arun\(_command : str_\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/powerbi.html#PowerBIDataset.arun)\#     

Execute a DAX command and return the result asynchronously.

Parameters:     

**command** \(_str_\)

Return type:     

_Any_

get\_schemas\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/powerbi.html#PowerBIDataset.get_schemas)\#     

Get the available schema’s.

Return type:     

str

get\_table\_info\(

    _table\_names : List\[str\] | str | None = None_, \) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/powerbi.html#PowerBIDataset.get_table_info)\#     

Get information about specified tables.

Parameters:     

**table\_names** \(_List_ _\[__str_ _\]__|__str_ _|__None_\)

Return type:     

str

get\_table\_names\(\) → Iterable\[str\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/powerbi.html#PowerBIDataset.get_table_names)\#     

Get names of tables available.

Return type:     

_Iterable_\[str\]

run\(_command : str_\) → Any[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/powerbi.html#PowerBIDataset.run)\#     

Execute a DAX command and return a json representing the results.

Parameters:     

**command** \(_str_\)

Return type:     

_Any_

_property _headers _: Dict\[str, str\]_\#     

Get the token.

_property _request\_url _: str_\#     

Get the request url.

_property _table\_info _: str_\#     

Information about all tables in the database.

Examples using PowerBIDataset

  * [Microsoft](https://python.langchain.com/docs/integrations/providers/microsoft/)

  * [PowerBI Toolkit](https://python.langchain.com/docs/integrations/tools/powerbi/)

__On this page