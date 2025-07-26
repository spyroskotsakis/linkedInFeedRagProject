# TitanTakeoffEmbed — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.titan_takeoff.TitanTakeoffEmbed.html
**Word Count:** 275
**Links Count:** 230
**Scraped:** 2025-07-21 08:04:25
**Status:** completed

---

# TitanTakeoffEmbed\#

_class _langchain\_community.embeddings.titan\_takeoff.TitanTakeoffEmbed\(

    _base\_url : str = 'http://localhost'_,     _port : int = 3000_,     _mgmt\_port : int = 3001_,     _models : List\[[ReaderConfig](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.titan_takeoff.ReaderConfig.html#langchain_community.embeddings.titan_takeoff.ReaderConfig "langchain_community.embeddings.titan_takeoff.ReaderConfig")\] = \[\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/titan_takeoff.html#TitanTakeoffEmbed)\#     

Interface with Takeoff Inference API for embedding models.

Use it to send embedding requests and to deploy embedding readers with Takeoff.

Examples

This is an example how to deploy an embedding model and send requests.

Initialize the Titan Takeoff embedding wrapper.

Parameters:     

  * **base\_url** \(_str_ _,__optional_\) – The base url where Takeoff Inference Server is

  * **"http** \(_listening. Defaults to_\) – //localhost”.

  * **port** \(_int_ _,__optional_\) – What port is Takeoff Inference API listening on.

  * **3000.** \(_Defaults to_\)

  * **mgmt\_port** \(_int_ _,__optional_\) – What port is Takeoff Management API listening on.

  * **3001.** \(_Defaults to_\)

  * **models** \(_List_ _\[_[_ReaderConfig_](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.titan_takeoff.ReaderConfig.html#langchain_community.embeddings.titan_takeoff.ReaderConfig "langchain_community.embeddings.titan_takeoff.ReaderConfig") _\]__,__optional_\) – Any readers you’d like to spin up on.

  * **\[****\]****.** \(_Defaults to_\)

Raises:     

  * **ImportError** – If you haven’t installed takeoff-client, you will get an

  * **ImportError. To remedy run pip install 'takeoff-client==0.4.0'** – 

Attributes

`base_url` | //localhost".   ---|---   `client` | Takeoff Client Python SDK used to interact with Takeoff API   `embed_consumer_groups` | The consumer groups in Takeoff which contain embedding models   `mgmt_port` | The management port of the Titan Takeoff \(Pro\) server.   `port` | The port of the Titan Takeoff \(Pro\) server.      Methods

`__init__`\(\[base\_url, port, mgmt\_port, models\]\) | Initialize the Titan Takeoff embedding wrapper.   ---|---   `aembed_documents`\(texts\) | Asynchronous Embed search docs.   `aembed_query`\(text\) | Asynchronous Embed query text.   `embed_documents`\(texts\[, consumer\_group\]\) | Embed documents.   `embed_query`\(text\[, consumer\_group\]\) | Embed query.      \_\_init\_\_\(

    _base\_url : str = 'http://localhost'_,     _port : int = 3000_,     _mgmt\_port : int = 3001_,     _models : List\[[ReaderConfig](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.titan_takeoff.ReaderConfig.html#langchain_community.embeddings.titan_takeoff.ReaderConfig "langchain_community.embeddings.titan_takeoff.ReaderConfig")\] = \[\]_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/titan_takeoff.html#TitanTakeoffEmbed.__init__)\#     

Initialize the Titan Takeoff embedding wrapper.

Parameters:     

  * **base\_url** \(_str_ _,__optional_\) – The base url where Takeoff Inference Server is

  * **"http** \(_listening. Defaults to_\) – //localhost”.

  * **port** \(_int_ _,__optional_\) – What port is Takeoff Inference API listening on.

  * **3000.** \(_Defaults to_\)

  * **mgmt\_port** \(_int_ _,__optional_\) – What port is Takeoff Management API listening on.

  * **3001.** \(_Defaults to_\)

  * **models** \(_List_ _\[_[_ReaderConfig_](https://python.langchain.com/api_reference/community/embeddings/langchain_community.embeddings.titan_takeoff.ReaderConfig.html#langchain_community.embeddings.titan_takeoff.ReaderConfig "langchain_community.embeddings.titan_takeoff.ReaderConfig") _\]__,__optional_\) – Any readers you’d like to spin up on.

  * **\[****\]****.** \(_Defaults to_\)

Raises:     

  * **ImportError** – If you haven’t installed takeoff-client, you will get an

  * **ImportError. To remedy run pip install 'takeoff-client==0.4.0'** – 

_async _aembed\_documents\(

    _texts : list\[str\]_, \) → list\[list\[float\]\]\#     

Asynchronous Embed search docs.

Parameters:     

**texts** \(_list_ _\[__str_ _\]_\) – List of text to embed.

Returns:     

List of embeddings.

Return type:     

list\[list\[float\]\]

_async _aembed\_query\(_text : str_\) → list\[float\]\#     

Asynchronous Embed query text.

Parameters:     

**text** \(_str_\) – Text to embed.

Returns:     

Embedding.

Return type:     

list\[float\]

embed\_documents\(

    _texts : List\[str\]_,     _consumer\_group : str | None = None_, \) → List\[List\[float\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/titan_takeoff.html#TitanTakeoffEmbed.embed_documents)\#     

Embed documents.

Parameters:     

  * **texts** \(_List_ _\[__str_ _\]_\) – List of prompts/documents to embed

  * **consumer\_group** \(_Optional_ _\[__str_ _\]__,__optional_\) – Consumer group to send request

  * **None.** \(_to containing embedding model. Defaults to_\)

Returns:     

List of embeddings

Return type:     

List\[List\[float\]\]

embed\_query\(

    _text : str_,     _consumer\_group : str | None = None_, \) → List\[float\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/embeddings/titan_takeoff.html#TitanTakeoffEmbed.embed_query)\#     

Embed query.

Parameters:     

  * **text** \(_str_\) – Prompt/document to embed

  * **consumer\_group** \(_Optional_ _\[__str_ _\]__,__optional_\) – Consumer group to send request

  * **None.** \(_to containing embedding model. Defaults to_\)

Returns:     

Embedding

Return type:     

List\[float\]

Examples using TitanTakeoffEmbed

  * [Titan Takeoff](https://python.langchain.com/docs/integrations/text_embedding/titan_takeoff/)

__On this page