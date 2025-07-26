# BashProcess — 🦜🔗 LangChain  documentation

**URL:** https://python.langchain.com/api_reference/experimental/llm_bash/langchain_experimental.llm_bash.bash.BashProcess.html
**Word Count:** 147
**Links Count:** 109
**Scraped:** 2025-07-21 08:23:33
**Status:** completed

---

# BashProcess\#

_class _langchain\_experimental.llm\_bash.bash.BashProcess\(

    _strip\_newlines : bool = False_,     _return\_err\_output : bool = False_,     _persistent : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/llm_bash/bash.html#BashProcess)\#     

Wrapper for starting subprocesses.

Uses the python built-in subprocesses.run\(\) Persistent processes are **not** available on Windows systems, as pexpect makes use of Unix pseudoterminals \(ptys\). MacOS and Linux are okay.

Example               from langchain_community.utilities.bash import BashProcess          bash = BashProcess(         strip_newlines = False,         return_err_output = False,         persistent = False     )     bash.run('echo 'hello world'')     

Initializes with default settings

Attributes

`persistent` | Whether or not to spawn a persistent session NOTE: Unavailable for Windows environments   ---|---   `return_err_output` | Whether or not to return the output of a failed command, or just the error message and stacktrace   `strip_newlines` | Whether or not to run .strip\(\) on the output      Methods

`__init__`\(\[strip\_newlines, ...\]\) | Initializes with default settings   ---|---   `process_output`\(output, command\) | Uses regex to remove the command from the output   `run`\(commands\) | Run commands in either an existing persistent subprocess or on in a new subprocess environment.      Parameters:     

  * **strip\_newlines** \(_bool_\)

  * **return\_err\_output** \(_bool_\)

  * **persistent** \(_bool_\)

\_\_init\_\_\(

    _strip\_newlines : bool = False_,     _return\_err\_output : bool = False_,     _persistent : bool = False_, \)[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/llm_bash/bash.html#BashProcess.__init__)\#     

Initializes with default settings

Parameters:     

  * **strip\_newlines** \(_bool_\)

  * **return\_err\_output** \(_bool_\)

  * **persistent** \(_bool_\)

process\_output\(_output : str_, _command : str_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/llm_bash/bash.html#BashProcess.process_output)\#     

Uses regex to remove the command from the output

Parameters:     

  * **output** \(_str_\) – a process’ output string

  * **command** \(_str_\) – the executed command

Return type:     

str

run\(_commands : str | List\[str\]_\) → str[\[source\]](https://python.langchain.com/api_reference/_modules/langchain_experimental/llm_bash/bash.html#BashProcess.run)\#     

Run commands in either an existing persistent subprocess or on in a new subprocess environment.

Parameters:     

**commands** \(_List_ _\[__str_ _\]_\) – a list of commands to execute in the session

Return type:     

str

__On this page