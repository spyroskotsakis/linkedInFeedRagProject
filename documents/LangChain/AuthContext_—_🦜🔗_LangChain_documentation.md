# AuthContext — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/chains/langchain_community.chains.pebblo_retrieval.models.AuthContext.html
**Word Count:** 64
**Links Count:** 166
**Scraped:** 2025-07-21 08:10:45
**Status:** completed

---

# AuthContext\#

_class _langchain\_community.chains.pebblo\_retrieval.models.AuthContext[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/chains/pebblo_retrieval/models.html#AuthContext)\#     

Bases: `BaseModel`

Class for an authorization context.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _name _: str | None_ _ = None_\#     

_param _user\_auth _: List\[str\]__\[Required\]_\#     

List of user authorizations, which may include their User ID and the groups they are part of

_param _user\_id _: str_ _\[Required\]_\#     

Examples using AuthContext

  * [Identity-enabled RAG using PebbloRetrievalQA](https://python.langchain.com/docs/integrations/providers/pebblo/pebblo_retrieval_qa/)

__On this page