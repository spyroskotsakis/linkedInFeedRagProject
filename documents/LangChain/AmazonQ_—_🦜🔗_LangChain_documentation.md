# AmazonQ — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/aws/runnables/langchain_aws.runnables.q_business.AmazonQ.html
**Word Count:** 64
**Links Count:** 90
**Scraped:** 2025-07-21 08:28:38
**Status:** completed

---

# AmazonQ\#

_class _langchain\_aws.runnables.q\_business.AmazonQ\(

    _region\_name : str | None = None_,     _credentials : Any | None = None_,     _client : Any | None = None_,     _application\_id : str = None_,     _parent\_message\_id : str | None = None_,     _conversation\_id : str | None = None_,     _chat\_mode : str = 'RETRIEVAL\_MODE'_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_aws/runnables/q_business.html#AmazonQ)\#     

Beta

This API is in beta and can change in future.

Amazon Q Runnable wrapper.

To authenticate, the AWS client uses the following methods to automatically load credentials: <https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html>

Make sure the credentials / roles used have the required policies to access the Amazon Q service.

Parameters:     

  * **region\_name** \(_str_ _|__None_\)

  * **credentials** \(_Any_ _|__None_\)

  * **client** \(_Any_ _|__None_\)

  * **application\_id** \(_str_\)

  * **parent\_message\_id** \(_str_ _|__None_\)

  * **conversation\_id** \(_str_ _|__None_\)

  * **chat\_mode** \(_str_\)

Note

AmazonQ implements the standard [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable"). 🏃

> The [`Runnable Interface`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable "langchain_core.runnables.base.Runnable") has additional methods that are available on runnables, such as [`with_config`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_config "langchain_core.runnables.base.Runnable.with_config"), [`with_types`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_types "langchain_core.runnables.base.Runnable.with_types"), [`with_retry`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.with_retry "langchain_core.runnables.base.Runnable.with_retry"), [`assign`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.assign "langchain_core.runnables.base.Runnable.assign"), [`bind`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.bind "langchain_core.runnables.base.Runnable.bind"), [`get_graph`](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html#langchain_core.runnables.base.Runnable.get_graph "langchain_core.runnables.base.Runnable.get_graph"), and more.

Attributes

Methods

`__init__`\(\*args, \*\*kwargs\) | Initialize self.   ---|---     

__On this page