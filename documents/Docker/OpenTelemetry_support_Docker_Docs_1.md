# OpenTelemetry support | Docker Docs

**URL:** https://docs.docker.com/build/debug/opentelemetry/
**Word Count:** 1061
**Links Count:** 639
**Scraped:** 2025-07-16 01:53:49
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# OpenTelemetry support

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

Both Buildx and BuildKit support [OpenTelemetry](https://opentelemetry.io/).

To capture the trace to [Jaeger](https://github.com/jaegertracing/jaeger), set `JAEGER_TRACE` environment variable to the collection address using a `driver-opt`.

First create a Jaeger container:               $ docker run -d --name jaeger -p "6831:6831/udp" -p "16686:16686" --restart unless-stopped jaegertracing/all-in-one     

Then [create a `docker-container` builder](https://docs.docker.com/build/builders/drivers/docker-container/) that will use the Jaeger instance via the `JAEGER_TRACE` environment variable:               $ docker buildx create --use \       --name mybuilder \       --driver docker-container \       --driver-opt "network=host" \       --driver-opt "env.JAEGER_TRACE=localhost:6831"     

Boot and [inspect `mybuilder`](https://docs.docker.com/reference/cli/docker/buildx/inspect/):               $ docker buildx inspect --bootstrap     

Buildx commands should be traced at `http://127.0.0.1:16686/`:

![OpenTelemetry Buildx Bake](https://docs.docker.com/build/images/opentelemetry.png)

![OpenTelemetry Buildx Bake](https://docs.docker.com/build/images/opentelemetry.png)