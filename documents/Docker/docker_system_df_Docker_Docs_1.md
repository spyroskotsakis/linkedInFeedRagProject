# docker system df | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/system/df/
**Word Count:** 1002
**Links Count:** 482
**Scraped:** 2025-07-16 01:52:23
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker system df

Description| Show docker disk usage   ---|---   Usage| `docker system df [OPTIONS]`      ## Description

The `docker system df` command displays information regarding the amount of disk space used by the Docker daemon.

## Options

Option| Default| Description   ---|---|---   `--format`| | Format output using a custom template:   'table': Print output in table format with column headers \(default\)   'table TEMPLATE': Print output in table format using the given Go template   'json': Print in JSON format   'TEMPLATE': Print output using the given Go template.   Refer to <https://docs.docker.com/go/formatting/> for more information about formatting output with templates   `-v, --verbose`| | Show detailed information on space usage      ## Examples

By default the command displays a summary of the data used:               $ docker system df          TYPE                TOTAL               ACTIVE              SIZE                RECLAIMABLE     Images              5                   2                   16.43 MB            11.63 MB (70%)     Containers          2                   0                   212 B               212 B (100%)     Local Volumes       2                   1                   36 B                0 B (0%)     

Use the `-v, --verbose` flag to get more detailed information:               $ docker system df -v          Images space usage:          REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE                SHARED SIZE         UNIQUE SIZE         CONTAINERS     my-curl             latest              b2789dd875bf        6 minutes ago       11 MB               11 MB               5 B                 0     my-jq               latest              ae67841be6d0        6 minutes ago       9.623 MB            8.991 MB            632.1 kB            0     <none>              <none>              a0971c4015c1        6 minutes ago       11 MB               11 MB               0 B                 0     alpine              latest              4e38e38c8ce0        9 weeks ago         4.799 MB            0 B                 4.799 MB            1     alpine              3.3                 47cf20d8c26c        9 weeks ago         4.797 MB            4.797 MB            0 B                 1          Containers space usage:          CONTAINER ID        IMAGE               COMMAND             LOCAL VOLUMES       SIZE                CREATED             STATUS                      NAMES     4a7f7eebae0f        alpine:latest       "sh"                1                   0 B                 16 minutes ago      Exited (0) 5 minutes ago    hopeful_yalow     f98f9c2aa1ea        alpine:3.3          "sh"                1                   212 B               16 minutes ago      Exited (0) 48 seconds ago   anon-vol          Local Volumes space usage:          NAME                                                               LINKS               SIZE     07c7bdf3e34ab76d921894c2b834f073721fccfbbcba792aa7648e3a7a664c2e   2                   36 B     my-named-vol                                                       0                   0 B     

  * `SHARED SIZE` is the amount of space that an image shares with another one \(i.e. their common data\)   * `UNIQUE SIZE` is the amount of space that's only used by a given image   * `SIZE` is the virtual size of the image, it's the sum of `SHARED SIZE` and `UNIQUE SIZE`

> Note >  > Network information isn't shown, because it doesn't consume disk space.