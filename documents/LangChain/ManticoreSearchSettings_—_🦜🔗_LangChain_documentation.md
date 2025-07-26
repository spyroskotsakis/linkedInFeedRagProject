# ManticoreSearchSettings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.manticore_search.ManticoreSearchSettings.html
**Word Count:** 79
**Links Count:** 346
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# ManticoreSearchSettings\#

_class _langchain\_community.vectorstores.manticore\_search.ManticoreSearchSettings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/manticore_search.html#ManticoreSearchSettings)\#     

Bases: `BaseSettings`

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _column\_map _: Dict\[str, str\]__ = \{'document': 'document', 'embedding': 'embedding', 'id': 'id', 'metadata': 'metadata', 'uuid': 'uuid'\}_\#     

_param _hnsw\_ef\_construction _: int_ _ = 100_\#     

_param _hnsw\_m _: int_ _ = 16_\#     

_param _hnsw\_similarity _: str_ _ = 'L2'_\#     

_param _host _: str_ _ = 'localhost'_\#     

_param _knn\_dims _: int | None_ _ = None_\#     

_param _knn\_type _: str_ _ = 'hnsw'_\#     

_param _password _: str | None_ _ = None_\#     

_param _port _: int_ _ = 9308_\#     

_param _proto _: str_ _ = 'http'_\#     

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

get\_connection\_string\(\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/manticore_search.html#ManticoreSearchSettings.get_connection_string)\#     

Return type:     

str

Examples using ManticoreSearchSettings

  * [ManticoreSearch VectorStore](https://python.langchain.com/docs/integrations/vectorstores/manticore_search/)

__On this page