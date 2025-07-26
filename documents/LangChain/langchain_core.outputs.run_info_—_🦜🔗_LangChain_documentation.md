# langchain_core.outputs.run_info — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_core/outputs/run_info.html
**Word Count:** 62
**Links Count:** 13
**Scraped:** 2025-07-21 08:57:35
**Status:** completed

---

# Source code for langchain\_core.outputs.run\_info               """RunInfo class."""          from __future__ import annotations          from uuid import UUID          from pydantic import BaseModel                              [[docs]](https://python.langchain.com/api_reference/core/outputs/langchain_core.outputs.run_info.RunInfo.html#langchain_core.outputs.run_info.RunInfo)     class RunInfo(BaseModel):         """Class that contains metadata for a single execution of a Chain or model.              Defined for backwards compatibility with older versions of langchain_core.              This model will likely be deprecated in the future.              Users can acquire the run_id information from callbacks or via run_id         information present in the astream_event API (depending on the use case).         """              run_id: UUID         """A unique identifier for the model or chain run."""