# langchain-ibm: 0.3.15 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/ibm/index.html
**Word Count:** 60
**Links Count:** 93
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# langchain-ibm: 0.3.15\#

## [chat\_models](https://python.langchain.com/api_reference/ibm/chat_models.html#langchain-ibm-chat-models)\#

**Classes**

[`chat_models.ChatWatsonx`](https://python.langchain.com/api_reference/ibm/chat_models/langchain_ibm.chat_models.ChatWatsonx.html#langchain_ibm.chat_models.ChatWatsonx "langchain_ibm.chat_models.ChatWatsonx") | IBM watsonx.ai large language chat models.   ---|---      ## [embeddings](https://python.langchain.com/api_reference/ibm/embeddings.html#langchain-ibm-embeddings)\#

**Classes**

[`embeddings.WatsonxEmbeddings`](https://python.langchain.com/api_reference/ibm/embeddings/langchain_ibm.embeddings.WatsonxEmbeddings.html#langchain_ibm.embeddings.WatsonxEmbeddings "langchain_ibm.embeddings.WatsonxEmbeddings") | IBM watsonx.ai embedding models.   ---|---      ## [llms](https://python.langchain.com/api_reference/ibm/llms.html#langchain-ibm-llms)\#

**Classes**

[`llms.WatsonxLLM`](https://python.langchain.com/api_reference/ibm/llms/langchain_ibm.llms.WatsonxLLM.html#langchain_ibm.llms.WatsonxLLM "langchain_ibm.llms.WatsonxLLM") | IBM watsonx.ai large language models.   ---|---      ## [rerank](https://python.langchain.com/api_reference/ibm/rerank.html#langchain-ibm-rerank)\#

**Classes**

[`rerank.WatsonxRerank`](https://python.langchain.com/api_reference/ibm/rerank/langchain_ibm.rerank.WatsonxRerank.html#langchain_ibm.rerank.WatsonxRerank "langchain_ibm.rerank.WatsonxRerank") | Document compressor that uses watsonx Rerank API.   ---|---      ## [toolkit](https://python.langchain.com/api_reference/ibm/toolkit.html#langchain-ibm-toolkit)\#

**Classes**

[`toolkit.WatsonxTool`](https://python.langchain.com/api_reference/ibm/toolkit/langchain_ibm.toolkit.WatsonxTool.html#langchain_ibm.toolkit.WatsonxTool "langchain_ibm.toolkit.WatsonxTool") | IBM watsonx.ai Tool.   ---|---   [`toolkit.WatsonxToolkit`](https://python.langchain.com/api_reference/ibm/toolkit/langchain_ibm.toolkit.WatsonxToolkit.html#langchain_ibm.toolkit.WatsonxToolkit "langchain_ibm.toolkit.WatsonxToolkit") | IBM watsonx.ai Toolkit.      ## [utils](https://python.langchain.com/api_reference/ibm/utils.html#langchain-ibm-utils)\#

**Functions**

[`utils.async_gateway_error_handler`](https://python.langchain.com/api_reference/ibm/utils/langchain_ibm.utils.async_gateway_error_handler.html#langchain_ibm.utils.async_gateway_error_handler "langchain_ibm.utils.async_gateway_error_handler")\(func\) | Async decorator to catch ApiRequestFailure on Model Gateway calls and log a uniform warning.   ---|---   [`utils.check_duplicate_chat_params`](https://python.langchain.com/api_reference/ibm/utils/langchain_ibm.utils.check_duplicate_chat_params.html#langchain_ibm.utils.check_duplicate_chat_params "langchain_ibm.utils.check_duplicate_chat_params")\(params, kwargs\) |    [`utils.check_for_attribute`](https://python.langchain.com/api_reference/ibm/utils/langchain_ibm.utils.check_for_attribute.html#langchain_ibm.utils.check_for_attribute "langchain_ibm.utils.check_for_attribute")\(value, key, env\_key\) |    [`utils.convert_to_watsonx_tool`](https://python.langchain.com/api_reference/ibm/utils/langchain_ibm.utils.convert_to_watsonx_tool.html#langchain_ibm.utils.convert_to_watsonx_tool "langchain_ibm.utils.convert_to_watsonx_tool")\(tool\) | Convert WatsonxTool to watsonx tool structure.   [`utils.extract_chat_params`](https://python.langchain.com/api_reference/ibm/utils/langchain_ibm.utils.extract_chat_params.html#langchain_ibm.utils.extract_chat_params "langchain_ibm.utils.extract_chat_params")\(kwargs\[, ...\]\) |    [`utils.extract_params`](https://python.langchain.com/api_reference/ibm/utils/langchain_ibm.utils.extract_params.html#langchain_ibm.utils.extract_params "langchain_ibm.utils.extract_params")\(kwargs\[, default\_params\]\) |    [`utils.gateway_error_handler`](https://python.langchain.com/api_reference/ibm/utils/langchain_ibm.utils.gateway_error_handler.html#langchain_ibm.utils.gateway_error_handler "langchain_ibm.utils.gateway_error_handler")\(func\) | Decorator to catch ApiRequestFailure on Model Gateway calls and log a uniform warning.