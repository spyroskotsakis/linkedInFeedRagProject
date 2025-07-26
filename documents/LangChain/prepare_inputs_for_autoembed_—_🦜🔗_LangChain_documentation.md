# prepare_inputs_for_autoembed — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.base.prepare_inputs_for_autoembed.html
**Word Count:** 48
**Links Count:** 124
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# prepare\_inputs\_for\_autoembed\#

langchain\_experimental.rl\_chain.base.prepare\_inputs\_for\_autoembed\(

    _inputs : Dict\[str, Any\]_, \) → Dict\[str, Any\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/base.html#prepare_inputs_for_autoembed)\#     

Prepare the inputs for auto embedding.

Go over all the inputs and if something is either wrapped in \_ToSelectFrom or \_BasedOn, and if their inner values are not already \_Embed, then wrap them in EmbedAndKeep while retaining their \_ToSelectFrom or \_BasedOn status

Parameters:     

**inputs** \(_Dict_ _\[__str_ _,__Any_ _\]_\)

Return type:     

_Dict_\[str, _Any_\]

__On this page