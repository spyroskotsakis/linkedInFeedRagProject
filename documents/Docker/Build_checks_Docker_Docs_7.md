# Build checks | Docker Docs

**URL:** https://docs.docker.com/reference/build-checks/
**Word Count:** 1019
**Links Count:** 493
**Scraped:** 2025-07-16 01:49:39
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# Build checks

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

* * *

BuildKit has built-in support for analyzing your build configuration based on a set of pre-defined rules for enforcing Dockerfile and building best practices. Adhering to these rules helps avoid errors and ensures good readability of your Dockerfile.

Checks run as a build invocation, but instead of producing a build output, it performs a series of checks to validate that your build doesn't violate any of the rules. To run a check, use the `--check` flag:               $ docker build --check .     

To learn more about how to use build checks, see [Checking your build configuration](https://docs.docker.com/build/checks/).

Name| Description   ---|---   [StageNameCasing](https://docs.docker.com/reference/build-checks/stage-name-casing/)| Stage names should be lowercase   [FromAsCasing](https://docs.docker.com/reference/build-checks/from-as-casing/)| The 'as' keyword should match the case of the 'from' keyword   [NoEmptyContinuation](https://docs.docker.com/reference/build-checks/no-empty-continuation/)| Empty continuation lines will become errors in a future release   [ConsistentInstructionCasing](https://docs.docker.com/reference/build-checks/consistent-instruction-casing/)| All commands within the Dockerfile should use the same casing \(either upper or lower\)   [DuplicateStageName](https://docs.docker.com/reference/build-checks/duplicate-stage-name/)| Stage names should be unique   [ReservedStageName](https://docs.docker.com/reference/build-checks/reserved-stage-name/)| Reserved words should not be used as stage names   [JSONArgsRecommended](https://docs.docker.com/reference/build-checks/json-args-recommended/)| JSON arguments recommended for ENTRYPOINT/CMD to prevent unintended behavior related to OS signals   [MaintainerDeprecated](https://docs.docker.com/reference/build-checks/maintainer-deprecated/)| The MAINTAINER instruction is deprecated, use a label instead to define an image author   [UndefinedArgInFrom](https://docs.docker.com/reference/build-checks/undefined-arg-in-from/)| FROM command must use declared ARGs   [WorkdirRelativePath](https://docs.docker.com/reference/build-checks/workdir-relative-path/)| Relative workdir without an absolute workdir declared within the build can have unexpected results if the base image changes   [UndefinedVar](https://docs.docker.com/reference/build-checks/undefined-var/)| Variables should be defined before their use   [MultipleInstructionsDisallowed](https://docs.docker.com/reference/build-checks/multiple-instructions-disallowed/)| Multiple instructions of the same type should not be used in the same stage   [LegacyKeyValueFormat](https://docs.docker.com/reference/build-checks/legacy-key-value-format/)| Legacy key/value format with whitespace separator should not be used   [RedundantTargetPlatform](https://docs.docker.com/reference/build-checks/redundant-target-platform/)| Setting platform to predefined $TARGETPLATFORM in FROM is redundant as this is the default behavior   [SecretsUsedInArgOrEnv](https://docs.docker.com/reference/build-checks/secrets-used-in-arg-or-env/)| Sensitive data should not be used in the ARG or ENV commands   [InvalidDefaultArgInFrom](https://docs.docker.com/reference/build-checks/invalid-default-arg-in-from/)| Default value for global ARG results in an empty or invalid base image name   [FromPlatformFlagConstDisallowed](https://docs.docker.com/reference/build-checks/from-platform-flag-const-disallowed/)| FROM --platform flag should not use a constant value   [CopyIgnoredFile \(experimental\)](https://docs.docker.com/reference/build-checks/copy-ignored-file/)| Attempting to Copy file that is excluded by .dockerignore   [InvalidDefinitionDescription \(experimental\)](https://docs.docker.com/reference/build-checks/invalid-definition-description/)| Comment for build stage or argument should follow the format: \`\# \`. If this is not intended to be a description comment, add an empty line or comment between the instruction and the comment.