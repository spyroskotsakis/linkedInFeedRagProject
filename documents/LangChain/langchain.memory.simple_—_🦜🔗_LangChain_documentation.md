# langchain.memory.simple — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/memory/simple.html
**Word Count:** 36
**Links Count:** 16
**Scraped:** 2025-07-21 07:58:35
**Status:** completed

---

# Source code for langchain.memory.simple               from typing import Any          from langchain_core.memory import BaseMemory                              [[docs]](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.simple.SimpleMemory.html#langchain.memory.simple.SimpleMemory)     class SimpleMemory(BaseMemory):         """Simple memory for storing context or other information that shouldn't         ever change between prompts.         """              memories: dict[str, Any] = {}              @property         def memory_variables(self) -> list[str]:             return list(self.memories.keys())                         [[docs]](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.simple.SimpleMemory.html#langchain.memory.simple.SimpleMemory.load_memory_variables)         def load_memory_variables(self, inputs: dict[str, Any]) -> dict[str, str]:             return self.memories                                        [[docs]](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.simple.SimpleMemory.html#langchain.memory.simple.SimpleMemory.save_context)         def save_context(self, inputs: dict[str, Any], outputs: dict[str, str]) -> None:             """Nothing should be saved or changed, my memory is set in stone."""                                        [[docs]](https://python.langchain.com/api_reference/langchain/memory/langchain.memory.simple.SimpleMemory.html#langchain.memory.simple.SimpleMemory.clear)         def clear(self) -> None:             """Nothing to clear, got a memory like a vault."""