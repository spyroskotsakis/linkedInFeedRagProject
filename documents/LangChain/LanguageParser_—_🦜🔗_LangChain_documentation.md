# LanguageParser — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/document_loaders/langchain_community.document_loaders.parsers.language.language_parser.LanguageParser.html
**Word Count:** 286
**Links Count:** 406
**Scraped:** 2025-07-21 08:11:13
**Status:** completed

---

# LanguageParser\#

_class _langchain\_community.document\_loaders.parsers.language.language\_parser.LanguageParser\(

    _language : Literal\['cpp', 'go', 'java', 'kotlin', 'js', 'ts', 'php', 'proto', 'python', 'rst', 'ruby', 'rust', 'scala', 'markdown', 'latex', 'html', 'sol', 'csharp', 'cobol', 'c', 'lua', 'perl', 'elixir', 'sql'\] | None = None_,     _parser\_threshold : int = 0_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/language_parser.html#LanguageParser)\#     

Parse using the respective programming language syntax.

Each top-level function and class in the code is loaded into separate documents. Furthermore, an extra document is generated, containing the remaining top-level code that excludes the already segmented functions and classes.

This approach can potentially improve the accuracy of QA models over source code.

The supported languages for code parsing are:

  * C: “c” \(\*\)

  * C++: “cpp” \(\*\)

  * C\#: “csharp” \(\*\)

  * COBOL: “cobol”

  * Elixir: “elixir”

  * Go: “go” \(\*\)

  * Java: “java” \(\*\)

  * JavaScript: “js” \(requires package esprima\)

  * Kotlin: “kotlin” \(\*\)

  * Lua: “lua” \(\*\)

  * Perl: “perl” \(\*\)

  * Python: “python”

  * Ruby: “ruby” \(\*\)

  * Rust: “rust” \(\*\)

  * Scala: “scala” \(\*\)

  * SQL: “sql” \(\*\)

  * TypeScript: “ts” \(\*\)

Items marked with \(\*\) require the packages tree\_sitter and tree\_sitter\_languages. It is straightforward to add support for additional languages using tree\_sitter, although this currently requires modifying LangChain.

The language used for parsing can be configured, along with the minimum number of lines required to activate the splitting based on syntax.

If a language is not explicitly specified, LanguageParser will infer one from filename extensions, if present.

Examples                   from langchain_community.document_loaders.generic import GenericLoader         from langchain_community.document_loaders.parsers import LanguageParser              loader = GenericLoader.from_filesystem(             "./code",             glob="**/*",             suffixes=[".py", ".js"],             parser=LanguageParser()         )         docs = loader.load()          Example instantiations to manually select the language:          .. code-block:: python                   loader = GenericLoader.from_filesystem(             "./code",             glob="**/*",             suffixes=[".py"],             parser=LanguageParser(language="python")         )          Example instantiations to set number of lines threshold:          .. code-block:: python              loader = GenericLoader.from_filesystem(             "./code",             glob="**/*",             suffixes=[".py"],             parser=LanguageParser(parser_threshold=200)         )     

Language parser that split code using the respective language syntax.

Parameters:     

  * **language** \(_Optional_ _\[_[_Language_](https://python.langchain.com/api_reference/text_splitters/base/langchain_text_splitters.base.Language.html#langchain_text_splitters.base.Language "langchain_text_splitters.base.Language") _\]_\) – If None \(default\), it will try to infer language from source.

  * **parser\_threshold** \(_int_\) – Minimum lines needed to activate parsing \(0 by default\).

Methods

`__init__`\(\[language, parser\_threshold\]\) | Language parser that split code using the respective language syntax.   ---|---   `lazy_parse`\(blob\) | Lazy parsing interface.   `parse`\(blob\) | Eagerly parse the blob into a document or documents.      \_\_init\_\_\(

    _language : Literal\['cpp', 'go', 'java', 'kotlin', 'js', 'ts', 'php', 'proto', 'python', 'rst', 'ruby', 'rust', 'scala', 'markdown', 'latex', 'html', 'sol', 'csharp', 'cobol', 'c', 'lua', 'perl', 'elixir', 'sql'\] | None = None_,     _parser\_threshold : int = 0_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/language_parser.html#LanguageParser.__init__)\#     

Language parser that split code using the respective language syntax.

Parameters:     

  * **language** \(_Literal_ _\[__'cpp'__,__'go'__,__'java'__,__'kotlin'__,__'js'__,__'ts'__,__'php'__,__'proto'__,__'python'__,__'rst'__,__'ruby'__,__'rust'__,__'scala'__,__'markdown'__,__'latex'__,__'html'__,__'sol'__,__'csharp'__,__'cobol'__,__'c'__,__'lua'__,__'perl'__,__'elixir'__,__'sql'__\]__|__None_\) – If None \(default\), it will try to infer language from source.

  * **parser\_threshold** \(_int_\) – Minimum lines needed to activate parsing \(0 by default\).

lazy\_parse\(

    _blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_, \) → Iterator\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\][\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/document_loaders/parsers/language/language_parser.html#LanguageParser.lazy_parse)\#     

Lazy parsing interface.

Subclasses are required to implement this method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

Generator of documents

Return type:     

_Iterator_\[[_Document_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

parse\(_blob : [Blob](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")_\) → list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]\#     

Eagerly parse the blob into a document or documents.

This is a convenience method for interactive development environment.

Production applications should favor the lazy\_parse method instead.

Subclasses should generally not over-ride this parse method.

Parameters:     

**blob** \([_Blob_](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Blob.html#langchain_core.documents.base.Blob "langchain_core.documents.base.Blob")\) – Blob instance

Returns:     

List of documents

Return type:     

list\[[Document](https://python.langchain.com/api_reference/core/documents/langchain_core.documents.base.Document.html#langchain_core.documents.base.Document "langchain_core.documents.base.Document")\]

Examples using LanguageParser

  * [Source Code](https://python.langchain.com/docs/integrations/document_loaders/source_code/)

__On this page