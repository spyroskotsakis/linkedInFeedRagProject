# langchain_prompty.renderers — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain_prompty/renderers.html
**Word Count:** 15
**Links Count:** 15
**Scraped:** 2025-07-21 09:20:15
**Status:** completed

---

# Source code for langchain\_prompty.renderers               from langchain_core.utils import mustache     from pydantic import BaseModel          from .core import Invoker, Prompty, SimpleModel                              [[docs]](https://python.langchain.com/api_reference/prompty/renderers/langchain_prompty.renderers.MustacheRenderer.html#langchain_prompty.renderers.MustacheRenderer)     class MustacheRenderer(Invoker):         """Render a mustache template."""                         [[docs]](https://python.langchain.com/api_reference/prompty/renderers/langchain_prompty.renderers.MustacheRenderer.html#langchain_prompty.renderers.MustacheRenderer.__init__)         def __init__(self, prompty: Prompty) -> None:             self.prompty = prompty                                        [[docs]](https://python.langchain.com/api_reference/prompty/renderers/langchain_prompty.renderers.MustacheRenderer.html#langchain_prompty.renderers.MustacheRenderer.invoke)         def invoke(self, data: BaseModel) -> BaseModel:             if not isinstance(data, SimpleModel):                 raise ValueError("Expected data to be an instance of SimpleModel")             generated = mustache.render(self.prompty.content, data.item)             return SimpleModel[str](item=generated)