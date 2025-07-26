# Share your extension | Docker Docs

**URL:** https://docs.docker.com/extensions/extensions-sdk/extensions/share/
**Word Count:** 1142
**Links Count:** 640
**Scraped:** 2025-07-16 01:48:09
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Share your extension

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Once your extension image is accessible on Docker Hub, anyone with access to the image can install the extension.

People can install your extension by typing `docker extension install my/awesome-extension:latest` in to the terminal.

However, this option doesn't provide a preview of the extension before it's installed.

## Create a share URL

Docker lets you share your extensions using a URL.

When people navigate to this URL, it opens Docker Desktop and displays a preview of your extension in the same way as an extension in the Marketplace. From the preview, users can then select **Install**.

![Navigate to extension link](https://docs.docker.com/extensions/extensions-sdk/extensions/images/open-share.png)

![Navigate to extension link](https://docs.docker.com/extensions/extensions-sdk/extensions/images/open-share.png)

To generate this link you can either:

  * Run the following command:                  $ docker extension share my/awesome-extension:0.0.1         

  * Once you have installed your extension locally, navigate to the **Manage** tab and select **Share**.

![Share button](https://docs.docker.com/extensions/extensions-sdk/extensions/images/list-preview.png)

![Share button](https://docs.docker.com/extensions/extensions-sdk/extensions/images/list-preview.png)

> Note >  > Previews of the extension description or screenshots, for example, are created using [extension labels](https://docs.docker.com/extensions/extensions-sdk/extensions/labels/).