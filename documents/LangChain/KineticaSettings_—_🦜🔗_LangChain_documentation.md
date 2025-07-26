# KineticaSettings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.kinetica.KineticaSettings.html
**Word Count:** 156
**Links Count:** 336
**Scraped:** 2025-07-21 08:07:56
**Status:** completed

---

# KineticaSettings\#

_class _langchain\_community.vectorstores.kinetica.KineticaSettings[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/kinetica.html#KineticaSettings)\#     

Bases: `BaseSettings`

Kinetica client configuration.

Attribute:     

host \(str\)An URL to connect to MyScale backend.     

Defaults to ‘localhost’.

port \(int\) : URL port to connect with HTTP. Defaults to 8443. username \(str\) : Username to login. Defaults to None. password \(str\) : Password to login. Defaults to None. database \(str\) : Database name to find the table. Defaults to ‘default’. table \(str\) : Table name to operate on.

> Defaults to ‘vector\_table’.

metric \(str\)Metric to compute distance,     

supported are \(‘angular’, ‘euclidean’, ‘manhattan’, ‘hamming’, ‘dot’\). Defaults to ‘angular’. [spotify/annoy](https://github.com/spotify/annoy/blob/main/src/annoymodule.cc#L149-L169)

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _database _: str_ _ = 'langchain'_\#     

_param _host _: str_ _ = 'http://127.0.0.1'_\#     

_param _metric _: str_ _ = 'l2'_\#     

_param _password _: str | None_ _ = None_\#     

_param _port _: int_ _ = 9191_\#     

_param _table _: str_ _ = 'langchain\_kinetica\_embeddings'_\#     

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

Examples using KineticaSettings

  * [Kinetica](https://python.langchain.com/docs/integrations/document_loaders/kinetica/)

  * [Kinetica Vectorstore API](https://python.langchain.com/docs/integrations/vectorstores/kinetica/)

  * [Kinetica Vectorstore based Retriever](https://python.langchain.com/docs/integrations/retrievers/kinetica/)

__On this page