# docker buildx debug build | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/buildx/debug/build
**Word Count:** 928
**Links Count:** 480
**Scraped:** 2025-07-16 01:58:31
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker buildx debug build

Description| Start a build   ---|---   Usage| `docker buildx debug build [OPTIONS] PATH | URL | -`   AliasesAn alias is a short or memorable alternative for a longer command.| `docker build` `docker builder build` `docker image build` `docker buildx b`      **Experimental**

**This command is experimental.**

Experimental features are intended for testing and feedback as their functionality or design may change between releases without warning or can be removed entirely in a future release.

## Description

Start a build

## Options

Option| Default| Description   ---|---|---   `--add-host`| | Add a custom host-to-IP mapping \(format: `host:ip`\)   `--allow`| | Allow extra privileged entitlement \(e.g., `network.host`, `security.insecure`\)      `--annotation`| | Add annotation to the image   `--attest`| | Attestation parameters \(format: `type=sbom,generator=image`\)   `--build-arg`| | Set build-time variables   `--build-context`| | Additional build contexts \(e.g., name=path\)   `--cache-from`| | External cache sources \(e.g., `user/app:cache`, `type=local,src=path/to/dir`\)      `--cache-to`| | Cache export destinations \(e.g., `user/app:cache`, `type=local,dest=path/to/dir`\)      `--call`| `build`| Set method for evaluating build \(`check`, `outline`, `targets`\)   `--cgroup-parent`| | Set the parent cgroup for the `RUN` instructions during build   `--check`| | Shorthand for `--call=check`   `-f, --file`| | Name of the Dockerfile \(default: `PATH/Dockerfile`\)   `--iidfile`| | Write the image ID to a file   `--label`| | Set metadata for an image   `--load`| | Shorthand for `--output=type=docker`   `--metadata-file`| | Write build result metadata to a file   `--network`| | Set the networking mode for the `RUN` instructions during build   `--no-cache`| | Do not use cache when building the image   `--no-cache-filter`| | Do not cache specified stages   `-o, --output`| | Output destination \(format: `type=local,dest=path`\)   `--platform`| | Set target platform for build   `--progress`| `auto`| Set type of progress output \(`auto`, `quiet`, `plain`, `tty`, `rawjson`\). Use plain to show container output      `--provenance`| | Shorthand for `--attest=type=provenance`   `--pull`| | Always attempt to pull all referenced images   `--push`| | Shorthand for `--output=type=registry`   `-q, --quiet`| | Suppress the build output and print image ID on success   `--sbom`| | Shorthand for `--attest=type=sbom`   `--secret`| | Secret to expose to the build \(format: `id=mysecret[,src=/local/secret]`\)      `--shm-size`| | Shared memory size for build containers   `--ssh`| | SSH agent socket or keys to expose to the build \(format: `default|<id>[=<socket>|<key>[,<key>]]`\)      `-t, --tag`| | Name and optionally a tag \(format: `name:tag`\)   `--target`| | Set the target build stage to build   `--ulimit`| | Ulimit options