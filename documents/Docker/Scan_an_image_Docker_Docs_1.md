# Scan an image | Docker Docs

**URL:** https://docs.docker.com/dhi/how-to/scan
**Word Count:** 1710
**Links Count:** 667
**Scraped:** 2025-07-16 02:00:24
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Scan Docker Hardened Images

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

Subscription: Docker Hardened Images

Docker Hardened Images \(DHIs\) are designed to be secure by default, but like any container image, it's important to scan them regularly as part of your vulnerability management process.

You can scan DHIs using the same tools you already use for standard images, such as Docker Scout, Grype, and Trivy. DHIs follow the same formats and standards for compatibility across your security tooling. Before you scan an image, the image must be mirrored into your organization on Docker Hub.

> Note >  > [Docker Scout](https://docs.docker.com/scout/) is automatically enabled at no additional cost for all mirrored Docker Hardened Image repositories on Docker Hub. You can view scan results directly in the Docker Hub UI under your organization's repository.

## Docker Scout

Docker Scout is integrated into Docker Desktop and the Docker CLI. It provides vulnerability insights, CVE summaries, and direct links to remediation guidance.

### Scan a DHI using Docker Scout

To scan a Docker Hardened Image using Docker Scout, run the following command:               $ docker scout cves <your-namespace>/dhi-<image>:<tag> --platform <platform>     

Example output:                   v SBOM obtained from attestation, 101 packages found         v Provenance obtained from attestation         v VEX statements obtained from attestation         v No vulnerable package detected         ...

For more detailed filtering and JSON output, see [Docker Scout CLI reference](https://docs.docker.com/reference/cli/docker/scout/).

### Automate DHI scanning in CI/CD with Docker Scout

Integrating Docker Scout into your CI/CD pipeline enables you to automatically verify that images built from Docker Hardened Images remain free from known vulnerabilities during the build process. This proactive approach ensures the continued security integrity of your images throughout the development lifecycle.

#### Example GitHub Actions workflow

The following is a sample GitHub Actions workflow that builds an image and scans it using Docker Scout:

Show more               name: DHI Vulnerability Scan          on:       push:         branches: [ main ]       pull_request:         branches: [ "**" ]          env:       REGISTRY: docker.io       IMAGE_NAME: ${{ github.repository }}       SHA: ${{ github.event.pull_request.head.sha || github.event.after }}          jobs:       scan:         runs-on: ubuntu-latest         permissions:           contents: read           packages: write           pull-requests: write              steps:           - name: Checkout repository             uses: actions/checkout@v3                - name: Set up Docker Buildx             uses: docker/setup-buildx-action@v3                - name: Log in to Docker Hub             uses: docker/login-action@v2             with:               username: ${{ secrets.DOCKER_USERNAME }}               password: ${{ secrets.DOCKER_PASSWORD }}                - name: Build Docker image             run: |               docker build -t ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ env.SHA }} .                - name: Run Docker Scout CVE scan             uses: docker/scout-action@v1             with:               command: cves               image: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ env.SHA }}               only-severities: critical,high               exit-code: true

Hide

The `exit-code: true` parameter ensures that the workflow fails if any critical or high-severity vulnerabilities are detected, preventing the deployment of insecure images.

For more details on using Docker Scout in CI, see [Integrating Docker Scout with other systems](https://docs.docker.com/scout/integrations/).

## Grype

[Grype](https://github.com/anchore/grype) is an open-source scanner that checks container images against vulnerability databases like the NVD and distro advisories.

### Scan a DHI using Grype

After installing Grype, you can scan a Docker Hardened Image by pulling the image and running the scan command:               $ docker pull <your-namespace>/dhi-<image>:<tag>     $ grype <your-namespace>/dhi-<image>:<tag>     

Example output:               NAME               INSTALLED              FIXED-IN     TYPE  VULNERABILITY     SEVERITY    EPSS%  RISK     libperl5.36        5.36.0-7+deb12u2       (won't fix)  deb   CVE-2023-31484    High        79.45    1.1     perl               5.36.0-7+deb12u2       (won't fix)  deb   CVE-2023-31484    High        79.45    1.1     perl-base          5.36.0-7+deb12u2       (won't fix)  deb   CVE-2023-31484    High        79.45    1.1     ...

You should include the `--vex` flag to apply VEX statements during the scan, which filter out known non-exploitable CVEs. For more information, see the VEX section.

## Trivy

[Trivy](https://github.com/aquasecurity/trivy) is an open-source vulnerability scanner for containers and other artifacts. It detects vulnerabilities in OS packages and application dependencies.

### Scan a DHI using Trivy

After installing Trivy, you can scan a Docker Hardened Image by pulling the image and running the scan command:               $ docker pull <your-namespace>/dhi-<image>:<tag>     $ trivy image <your-namespace>/dhi-<image>:<tag>     

Example output:               Report Summary          ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ¬âââââââââââââ¬ââââââââââââââââââ¬ââââââââââ     â                                    Target                                    â    Type    â Vulnerabilities â Secrets â     ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ¼âââââââââââââ¼ââââââââââââââââââ¼ââââââââââ¤     â <namespace>/dhi-<image>:<tag> (debian 12.11)                                 â   debian   â       66        â    -    â     ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ¼âââââââââââââ¼ââââââââââââââââââ¼ââââââââââ¤     â opt/python-3.13.4/lib/python3.13/site-packages/pip-25.1.1.dist-info/METADATA â python-pkg â        0        â    -    â     ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ´âââââââââââââ´ââââââââââââââââââ´ââââââââââ

You should include the `--vex` flag to apply VEX statements during the scan, which filter out known non-exploitable CVEs. For more information, see the VEX section.

## Use VEX to filter known non-exploitable CVEs

Docker Hardened Images include signed VEX \(Vulnerability Exploitability eXchange\) attestations that identify vulnerabilities not relevant to the imageâs runtime behavior.

When using Docker Scout, these VEX statements are automatically applied and no manual configuration needed.

To manually create a JSON file VEX attestation for tools that support it:               $ docker scout attest get \       --predicate-type https://openvex.dev/ns/v0.2.0 \       --predicate \       <your-namespace>/dhi-<image>:<tag> --platform <platform> > vex.json     

For example:               $ docker scout attest get \       --predicate-type https://openvex.dev/ns/v0.2.0 \       --predicate \       docs/dhi-python:3.13 --platform linux/amd64 > vex.json     

This creates a `vex.json` file containing the VEX statements for the specified image. You can then use this file with tools that support VEX to filter out known non-exploitable CVEs.

For example, with Grype and Trivy, you can use the `--vex` flag to apply the VEX statements during the scan:               $ grype <your-namespace>/dhi-<image>:<tag> --vex vex.json