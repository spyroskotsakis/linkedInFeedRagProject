# langchain-upstage: 0.6.0 — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/upstage/index.html
**Word Count:** 71
**Links Count:** 88
**Scraped:** 2025-07-21 07:51:39
**Status:** completed

---

# langchain-upstage: 0.6.0\#

## [chat\_models](https://python.langchain.com/api_reference/upstage/chat_models.html#langchain-upstage-chat-models)\#

**Classes**

[`chat_models.ChatUpstage`](https://python.langchain.com/api_reference/upstage/chat_models/langchain_upstage.chat_models.ChatUpstage.html#langchain_upstage.chat_models.ChatUpstage "langchain_upstage.chat_models.ChatUpstage") | ChatUpstage chat model.   ---|---      ## [document\_parse](https://python.langchain.com/api_reference/upstage/document_parse.html#langchain-upstage-document-parse)\#

**Classes**

[`document_parse.UpstageDocumentParseLoader`](https://python.langchain.com/api_reference/upstage/document_parse/langchain_upstage.document_parse.UpstageDocumentParseLoader.html#langchain_upstage.document_parse.UpstageDocumentParseLoader "langchain_upstage.document_parse.UpstageDocumentParseLoader")\(...\) | Upstage Document Parse Loader.   ---|---      **Functions**

[`document_parse.get_from_param_or_env`](https://python.langchain.com/api_reference/upstage/document_parse/langchain_upstage.document_parse.get_from_param_or_env.html#langchain_upstage.document_parse.get_from_param_or_env "langchain_upstage.document_parse.get_from_param_or_env")\(key\[, ...\]\) | Get a value from a param or an environment variable.   ---|---   [`document_parse.validate_file_path`](https://python.langchain.com/api_reference/upstage/document_parse/langchain_upstage.document_parse.validate_file_path.html#langchain_upstage.document_parse.validate_file_path "langchain_upstage.document_parse.validate_file_path")\(file\_path\) | Validates if a file exists at the given file path.      ## [document\_parse\_parsers](https://python.langchain.com/api_reference/upstage/document_parse_parsers.html#langchain-upstage-document-parse-parsers)\#

**Classes**

[`document_parse_parsers.UpstageDocumentParseParser`](https://python.langchain.com/api_reference/upstage/document_parse_parsers/langchain_upstage.document_parse_parsers.UpstageDocumentParseParser.html#langchain_upstage.document_parse_parsers.UpstageDocumentParseParser "langchain_upstage.document_parse_parsers.UpstageDocumentParseParser")\(\[...\]\) | Upstage Document Parse Parser.   ---|---      **Functions**

[`document_parse_parsers.get_from_param_or_env`](https://python.langchain.com/api_reference/upstage/document_parse_parsers/langchain_upstage.document_parse_parsers.get_from_param_or_env.html#langchain_upstage.document_parse_parsers.get_from_param_or_env "langchain_upstage.document_parse_parsers.get_from_param_or_env")\(key\) | Get a value from a param or an environment variable.   ---|---   [`document_parse_parsers.parse_output`](https://python.langchain.com/api_reference/upstage/document_parse_parsers/langchain_upstage.document_parse_parsers.parse_output.html#langchain_upstage.document_parse_parsers.parse_output "langchain_upstage.document_parse_parsers.parse_output")\(data, ...\) | Parse the output data based on the specified output type.      ## [embeddings](https://python.langchain.com/api_reference/upstage/embeddings.html#langchain-upstage-embeddings)\#

**Classes**

[`embeddings.UpstageEmbeddings`](https://python.langchain.com/api_reference/upstage/embeddings/langchain_upstage.embeddings.UpstageEmbeddings.html#langchain_upstage.embeddings.UpstageEmbeddings "langchain_upstage.embeddings.UpstageEmbeddings") | UpstageEmbeddings embedding model.   ---|---      ## [tools](https://python.langchain.com/api_reference/upstage/tools.html#langchain-upstage-tools)\#

**Classes**

[`tools.groundedness_check.UpstageGroundednessCheck`](https://python.langchain.com/api_reference/upstage/tools/langchain_upstage.tools.groundedness_check.UpstageGroundednessCheck.html#langchain_upstage.tools.groundedness_check.UpstageGroundednessCheck "langchain_upstage.tools.groundedness_check.UpstageGroundednessCheck") | Tool that checks the groundedness of a context and an assistant message.   ---|---   [`tools.groundedness_check.UpstageGroundednessCheckInput`](https://python.langchain.com/api_reference/upstage/tools/langchain_upstage.tools.groundedness_check.UpstageGroundednessCheckInput.html#langchain_upstage.tools.groundedness_check.UpstageGroundednessCheckInput "langchain_upstage.tools.groundedness_check.UpstageGroundednessCheckInput") | Input for the Groundedness Check tool.      **Deprecated classes**

[`tools.groundedness_check.GroundednessCheck`](https://python.langchain.com/api_reference/upstage/tools/langchain_upstage.tools.groundedness_check.GroundednessCheck.html#langchain_upstage.tools.groundedness_check.GroundednessCheck "langchain_upstage.tools.groundedness_check.GroundednessCheck") |    ---|---