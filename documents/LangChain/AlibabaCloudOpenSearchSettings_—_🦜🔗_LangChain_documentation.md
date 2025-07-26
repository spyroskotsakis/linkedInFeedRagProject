# AlibabaCloudOpenSearchSettings — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/vectorstores/langchain_community.vectorstores.alibabacloud_opensearch.AlibabaCloudOpenSearchSettings.html
**Word Count:** 242
**Links Count:** 322
**Scraped:** 2025-07-21 08:21:12
**Status:** completed

---

# AlibabaCloudOpenSearchSettings\#

_class _langchain\_community.vectorstores.alibabacloud\_opensearch.AlibabaCloudOpenSearchSettings\(

    _endpoint : str_,     _instance\_id : str_,     _username : str_,     _password : str_,     _table\_name : str_,     _field\_name\_mapping : Dict\[str, str\]_,     _protocol : str = 'http'_,     _namespace : str = ''_,     _embedding\_field\_separator : str = ','_,     _output\_fields : List\[str\] | None = None_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/alibabacloud_opensearch.html#AlibabaCloudOpenSearchSettings)\#     

Alibaba Cloud Opensearch\` client configuration.

Attribute:     

endpoint \(str\)The endpoint of opensearch instance, You can find it     

from the console of Alibaba Cloud OpenSearch.

instance\_id \(str\)The identify of opensearch instance, You can find     

it from the console of Alibaba Cloud OpenSearch.

username \(str\) : The username specified when purchasing the instance. password \(str\) : The password specified when purchasing the instance，

> After the instance is created, you can modify it on the console.

tablename \(str\): The table name specified during instance configuration. field\_name\_mapping \(Dict\) : Using field name mapping between opensearch

> vector store and opensearch instance configuration table field names:

\{     

‘id’: ‘The id field name map of index document.’, ‘document’: ‘The text field name map of index document.’, ‘embedding’: ‘In the embedding field of the opensearch instance,

> the values must be in float type and separated by separator, default is comma.’,

‘metadata\_field\_x’: ‘Metadata field mapping includes the mapped     

field name and operator in the mapping value, separated by a comma between the mapped field name and the operator.’,

\} protocol \(str\): Communication Protocol between SDK and Server, default is http. namespace \(str\) : The instance data will be partitioned based on the “namespace”

> field,If the namespace is enabled, you need to specify the namespace field name during initialization, Otherwise, the queries cannot be executed correctly.

embedding\_field\_separator\(str\): Delimiter specified for writing vector     

field data, default is comma.

output\_fields: Specify the field list returned when invoking OpenSearch,     

by default it is the value list of the field mapping field.

Methods

`__init__`\(endpoint, instance\_id, username, ...\) |    ---|---      Parameters:     

  * **endpoint** \(_str_\)

  * **instance\_id** \(_str_\)

  * **username** \(_str_\)

  * **password** \(_str_\)

  * **table\_name** \(_str_\)

  * **field\_name\_mapping** \(_Dict_ _\[__str_ _,__str_ _\]_\)

  * **protocol** \(_str_\)

  * **namespace** \(_str_\)

  * **embedding\_field\_separator** \(_str_\)

  * **output\_fields** \(_List_ _\[__str_ _\]__|__None_\)

\_\_init\_\_\(

    _endpoint : str_,     _instance\_id : str_,     _username : str_,     _password : str_,     _table\_name : str_,     _field\_name\_mapping : Dict\[str, str\]_,     _protocol : str = 'http'_,     _namespace : str = ''_,     _embedding\_field\_separator : str = ','_,     _output\_fields : List\[str\] | None = None_, \) → None[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/vectorstores/alibabacloud_opensearch.html#AlibabaCloudOpenSearchSettings.__init__)\#     

Parameters:     

  * **endpoint** \(_str_\)

  * **instance\_id** \(_str_\)

  * **username** \(_str_\)

  * **password** \(_str_\)

  * **table\_name** \(_str_\)

  * **field\_name\_mapping** \(_Dict_ _\[__str_ _,__str_ _\]_\)

  * **protocol** \(_str_\)

  * **namespace** \(_str_\)

  * **embedding\_field\_separator** \(_str_\)

  * **output\_fields** \(_List_ _\[__str_ _\]__|__None_\)

Return type:     

None

Examples using AlibabaCloudOpenSearchSettings

  * [Alibaba Cloud](https://python.langchain.com/docs/integrations/providers/alibaba_cloud/)

  * [Alibaba Cloud OpenSearch](https://python.langchain.com/docs/integrations/vectorstores/alibabacloud_opensearch/)

__On this page