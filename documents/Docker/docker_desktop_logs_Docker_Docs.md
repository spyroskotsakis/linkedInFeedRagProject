# docker desktop logs | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/desktop/logs
**Word Count:** 820
**Links Count:** 477
**Scraped:** 2025-07-16 01:56:12
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker desktop logs

Description| Print log entries for Docker Desktop   ---|---   Usage| `docker desktop logs [OPTIONS]`      Requires: Docker Desktop 4.39 and later

## Options

Option| Default| Description   ---|---|---   `-b, --boot`| | Show logs from a specified boot. Zero means the current or boot, one the second last boot, and so on   `-c, --color`| | Enable colored output. Priority levels are highlighted.   `-m, --color-mode`| | Color mode to use. Can be `default` or `priority`   `-D, --directory`| | Specifies a custom directory to search for log entries   `-p, --priority`| `%!s(int=-1)`| Filter output by log priorities. `-1` is all, `0` is info or above, `1` filters for warnings or above, `2` filters for errors.   `-S, --since`| | Start showing entries on or newer than the specified date and time. Uses the systemd.time\(7\) format.   `-u, --unit`| | Filter by one or more categories \(e.g. `--unit=com.docker.backend.ipc`, `com.docker.backend.apiproxy`\)   `-U, --until`| | Start showing entries on or before the specified date and time. Uses the systemd.time\(7\) format.