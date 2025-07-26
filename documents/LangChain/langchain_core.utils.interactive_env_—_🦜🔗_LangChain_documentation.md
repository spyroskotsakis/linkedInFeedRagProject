# langchain_core.utils.interactive_env — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_core/utils/interactive_env.html
**Word Count:** 16
**Links Count:** 13
**Scraped:** 2025-07-21 08:57:58
**Status:** completed

---

# Source code for langchain\_core.utils.interactive\_env               """Utilities for working with interactive environments."""                              [[docs]](https://python.langchain.com/api_reference/core/utils/langchain_core.utils.interactive_env.is_interactive_env.html#langchain_core.utils.interactive_env.is_interactive_env)     def is_interactive_env() -> bool:         """Determine if running within IPython or Jupyter."""         import sys              return hasattr(sys, "ps2")