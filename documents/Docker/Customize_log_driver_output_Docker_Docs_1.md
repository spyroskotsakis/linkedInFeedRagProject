# Customize log driver output | Docker Docs

**URL:** https://docs.docker.com/engine/logging/log_tags/
**Word Count:** 1149
**Links Count:** 635
**Scraped:** 2025-07-16 01:49:59
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Customize log driver output

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

The `tag` log option specifies how to format a tag that identifies the container's log messages. By default, the system uses the first 12 characters of the container ID. To override this behavior, specify a `tag` option:               $ docker run --log-driver=fluentd --log-opt fluentd-address=myhost.local:24224 --log-opt tag="mailer"     

Docker supports some special template markup you can use when specifying a tag's value:

Markup| Description   ---|---   `{{.ID}}`| The first 12 characters of the container ID.   `{{.FullID}}`| The full container ID.   `{{.Name}}`| The container name.   `{{.ImageID}}`| The first 12 characters of the container's image ID.   `{{.ImageFullID}}`| The container's full image ID.   `{{.ImageName}}`| The name of the image used by the container.   `{{.DaemonName}}`| The name of the Docker program \(`docker`\).      For example, specifying a `--log-opt tag="{{.ImageName}}/{{.Name}}/{{.ID}}"` value yields `syslog` log lines like:               Aug  7 18:33:19 HOSTNAME hello-world/foobar/5790672ab6a0[9103]: Hello from Docker.

At startup time, the system sets the `container_name` field and `{{.Name}}` in the tags. If you use `docker rename` to rename a container, the new name isn't reflected in the log messages. Instead, these messages continue to use the original container name.