# docker context show | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/context/show
**Word Count:** 841
**Links Count:** 482
**Scraped:** 2025-07-16 01:56:12
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker context show

Description| Print the name of the current context   ---|---   Usage| `docker context show`      ## Description

Print the name of the current context, possibly set by `DOCKER_CONTEXT` environment variable or `--context` global option.

## Examples

### Print the current context

The following example prints the currently used [`docker context`](https://docs.docker.com/reference/cli/docker/context/):               $ docker context show'     default     

As an example, this output can be used to dynamically change your shell prompt to indicate your active context. The example below illustrates how this output could be used when using Bash as your shell.

Declare a function to obtain the current context in your `~/.bashrc`, and set this command as your `PROMPT_COMMAND`               function docker_context_prompt() {             PS1="context: $(docker context show)> "     }          PROMPT_COMMAND=docker_context_prompt     

After reloading the `~/.bashrc`, the prompt now shows the currently selected `docker context`:               $ source ~/.bashrc     context: default> docker context create --docker host=unix:///var/run/docker.sock my-context     my-context     Successfully created context "my-context"     context: default> docker context use my-context     my-context     Current context is now "my-context"     context: my-context> docker context use default     default     Current context is now "default"     context: default>