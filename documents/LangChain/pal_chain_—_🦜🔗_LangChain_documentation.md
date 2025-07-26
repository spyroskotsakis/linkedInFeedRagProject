# pal_chain — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/pal_chain.html
**Word Count:** 26
**Links Count:** 96
**Scraped:** 2025-07-21 08:25:17
**Status:** completed

---

# `pal_chain`\#

**PAL Chain** implements **Program-Aided Language** Models.

See the paper: <https://arxiv.org/pdf/2211.10435.pdf>.

This chain is vulnerable to \[arbitrary code execution\]\([langchain-ai/langchain\#5872](https://github.com/langchain-ai/langchain/issues/5872)\).

**Classes**

[`pal_chain.base.PALChain`](https://python.langchain.com/api_reference/experimental/pal_chain/langchain_experimental.pal_chain.base.PALChain.html#langchain_experimental.pal_chain.base.PALChain "langchain_experimental.pal_chain.base.PALChain") | Chain that implements Program-Aided Language Models \(PAL\).   ---|---   [`pal_chain.base.PALValidation`](https://python.langchain.com/api_reference/experimental/pal_chain/langchain_experimental.pal_chain.base.PALValidation.html#langchain_experimental.pal_chain.base.PALValidation "langchain_experimental.pal_chain.base.PALValidation")\(\[...\]\) | Validation for PAL generated code.