# RuleSchema — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.rule.RuleSchema.html
**Word Count:** 53
**Links Count:** 414
**Scraped:** 2025-07-21 08:23:06
**Status:** completed

---

# RuleSchema\#

_class _langchain\_community.tools.ainetwork.rule.RuleSchema[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/ainetwork/rule.html#RuleSchema)\#     

Bases: `BaseModel`

Schema for owner operations.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _eval _: str | None_ _ = None_\#     

eval string to determine permission

_param _path _: str_ _\[Required\]_\#     

Path on the blockchain where the rule applies

_param _type _: [OperationType](https://python.langchain.com/api_reference/community/tools/langchain_community.tools.ainetwork.base.OperationType.html#langchain_community.tools.ainetwork.base.OperationType "langchain_community.tools.ainetwork.base.OperationType")_ _\[Required\]_\#     

__On this page