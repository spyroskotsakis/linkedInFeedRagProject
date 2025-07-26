# ApacheDorisSettings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.apache_doris.ApacheDorisSettings.html
**Word Count:** 157
**Links Count:** 347
**Scraped:** 2025-07-21 08:01:32
**Status:** completed

---

# ApacheDorisSettings\#

_class _langchain\_community.vectorstores.apache\_doris.ApacheDorisSettings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/apache_doris.html#ApacheDorisSettings)\#     

Bases: `BaseSettings`

Apache Doris client configuration.

apache\_doris\_host\#     

An URL to connect to frontend. Defaults to ‘localhost’.

Type:     

str

apache\_doris\_port\#     

URL port to connect with HTTP. Defaults to 9030.

Type:     

int

username\#     

Username to login. Defaults to ‘root’.

Type:     

str

password\#     

Password to login. Defaults to None.

Type:     

str

database\#     

Database name to find the table. Defaults to ‘default’.

Type:     

str

table\#     

Table name to operate on. Defaults to ‘langchain’.

Type:     

str

column\_map\#     

Column type map to project column name onto langchain semantics. Must have keys: text, id, vector, must be same size to number of columns. For example: .. code-block:: python

> \{ >      >  > ‘id’: ‘text\_id’, ‘embedding’: ‘text\_embedding’, ‘document’: ‘text\_plain’, ‘metadata’: ‘metadata\_dictionary\_in\_json’, >  > \}

Defaults to identity map.

Type:     

Dict

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _column\_map _: Dict\[str, str\]__ = \{'document': 'document', 'embedding': 'embedding', 'id': 'id', 'metadata': 'metadata'\}_\#     

_param _database _: str_ _ = 'default'_\#     

_param _host _: str_ _ = 'localhost'_\#     

_param _password _: str_ _ = ''_\#     

_param _port _: int_ _ = 9030_\#     

_param _table _: str_ _ = 'langchain'_\#     

_param _username _: str_ _ = 'root'_\#     

_classmethod _settings\_customise\_sources\(

    _settings\_cls : type\[BaseSettings\]_,     _init\_settings : PydanticBaseSettingsSource_,     _env\_settings : PydanticBaseSettingsSource_,     _dotenv\_settings : PydanticBaseSettingsSource_,     _file\_secret\_settings : PydanticBaseSettingsSource_, \) → tuple\[PydanticBaseSettingsSource, ...\]\#     

Define the sources and their order for loading the settings values.

Parameters:     

  * **settings\_cls** \(_type_ _\[__BaseSettings_ _\]_\) – The Settings class.

  * **init\_settings** \(_PydanticBaseSettingsSource_\) – The InitSettingsSource instance.

  * **env\_settings** \(_PydanticBaseSettingsSource_\) – The EnvSettingsSource instance.

  * **dotenv\_settings** \(_PydanticBaseSettingsSource_\) – The DotEnvSettingsSource instance.

  * **file\_secret\_settings** \(_PydanticBaseSettingsSource_\) – The SecretsSettingsSource instance.

Returns:     

A tuple containing the sources and their order for loading the settings values.

Return type:     

tuple\[_PydanticBaseSettingsSource_ , …\]

Examples using ApacheDorisSettings

  * [Apache Doris](https://python.langchain.com/docs/integrations/vectorstores/apache_doris/)

__On this page