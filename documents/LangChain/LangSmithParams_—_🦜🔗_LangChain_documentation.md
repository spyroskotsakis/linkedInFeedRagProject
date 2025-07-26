# LangSmithParams — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.base.LangSmithParams.html
**Word Count:** 32
**Links Count:** 132
**Scraped:** 2025-07-21 07:53:34
**Status:** completed

---

# LangSmithParams\#

_class _langchain\_core.language\_models.base.LangSmithParams[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_core/language_models/base.html#LangSmithParams)\#     

LangSmith parameters for tracing.

ls\_provider _: str_\#     

Provider of the model.

ls\_model\_name _: str_\#     

Name of the model.

ls\_model\_type _: Literal\['chat', 'llm'\]_\#     

Type of the model. Should be ‘chat’ or ‘llm’.

ls\_temperature _: float | None_\#     

Temperature for generation.

ls\_max\_tokens _: int | None_\#     

Max tokens for generation.

ls\_stop _: list\[str\] | None_\#     

Stop words for generation.

__On this page