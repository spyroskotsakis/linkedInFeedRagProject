# docker trust key load | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/trust/key/load/
**Word Count:** 825
**Links Count:** 484
**Scraped:** 2025-07-16 01:52:23
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker trust key load

Description| Load a private key file for signing   ---|---   Usage| `docker trust key load [OPTIONS] KEYFILE`      ## Description

`docker trust key load` adds private keys to the local Docker trust keystore.

To add a signer to a repository use `docker trust signer add`.

## Options

Option| Default| Description   ---|---|---   `--name`| `signer`| Name for the loaded key      ## Examples

### Load a single private key

For a private key `alice.pem` with permissions `-rw-------`               $ docker trust key load alice.pem          Loading key from "alice.pem"...     Enter passphrase for new signer key with ID f8097df:     Repeat passphrase for new signer key with ID f8097df:     Successfully imported key from alice.pem     

To specify a name use the `--name` flag:               $ docker trust key load --name alice-key alice.pem          Loading key from "alice.pem"...     Enter passphrase for new alice-key key with ID f8097df:     Repeat passphrase for new alice-key key with ID f8097df:     Successfully imported key from alice.pem