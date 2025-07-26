# RedisConfig — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/redis/config/langchain_redis.config.RedisConfig.html
**Word Count:** 1292
**Links Count:** 188
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# RedisConfig\#

_class _langchain\_redis.config.RedisConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/config.html#RedisConfig)\#     

Bases: `BaseModel`

Configuration class for Redis vector store settings.

This class defines the configuration parameters for setting up and interacting with a Redis vector store. It uses Pydantic for data validation and settings management.

index\_name\#     

Name of the index in Redis. Defaults to a generated ULID.

Type:     

str

from\_existing\#     

Whether to use an existing index. Defaults to False.

Type:     

bool

key\_prefix\#     

Prefix for Redis keys. Defaults to index\_name if not set.

Type:     

Optional\[str\]

redis\_url\#     

URL of the Redis instance. Defaults to “redis://localhost:6379”.

Type:     

str

redis\_client\#     

Pre-existing Redis client instance.

Type:     

Optional\[[Redis](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis")\]

connection\_args\#     

Additional Redis connection arguments.

Type:     

Optional\[Dict\[str, Any\]\]

distance\_metric\#     

Distance metric for vector similarity. Defaults to “COSINE”.

Type:     

str

indexing\_algorithm\#     

Algorithm used for indexing. Defaults to “FLAT”.

Type:     

str

vector\_datatype\#     

Data type of the vector. Defaults to “FLOAT32”.

Type:     

str

storage\_type\#     

Storage type in Redis. Defaults to “hash”.

Type:     

str

id\_field\#     

Field name for document ID. Defaults to “id”.

Type:     

str

content\_field\#     

Field name for document content. Defaults to “text”.

Type:     

str

embedding\_field\#     

Field name for embedding vector. Defaults to “embedding”.

Type:     

str

default\_tag\_separator\#     

Separator for tag fields. Defaults to “|”.

Type:     

str

metadata\_schema\#     

Schema for metadata fields.

Type:     

Optional\[List\[Dict\[str, Any\]\]\]

index\_schema\#     

Full index schema definition.

Type:     

Optional\[IndexSchema\]

schema\_path\#     

Path to a YAML file containing the index schema.

Type:     

Optional\[str\]

return\_keys\#     

Whether to return keys after adding documents. Defaults to False.

Type:     

bool

custom\_keys\#     

Custom keys for documents.

Type:     

Optional\[List\[str\]\]

embedding\_dimensions\#     

Dimensionality of embedding vectors.

Type:     

Optional\[int\]

Example               from langchain_redis import RedisConfig          config = RedisConfig(         index_name="my_index",         redis_url="redis://localhost:6379",         distance_metric="COSINE",         embedding_dimensions=1536     )          # Use this config to initialize a RedisVectorStore     vector_store = RedisVectorStore(embeddings=my_embeddings, config=config)     

Note

  * Only one of ‘index\_schema’, ‘schema\_path’, or ‘metadata\_schema’ should be specified.

  * The ‘key\_prefix’ is automatically set to ‘index\_name’ if not provided.

  * When ‘from\_existing’ is True, it connects to an existing index instead of creating a new one.

  * Custom validation ensures that incompatible options are not simultaneously specified.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _connection\_args _: Dict\[str, Any\] | None_ _ = \{\}_\#     

_param _content\_field _: str_ _ = 'text'_\#     

_param _custom\_keys _: List\[str\] | None_ _ = None_\#     

_param _default\_tag\_separator _: str_ _ = '|'_\#     

_param _distance\_metric _: str_ _ = 'COSINE'_\#     

_param _embedding\_dimensions _: int | None_ _ = None_\#     

_param _embedding\_field _: str_ _ = 'embedding'_\#     

_param _from\_existing _: bool_ _ = False_\#     

_param _id\_field _: str_ _ = 'id'_\#     

_param _index\_name _: str_ _\[Optional\]_\#     

_param _index\_schema _: Annotated\[IndexSchema | None, SkipValidation\(\)\]__ = None_ _\(alias 'schema'\)_\#     

_param _indexing\_algorithm _: str_ _ = 'FLAT'_\#     

_param _key\_prefix _: str | None_ _ = None_\#     

_param _metadata\_schema _: List\[Dict\[str, Any\]\] | None_ _\[Optional\]_\#     

_param _redis\_client _: Redis | None_ _ = None_\#     

_param _redis\_url _: str_ _ = 'redis://localhost:6379'_\#     

_param _return\_keys _: bool_ _ = False_\#     

_param _schema\_path _: str | None_ _ = None_\#     

_param _storage\_type _: str_ _ = 'hash'_\#     

_param _vector\_datatype _: str_ _ = 'FLOAT32'_\#     

_classmethod _from\_existing\_index\(

    _index\_name : str_,     _redis : Redis_, \) → RedisConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/config.html#RedisConfig.from_existing_index)\#     

Create a RedisConfig object from an existing Redis index.

This class method creates a RedisConfig instance based on the configuration of an existing index in Redis. It’s useful for connecting to and working with pre-existing Redis vector store indexes.

Parameters:     

  * **index\_name** \(_str_\) – The name of the existing index in Redis.

  * **redis** \([_Redis_](https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.redis.base.Redis.html#langchain_community.vectorstores.redis.base.Redis "langchain_community.vectorstores.redis.base.Redis")\) – An active Redis client instance connected to the Redis server where the index exists.

Returns:     

A new instance of RedisConfig configured to match the existing     

index.

Return type:     

RedisConfig

Example               from redis import Redis     from langchain_redis import RedisConfig          # Assuming an existing Redis connection     redis_client = Redis.from_url("redis://localhost:6379")          config = RedisConfig.from_existing_index(         index_name="my_existing_index",         redis_client=redis_client     )          print(config.index_name)  # Output: my_existing_index     print(config.from_existing)  # Output: True     

Note

  * This method sets the ‘from\_existing’ attribute to True, indicating that the configuration is based on an existing index.

  * The method doesn’t fetch the full schema or configuration of the existing index. It only sets up the basic parameters needed to connect to the index.

  * Additional index details \(like field configurations\) are not retrieved and should be known or discovered separately if needed.

  * This method is particularly useful when you need to work with or extend an existing Redis vector store index.

  * Ensure that the provided Redis client has the necessary permissions to access the specified index.

  * If the index doesn’t exist, this method will still create a config, but operations using this config may fail until the index is created.

Raises:     

  * **ValueError** – If the index\_name is empty or None.

  * **ConnectionError** – If there’s an issue connecting to Redis using the provided client.

Parameters:     

  * **index\_name** \(_str_\)

  * **redis** \(_Redis_\)

Return type:     

_RedisConfig_

_classmethod _from\_kwargs\(

    _\*\* kwargs: Any_, \) → RedisConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/config.html#RedisConfig.from_kwargs)\#     

Create a RedisConfig object with default values,     

overwritten by provided kwargs.

This class method allows for flexible creation of a RedisConfig object, using default values where not specified and overriding with any provided keyword arguments. If a ‘schema’ argument is provided, it will be set as ‘index\_schema’ in the config.

Parameters:     

**\*\*kwargs** \(_Any_\) – 

Keyword arguments that match RedisConfig attributes. These will     

override default values.

Common kwargs include: \- index\_name \(str\): Name of the index in Redis. \- redis\_url \(str\): URL of the Redis instance. \- distance\_metric \(str\): Distance metric for vector similarity. \- indexing\_algorithm \(str\): Algorithm used for indexing. \- vector\_datatype \(str\): Data type of the vector. \- embedding\_dimensions \(int\): Dimensionality of embedding vectors.

Returns:     

A new instance of RedisConfig with applied settings.

Return type:     

RedisConfig

Example               from langchain_redis import RedisConfig          config = RedisConfig.from_kwargs(         index_name="my_custom_index",         redis_url="redis://custom-host:6379",         distance_metric="COSINE",         embedding_dimensions=768     )          print(config.index_name)  # Output: my_custom_index     print(config.distance_metric)  # Output: COSINE     

_classmethod _from\_schema\(

    _schema : IndexSchema_,     _\*\* kwargs: Any_, \) → RedisConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/config.html#RedisConfig.from_schema)\#     

Create a RedisConfig object from an IndexSchema.

This class method creates a RedisConfig instance using the provided IndexSchema, which defines the structure of the Redis index.

Parameters:     

  * **schema** \(_IndexSchema_\) – An IndexSchema object defining the structure of the Redis index.

  * **\*\*kwargs** – 

Additional keyword arguments to override or supplement the     

schema-derived settings.

Common kwargs include: \- redis\_url \(str\): URL of the Redis instance. \- distance\_metric \(str\): Distance metric for vector similarity. \- embedding\_dimensions \(int\): Dimensionality of embedding vectors.

Returns:     

A new instance of RedisConfig configured based on the provided     

schema and kwargs.

Return type:     

RedisConfig

Example               from redisvl.schema import IndexSchema     from langchain_redis import RedisConfig          schema = IndexSchema.from_dict({         "index": {"name": "my_index", "storage_type": "hash"},         "fields": [             {"name": "text", "type": "text"},             {                 "name": "embedding",                 "type": "vector",                 "attrs": {"dims": 1536, "distance_metric": "cosine"}             }         ]     })          config = RedisConfig.from_schema(         schema,         redis_url="redis://localhost:6379"     )          print(config.index_name)  # Output: my_index     print(config.storage_type)  # Output: hash     

Note

  * The method extracts index name, key prefix, and storage type from the schema.

  * If the schema specifies a vector field, its attributes \(like dimensions and distance metric\) are used.

  * Additional kwargs can override settings derived from the schema.

  * This method is useful when you have a pre-defined index structure and want to create a matching config.

  * The resulting config can be used to ensure that a RedisVectorStore matches an existing index structure.

_classmethod _from\_yaml\(

    _schema\_path : str_,     _\*\* kwargs: Any_, \) → RedisConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/config.html#RedisConfig.from_yaml)\#     

Create a RedisConfig object from a YAML file containing the index schema.

This class method creates a RedisConfig instance using a YAML file that defines the structure of the Redis index.

Parameters:     

  * **schema\_path** \(_str_\) – Path to the YAML file containing the index schema definition.

  * **\*\*kwargs** – 

Additional keyword arguments to override or supplement the     

schema-derived settings.

Common kwargs include: \- redis\_url \(str\): URL of the Redis instance. \- distance\_metric \(str\): Distance metric for vector similarity. \- embedding\_dimensions \(int\): Dimensionality of embedding vectors.

Returns:     

A new instance of RedisConfig configured based on the YAML     

schema and kwargs.

Return type:     

RedisConfig

Example               from langchain_redis import RedisConfig          # Assuming 'index_schema.yaml' contains a valid index schema     config = RedisConfig.from_yaml(         schema_path="path/to/index_schema.yaml",         redis_url="redis://localhost:6379"     )          print(config.index_name)  # Output: Name defined in YAML     print(config.storage_type)  # Output: Storage type defined in YAML     

Note

  * The YAML file should contain a valid index schema definition compatible with RedisVL.

  * This method internally uses IndexSchema.from\_yaml\(\) to parse the YAML file.

  * Settings derived from the YAML schema can be overridden by additional kwargs.

  * This method is particularly useful when index structures are defined externally in YAML files.

  * Ensure that the YAML file is correctly formatted and accessible at the given path.

  * Any errors in reading or parsing the YAML file will be propagated as exceptions.

Raises:     

  * **FileNotFoundError** – If the specified YAML file does not exist.

  * **YAMLError** – If there are issues parsing the YAML file.

  * **ValueError** – If the YAML content is not a valid index schema.

Parameters:     

  * **schema\_path** \(_str_\)

  * **kwargs** \(_Any_\)

Return type:     

_RedisConfig_

_classmethod _with\_metadata\_schema\(

    _metadata\_schema : List\[Dict\[str, Any\]\]_,     _\*\* kwargs: Any_, \) → RedisConfig[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/config.html#RedisConfig.with_metadata_schema)\#     

Create a RedisConfig object with a specified metadata schema.

This class method creates a RedisConfig instance using a provided metadata schema, which defines the structure of additional metadata fields in the Redis index.

Parameters:     

  * **metadata\_schema** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\) – A list of dictionaries defining the metadata fields. Each dictionary should contain at least ‘name’ and ‘type’ keys.

  * **\*\*kwargs** – 

Additional keyword arguments to configure the RedisConfig     

instance.

Common kwargs include: \- index\_name \(str\): Name of the index in Redis. \- redis\_url \(str\): URL of the Redis instance. \- distance\_metric \(str\): Distance metric for vector similarity. \- embedding\_dimensions \(int\): Dimensionality of embedding vectors.

Returns:     

A new instance of RedisConfig configured with the specified     

metadata schema.

Return type:     

RedisConfig

Example               from langchain_redis import RedisConfig          metadata_schema = [         {"name": "author", "type": "text"},         {"name": "publication_date", "type": "numeric"},         {"name": "tags", "type": "tag", "separator": ","}     ]          config = RedisConfig.with_metadata_schema(         metadata_schema,         index_name="book_index",         redis_url="redis://localhost:6379",         embedding_dimensions=1536     )          print(config.metadata_schema)  # Output: The metadata schema list     print(config.index_name)  # Output: book_index     

Note

  * The metadata\_schema defines additional fields beyond the default content and embedding fields.

  * Common metadata field types include ‘text’, ‘numeric’, and ‘tag’.

  * For ‘tag’ fields, you can specify a custom separator using the ‘separator’ key.

  * This method is useful when you need to index and search on specific metadata attributes.

  * The resulting config ensures that the RedisVectorStore will create an index with the specified metadata fields.

  * Make sure the metadata schema aligns with the actual metadata you plan to store with your documents.

  * This method sets only the metadata\_schema; other configurations should be provided via kwargs.

Raises:     

**ValueError** – If the metadata\_schema is not a list of dictionaries or if required keys are missing.

Parameters:     

  * **metadata\_schema** \(_List_ _\[__Dict_ _\[__str_ _,__Any_ _\]__\]_\)

  * **kwargs** \(_Any_\)

Return type:     

_RedisConfig_

redis\(\) → Redis[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/config.html#RedisConfig.redis)\#     

Return type:     

_Redis_

to\_index\_schema\(\) → IndexSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_redis/config.html#RedisConfig.to_index_schema)\#     

Convert the RedisConfig to an IndexSchema.

This method creates an IndexSchema object based on the current configuration. It’s useful for generating a schema that can be used to create or update a Redis index.

Returns:     

An IndexSchema object representing the current configuration.

Return type:     

IndexSchema

Example               from langchain_redis import RedisConfig          config = RedisConfig(         index_name="my_index",         embedding_dimensions=1536,         distance_metric="COSINE",         metadata_schema=[             {"name": "author", "type": "text"},             {"name": "year", "type": "numeric"}         ]     )          schema = config.to_index_schema()     print(schema.index.name)     # Output: my_index     print(len(schema.fields))     # Output: 4 (id, content, embedding, author, year)     

Note

  * If an index\_schema is already set, it will be returned directly.

  * If a schema\_path is set, the schema will be loaded from the YAML file.

  * Otherwise, a new IndexSchema is created based on the current configuration.

  * The resulting schema includes fields for id, content, and embedding vector, as well as any additional fields specified in metadata\_schema.

  * The embedding field is configured with the specified dimensions, distance metric, and other relevant attributes.

  * This method is particularly useful when you need to create a new index or validate the structure of an existing one.

  * The generated schema can be used with RedisVL operations that require an IndexSchema.

Raises:     

**ValueError** – If essential configuration elements \(like embedding\_dimensions\) are missing.

Return type:     

_IndexSchema_

__On this page