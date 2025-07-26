# langchain_community.llms.utils — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/llms/utils.html
**Word Count:** 20
**Links Count:** 13
**Scraped:** 2025-07-21 09:17:16
**Status:** completed

---

# Source code for langchain\_community.llms.utils               """Common utility functions for LLM APIs."""          import re     from typing import List                              [[docs]](https://python.langchain.com/api_reference/community/llms/langchain_community.llms.utils.enforce_stop_tokens.html#langchain_community.llms.utils.enforce_stop_tokens)     def enforce_stop_tokens(text: str, stop: List[str]) -> str:         """Cut off the text as soon as any stop words occur."""         return re.split("|".join(stop), text, maxsplit=1)[0]