# langchain_experimental.rl_chain.vw_logger — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_experimental/rl_chain/vw_logger.html
**Word Count:** 8
**Links Count:** 16
**Scraped:** 2025-07-21 09:19:27
**Status:** completed

---

# Source code for langchain\_experimental.rl\_chain.vw\_logger               from os import PathLike     from pathlib import Path     from typing import Optional, Union                              [[docs]](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.vw_logger.VwLogger.html#langchain_experimental.rl_chain.vw_logger.VwLogger)     class VwLogger:         """Vowpal Wabbit custom logger."""                         [[docs]](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.vw_logger.VwLogger.html#langchain_experimental.rl_chain.vw_logger.VwLogger.__init__)         def __init__(self, path: Optional[Union[str, PathLike]]):             self.path = Path(path) if path else None             if self.path:                 self.path.parent.mkdir(parents=True, exist_ok=True)                                        [[docs]](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.vw_logger.VwLogger.html#langchain_experimental.rl_chain.vw_logger.VwLogger.log)         def log(self, vw_ex: str) -> None:             if self.path:                 with open(self.path, "a") as f:                     f.write(f"{vw_ex}\n\n")                                        [[docs]](https://python.langchain.com/api_reference/experimental/rl_chain/langchain_experimental.rl_chain.vw_logger.VwLogger.html#langchain_experimental.rl_chain.vw_logger.VwLogger.logging_enabled)         def logging_enabled(self) -> bool:             return bool(self.path)