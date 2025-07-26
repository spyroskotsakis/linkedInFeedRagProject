# Example prompts | Docker Docs

**URL:** https://docs.docker.com/copilot/examples/
**Word Count:** 1257
**Links Count:** 656
**Scraped:** 2025-07-16 01:47:29
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Example prompts for the Docker agent

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Availability: Early Access 

## Use cases

Here are some examples of the types of questions you can ask the Docker agent:

### Ask general Docker questions

You can ask general question about Docker. For example:

  * `@docker what is a Dockerfile?`   * `@docker how do I build a Docker image?`   * `@docker how do I run a Docker container?`   * `@docker what does 'docker buildx imagetools inspect' do?`

### Get help containerizing your project

You can ask the agent to help you containerize your existing project:

  * `@docker can you help create a compose file for this project?`   * `@docker can you create a Dockerfile for this project?`

#### Opening pull requests

The Docker agent will analyze your project, generate the necessary files, and, if applicable, offer to raise a pull request with the necessary Docker assets.

Automatically opening pull requests against your repositories is only available when the agent generates new Docker assets.

### Analyze a project for vulnerabilities

The agent can help you improve your security posture with [Docker Scout](https://docs.docker.com/scout/):

  * `@docker can you help me find vulnerabilities in my project?`   * `@docker does my project contain any insecure dependencies?`

The agent will run use Docker Scout to analyze your project's dependencies, and report whether you're vulnerable to any [known CVEs](https://docs.docker.com/scout/deep-dive/advisory-db-sources/).

![Copilot vulnerabilities report](https://docs.docker.com/copilot/images/copilot-vuln-report.png)

![Copilot vulnerabilities report](https://docs.docker.com/copilot/images/copilot-vuln-report.png)

## Limitations

  * The agent is currently not able to access specific files in your repository, such as the currently-opened file in your editor, or if you pass a file reference with your message in the chat message.

## Feedback

For issues or feedback, visit the [GitHub feedback repository](https://github.com/docker/copilot-issues).