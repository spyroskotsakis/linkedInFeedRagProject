# langchain.output_parsers.loading — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/_modules/langchain/output_parsers/loading.html
**Word Count:** 17
**Links Count:** 13
**Scraped:** 2025-07-21 07:59:00
**Status:** completed

---

# Source code for langchain.output\_parsers.loading               from langchain.output_parsers.regex import RegexParser                              [[docs]](https://python.langchain.com/api_reference/langchain/output_parsers/langchain.output_parsers.loading.load_output_parser.html#langchain.output_parsers.loading.load_output_parser)     def load_output_parser(config: dict) -> dict:         """Load an output parser.              Args:             config: config dict              Returns:             config dict with output parser loaded         """         if "output_parsers" in config and config["output_parsers"] is not None:             _config = config["output_parsers"]             output_parser_type = _config["_type"]             if output_parser_type == "regex_parser":                 output_parser = RegexParser(**_config)             else:                 msg = f"Unsupported output parser {output_parser_type}"                 raise ValueError(msg)             config["output_parsers"] = output_parser         return config