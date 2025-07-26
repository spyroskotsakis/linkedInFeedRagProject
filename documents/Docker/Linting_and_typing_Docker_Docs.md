# Linting and typing | Docker Docs

**URL:** https://docs.docker.com/guides/python/lint-format-typing
**Word Count:** 320
**Links Count:** 71
**Scraped:** 2025-07-16 02:04:38
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Python language-specific guide](https://docs.docker.com/guides/python/)

This guide explains how to containerize Python applications using Docker.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg) Python

20 minutes

[1](https://docs.docker.com/guides/python/containerize/)

[Containerize your app](https://docs.docker.com/guides/python/containerize/)

[2](https://docs.docker.com/guides/python/develop/)

[Develop your app](https://docs.docker.com/guides/python/develop/)

[3](https://docs.docker.com/guides/python/lint-format-typing/)

[Linting and typing](https://docs.docker.com/guides/python/lint-format-typing/)

[4](https://docs.docker.com/guides/python/configure-github-actions/)

[Automate your builds with GitHub Actions](https://docs.docker.com/guides/python/configure-github-actions/)

[5](https://docs.docker.com/guides/python/deploy/)

[Test your deployment](https://docs.docker.com/guides/python/deploy/)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Linting, formatting, and type checking for Python

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Prerequisites

Complete [Develop your app](https://docs.docker.com/guides/python/develop/).

## Overview

In this section, you'll learn how to set up code quality tools for your Python application. This includes:

  * Linting and formatting with Ruff   * Static type checking with Pyright   * Automating checks with pre-commit hooks

## Linting and formatting with Ruff

Ruff is an extremely fast Python linter and formatter written in Rust. It replaces multiple tools like flake8, isort, and black with a single unified tool.

Create a `pyproject.toml` file:               [tool.ruff]     target-version = "py312"          [tool.ruff.lint]     select = [         "E",  # pycodestyle errors         "W",  # pycodestyle warnings         "F",  # pyflakes         "I",  # isort         "B",  # flake8-bugbear         "C4",  # flake8-comprehensions         "UP",  # pyupgrade         "ARG001", # unused arguments in functions     ]     ignore = [         "E501",  # line too long, handled by black         "B008",  # do not perform function calls in argument defaults         "W191",  # indentation contains tabs         "B904",  # Allow raising exceptions without from e, for HTTPException     ]

### Using Ruff

Run these commands to check and format your code:               # Check for errors     ruff check .          # Automatically fix fixable errors     ruff check --fix .          # Format code     ruff format .

## Type checking with Pyright

Pyright is a fast static type checker for Python that works well with modern Python features.

Add `Pyright` configuration in `pyproject.toml`:               [tool.pyright]     typeCheckingMode = "strict"     pythonVersion = "3.12"     exclude = [".venv"]

### Running Pyright

To check your code for type errors:               pyright

## Setting up pre-commit hooks

Pre-commit hooks automatically run checks before each commit. The following `.pre-commit-config.yaml` snippet sets up Ruff:                 https: https://github.com/charliermarsh/ruff-pre-commit       rev: v0.2.2       hooks:         - id: ruff           args: [--fix]         - id: ruff-format

To install and use:               pre-commit install     git commit -m "Test commit"  # Automatically runs checks

## Summary

In this section, you learned how to:

  * Configure and use Ruff for linting and formatting   * Set up Pyright for static type checking   * Automate checks with pre-commit hooks

These tools help maintain code quality and catch errors early in development.

## Next steps

  * [Configure GitHub Actions](https://docs.docker.com/guides/python/configure-github-actions/) to run these checks automatically   * Customize linting rules to match your team's style preferences   * Explore advanced type checking features

[Automate your builds with GitHub Actions Â»](https://docs.docker.com/guides/python/configure-github-actions/)