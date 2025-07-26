# Invoke host binaries | Docker Docs

**URL:** https://docs.docker.com/extensions/extensions-sdk/guides/invoke-host-binaries
**Word Count:** 1411
**Links Count:** 650
**Scraped:** 2025-07-16 01:59:56
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Invoke host binaries

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

In some cases, your extension may need to invoke some command from the host. For example, you might want to invoke the CLI of your cloud provider to create a new resource, or the CLI of a tool your extension provides, or even a shell script that you want to run on the host.

You could do that by executing the CLI from a container with the extension SDK. But this CLI needs to access the host's filesystem, which isn't easy nor fast if it runs in a container.

However host binaries invoke from the extension executables \(as binaries, shell scripts\) shipped as part of your extension and deployed to the host. As extensions can run on multiple platforms, this means that you need to ship the executables for all the platforms you want to support.

Learn more about extensions [architecture](https://docs.docker.com/extensions/extensions-sdk/architecture/).

> Note >  > Only executables shipped as part of the extension can be invoked with the SDK.

In this example, the CLI is a simple `Hello world` script that must be invoked with a parameter and returns a string.

## Add the executables to the extension

Mac and Linux  Windows

Create a `bash` script for macOS and Linux, in the file `binaries/unix/hello.sh` with the following content:               #!/bin/sh     echo "Hello, $1!"

Create a `batch script` for Windows in another file `binaries/windows/hello.cmd` with the following content:               @echo off     echo "Hello, %1!"

Then update the `Dockerfile` to copy the `binaries` folder into the extension's container filesystem and make the files executable.               # Copy the binaries into the right folder     COPY --chmod=0755 binaries/windows/hello.cmd /windows/hello.cmd     COPY --chmod=0755 binaries/unix/hello.sh /linux/hello.sh     COPY --chmod=0755 binaries/unix/hello.sh /darwin/hello.sh

## Invoke the executable from the UI

In your extension, use the Docker Desktop Client object to [invoke the shell script](https://docs.docker.com/extensions/extensions-sdk/dev/api/backend/#invoke-an-extension-binary-on-the-host) provided by the extension with the `ddClient.extension.host.cli.exec()` function. In this example, the binary returns a string as result, obtained by `result?.stdout`, as soon as the extension view is rendered.

React  Vue  Angular  Svelte               export function App() {       const ddClient = createDockerDesktopClient();       const [hello, setHello] = useState("");            useEffect(() => {         const run = async () => {           let binary = "hello.sh";           if (ddClient.host.platform === 'win32') {             binary = "hello.cmd";           }                const result = await ddClient.extension.host?.cli.exec(binary, ["world"]);           setHello(result?.stdout);              };         run();       }, [ddClient]);                return (         <div>           {hello}         </div>       );     }

> Important >  > We don't have an example for Vue yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Vue) and let us know if you'd like a sample with Vue.

> Important >  > We don't have an example for Angular yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Angular) and let us know if you'd like a sample with Angular.

> Important >  > We don't have an example for Svelte yet. [Fill out the form](https://docs.google.com/forms/d/e/1FAIpQLSdxJDGFJl5oJ06rG7uqtw1rsSBZpUhv_s9HHtw80cytkh2X-Q/viewform?usp=pp_url&entry.1333218187=Svelte) and let us know if you'd like a sample with Svelte.

## Configure the metadata file

The host binaries must be specified in the `metadata.json` file so that Docker Desktop copies them on to the host when installing the extension. Once the extension is uninstalled, the binaries that were copied are removed as well.               {       "vm": {         ...       },       "ui": {         ...       },       "host": {         "binaries": [           {             "darwin": [               {                 "path": "/darwin/hello.sh"               }             ],             "linux": [               {                 "path": "/linux/hello.sh"               }             ],             "windows": [               {                 "path": "/windows/hello.cmd"               }             ]           }         ]       }     }

The `path` must reference the path of the binary inside the container.