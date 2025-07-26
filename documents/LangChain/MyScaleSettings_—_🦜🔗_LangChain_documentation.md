# MyScaleSettings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.myscale.MyScaleSettings.html
**Word Count:** 193
**Links Count:** 338
**Scraped:** 2025-07-21 08:22:37
**Status:** completed

---

# MyScaleSettings\#

_class _langchain\_community.vectorstores.myscale.MyScaleSettings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/myscale.html#MyScaleSettings)\#     

Bases: `BaseSettings`

MyScale client configuration.

Attribute:     

myscale\_host \(str\)An URL to connect to MyScale backend.     

Defaults to ‘localhost’.

myscale\_port \(int\) : URL port to connect with HTTP. Defaults to 8443. username \(str\) : Username to login. Defaults to None. password \(str\) : Password to login. Defaults to None. index\_type \(str\): index type string. index\_param \(dict\): index build parameter. database \(str\) : Database name to find the table. Defaults to ‘default’. table \(str\) : Table name to operate on.

> Defaults to ‘vector\_table’.

metric \(str\)Metric to compute distance,     

supported are \(‘L2’, ‘Cosine’, ‘IP’\). Defaults to ‘Cosine’.

column\_map \(Dict\)Column type map to project column name onto langchain     

semantics. Must have keys: text, id, vector, must be same size to number of columns. For example: .. code-block:: python

> \{ >      >  > ‘id’: ‘text\_id’, ‘vector’: ‘text\_embedding’, ‘text’: ‘text\_plain’, ‘metadata’: ‘metadata\_dictionary\_in\_json’, >  > \}

Defaults to identity map.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _column\_map _: Dict\[str, str\]__ = \{'id': 'id', 'metadata': 'metadata', 'text': 'text', 'vector': 'vector'\}_\#     

_param _database _: str_ _ = 'default'_\#     

_param _host _: str_ _ = 'localhost'_\#     

_param _index\_param _: Dict\[str, str\] | None_ _ = None_\#     

_param _index\_type _: str_ _ = 'MSTG'_\#     

_param _metric _: str_ _ = 'Cosine'_\#     

_param _password _: str | None_ _ = None_\#     

_param _port _: int_ _ = 8443_\#     

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

__On this page