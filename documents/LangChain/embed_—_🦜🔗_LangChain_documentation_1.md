# embed — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.helpers.embed.html
**Word Count:** 89
**Links Count:** 130
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# embed\#

langchain\_experimental.rl\_chain.helpers.embed\(

    _to\_embed : str | \_Embed | Dict | List\[str | \_Embed\] | List\[Dict\]_,     _model : Any_,     _namespace : str | None = None_, \) → List\[Dict\[str, str | List\[str\]\]\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/helpers.html#embed)\#     

Embed the actions or context using the SentenceTransformer model \(or a model that has an encode function\).

langchain\_experimental.rl\_chain.helpers.to\_embed\#     

\(Union\[Union\(str, \_Embed\(str\)\), Dict, List\[Union\(str, \_Embed\(str\)\)\], List\[Dict\]\], required\) The text to be embedded, either a string, a list of strings or a dictionary or a list of dictionaries.

langchain\_experimental.rl\_chain.helpers.namespace\#     

\(str, optional\) The default namespace to use when dictionary or list of dictionaries not provided.

langchain\_experimental.rl\_chain.helpers.model\#     

\(Any, required\) The model to use for embedding

Returns:     

A list of dictionaries where each dictionary has the namespace as the key and the embedded string as the value

Return type:     

List\[Dict\[str, str\]\]

Parameters:     

  * **to\_embed** \(_str_ _|__\_Embed_ _|__Dict_ _|__List_ _\[__str_ _|__\_Embed_ _\]__|__List_ _\[__Dict_ _\]_\)

  * **model** \(_Any_\)

  * **namespace** \(_str_ _|__None_\)

__On this page