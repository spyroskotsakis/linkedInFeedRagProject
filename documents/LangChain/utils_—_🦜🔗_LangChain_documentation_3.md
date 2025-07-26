# utils — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/utils.html
**Word Count:** 73
**Links Count:** 108
**Scraped:** 2025-07-21 08:03:51
**Status:** completed

---

# `utils`\#

**Utility functions** for LangChain.

**Classes**

[`utils.ernie_functions.FunctionDescription`](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.ernie_functions.FunctionDescription.html#langchain_community.utils.ernie_functions.FunctionDescription "langchain_community.utils.ernie_functions.FunctionDescription") | Representation of a callable function to the Ernie API.   ---|---   [`utils.ernie_functions.ToolDescription`](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.ernie_functions.ToolDescription.html#langchain_community.utils.ernie_functions.ToolDescription "langchain_community.utils.ernie_functions.ToolDescription") | Representation of a callable function to the Ernie API.      **Functions**

[`utils.ernie_functions.convert_pydantic_to_ernie_function`](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.ernie_functions.convert_pydantic_to_ernie_function.html#langchain_community.utils.ernie_functions.convert_pydantic_to_ernie_function "langchain_community.utils.ernie_functions.convert_pydantic_to_ernie_function")\(...\) | Convert a Pydantic model to a function description for the Ernie API.   ---|---   [`utils.ernie_functions.convert_pydantic_to_ernie_tool`](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.ernie_functions.convert_pydantic_to_ernie_tool.html#langchain_community.utils.ernie_functions.convert_pydantic_to_ernie_tool "langchain_community.utils.ernie_functions.convert_pydantic_to_ernie_tool")\(...\) | Convert a Pydantic model to a function description for the Ernie API.   [`utils.google.get_client_info`](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.google.get_client_info.html#langchain_community.utils.google.get_client_info "langchain_community.utils.google.get_client_info")\(\[module\]\) | Return a custom user agent header.   [`utils.math.cosine_similarity`](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.math.cosine_similarity.html#langchain_community.utils.math.cosine_similarity "langchain_community.utils.math.cosine_similarity")\(X, Y\) | Row-wise cosine similarity between two equal-width matrices.   [`utils.math.cosine_similarity_top_k`](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.math.cosine_similarity_top_k.html#langchain_community.utils.math.cosine_similarity_top_k "langchain_community.utils.math.cosine_similarity_top_k")\(X, Y\[, ...\]\) | Row-wise cosine similarity with optional top-k and score threshold filtering.   [`utils.user_agent.get_user_agent`](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.user_agent.get_user_agent.html#langchain_community.utils.user_agent.get_user_agent "langchain_community.utils.user_agent.get_user_agent")\(\) | Get user agent from environment variable.