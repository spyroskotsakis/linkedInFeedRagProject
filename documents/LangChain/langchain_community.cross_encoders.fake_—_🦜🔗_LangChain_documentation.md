# langchain_community.cross_encoders.fake — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_community/cross_encoders/fake.html
**Word Count:** 8
**Links Count:** 14
**Scraped:** 2025-07-21 09:14:56
**Status:** completed

---

# Source code for langchain\_community.cross\_encoders.fake               from difflib import SequenceMatcher     from typing import List, Tuple          from pydantic import BaseModel          from langchain_community.cross_encoders.base import BaseCrossEncoder                              [[docs]](https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.fake.FakeCrossEncoder.html#langchain_community.cross_encoders.fake.FakeCrossEncoder)     class FakeCrossEncoder(BaseCrossEncoder, BaseModel):         """Fake cross encoder model."""                         [[docs]](https://python.langchain.com/api_reference/community/cross_encoders/langchain_community.cross_encoders.fake.FakeCrossEncoder.html#langchain_community.cross_encoders.fake.FakeCrossEncoder.score)         def score(self, text_pairs: List[Tuple[str, str]]) -> List[float]:             scores = list(                 map(                     lambda pair: SequenceMatcher(None, pair[0], pair[1]).ratio(), text_pairs                 )             )             return scores