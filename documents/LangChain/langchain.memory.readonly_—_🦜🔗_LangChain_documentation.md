# langchain.memory.readonly — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/memory/readonly.html
**Word Count:** 32
**Links Count:** 16
**Scraped:** 2025-07-21 08:00:23
**Status:** completed

---

# Source code for langchain.memory.readonly               from typing import Any          from langchain_core.memory import BaseMemory                              [[docs]](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.readonly.ReadOnlySharedMemory.html#langchain.memory.readonly.ReadOnlySharedMemory)     class ReadOnlySharedMemory(BaseMemory):         """Memory wrapper that is read-only and cannot be changed."""              memory: BaseMemory              @property         def memory_variables(self) -> list[str]:             """Return memory variables."""             return self.memory.memory_variables                         [[docs]](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.readonly.ReadOnlySharedMemory.html#langchain.memory.readonly.ReadOnlySharedMemory.load_memory_variables)         def load_memory_variables(self, inputs: dict[str, Any]) -> dict[str, str]:             """Load memory variables from memory."""             return self.memory.load_memory_variables(inputs)                                        [[docs]](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.readonly.ReadOnlySharedMemory.html#langchain.memory.readonly.ReadOnlySharedMemory.save_context)         def save_context(self, inputs: dict[str, Any], outputs: dict[str, str]) -> None:             """Nothing should be saved or changed"""                                        [[docs]](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.readonly.ReadOnlySharedMemory.html#langchain.memory.readonly.ReadOnlySharedMemory.clear)         def clear(self) -> None:             """Nothing to clear, got a memory like a vault."""