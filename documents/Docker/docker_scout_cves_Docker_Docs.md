# docker scout cves | Docker Docs

**URL:** http://docs.docker.com/reference/cli/docker/scout/cves
**Word Count:** 1740
**Links Count:** 501
**Scraped:** 2025-07-16 02:11:42
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Manuals](http://docs.docker.com/manuals/)

* * *

# docker scout cves

Description| Display CVEs identified in a software artifact   ---|---   Usage| `docker scout cves [OPTIONS] [IMAGE|DIRECTORY|ARCHIVE]`      ## Description

The `docker scout cves` command analyzes a software artifact for vulnerabilities.

If no image is specified, the most recently built image is used.

The following artifact types are supported:

  * Images   * OCI layout directories   * Tarball archives, as created by `docker save`   * Local directory or file

By default, the tool expects an image reference, such as:

  * `redis`   * `curlimages/curl:7.87.0`   * `mcr.microsoft.com/dotnet/runtime:7.0`

If the artifact you want to analyze is an OCI directory, a tarball archive, a local file or directory, or if you want to control from where the image will be resolved, you must prefix the reference with one of the following:

  * `image://` \(default\) use a local image, or fall back to a registry lookup   * `local://` use an image from the local image store \(don't do a registry lookup\)   * `registry://` use an image from a registry \(don't use a local image\)   * `oci-dir://` use an OCI layout directory   * `archive://` use a tarball archive, as created by `docker save`   * `fs://` use a local directory or file   * `sbom://` SPDX file or in-toto attestation file with SPDX predicate or `syft` json SBOM file In case of `sbom://` prefix, if the file is not defined then it will try to read it from the standard input.

## Options

Option| Default| Description   ---|---|---   `--details`| | Print details on default text output   `--env`| | Name of environment   `--epss`| | Display the EPSS scores and organize the package's CVEs according to their EPSS score      `--epss-percentile`| | Exclude CVEs with EPSS scores less than the specified percentile \(0 to 1\)      `--epss-score`| | Exclude CVEs with EPSS scores less than the specified value \(0 to 1\)      `-e, --exit-code`| | Return exit code '2' if vulnerabilities are detected   `--format`| `packages`| Output format of the generated vulnerability report:   \- packages: default output, plain text with vulnerabilities grouped by packages   \- sarif: json Sarif output   \- spdx: json SPDX output   \- gitlab: json GitLab output   \- markdown: markdown output \(including some html tags like collapsible sections\)   \- sbom: json SBOM output   `--ignore-base`| | Filter out CVEs introduced from base image   `--ignore-suppressed`| | Filter CVEs found in Scout exceptions based on the specified exception scope      `--locations`| | Print package locations including file paths and layer diff\_id   `--multi-stage`| | Show packages from multi-stage Docker builds   `--only-base`| | Only show CVEs introduced by the base image   `--only-cisa-kev`| | Filter to CVEs listed in the CISA KEV catalog   `--only-cve-id`| | Comma separated list of CVE ids \(like CVE-2021-45105\) to search for      `--only-fixed`| | Filter to fixable CVEs   `--only-metric`| | Comma separated list of CVSS metrics \(like AV:N or PR:L\) to filter CVEs by      `--only-package`| | Comma separated regular expressions to filter packages by   `--only-package-type`| | Comma separated list of package types \(like apk, deb, rpm, npm, pypi, golang, etc\)      `--only-severity`| | Comma separated list of severities \(critical, high, medium, low, unspecified\) to filter CVEs by      `--only-stage`| | Comma separated list of multi-stage Docker build stage names   `--only-unfixed`| | Filter to unfixed CVEs   `--only-vex-affected`| | Filter CVEs by VEX statements with status not affected   `--only-vuln-packages`| | When used with --format=only-packages ignore packages with no vulnerabilities      `--org`| | Namespace of the Docker organization   `-o, --output`| | Write the report to a file   `--platform`| | Platform of image to analyze   `--ref`| | Reference to use if the provided tarball contains multiple references.   Can only be used with archive   `--vex-author`| | List of VEX statement authors to accept   `--vex-location`| | File location of directory or file containing VEX statements      ## Examples

### Display vulnerabilities grouped by package               $ docker scout cves alpine     Analyzing image alpine     â Image stored for indexing     â Indexed 18 packages     â No vulnerable package detected     

### Display vulnerabilities from a `docker save` tarball               $ docker save alpine > alpine.tar          $ docker scout cves archive://alpine.tar     Analyzing archive alpine.tar     â Archive read     â SBOM of image already cached, 18 packages indexed     â No vulnerable package detected     

### Display vulnerabilities from an OCI directory               $ skopeo copy --override-os linux docker://alpine oci:alpine          $ docker scout cves oci-dir://alpine     Analyzing OCI directory alpine     â OCI directory read     â Image stored for indexing     â Indexed 19 packages     â No vulnerable package detected     

### Display vulnerabilities from the current directory               $ docker scout cves fs://.     

### Export vulnerabilities to a SARIF JSON file               $ docker scout cves --format sarif --output alpine.sarif.json alpine     Analyzing image alpine     â SBOM of image already cached, 18 packages indexed     â No vulnerable package detected     â Report written to alpine.sarif.json     

### Display markdown output

The following example shows how to generate the vulnerability report as markdown.               $ docker scout cves --format markdown alpine     â Pulled     â SBOM of image already cached, 19 packages indexed     â Detected 1 vulnerable package with 3 vulnerabilities     <h2>:mag: Vulnerabilities of <code>alpine</code></h2>          <details open="true"><summary>:package: Image Reference</strong> <code>alpine</code></summary>     <table>     <tr><td>digest</td><td><code>sha256:e3bd82196e98898cae9fe7fbfd6e2436530485974dc4fb3b7ddb69134eda2407</code></td><tr><tr><td>vulnerabilities</td><td><img alt="critical: 0" src="https://img.shields.io/badge/critical-0-lightgrey"/> <img alt="high: 0" src="https://img.shields.io/badge/high-0-lightgrey"/> <img alt="medium: 2" src="https://img.shields.io/badge/medium-2-fbb552"/> <img alt="low: 0" src="https://img.shields.io/badge/low-0-lightgrey"/> <img alt="unspecified: 1" src="https://img.shields.io/badge/unspecified-1-lightgrey"/></td></tr>     <tr><td>platform</td><td>linux/arm64</td></tr>     <tr><td>size</td><td>3.3 MB</td></tr>     <tr><td>packages</td><td>19</td></tr>     </table>     </details></table>     </details>     ...     

### List all vulnerable packages of a certain type

The following example shows how to generate a list of packages, only including packages of the specified type, and only showing packages that are vulnerable.               $ docker scout cves --format only-packages --only-package-type golang --only-vuln-packages golang:1.18.0     â Pulled     â SBOM of image already cached, 296 packages indexed     â Detected 1 vulnerable package with 40 vulnerabilities          Name   Version   Type         Vulnerabilities     âââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ     stdlib  1.18     golang     2C    29H     8M     1L     

### Display EPSS score \(--epss\)

The `--epss` flag adds [Exploit Prediction Scoring System \(EPSS\)](https://www.first.org/epss/) scores to the `docker scout cves` output. EPSS scores are estimates of the likelihood \(probability\) that a software vulnerability will be exploited in the wild in the next 30 days. The higher the score, the greater the probability that a vulnerability will be exploited.               $ docker scout cves --epss nginx      â Provenance obtained from attestation      â SBOM obtained from attestation, 232 packages indexed      â Pulled      â Detected 23 vulnerable packages with a total of 39 vulnerabilities          ...           â HIGH CVE-2023-52425        https://scout.docker.com/v/CVE-2023-52425        Affected range  : >=2.5.0-1        Fixed version   : not fixed        EPSS Score      : 0.000510        EPSS Percentile : 0.173680     

  * `EPSS Score` is a floating point number between 0 and 1 representing the probability of exploitation in the wild in the next 30 days \(following score publication\).   * `EPSS Percentile` is the percentile of the current score, the proportion of all scored vulnerabilities with the same or a lower EPSS score.

You can use the `--epss-score` and `--epss-percentile` flags to filter the output of `docker scout cves` based on these scores. For example, to only show vulnerabilities with an EPSS score higher than 0.5:               $ docker scout cves --epss --epss-score 0.5 nginx      â SBOM of image already cached, 232 packages indexed      â EPSS scores for 2024-03-01 already cached      â Detected 1 vulnerable package with 1 vulnerability          ...           â LOW CVE-2023-44487        https://scout.docker.com/v/CVE-2023-44487        Affected range  : >=1.22.1-9        Fixed version   : not fixed        EPSS Score      : 0.705850        EPSS Percentile : 0.979410     

EPSS scores are updated on a daily basis. By default, the latest available score is displayed. You can use the `--epss-date` flag to manually specify a date in the format `yyyy-mm-dd` for fetching EPSS scores.               $ docker scout cves --epss --epss-date 2024-01-02 nginx     

### List vulnerabilities from an SPDX file

The following example shows how to generate a list of vulnerabilities from an SPDX file using `syft`.               $ syft -o spdx-json alpine:3.16.1 | docker scout cves sbom://      â Pulled image      â Loaded image                                                                                                                              alpine:3.16.1      â Parsed image                                                                    sha256:3d81c46cd8756ddb6db9ec36fa06a6fb71c287fb265232ba516739dc67a5f07d      â Cataloged contents                                                                     274a317d88b54f9e67799244a1250cad3fe7080f45249fa9167d1f871218d35f        âââ â Packages                        [14 packages]        âââ â File digests                    [75 files]        âââ â File metadata                   [75 locations]        âââ â Executables                     [16 executables]         â Detected 2 vulnerable packages with a total of 11 vulnerabilities