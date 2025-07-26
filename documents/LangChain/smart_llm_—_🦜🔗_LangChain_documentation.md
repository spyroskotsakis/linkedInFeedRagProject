# smart_llm — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/smart_llm.html
**Word Count:** 120
**Links Count:** 93
**Scraped:** 2025-07-21 08:24:00
**Status:** completed

---

# `smart_llm`\#

**SmartGPT** chain is applying self-critique using the SmartGPT workflow.

See details at <https://youtu.be/wVzuvf9D9BU>

The workflow performs these 3 steps: 1\. **Ideate** : Pass the user prompt to an Ideation LLM n\_ideas times,

> each result is an “idea”

  2. **Critique** : Pass the ideas to a Critique LLM which looks for flaws in the ideas & picks the best one

  3. **Resolve** : Pass the critique to a Resolver LLM which improves upon the best idea & outputs only the \(improved version of\) the best output

In total, the SmartGPT workflow will use n\_ideas+2 LLM calls

Note that SmartLLMChain will only improve results \(compared to a basic LLMChain\), when the underlying models have the capability for reflection, which smaller models often don’t.

Finally, a SmartLLMChain assumes that each underlying LLM outputs exactly 1 result.

**Classes**

[`smart_llm.base.SmartLLMChain`](https://python.langchain.com/api_reference/experimental/smart_llm/langchain_experimental.smart_llm.base.SmartLLMChain.html#langchain_experimental.smart_llm.base.SmartLLMChain "langchain_experimental.smart_llm.base.SmartLLMChain") | Chain for applying self-critique using the SmartGPT workflow.   ---|---