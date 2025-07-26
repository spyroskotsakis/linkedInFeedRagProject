# docker trust signer add | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/trust/signer/add
**Word Count:** 831
**Links Count:** 484
**Scraped:** 2025-07-16 01:56:34
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker trust signer add

Description| Add a signer   ---|---   Usage| `docker trust signer add OPTIONS NAME REPOSITORY [REPOSITORY...]`      ## Description

`docker trust signer add` adds signers to signed repositories.

## Options

Option| Default| Description   ---|---|---   `--key`| | Path to the signer's public key file      ## Examples

### Add a signer to a repository

To add a new signer, `alice`, to this repository:               $ docker trust inspect --pretty example/trust-demo          No signatures for example/trust-demo               List of signers and their keys:          SIGNER              KEYS     bob                 5600f5ab76a2          Administrative keys for example/trust-demo:     Repository Key: 642692c14c9fc399da523a5f4e24fe306a0a6ee1cc79a10e4555b3c6ab02f71e     Root Key:       3cb2228f6561e58f46dbc4cda4fcaff9d5ef22e865a94636f82450d1d2234949     

Add `alice` with `docker trust signer add`:               $ docker trust signer add alice example/trust-demo --key alice.crt       Adding signer "alice" to example/trust-demo...       Enter passphrase for repository key with ID 642692c:     Successfully added signer: alice to example/trust-demo     

`docker trust inspect --pretty` now lists `alice` as a valid signer:               $ docker trust inspect --pretty example/trust-demo          No signatures for example/trust-demo               List of signers and their keys:          SIGNER              KEYS     alice               05e87edcaecb     bob                 5600f5ab76a2          Administrative keys for example/trust-demo:     Repository Key: 642692c14c9fc399da523a5f4e24fe306a0a6ee1cc79a10e4555b3c6ab02f71e     Root Key:       3cb2228f6561e58f46dbc4cda4fcaff9d5ef22e865a94636f82450d1d2234949