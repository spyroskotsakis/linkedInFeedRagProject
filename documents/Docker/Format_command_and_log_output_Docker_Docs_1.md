# Format command and log output | Docker Docs

**URL:** https://docs.docker.com/engine/cli/formatting
**Word Count:** 1317
**Links Count:** 669
**Scraped:** 2025-07-16 01:59:28
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Format command and log output

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Docker supports [Go templates](https://golang.org/pkg/text/template/) which you can use to manipulate the output format of certain commands and log drivers.

Docker provides a set of basic functions to manipulate template elements. All of these examples use the `docker inspect` command, but many other CLI commands have a `--format` flag, and many of the CLI command references include examples of customizing the output format.

> Note >  > When using the `--format` flag, you need observe your shell environment. In a POSIX shell, you can run the following with a single quote: >      >      >     $ docker inspect --format '{{join .Args " , "}}' >      >  > Otherwise, in a Windows shell \(for example, PowerShell\), you need to use single quotes, but escape the double quotes inside the parameters as follows: >      >      >     $ docker inspect --format '{{join .Args \" , \"}}' >     

## join

`join` concatenates a list of strings to create a single string. It puts a separator between each element in the list.               $ docker inspect --format '{{join .Args " , "}}' container     

## table

`table` specifies which fields you want to see its output.               $ docker image list --format "table {{.ID}}\t{{.Repository}}\t{{.Tag}}\t{{.Size}}"     

## json

`json` encodes an element as a json string.               $ docker inspect --format '{{json .Mounts}}' container     

## lower

`lower` transforms a string into its lowercase representation.               $ docker inspect --format "{{lower .Name}}" container     

## split

`split` slices a string into a list of strings separated by a separator.               $ docker inspect --format '{{split .Image ":"}}' container     

## title

`title` capitalizes the first character of a string.               $ docker inspect --format "{{title .Name}}" container     

## upper

`upper` transforms a string into its uppercase representation.               $ docker inspect --format "{{upper .Name}}" container     

## pad

`pad` adds whitespace padding to a string. You can specify the number of spaces to add before and after the string.               $ docker image list --format '{{pad .Repository 5 10}}'     

This example adds 5 spaces before the image repository name and 10 spaces after.

## truncate

`truncate` shortens a string to a specified length. If the string is shorter than the specified length, it remains unchanged.               $ docker image list --format '{{truncate .Repository 15}}'     

This example displays the image repository name, truncating it to the first 15 characters if it's longer.

## println

`println` prints each value on a new line.               $ docker inspect --format='{{range .NetworkSettings.Networks}}{{println .IPAddress}}{{end}}' container     

## Hint

To find out what data can be printed, show all content as json:               $ docker container ls --format='{{json .}}'