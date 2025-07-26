# ConsistentInstructionCasing | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/consistent-instruction-casing
**Word Count:** 772
**Links Count:** 483
**Scraped:** 2025-07-16 01:56:12
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# ConsistentInstructionCasing

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Output               Command 'EntryPoint' should be consistently cased

## Description

Instruction keywords should use consistent casing \(all lowercase or all uppercase\). Using a case that mixes uppercase and lowercase, such as `PascalCase` or `snakeCase`, letters result in poor readability.

## Examples

â Bad: don't mix uppercase and lowercase.               From alpine     Run echo hello > /greeting.txt     EntRYpOiNT ["cat", "/greeting.txt"]

â Good: all uppercase.               FROM alpine     RUN echo hello > /greeting.txt     ENTRYPOINT ["cat", "/greeting.txt"]

â Good: all lowercase.               from alpine     run echo hello > /greeting.txt     entrypoint ["cat", "/greeting.txt"]