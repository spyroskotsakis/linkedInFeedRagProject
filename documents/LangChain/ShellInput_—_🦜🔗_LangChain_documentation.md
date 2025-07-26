# ShellInput — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/community/tools/langchain_community.tools.shell.tool.ShellInput.html
**Word Count:** 57
**Links Count:** 409
**Scraped:** 2025-07-21 08:22:10
**Status:** completed

---

# ShellInput\#

_class _langchain\_community.tools.shell.tool.ShellInput[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_community/tools/shell/tool.html#ShellInput)\#     

Bases: `BaseModel`

Commands for the Bash Shell tool.

Create a new model by parsing and validating input data from keyword arguments.

Raises \[ValidationError\]\[pydantic\_core.ValidationError\] if the input data cannot be validated to form a valid model.

self is explicitly positional-only to allow self as a field name.

_param _commands _: str | List\[str\]__\[Required\]_\#     

List of shell commands to run.

List of shell commands to run. Deserialized using json.loads

__On this page