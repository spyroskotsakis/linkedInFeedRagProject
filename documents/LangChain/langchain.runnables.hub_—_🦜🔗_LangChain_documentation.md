# langchain.runnables.hub — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/runnables/hub.html
**Word Count:** 14
**Links Count:** 13
**Scraped:** 2025-07-21 08:25:40
**Status:** completed

---

# Source code for langchain.runnables.hub               from typing import Any, Optional          from langchain_core.runnables.base import RunnableBindingBase     from langchain_core.runnables.utils import Input, Output                              [[docs]](https://python.langchain.com/api_reference/langchain/runnables/langchain.runnables.hub.HubRunnable.html#langchain.runnables.hub.HubRunnable)     class HubRunnable(RunnableBindingBase[Input, Output]):         """         An instance of a runnable stored in the LangChain Hub.         """              owner_repo_commit: str              def __init__(             self,             owner_repo_commit: str,             *,             api_url: Optional[str] = None,             api_key: Optional[str] = None,             **kwargs: Any,         ) -> None:             from langchain.hub import pull                  pulled = pull(owner_repo_commit, api_url=api_url, api_key=api_key)             super_kwargs = {                 "kwargs": {},                 "config": {},                 **kwargs,                 "bound": pulled,                 "owner_repo_commit": owner_repo_commit,             }             super().__init__(**super_kwargs)