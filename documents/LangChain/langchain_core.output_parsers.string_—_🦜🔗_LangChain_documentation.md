# langchain_core.output_parsers.string — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_core/output_parsers/string.html
**Word Count:** 39
**Links Count:** 14
**Scraped:** 2025-07-21 08:57:58
**Status:** completed

---

# Source code for langchain\_core.output\_parsers.string               """String output parser."""          from langchain_core.output_parsers.transform import BaseTransformOutputParser                              [[docs]](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html#langchain_core.output_parsers.string.StrOutputParser)     class StrOutputParser(BaseTransformOutputParser[str]):         """OutputParser that parses LLMResult into the top likely string."""              @classmethod         def is_lc_serializable(cls) -> bool:             """StrOutputParser is serializable.                  Returns:                 True             """             return True              @classmethod         def get_lc_namespace(cls) -> list[str]:             """Get the namespace of the langchain object.                  Default is ["langchain", "schema", "output_parser"].             """             return ["langchain", "schema", "output_parser"]              @property         def _type(self) -> str:             """Return the output parser type for serialization."""             return "default"                         [[docs]](https://python.langchain.com/api_reference/core/output_parsers/langchain_core.output_parsers.string.StrOutputParser.html#langchain_core.output_parsers.string.StrOutputParser.parse)         def parse(self, text: str) -> str:             """Returns the input text with no changes."""             return text