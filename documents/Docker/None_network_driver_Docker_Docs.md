# None network driver | Docker Docs

**URL:** https://docs.docker.com/engine/network/drivers/none
**Word Count:** 1134
**Links Count:** 644
**Scraped:** 2025-07-16 01:59:56
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# None network driver

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

If you want to completely isolate the networking stack of a container, you can use the `--network none` flag when starting the container. Within the container, only the loopback device is created.

The following example shows the output of `ip link show` in an `alpine` container using the `none` network driver.               $ docker run --rm --network none alpine:latest ip link show     1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000         link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00     

No IPv6 loopback address is configured for containers using the `none` driver.               $ docker run --rm --network none --name no-net-alpine alpine:latest ip addr show     1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000         link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00         inet 127.0.0.1/8 scope host lo            valid_lft forever preferred_lft forever     

## Next steps

  * Go through the [host networking tutorial](https://docs.docker.com/engine/network/tutorials/host/)   * Learn about [networking from the container's point of view](https://docs.docker.com/engine/network/)   * Learn about [bridge networks](https://docs.docker.com/engine/network/drivers/bridge/)   * Learn about [overlay networks](https://docs.docker.com/engine/network/drivers/overlay/)   * Learn about [Macvlan networks](https://docs.docker.com/engine/network/drivers/macvlan/)