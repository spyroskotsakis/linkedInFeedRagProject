# CVEs | Docker Docs

**URL:** http://docs.docker.com/dhi/core-concepts/cves
**Word Count:** 1720
**Links Count:** 666
**Scraped:** 2025-07-16 02:11:42
**Status:** completed

---

Back

[Manuals](https://docs.docker.com/manuals/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Reference](http://docs.docker.com/reference/)

* * *

# Common Vulnerabilities and Exposures \(CVEs\)

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## What are CVEs?

CVEs are publicly disclosed cybersecurity flaws in software or hardware. Each CVE is assigned a unique identifier \(e.g., CVE-2024-12345\) and includes a standardized description, allowing organizations to track and address vulnerabilities consistently.

In the context of Docker, CVEs often pertain to issues within base images, or application dependencies. These vulnerabilities can range from minor bugs to critical security risks, such as remote code execution or privilege escalation.

## Why are CVEs important?

Regularly scanning and updating Docker images to mitigate CVEs is crucial for maintaining a secure and compliant environment. Ignoring CVEs can lead to severe security breaches, including:

  * Unauthorized access: Exploits can grant attackers unauthorized access to systems.   * Data breaches: Sensitive information can be exposed or stolen.   * Service disruptions: Vulnerabilities can be leveraged to disrupt services or cause downtime.   * Compliance violations: Failure to address known vulnerabilities can lead to non-compliance with industry regulations and standards.

## How Docker Hardened Images help mitigate CVEs

Docker Hardened Images \(DHIs\) are crafted to minimize the risk of CVEs from the outset. By adopting a security-first approach, DHIs offer several advantages in CVE mitigation:

  * Reduced attack surface: DHIs are built using a distroless approach, stripping away unnecessary components and packages. This reduction in image size, up to 95% smaller than traditional images, limits the number of potential vulnerabilities, making it harder for attackers to exploit unneeded software.

  * Faster CVE remediation: Maintained by Docker with an enterprise-grade SLA, DHIs are continuously updated to address known vulnerabilities. Critical and high-severity CVEs are patched quickly, ensuring that your containers remain secure without manual intervention.

  * Proactive vulnerability management: By utilizing DHIs, organizations can proactively manage vulnerabilities. The images come with CVE and Vulnerability Exposure \(VEX\) feeds, enabling teams to stay informed about potential threats and take necessary actions promptly.

## Scan images for CVEs

Regularly scanning Docker images for CVEs is essential for maintaining a secure containerized environment. While Docker Scout is integrated into Docker Desktop and the Docker CLI, tools like Grype and Trivy offer alternative scanning capabilities. The following are instructions for using each tool to scan Docker images for CVEs.

### Docker Scout

Docker Scout is integrated into Docker Desktop and the Docker CLI. It provides vulnerability insights, CVE summaries, and direct links to remediation guidance.

#### Scan a DHI using Docker Scout

To scan a Docker Hardened Image using Docker Scout, run the following command:               $ docker scout cves <your-namespace>/dhi-<image>:<tag>     

Example output:                   v SBOM obtained from attestation, 101 packages found         v Provenance obtained from attestation         v VEX statements obtained from attestation         v No vulnerable package detected         ...

For more detailed filtering and JSON output, see [Docker Scout CLI reference](https://docs.docker.com/reference/cli/docker/scout/).

### Grype

[Grype](https://github.com/anchore/grype) is an open-source scanner that checks container images against vulnerability databases like the NVD and distro advisories.

#### Scan a DHI using Grype

After installing Grype, you can scan a Docker Hardened Image by pulling the image and running the scan command:               $ docker pull <your-namespace>/dhi-<image>:<tag>     $ grype <your-namespace>/dhi-<image>:<tag>     

Example output:               NAME               INSTALLED              FIXED-IN     TYPE  VULNERABILITY     SEVERITY    EPSS%  RISK     libperl5.36        5.36.0-7+deb12u2       (won't fix)  deb   CVE-2023-31484    High        79.45    1.1     perl               5.36.0-7+deb12u2       (won't fix)  deb   CVE-2023-31484    High        79.45    1.1     perl-base          5.36.0-7+deb12u2       (won't fix)  deb   CVE-2023-31484    High        79.45    1.1     ...

### Trivy

[Trivy](https://github.com/aquasecurity/trivy) is an open-source vulnerability scanner for containers and other artifacts. It detects vulnerabilities in OS packages and application dependencies.

#### Scan a DHI using Trivy

After installing Trivy, you can scan a Docker Hardened Image by pulling the image and running the scan command:               $ docker pull <your-namespace>/dhi-<image>:<tag>     $ trivy image <your-namespace>/dhi-<image>:<tag>     

Example output:               Report Summary          ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ¬âââââââââââââ¬ââââââââââââââââââ¬ââââââââââ     â                                    Target                                    â    Type    â Vulnerabilities â Secrets â     ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ¼âââââââââââââ¼ââââââââââââââââââ¼ââââââââââ¤     â <namespace>/dhi-<image>:<tag> (debian 12.11)                                 â   debian   â       66        â    -    â     ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ¼âââââââââââââ¼ââââââââââââââââââ¼ââââââââââ¤     â opt/python-3.13.4/lib/python3.13/site-packages/pip-25.1.1.dist-info/METADATA â python-pkg â        0        â    -    â     ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ´âââââââââââââ´ââââââââââââââââââ´ââââââââââ

## Use VEX to filter known non-exploitable CVEs

Docker Hardened Images include signed [VEX \(Vulnerability Exploitability eXchange\)](https://docs.docker.com/dhi/core-concepts/vex/) attestations that identify vulnerabilities not relevant to the imageâs runtime behavior.

When using Docker Scout, these VEX statements are automatically applied and no manual configuration needed.

To manually retrieve the VEX attestation for tools that support it:               $ docker scout attest get \       --predicate-type https://openvex.dev/ns/v0.2.0 \       --predicate \       <your-namespace>/dhi-<image>:<tag> --platform <platform> > vex.json     

For example:               $ docker scout attest get \       --predicate-type https://openvex.dev/ns/v0.2.0 \       --predicate \       docs/dhi-python:3.13 --platform linux/amd64 > vex.json     

This creates a `vex.json` file containing the VEX statements for the specified image. You can then use this file with tools that support VEX to filter out known non-exploitable CVEs.

For example, with Grype and Trivy, you can use the `--vex` flag to apply the VEX statements during the scan:               $ grype <your-namespace>/dhi-<image>:<tag> --vex vex.json