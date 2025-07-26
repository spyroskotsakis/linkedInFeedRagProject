# langchain_experimental.tot.thought — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_experimental/tot/thought.html
**Word Count:** 15
**Links Count:** 14
**Scraped:** 2025-07-21 09:19:27
**Status:** completed

---

# Source code for langchain\_experimental.tot.thought               from __future__ import annotations          from enum import Enum     from typing import Set          from pydantic import BaseModel, Field                              [[docs]](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.ThoughtValidity.html#langchain_experimental.tot.thought.ThoughtValidity)     class ThoughtValidity(Enum):         """Enum for the validity of a thought."""              VALID_INTERMEDIATE = 0         VALID_FINAL = 1         INVALID = 2                                             [[docs]](https://python.langchain.com/api_reference/experimental/tot/langchain_experimental.tot.thought.Thought.html#langchain_experimental.tot.thought.Thought)     class Thought(BaseModel):         """A thought in the ToT."""              text: str         validity: ThoughtValidity         children: Set[Thought] = Field(default_factory=set)              def __hash__(self) -> int:             return id(self)