# langchain-text-splitters: 0.3.9 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/text_splitters/index.html
**Word Count:** 171
**Links Count:** 123
**Scraped:** 2025-07-21 07:48:33
**Status:** completed

---

# langchain-text-splitters: 0.3.9\#

**Text Splitters** are classes for splitting text.

**Class hierarchy:**               BaseDocumentTransformer --> TextSplitter --> <name>TextSplitter  # Example: CharacterTextSplitter                                                  RecursiveCharacterTextSplitter -->  <name>TextSplitter     

Note: **MarkdownHeaderTextSplitter** and \*\*HTMLHeaderTextSplitter do not derive from TextSplitter.

**Main helpers:**               Document, Tokenizer, Language, LineType, HeaderType     

## [base](https://python.langchain.com/api_reference/text_splitters/base.html#langchain-text-splitters-base)\#

**Classes**

[`base.Language`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language")\(value\) | Enum of the programming languages.   ---|---   [`base.TextSplitter`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TextSplitter.html#langchain_text_splitters.base.TextSplitter "langchain_text_splitters.base.TextSplitter")\(chunk\_size, chunk\_overlap, ...\) | Interface for splitting text into chunks.   [`base.TokenTextSplitter`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.TokenTextSplitter.html#langchain_text_splitters.base.TokenTextSplitter "langchain_text_splitters.base.TokenTextSplitter")\(\[encoding\_name, ...\]\) | Splitting text to tokens using model tokenizer.   [`base.Tokenizer`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Tokenizer.html#langchain_text_splitters.base.Tokenizer "langchain_text_splitters.base.Tokenizer")\(chunk\_overlap, ...\) | Tokenizer data class.      **Functions**

[`base.split_text_on_tokens`](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.split_text_on_tokens.html#langchain_text_splitters.base.split_text_on_tokens "langchain_text_splitters.base.split_text_on_tokens")\(\*, text, tokenizer\) | Split incoming text and return chunks using tokenizer.   ---|---      ## [character](https://python.langchain.com/api_reference/text_splitters/character.html#langchain-text-splitters-character)\#

**Classes**

[`character.CharacterTextSplitter`](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.CharacterTextSplitter.html#langchain_text_splitters.character.CharacterTextSplitter "langchain_text_splitters.character.CharacterTextSplitter")\(\[separator, ...\]\) | Splitting text that looks at characters.   ---|---   [`character.RecursiveCharacterTextSplitter`](https://python.langchain.com/api_reference/text_splitters/character/langchain_text_splitters.character.RecursiveCharacterTextSplitter.html#langchain_text_splitters.character.RecursiveCharacterTextSplitter "langchain_text_splitters.character.RecursiveCharacterTextSplitter")\(\[...\]\) | Splitting text by recursively look at characters.      ## [html](https://python.langchain.com/api_reference/text_splitters/html.html#langchain-text-splitters-html)\#

**Classes**

[`html.ElementType`](https://python.langchain.com/api_reference/text_splitters/html/langchain_text_splitters.html.ElementType.html#langchain_text_splitters.html.ElementType "langchain_text_splitters.html.ElementType") | Element type as typed dict.   ---|---   [`html.HTMLHeaderTextSplitter`](https://python.langchain.com/api_reference/text_splitters/html/langchain_text_splitters.html.HTMLHeaderTextSplitter.html#langchain_text_splitters.html.HTMLHeaderTextSplitter "langchain_text_splitters.html.HTMLHeaderTextSplitter")\(headers\_to\_split\_on\) | Split HTML content into structured Documents based on specified headers.   [`html.HTMLSectionSplitter`](https://python.langchain.com/api_reference/text_splitters/html/langchain_text_splitters.html.HTMLSectionSplitter.html#langchain_text_splitters.html.HTMLSectionSplitter "langchain_text_splitters.html.HTMLSectionSplitter")\(...\) | Splitting HTML files based on specified tag and font sizes.   [`html.HTMLSemanticPreservingSplitter`](https://python.langchain.com/api_reference/text_splitters/html/langchain_text_splitters.html.HTMLSemanticPreservingSplitter.html#langchain_text_splitters.html.HTMLSemanticPreservingSplitter "langchain_text_splitters.html.HTMLSemanticPreservingSplitter")\(...\[, ...\]\) |       ## [json](https://python.langchain.com/api_reference/text_splitters/json.html#langchain-text-splitters-json)\#

**Classes**

[`json.RecursiveJsonSplitter`](https://python.langchain.com/api_reference/text_splitters/json/langchain_text_splitters.json.RecursiveJsonSplitter.html#langchain_text_splitters.json.RecursiveJsonSplitter "langchain_text_splitters.json.RecursiveJsonSplitter")\(\[max\_chunk\_size, ...\]\) | Splits JSON data into smaller, structured chunks while preserving hierarchy.   ---|---      ## [jsx](https://python.langchain.com/api_reference/text_splitters/jsx.html#langchain-text-splitters-jsx)\#

**Classes**

[`jsx.JSFrameworkTextSplitter`](https://python.langchain.com/api_reference/text_splitters/jsx/langchain_text_splitters.jsx.JSFrameworkTextSplitter.html#langchain_text_splitters.jsx.JSFrameworkTextSplitter "langchain_text_splitters.jsx.JSFrameworkTextSplitter")\(\[separators, ...\]\) | Text splitter that handles React \(JSX\), Vue, and Svelte code.   ---|---      ## [konlpy](https://python.langchain.com/api_reference/text_splitters/konlpy.html#langchain-text-splitters-konlpy)\#

**Classes**

[`konlpy.KonlpyTextSplitter`](https://python.langchain.com/api_reference/text_splitters/konlpy/langchain_text_splitters.konlpy.KonlpyTextSplitter.html#langchain_text_splitters.konlpy.KonlpyTextSplitter "langchain_text_splitters.konlpy.KonlpyTextSplitter")\(\[separator\]\) | Splitting text using Konlpy package.   ---|---      ## [latex](https://python.langchain.com/api_reference/text_splitters/latex.html#langchain-text-splitters-latex)\#

**Classes**

[`latex.LatexTextSplitter`](https://python.langchain.com/api_reference/text_splitters/latex/langchain_text_splitters.latex.LatexTextSplitter.html#langchain_text_splitters.latex.LatexTextSplitter "langchain_text_splitters.latex.LatexTextSplitter")\(\*\*kwargs\) | Attempts to split the text along Latex-formatted layout elements.   ---|---      ## [markdown](https://python.langchain.com/api_reference/text_splitters/markdown.html#langchain-text-splitters-markdown)\#

**Classes**

[`markdown.ExperimentalMarkdownSyntaxTextSplitter`](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.ExperimentalMarkdownSyntaxTextSplitter.html#langchain_text_splitters.markdown.ExperimentalMarkdownSyntaxTextSplitter "langchain_text_splitters.markdown.ExperimentalMarkdownSyntaxTextSplitter")\(\[...\]\) | An experimental text splitter for handling Markdown syntax.   ---|---   [`markdown.HeaderType`](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.HeaderType.html#langchain_text_splitters.markdown.HeaderType "langchain_text_splitters.markdown.HeaderType") | Header type as typed dict.   [`markdown.LineType`](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.LineType.html#langchain_text_splitters.markdown.LineType "langchain_text_splitters.markdown.LineType") | Line type as typed dict.   [`markdown.MarkdownHeaderTextSplitter`](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.MarkdownHeaderTextSplitter.html#langchain_text_splitters.markdown.MarkdownHeaderTextSplitter "langchain_text_splitters.markdown.MarkdownHeaderTextSplitter")\(...\[, ...\]\) | Splitting markdown files based on specified headers.   [`markdown.MarkdownTextSplitter`](https://python.langchain.com/api_reference/text_splitters/markdown/langchain_text_splitters.markdown.MarkdownTextSplitter.html#langchain_text_splitters.markdown.MarkdownTextSplitter "langchain_text_splitters.markdown.MarkdownTextSplitter")\(\*\*kwargs\) | Attempts to split the text along Markdown-formatted headings.      ## [nltk](https://python.langchain.com/api_reference/text_splitters/nltk.html#langchain-text-splitters-nltk)\#

**Classes**

[`nltk.NLTKTextSplitter`](https://python.langchain.com/api_reference/text_splitters/nltk/langchain_text_splitters.nltk.NLTKTextSplitter.html#langchain_text_splitters.nltk.NLTKTextSplitter "langchain_text_splitters.nltk.NLTKTextSplitter")\(\[separator, language, ...\]\) | Splitting text using NLTK package.   ---|---      ## [python](https://python.langchain.com/api_reference/text_splitters/python.html#langchain-text-splitters-python)\#

**Classes**

[`python.PythonCodeTextSplitter`](https://python.langchain.com/api_reference/text_splitters/python/langchain_text_splitters.python.PythonCodeTextSplitter.html#langchain_text_splitters.python.PythonCodeTextSplitter "langchain_text_splitters.python.PythonCodeTextSplitter")\(\*\*kwargs\) | Attempts to split the text along Python syntax.   ---|---      ## [sentence\_transformers](https://python.langchain.com/api_reference/text_splitters/sentence_transformers.html#langchain-text-splitters-sentence-transformers)\#

**Classes**

[`sentence_transformers.SentenceTransformersTokenTextSplitter`](https://python.langchain.com/api_reference/text_splitters/sentence_transformers/langchain_text_splitters.sentence_transformers.SentenceTransformersTokenTextSplitter.html#langchain_text_splitters.sentence_transformers.SentenceTransformersTokenTextSplitter "langchain_text_splitters.sentence_transformers.SentenceTransformersTokenTextSplitter")\(\[...\]\) | Splitting text to tokens using sentence model tokenizer.   ---|---      ## [spacy](https://python.langchain.com/api_reference/text_splitters/spacy.html#langchain-text-splitters-spacy)\#

**Classes**

[`spacy.SpacyTextSplitter`](https://python.langchain.com/api_reference/text_splitters/spacy/langchain_text_splitters.spacy.SpacyTextSplitter.html#langchain_text_splitters.spacy.SpacyTextSplitter "langchain_text_splitters.spacy.SpacyTextSplitter")\(\[separator, ...\]\) | Splitting text using Spacy package.   ---|---