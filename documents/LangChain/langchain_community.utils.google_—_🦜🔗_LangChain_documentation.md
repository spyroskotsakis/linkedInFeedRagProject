# langchain_community.utils.google — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/utils/google.html
**Word Count:** 24
**Links Count:** 13
**Scraped:** 2025-07-21 09:16:48
**Status:** completed

---

# Source code for langchain\_community.utils.google               """Utilities to use Google provided components."""          from importlib import metadata     from typing import Any, Optional                              [[docs]](https://python.langchain.com/api_reference/community/utils/langchain_community.utils.google.get_client_info.html#langchain_community.utils.google.get_client_info)     def get_client_info(module: Optional[str] = None) -> Any:         r"""Return a custom user agent header.              Args:             module (Optional[str]):                 Optional. The module for a custom user agent header.         Returns:             google.api_core.gapic_v1.client_info.ClientInfo         """         from google.api_core.gapic_v1.client_info import ClientInfo              langchain_version = metadata.version("langchain")         client_library_version = (             f"{langchain_version}-{module}" if module else langchain_version         )         return ClientInfo(             client_library_version=client_library_version,             user_agent=f"langchain/{client_library_version}",         )