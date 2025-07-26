# ApifyWrapper — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.apify.ApifyWrapper.html
**Word Count:** 550
**Links Count:** 282
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# ApifyWrapper\#

_class _langchain\_community.utilities.apify.ApifyWrapper[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/apify.html#ApifyWrapper)\#     

Bases: `BaseModel`

Deprecated since version 0.3.18: This class is deprecated and will be removed in a future version. You can swap to using the ApifyWrapper implementation in langchain\_apify package. See <[apify/langchain-apify](https://github.com/apify/langchain-apify)> Use `:class:`~langchain_apify.ApifyWrapper`` instead.

Wrapper around Apify. To use, you should have the `apify-client` python package installed, and the environment variable `APIFY_API_TOKEN` set with your API key, or pass apify\_api\_token as a named parameter to the constructor.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _apify\_api\_token _: str | None_ _ = None_\#     

_param _apify\_client _: Any_ _\[Required\]_\#     

_param _apify\_client\_async _: Any_ _\[Required\]_\#     

_async _acall\_actor\(

    _actor\_id : str_,     _run\_input : Dict_,     _dataset\_mapping\_function : Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*_ ,     _build : str | None = None_,     _memory\_mbytes : int | None = None_,     _timeout\_secs : int | None = None_, \) → [ApifyDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader.html#langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader "langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/apify.html#ApifyWrapper.acall_actor)\#     

Run an Actor on the Apify platform and wait for results to be ready. :param actor\_id: The ID or name of the Actor on the Apify platform. :type actor\_id: str :param run\_input: The input object of the Actor that you’re trying to run. :type run\_input: Dict :param dataset\_mapping\_function: A function that takes a single

> dictionary \(an Apify dataset item\) and converts it to an instance of the Document class.

Parameters:     

  * **build** \(_str_ _,__optional_\) – Optionally specifies the actor build to run. It can be either a build tag or build number.

  * **memory\_mbytes** \(_int_ _,__optional_\) – Optional memory limit for the run, in megabytes.

  * **timeout\_secs** \(_int_ _,__optional_\) – Optional timeout for the run, in seconds.

  * **actor\_id** \(_str_\)

  * **run\_input** \(_Dict_\)

  * **dataset\_mapping\_function** \(_Callable_\)

Returns:     

A loader that will fetch the records from the     

Actor run’s default dataset.

Return type:     

[ApifyDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader.html#langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader "langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader")

_async _acall\_actor\_task\(

    _task\_id : str_,     _task\_input : Dict_,     _dataset\_mapping\_function : Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*_ ,     _build : str | None = None_,     _memory\_mbytes : int | None = None_,     _timeout\_secs : int | None = None_, \) → [ApifyDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader.html#langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader "langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/apify.html#ApifyWrapper.acall_actor_task)\#     

Run a saved Actor task on Apify and wait for results to be ready. :param task\_id: The ID or name of the task on the Apify platform. :type task\_id: str :param task\_input: The input object of the task that you’re trying to run.

> Overrides the task’s saved input.

Parameters:     

  * **dataset\_mapping\_function** \(_Callable_\) – A function that takes a single dictionary \(an Apify dataset item\) and converts it to an instance of the Document class.

  * **build** \(_str_ _,__optional_\) – Optionally specifies the actor build to run. It can be either a build tag or build number.

  * **memory\_mbytes** \(_int_ _,__optional_\) – Optional memory limit for the run, in megabytes.

  * **timeout\_secs** \(_int_ _,__optional_\) – Optional timeout for the run, in seconds.

  * **task\_id** \(_str_\)

  * **task\_input** \(_Dict_\)

Returns:     

A loader that will fetch the records from the     

task run’s default dataset.

Return type:     

[ApifyDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader.html#langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader "langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader")

call\_actor\(

    _actor\_id : str_,     _run\_input : Dict_,     _dataset\_mapping\_function : Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*_ ,     _build : str | None = None_,     _memory\_mbytes : int | None = None_,     _timeout\_secs : int | None = None_, \) → [ApifyDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader.html#langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader "langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/apify.html#ApifyWrapper.call_actor)\#     

Run an Actor on the Apify platform and wait for results to be ready. :param actor\_id: The ID or name of the Actor on the Apify platform. :type actor\_id: str :param run\_input: The input object of the Actor that you’re trying to run. :type run\_input: Dict :param dataset\_mapping\_function: A function that takes a single

> dictionary \(an Apify dataset item\) and converts it to an instance of the Document class.

Parameters:     

  * **build** \(_str_ _,__optional_\) – Optionally specifies the actor build to run. It can be either a build tag or build number.

  * **memory\_mbytes** \(_int_ _,__optional_\) – Optional memory limit for the run, in megabytes.

  * **timeout\_secs** \(_int_ _,__optional_\) – Optional timeout for the run, in seconds.

  * **actor\_id** \(_str_\)

  * **run\_input** \(_Dict_\)

  * **dataset\_mapping\_function** \(_Callable_\)

Returns:     

A loader that will fetch the records from the     

Actor run’s default dataset.

Return type:     

[ApifyDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader.html#langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader "langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader")

call\_actor\_task\(

    _task\_id : str_,     _task\_input : Dict_,     _dataset\_mapping\_function : Callable\[\[Dict\], [Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]_,     _\*_ ,     _build : str | None = None_,     _memory\_mbytes : int | None = None_,     _timeout\_secs : int | None = None_, \) → [ApifyDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader.html#langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader "langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader")[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/utilities/apify.html#ApifyWrapper.call_actor_task)\#     

Run a saved Actor task on Apify and wait for results to be ready. :param task\_id: The ID or name of the task on the Apify platform. :type task\_id: str :param task\_input: The input object of the task that you’re trying to run.

> Overrides the task’s saved input.

Parameters:     

  * **dataset\_mapping\_function** \(_Callable_\) – A function that takes a single dictionary \(an Apify dataset item\) and converts it to an instance of the Document class.

  * **build** \(_str_ _,__optional_\) – Optionally specifies the actor build to run. It can be either a build tag or build number.

  * **memory\_mbytes** \(_int_ _,__optional_\) – Optional memory limit for the run, in megabytes.

  * **timeout\_secs** \(_int_ _,__optional_\) – Optional timeout for the run, in seconds.

  * **task\_id** \(_str_\)

  * **task\_input** \(_Dict_\)

Returns:     

A loader that will fetch the records from the     

task run’s default dataset.

Return type:     

[ApifyDatasetLoader](https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader.html#langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader "langchain_community.document_loaders.apify_dataset.ApifyDatasetLoader")

Examples using ApifyWrapper

  * [Apify](https://python.langchain.com/docs/integrations/providers/apify/)

  * [Apify Dataset](https://python.langchain.com/docs/integrations/document_loaders/apify_dataset/)

__On this page   *[\*]: Keyword-only parameters separator (PEP 3102)