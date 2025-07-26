# Search | Docker Docs

**URL:** https://docs.docker.com/docker-hub/image-library/search
**Word Count:** 2026
**Links Count:** 663
**Scraped:** 2025-07-16 01:59:56
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Docker Hub search

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

The [Docker Hub search interface](https://hub.docker.com/search) lets you explore millions of resources. To help you find exactly what you need, it offers a variety of filters that let you narrow your results or discover different types of content.

## Filters

The search functionality includes filters to narrow down results based on your requirements, such as products, categories, and trusted content. This ensures that you can quickly find and access the resources best suited to your project.

### Products

Docker Hub's content library features three products, each designed to meet specific needs of developers and organizations. These products include images, plugins, and extensions.

#### Images

Docker Hub hosts millions of container images, making it the go-to repository for containerized applications and solutions. These images include:

  * Operating system images: Foundational images for Linux distributions like Ubuntu, Debian, and Alpine, or Windows Server images.   * Database and storage images: Pre-configured databases such as MySQL, PostgreSQL, and MongoDB to simplify application development.   * Languages and frameworks-based images: Popular images for Java, Python, Node.js, Ruby, .NET, and more, offering pre-built environments for faster development.

Images in Docker Hub simplify the development process by providing pre-built, reusable building blocks, reducing the need to start from scratch. Whether you're a beginner building your first container or an enterprise managing complex architectures, Docker Hub images provide a reliable foundation.

#### Plugins

Plugins in Docker Hub let you extend and customize Docker Engine to suit specialized requirements. Plugins integrate directly with the Docker Engine and provide capabilities such as:

  * Network plugins: Enhance networking functionality, enabling integration with complex network infrastructures.   * Volume plugins: Provide advanced storage options, supporting persistent and distributed storage across various backends.   * Authorization plugins: Offer fine-grained access control to secure Docker environments.

By leveraging Docker plugins, teams can tailor Docker Engine to meet their specific operational needs, ensuring compatibility with existing infrastructures and workflows.

To learn more about plugins, see [Docker Engine managed plugin system](https://docs.docker.com/engine/extend/).

#### Extensions

Docker Hub offers extensions for Docker Desktop, which enhance its core functionality. These extensions are purpose-built to streamline the software development lifecycle. Extensions provide tools for:

  * System optimization and monitoring: Manage resources and optimize Docker Desktopâs performance.   * Container management: Simplify container deployment and monitoring.   * Database management: Facilitate efficient database operations within containers.   * Kubernetes and cloud integration: Bridge local environments with cloud-native and Kubernetes workflows.   * Visualization tools: Gain insights into container resource usage through graphical representations.

Extensions help developers and teams create a more efficient and unified workflow by reducing context switching and bringing essential tools into Docker Desktop's interface.

To learn more about extensions, see [Docker Extensions](https://docs.docker.com/extensions/).

### Trusted content

Docker Hub's trusted content provides a curated selection of high-quality, secure images designed to give developers confidence in the reliability and security of the resources they use. These images are stable, regularly updated, and adhere to industry best practices, making them a strong foundation for building and deploying applications. Docker Hub's trusted content includes, Docker Official Images, Verified Publisher images, and Docker-Sponsored Open Source Software images.

For more details, see [Trusted content](https://docs.docker.com/docker-hub/image-library/trusted-content/).

### Categories

Docker Hub makes it easy to find and explore container images with categories. Categories group images based on their primary use case, helping you quickly locate the tools and resources you need to build, deploy, and run your applications.

The categories include:

  * **API Management** : Tools for creating, publishing, analyzing, and securing APIs.   * **Content Management System:** Software applications to create and manage digital content through templates, procedures, and standard formats.   * **Data Science:** Tools and software to support analyzing data and generating actionable insights.   * **Databases & Storage:** Systems for storing, retrieving, and managing data.   * **Languages & Frameworks:** Programming language runtimes and frameworks.   * **Integrations & Delivery:** Tools for Continuous Integration \(CI\) and Continuous Delivery \(CD\).   * **Internet of Things:** Tools supporting Internet of Things \(IoT\) applications.   * **Machine Learning & AI:** Tools and frameworks optimized for artificial intelligence and machine learning projects, such as pre-installed libraries and frameworks for data analysis, model training, and deployment.   * **Message Queues:** Message queuing systems optimized for reliable, scalable, and efficient message handling.   * **Monitoring & Observability:** Tools to track software and system performance through metrics, logs, and traces, as well as observability to explore the systemâs state and diagnose issues.   * **Networking:** Repositories that support data exchange and connecting computers and other devices to share resources.   * **Operating Systems:** Software that manages all other programs on a computer and serves as an intermediary between users and the computer hardware, while overseeing applications and system resources.   * **Security:** Tools to protect a computer system or network from theft, unauthorized access, or damage to their hardware, software, or electronic data, as well as from service disruption.   * **Web Servers:** Software to serve web pages, HTML files, and other assets to users or other systems.   * **Web Analytics:** Tools to collect, measure, analyze, and report on web data and website visitor engagement.

### Operating systems

The **Operating systems** filter lets you narrow your search to container images compatible with specific host operating systems. This filter ensures that the images you use align with your target environment, whether you're developing for Linux-based systems, Windows, or both.

  * **Linux** : Access a wide range of images tailored for Linux environments. These images provide foundational environments for building and running Linux-based applications in containers.   * **Windows** : Explore Windows container images.

> Note >  > The **Operating systems** filter is only available for images. If you select the **Extensions** or **Plugins** filter, then the **Operating systems** filter isn't available.

### Architectures

The **Architectures** filter lets you find images built to support specific CPU architectures. This ensures compatibility with your hardware environment, from development machines to production servers.

  * **ARM** : Select images compatible with ARM processors, commonly used in IoT devices and embedded systems.   * **ARM 64** : Locate 64-bit ARM-compatible images for modern ARM processors, such as those in AWS Graviton or Apple Silicon.   * **IBM POWER** : Find images optimized for IBM Power Systems, offering performance and reliability for enterprise workloads.   * **PowerPC 64 LE** : Access images designed for the little-endian PowerPC 64-bit architecture.   * **IBM Z** : Discover images tailored for IBM Z mainframes, ensuring compatibility with enterprise-grade hardware.   * **x86** : Choose images compatible with 32-bit x86 architectures, suitable for older systems or lightweight environments.   * **x86-64** : Filter images for modern 64-bit x86 systems, widely used in desktops, servers, and cloud infrastructures.

> Note >  > The **Architectures** filter is only available for images. If you select the **Extensions** or **Plugins** filter, then the **Architectures** filter isn't available.

### Reviewed by Docker

The **Reviewed by Docker** filter provides an extra layer of assurance when selecting extensions. This filter helps you identify whether a Docker Desktop extension has been reviewed by Docker for quality and reliability.

  * **Reviewed** : Extensions that have undergone Docker's review process, ensuring they meet high standards.   * **Not Reviewed** : Extensions that have not been reviewed by Docker.

> Note >  > The **Reviewed by Docker** filter is only available for extensions. To make the filter available, you must select only the **Extensions** filter in **Products**.