# langchain-prompty: 0.1.1 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/prompty/index.html
**Word Count:** 101
**Links Count:** 95
**Scraped:** 2025-07-21 07:50:36
**Status:** completed

---

# langchain-prompty: 0.1.1\#

## [core](https://python.langchain.com/api_reference/prompty/core.html#langchain-prompty-core)\#

**Classes**

[`core.Frontmatter`](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Frontmatter.html#langchain_prompty.core.Frontmatter "langchain_prompty.core.Frontmatter")\(\) | Class for reading frontmatter from a string or file.   ---|---   [`core.Invoker`](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Invoker.html#langchain_prompty.core.Invoker "langchain_prompty.core.Invoker")\(prompty\) | Base class for all invokers.   [`core.InvokerFactory`](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.InvokerFactory.html#langchain_prompty.core.InvokerFactory "langchain_prompty.core.InvokerFactory")\(\) | Factory for creating invokers.   [`core.ModelSettings`](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.ModelSettings.html#langchain_prompty.core.ModelSettings "langchain_prompty.core.ModelSettings") | Model settings for a prompty model.   [`core.NoOpParser`](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.NoOpParser.html#langchain_prompty.core.NoOpParser "langchain_prompty.core.NoOpParser")\(prompty\) | NoOp parser for invokers.   [`core.Prompty`](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.Prompty.html#langchain_prompty.core.Prompty "langchain_prompty.core.Prompty") | Base Prompty model.   [`core.PropertySettings`](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.PropertySettings.html#langchain_prompty.core.PropertySettings "langchain_prompty.core.PropertySettings") | Property settings for a prompty model.   [`core.SimpleModel`](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.SimpleModel.html#langchain_prompty.core.SimpleModel "langchain_prompty.core.SimpleModel") | Simple model for a single item.   [`core.TemplateSettings`](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.TemplateSettings.html#langchain_prompty.core.TemplateSettings "langchain_prompty.core.TemplateSettings") | Template settings for a prompty model.      **Functions**

[`core.param_hoisting`](https://python.langchain.com/api_reference/prompty/core/langchain_prompty.core.param_hoisting.html#langchain_prompty.core.param_hoisting "langchain_prompty.core.param_hoisting")\(top, bottom\[, top\_key\]\) | Merge two dictionaries with hoisting of parameters from bottom to top.   ---|---      ## [langchain](https://python.langchain.com/api_reference/prompty/langchain.html#langchain-prompty-langchain)\#

**Functions**

[`langchain.create_chat_prompt`](https://python.langchain.com/api_reference/prompty/langchain/langchain_prompty.langchain.create_chat_prompt.html#langchain_prompty.langchain.create_chat_prompt "langchain_prompty.langchain.create_chat_prompt")\(path\[, ...\]\) | Create a chat prompt from a Langchain schema.   ---|---      ## [parsers](https://python.langchain.com/api_reference/prompty/parsers.html#langchain-prompty-parsers)\#

**Classes**

[`parsers.PromptyChatParser`](https://python.langchain.com/api_reference/prompty/parsers/langchain_prompty.parsers.PromptyChatParser.html#langchain_prompty.parsers.PromptyChatParser "langchain_prompty.parsers.PromptyChatParser")\(prompty\) | Parse a chat prompt into a list of messages.   ---|---   [`parsers.RoleMap`](https://python.langchain.com/api_reference/prompty/parsers/langchain_prompty.parsers.RoleMap.html#langchain_prompty.parsers.RoleMap "langchain_prompty.parsers.RoleMap")\(\) |       ## [renderers](https://python.langchain.com/api_reference/prompty/renderers.html#langchain-prompty-renderers)\#

**Classes**

[`renderers.MustacheRenderer`](https://python.langchain.com/api_reference/prompty/renderers/langchain_prompty.renderers.MustacheRenderer.html#langchain_prompty.renderers.MustacheRenderer "langchain_prompty.renderers.MustacheRenderer")\(prompty\) | Render a mustache template.   ---|---      ## [utils](https://python.langchain.com/api_reference/prompty/utils.html#langchain-prompty-utils)\#

**Functions**

[`utils.execute`](https://python.langchain.com/api_reference/prompty/utils/langchain_prompty.utils.execute.html#langchain_prompty.utils.execute "langchain_prompty.utils.execute")\(prompt\[, configuration, ...\]\) | Execute a prompty.   ---|---   [`utils.load`](https://python.langchain.com/api_reference/prompty/utils/langchain_prompty.utils.load.html#langchain_prompty.utils.load "langchain_prompty.utils.load")\(prompt\_path\[, configuration\]\) | Load a prompty file and return a Prompty object.   [`utils.prepare`](https://python.langchain.com/api_reference/prompty/utils/langchain_prompty.utils.prepare.html#langchain_prompty.utils.prepare "langchain_prompty.utils.prepare")\(prompt\[, inputs\]\) | Prepare the inputs for the prompty.   [`utils.run`](https://python.langchain.com/api_reference/prompty/utils/langchain_prompty.utils.run.html#langchain_prompty.utils.run "langchain_prompty.utils.run")\(prompt, content\[, configuration, ...\]\) | Run the prompty.