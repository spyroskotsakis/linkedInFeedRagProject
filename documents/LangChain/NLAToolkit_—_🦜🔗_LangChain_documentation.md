# NLAToolkit — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.nla.toolkit.NLAToolkit.html
**Word Count:** 203
**Links Count:** 210
**Scraped:** 2025-07-21 08:16:51
**Status:** completed

---

# NLAToolkit\#

_class _langchain\_community.agent\_toolkits.nla.toolkit.NLAToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/nla/toolkit.html#NLAToolkit)\#     

Bases: [`BaseToolkit`](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseToolkit.html#langchain_core.tools.base.BaseToolkit "langchain_core.tools.base.BaseToolkit")

Natural Language API Toolkit.

_Security Note_ : This toolkit creates tools that enable making calls     

to an Open API compliant API.

The tools created by this toolkit may be able to make GET, POST, PATCH, PUT, DELETE requests to any of the exposed endpoints on the API.

Control access to who can use this toolkit.

See <https://python.langchain.com/docs/security> for more information.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _nla\_tools _: Sequence\[[NLATool](https://python.langchain.com/api_reference/community/agent_toolkits/langchain_community.agent_toolkits.nla.tool.NLATool.html#langchain_community.agent_toolkits.nla.tool.NLATool "langchain_community.agent_toolkits.nla.tool.NLATool")\]__\[Required\]_\#     

List of API Endpoint Tools.

_classmethod _from\_llm\_and\_ai\_plugin\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _ai\_plugin : [AIPlugin](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.plugin.AIPlugin.html#langchain_community.tools.plugin.AIPlugin "langchain_community.tools.plugin.AIPlugin")_,     _requests : [Requests](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html#langchain_community.utilities.requests.Requests "langchain_community.utilities.requests.Requests") | None = None_,     _verbose : bool = False_,     _\*\* kwargs: Any_, \) → NLAToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/nla/toolkit.html#NLAToolkit.from_llm_and_ai_plugin)\#     

Instantiate the toolkit from an OpenAPI Spec URL

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **ai\_plugin** \([_AIPlugin_](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.plugin.AIPlugin.html#langchain_community.tools.plugin.AIPlugin "langchain_community.tools.plugin.AIPlugin")\)

  * **requests** \([_Requests_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html#langchain_community.utilities.requests.Requests "langchain_community.utilities.requests.Requests") _|__None_\)

  * **verbose** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_NLAToolkit_

_classmethod _from\_llm\_and\_ai\_plugin\_url\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _ai\_plugin\_url : str_,     _requests : [Requests](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html#langchain_community.utilities.requests.Requests "langchain_community.utilities.requests.Requests") | None = None_,     _verbose : bool = False_,     _\*\* kwargs: Any_, \) → NLAToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/nla/toolkit.html#NLAToolkit.from_llm_and_ai_plugin_url)\#     

Instantiate the toolkit from an OpenAPI Spec URL

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\)

  * **ai\_plugin\_url** \(_str_\)

  * **requests** \([_Requests_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html#langchain_community.utilities.requests.Requests "langchain_community.utilities.requests.Requests") _|__None_\)

  * **verbose** \(_bool_\)

  * **kwargs** \(_Any_\)

Return type:     

_NLAToolkit_

_classmethod _from\_llm\_and\_spec\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _spec : [OpenAPISpec](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")_,     _requests : [Requests](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html#langchain_community.utilities.requests.Requests "langchain_community.utilities.requests.Requests") | None = None_,     _verbose : bool = False_,     _\*\* kwargs: Any_, \) → NLAToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/nla/toolkit.html#NLAToolkit.from_llm_and_spec)\#     

Instantiate the toolkit by creating tools for each operation.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **spec** \([_OpenAPISpec_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.openapi.OpenAPISpec.html#langchain_community.utilities.openapi.OpenAPISpec "langchain_community.utilities.openapi.OpenAPISpec")\) – The OpenAPI spec.

  * **requests** \([_Requests_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html#langchain_community.utilities.requests.Requests "langchain_community.utilities.requests.Requests") _|__None_\) – Optional requests object. Default is None.

  * **verbose** \(_bool_\) – Whether to print verbose output. Default is False.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The toolkit.

Return type:     

_NLAToolkit_

_classmethod _from\_llm\_and\_url\(

    _llm : [BaseLanguageModel](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")_,     _open\_api\_url : str_,     _requests : [Requests](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html#langchain_community.utilities.requests.Requests "langchain_community.utilities.requests.Requests") | None = None_,     _verbose : bool = False_,     _\*\* kwargs: Any_, \) → NLAToolkit[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/nla/toolkit.html#NLAToolkit.from_llm_and_url)\#     

Instantiate the toolkit from an OpenAPI Spec URL.

Parameters:     

  * **llm** \([_BaseLanguageModel_](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.BaseLanguageModel.html#langchain_core.language_models.base.BaseLanguageModel "langchain_core.language_models.base.BaseLanguageModel")\) – The language model to use.

  * **open\_api\_url** \(_str_\) – The URL of the OpenAPI spec.

  * **requests** \([_Requests_](https://python.langchain.com/api_reference/community/utilities/langchain_community.utilities.requests.Requests.html#langchain_community.utilities.requests.Requests "langchain_community.utilities.requests.Requests") _|__None_\) – Optional requests object. Default is None.

  * **verbose** \(_bool_\) – Whether to print verbose output. Default is False.

  * **kwargs** \(_Any_\) – Additional arguments.

Returns:     

The toolkit.

Return type:     

_NLAToolkit_

get\_tools\(\) → List\[[BaseTool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/agent_toolkits/nla/toolkit.html#NLAToolkit.get_tools)\#     

Get the tools for all the API operations.

Return type:     

_List_\[[_BaseTool_](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.base.BaseTool.html#langchain_core.tools.base.BaseTool "langchain_core.tools.base.BaseTool")\]

Examples using NLAToolkit

  * [Natural Language API Toolkits](https://python.langchain.com/docs/integrations/tools/openapi_nla/)

__On this page