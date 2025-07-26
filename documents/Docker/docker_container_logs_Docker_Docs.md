# docker container logs | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/container/logs
**Word Count:** 1054
**Links Count:** 486
**Scraped:** 2025-07-16 01:56:34
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker container logs

Description| Fetch the logs of a container   ---|---   Usage| `docker container logs [OPTIONS] CONTAINER`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker logs`      ## Description

The `docker logs` command batch-retrieves logs present at the time of execution.

For more information about selecting and configuring logging drivers, refer to [Configure logging drivers](https://docs.docker.com/engine/logging/configure/).

The `docker logs --follow` command will continue streaming the new output from the container's `STDOUT` and `STDERR`.

Passing a negative number or a non-integer to `--tail` is invalid and the value is set to `all` in that case.

The `docker logs --timestamps` command will add an [RFC3339Nano timestamp](https://pkg.go.dev/time#RFC3339Nano) , for example `2014-09-16T06:17:46.000000000Z`, to each log entry. To ensure that the timestamps are aligned the nano-second part of the timestamp will be padded with zero when necessary.

The `docker logs --details` command will add on extra attributes, such as environment variables and labels, provided to `--log-opt` when creating the container.

The `--since` option shows only the container logs generated after a given date. You can specify the date as an RFC 3339 date, a UNIX timestamp, or a Go duration string \(e.g. `1m30s`, `3h`\). Besides RFC3339 date format you may also use RFC3339Nano, `2006-01-02T15:04:05`, `2006-01-02T15:04:05.999999999`, `2006-01-02T07:00`, and `2006-01-02`. The local timezone on the client will be used if you do not provide either a `Z` or a `+-00:00` timezone offset at the end of the timestamp. When providing Unix timestamps enter seconds\[.nanoseconds\], where seconds is the number of seconds that have elapsed since January 1, 1970 \(midnight UTC/GMT\), not counting leap seconds \(aka Unix epoch or Unix time\), and the optional .nanoseconds field is a fraction of a second no more than nine digits long. You can combine the `--since` option with either or both of the `--follow` or `--tail` options.

## Options

Option| Default| Description   ---|---|---   `--details`| | Show extra details provided to logs   `-f, --follow`| | Follow log output   `--since`| | Show logs since timestamp \(e.g. `2013-01-02T13:23:37Z`\) or relative \(e.g. `42m` for 42 minutes\)      `-n, --tail`| `all`| Number of lines to show from the end of the logs   `-t, --timestamps`| | Show timestamps   `--until`| | API 1.35+ Show logs before a timestamp \(e.g. `2013-01-02T13:23:37Z`\) or relative \(e.g. `42m` for 42 minutes\)         ## Examples

### Retrieve logs until a specific point in time \(--until\)

In order to retrieve logs before a specific point in time, run:               $ docker run --name test -d busybox sh -c "while true; do $(echo date); sleep 1; done"     $ date     Tue 14 Nov 2017 16:40:00 CET     $ docker logs -f --until=2s test     Tue 14 Nov 2017 16:40:00 CET     Tue 14 Nov 2017 16:40:01 CET     Tue 14 Nov 2017 16:40:02 CET