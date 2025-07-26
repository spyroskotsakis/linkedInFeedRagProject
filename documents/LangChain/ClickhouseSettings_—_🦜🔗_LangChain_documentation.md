# ClickhouseSettings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.clickhouse.ClickhouseSettings.html
**Word Count:** 214
**Links Count:** 344
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# ClickhouseSettings\#

_class _langchain\_community.vectorstores.clickhouse.ClickhouseSettings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/clickhouse.html#ClickhouseSettings)\#     

Bases: `BaseSettings`

ClickHouse client configuration.

Attribute:     

host \(str\)An URL to connect to MyScale backend.     

Defaults to ‘localhost’.

port \(int\) : URL port to connect with HTTP. Defaults to 8443. username \(str\) : Username to login. Defaults to None. password \(str\) : Password to login. Defaults to None. secure \(bool\) : Connect to server over secure connection. Defaults to False. index\_type \(str\): index type string. index\_param \(list\): index build parameter. index\_query\_params\(dict\): index query parameters. database \(str\) : Database name to find the table. Defaults to ‘default’. table \(str\) : Table name to operate on.

> Defaults to ‘vector\_table’.

metric \(str\)Metric to compute distance,     

supported are \(‘angular’, ‘euclidean’, ‘manhattan’, ‘hamming’, ‘dot’\). Defaults to ‘angular’. [spotify/annoy](https://github.com/spotify/annoy/blob/main/src/annoymodule.cc#L149-L169)

column\_map \(Dict\)Column type map to project column name onto langchain     

semantics. Must have keys: text, id, vector, must be same size to number of columns. For example: .. code-block:: python

> \{ >      >  > ‘id’: ‘text\_id’, ‘uuid’: ‘global\_unique\_id’ ‘embedding’: ‘text\_embedding’, ‘document’: ‘text\_plain’, ‘metadata’: ‘metadata\_dictionary\_in\_json’, >  > \}

Defaults to identity map.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _column\_map _: Dict\[str, str\]__ = \{'document': 'document', 'embedding': 'embedding', 'id': 'id', 'metadata': 'metadata', 'uuid': 'uuid'\}_\#     

_param _database _: str_ _ = 'default'_\#     

_param _host _: str_ _ = 'localhost'_\#     

_param _index\_param _: List | Dict | None_ _ = \["'L2Distance'", 100\]_\#     

_param _index\_query\_params _: Dict\[str, str\]__ = \{\}_\#     

_param _index\_type _: str | None_ _ = 'annoy'_\#     

_param _metric _: str_ _ = 'angular'_\#     

_param _password _: str | None_ _ = None_\#     

_param _port _: int_ _ = 8123_\#     

_param _secure _: bool_ _ = False_\#     

_param _table _: str_ _ = 'langchain'_\#     

_param _username _: str | None_ _ = None_\#     

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

Examples using ClickhouseSettings

  * [ClickHouse](https://python.langchain.com/docs/integrations/vectorstores/clickhouse/)

__On this page