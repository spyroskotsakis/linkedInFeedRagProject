# Custom kernels on WSL | Docker Docs

**URL:** https://docs.docker.com/desktop/features/wsl/custom-kernels/
**Word Count:** 1180
**Links Count:** 640
**Scraped:** 2025-07-16 01:49:59
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Custom kernels on WSL

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

Docker Desktop depends on several kernel features built into the default WSL 2 Linux kernel distributed by Microsoft. Consequently, using a custom kernel with Docker Desktop on WSL 2 is not officially supported and may cause issues with Docker Desktop startup or operation.

However, in some cases it may be necessary to run custom kernels; Docker Desktop does not block their use, and some users have reported success using them.

If you choose to use a custom kernel, it is recommended you start from the kernel tree distributed by Microsoft from their [official repository](https://github.com/microsoft/WSL2-Linux-Kernel) and then add the features you need on top of that.

It's also recommended that you:

  * Use the same kernel version as the one distributed by the latest WSL2 release. You can find the version by running `wsl.exe --system uname -r` in a terminal.   * Start from the default kernel configuration as provided by Microsoft from their [repository](https://github.com/microsoft/WSL2-Linux-Kernel) and add the features you need on top of that.   * Make sure that your kernel build environment includes `pahole` and its version is properly reflected in the corresponding kernel config \(`CONFIG_PAHOLE_VERSION`\).