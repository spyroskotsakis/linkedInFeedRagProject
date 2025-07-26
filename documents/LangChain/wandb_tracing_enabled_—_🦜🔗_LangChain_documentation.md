# wandb_tracing_enabled — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/callbacks/langchain_community.callbacks.manager.wandb_tracing_enabled.html
**Word Count:** 32
**Links Count:** 182
**Scraped:** 2025-07-21 08:18:17
**Status:** completed

---

# wandb\_tracing\_enabled\#

langchain\_community.callbacks.manager.wandb\_tracing\_enabled\(

    _session\_name : str = 'default'_, \) → Generator\[None, None, None\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/callbacks/manager.html#wandb_tracing_enabled)\#     

Get the WandbTracer in a context manager.

Parameters:     

**session\_name** \(_str_ _,__optional_\) – The name of the session. Defaults to “default”.

Returns:     

None

Return type:     

_Generator_\[None, None, None\]

Example               >>> with wandb_tracing_enabled() as session:     ...     # Use the WandbTracer session     

Examples using wandb\_tracing\_enabled

  * [WandB Tracing](https://python.langchain.com/docs/integrations/providers/wandb_tracing/)

__On this page