# langchain.evaluation.qa.generate_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/evaluation/qa/generate_chain.html
**Word Count:** 26
**Links Count:** 14
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# Source code for langchain.evaluation.qa.generate\_chain               """LLM Chain for generating examples for question answering."""          from __future__ import annotations          from typing import Any          from langchain_core.language_models import BaseLanguageModel     from langchain_core.output_parsers import BaseLLMOutputParser     from pydantic import Field          from langchain.chains.llm import LLMChain     from langchain.evaluation.qa.generate_prompt import PROMPT     from langchain.output_parsers.regex import RegexParser          _QA_OUTPUT_PARSER = RegexParser(         regex=r"QUESTION: (.*?)\n+ANSWER: (.*)",         output_keys=["query", "answer"],     )                              [[docs]](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.qa.generate_chain.QAGenerateChain.html#langchain.evaluation.qa.generate_chain.QAGenerateChain)     class QAGenerateChain(LLMChain):         """LLM Chain for generating examples for question answering."""              output_parser: BaseLLMOutputParser = Field(default=_QA_OUTPUT_PARSER)         output_key: str = "qa_pairs"              @classmethod         def is_lc_serializable(cls) -> bool:             return False                         [[docs]](https://python.langchain.com/api_reference/langchain/evaluation/langchain.evaluation.qa.generate_chain.QAGenerateChain.html#langchain.evaluation.qa.generate_chain.QAGenerateChain.from_llm)         @classmethod         def from_llm(cls, llm: BaseLanguageModel, **kwargs: Any) -> QAGenerateChain:             """Load QA Generate Chain from LLM."""             return cls(llm=llm, prompt=PROMPT, **kwargs)