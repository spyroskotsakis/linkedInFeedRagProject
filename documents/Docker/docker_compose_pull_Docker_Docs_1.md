# docker compose pull | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/compose/pull/
**Word Count:** 913
**Links Count:** 481
**Scraped:** 2025-07-16 01:50:39
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker compose pull

Description| Pull service images   ---|---   Usage| `docker compose pull [OPTIONS] [SERVICE...]`      ## Description

Pulls an image associated with a service defined in a `compose.yaml` file, but does not start containers based on those images

## Options

Option| Default| Description   ---|---|---   `--ignore-buildable`| | Ignore images that can be built   `--ignore-pull-failures`| | Pull what it can and ignores images with pull failures   `--include-deps`| | Also pull services declared as dependencies   `--policy`| | Apply pull policy \("missing"|"always"\)   `-q, --quiet`| | Pull without printing progress information      ## Examples

Consider the following `compose.yaml`:               services:       db:         image: postgres       web:         build: .         command: bundle exec rails s -p 3000 -b '0.0.0.0'         volumes:           - .:/myapp         ports:           - "3000:3000"         depends_on:           - db

If you run `docker compose pull ServiceName` in the same directory as the `compose.yaml` file that defines the service, Docker pulls the associated image. For example, to call the postgres image configured as the db service in our example, you would run `docker compose pull db`.               $ docker compose pull db     [+] Running 1/15      â ¸ db Pulling                                                             12.4s        â ¿ 45b42c59be33 Already exists                                           0.0s        â ¹ 40adec129f1a Downloading  3.374MB/4.178MB                             9.3s        â ¹ b4c431d00c78 Download complete                                        9.3s        â ¹ 2696974e2815 Download complete                                        9.3s        â ¹ 564b77596399 Downloading  5.622MB/7.965MB                             9.3s        â ¹ 5044045cf6f2 Downloading  216.7kB/391.1kB                             9.3s        â ¹ d736e67e6ac3 Waiting                                                  9.3s        â ¹ 390c1c9a5ae4 Waiting                                                  9.3s        â ¹ c0e62f172284 Waiting                                                  9.3s        â ¹ ebcdc659c5bf Waiting                                                  9.3s        â ¹ 29be22cb3acc Waiting                                                  9.3s        â ¹ f63c47038e66 Waiting                                                  9.3s        â ¹ 77a0c198cde5 Waiting                                                  9.3s        â ¹ c8752d5b785c Waiting                                                  9.3s     

`docker compose pull` tries to pull image for services with a build section. If pull fails, it lets you know this service image must be built. You can skip this by setting `--ignore-buildable` flag.