# Build checks | Docker Docs

**URL:** http://docs.docker.com/reference/build-checks
**Word Count:** 1019
**Links Count:** 493
**Scraped:** 2025-07-16 02:10:49
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](http://docs.docker.com/get-started/)   * [Guides](http://docs.docker.com/guides/)   * [Manuals](http://docs.docker.com/manuals/)

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

Name| Description   ---|---   [StageNameCasing](http://docs.docker.com/reference/stage-name-casing/)| Stage names should be lowercase   [FromAsCasing](http://docs.docker.com/reference/from-as-casing/)| The 'as' keyword should match the case of the 'from' keyword   [NoEmptyContinuation](http://docs.docker.com/reference/no-empty-continuation/)| Empty continuation lines will become errors in a future release   [ConsistentInstructionCasing](http://docs.docker.com/reference/consistent-instruction-casing/)| All commands within the Dockerfile should use the same casing \(either upper or lower\)   [DuplicateStageName](http://docs.docker.com/reference/duplicate-stage-name/)| Stage names should be unique   [ReservedStageName](http://docs.docker.com/reference/reserved-stage-name/)| Reserved words should not be used as stage names   [JSONArgsRecommended](http://docs.docker.com/reference/json-args-recommended/)| JSON arguments recommended for ENTRYPOINT/CMD to prevent unintended behavior related to OS signals   [MaintainerDeprecated](http://docs.docker.com/reference/maintainer-deprecated/)| The MAINTAINER instruction is deprecated, use a label instead to define an image author   [UndefinedArgInFrom](http://docs.docker.com/reference/undefined-arg-in-from/)| FROM command must use declared ARGs   [WorkdirRelativePath](http://docs.docker.com/reference/workdir-relative-path/)| Relative workdir without an absolute workdir declared within the build can have unexpected results if the base image changes   [UndefinedVar](http://docs.docker.com/reference/undefined-var/)| Variables should be defined before their use   [MultipleInstructionsDisallowed](http://docs.docker.com/reference/multiple-instructions-disallowed/)| Multiple instructions of the same type should not be used in the same stage   [LegacyKeyValueFormat](http://docs.docker.com/reference/legacy-key-value-format/)| Legacy key/value format with whitespace separator should not be used   [RedundantTargetPlatform](http://docs.docker.com/reference/redundant-target-platform/)| Setting platform to predefined $TARGETPLATFORM in FROM is redundant as this is the default behavior   [SecretsUsedInArgOrEnv](http://docs.docker.com/reference/secrets-used-in-arg-or-env/)| Sensitive data should not be used in the ARG or ENV commands   [InvalidDefaultArgInFrom](http://docs.docker.com/reference/invalid-default-arg-in-from/)| Default value for global ARG results in an empty or invalid base image name   [FromPlatformFlagConstDisallowed](http://docs.docker.com/reference/from-platform-flag-const-disallowed/)| FROM --platform flag should not use a constant value   [CopyIgnoredFile \(experimental\)](http://docs.docker.com/reference/copy-ignored-file/)| Attempting to Copy file that is excluded by .dockerignore   [InvalidDefinitionDescription \(experimental\)](http://docs.docker.com/reference/invalid-definition-description/)| Comment for build stage or argument should follow the format: \`\# \`. If this is not intended to be a description comment, add an empty line or comment between the instruction and the comment.