# base — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/base.html
**Word Count:** 35
**Links Count:** 85
**Scraped:** 2025-07-21 07:58:09
**Status:** completed

---

# `base`\#

**Classes**

[`base.Language`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")\(value\) | Enum of the programming languages.   ---|---   [`base.TextSplitter`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter")\(chunk\_size, chunk\_overlap, ...\) | Interface for splitting text into chunks.   [`base.TokenTextSplitter`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter "langchain_text_splitters.base.TokenTextSplitter")\(\[encoding\_name, ...\]\) | Splitting text to tokens using model tokenizer.   [`base.Tokenizer`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Tokenizer.html#langchain_text_splitters.base.Tokenizer "langchain_text_splitters.base.Tokenizer")\(chunk\_overlap, ...\) | Tokenizer data class.      **Functions**

[`base.split_text_on_tokens`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.split_text_on_tokens.html#langchain_text_splitters.base.split_text_on_tokens "langchain_text_splitters.base.split_text_on_tokens")\(\*, text, tokenizer\) | Split incoming text and return chunks using tokenizer.   ---|---