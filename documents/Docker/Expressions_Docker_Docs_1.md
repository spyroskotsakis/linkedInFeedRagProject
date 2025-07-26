# Expressions | Docker Docs

**URL:** https://docs.docker.com/build/bake/expressions/
**Word Count:** 1195
**Links Count:** 646
**Scraped:** 2025-07-16 01:48:31
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Expression evaluation in Bake

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Bake files in the HCL format support expression evaluation, which lets you perform arithmetic operations, conditionally set values, and more.

## Arithmetic operations

You can perform arithmetic operations in expressions. The following example shows how to multiply two numbers.

docker-bake.hcl               sum = 7*6          target "default" {       args = {         answer = sum       }     }

Printing the Bake file with the `--print` flag shows the evaluated value for the `answer` build argument.               $ docker buildx bake --print                    {       "target": {         "default": {           "context": ".",           "dockerfile": "Dockerfile",           "args": {             "answer": "42"           }         }       }     }

## Ternary operators

You can use ternary operators to conditionally register a value.

The following example adds a tag only when a variable is not empty, using the built-in `notequal` [function](https://docs.docker.com/build/bake/funcs/).

docker-bake.hcl               variable "TAG" {}          target "default" {       context="."       dockerfile="Dockerfile"       tags = [         "my-image:latest",         notequal("",TAG) ? "my-image:${TAG}": ""       ]     }

In this case, `TAG` is an empty string, so the resulting build configuration only contains the hard-coded `my-image:latest` tag.               $ docker buildx bake --print                    {       "target": {         "default": {           "context": ".",           "dockerfile": "Dockerfile",           "tags": ["my-image:latest"]         }       }     }

## Expressions with variables

You can use expressions with [variables](https://docs.docker.com/build/bake/variables/) to conditionally set values, or to perform arithmetic operations.

The following example uses expressions to set values based on the value of variables. The `v1` build argument is set to "higher" if the variable `FOO` is greater than 5, otherwise it is set to "lower". The `v2` build argument is set to "yes" if the `IS_FOO` variable is true, otherwise it is set to "no".

docker-bake.hcl               variable "FOO" {       default = 3     }          variable "IS_FOO" {       default = true     }          target "app" {       args = {         v1 = FOO > 5 ? "higher" : "lower"         v2 = IS_FOO ? "yes" : "no"       }     }

Printing the Bake file with the `--print` flag shows the evaluated values for the `v1` and `v2` build arguments.               $ docker buildx bake --print app                    {       "group": {         "default": {           "targets": ["app"]         }       },       "target": {         "app": {           "context": ".",           "dockerfile": "Dockerfile",           "args": {             "v1": "lower",             "v2": "yes"           }         }       }     }