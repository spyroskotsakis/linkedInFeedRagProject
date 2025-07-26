# Laravel applications with Docker Compose | Docker Docs

**URL:** https://docs.docker.com/guides/frameworks/laravel
**Word Count:** 359
**Links Count:** 54
**Scraped:** 2025-07-16 02:04:56
**Status:** completed

---

Back

[Guides](https://docs.docker.com/guides/)

  * [Get started](https://docs.docker.com/get-started/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

[Develop and Deploy Laravel applications with Docker Compose](https://docs.docker.com/guides/frameworks/laravel/)

Learn how to efficiently set up Laravel development and production environments using Docker Compose.

![](https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/php/php-original.svg) PHP [ Frameworks](https://docs.docker.com/tags/frameworks/)

30 minutes

[1](https://docs.docker.com/guides/frameworks/laravel/prerequisites/)

[Prerequisites for Setting Up Laravel with Docker Compose](https://docs.docker.com/guides/frameworks/laravel/prerequisites/)

[2](https://docs.docker.com/guides/frameworks/laravel/production-setup/)

[Laravel Production Setup with Docker Compose](https://docs.docker.com/guides/frameworks/laravel/production-setup/)

[3](https://docs.docker.com/guides/frameworks/laravel/development-setup/)

[Laravel Development Setup with Docker Compose](https://docs.docker.com/guides/frameworks/laravel/development-setup/)

[4](https://docs.docker.com/guides/frameworks/laravel/common-questions/)

[Common Questions on Using Laravel with Docker](https://docs.docker.com/guides/frameworks/laravel/common-questions/)

Resources:

  * [Laravel](https://laravel.com/)   * [Docker Compose](https://docs.docker.com/compose/)   * [Use Compose in production](https://docs.docker.com/compose/how-tos/production/)   * [Repository with examples](https://github.com/dockersamples/laravel-docker-examples)

[Â« Back to all guides](https://docs.docker.com/guides/)

# Develop and Deploy Laravel applications with Docker Compose

Table of contents

* * *

Laravel is a popular PHP framework that allows developers to build web applications quickly and effectively. Docker Compose simplifies the management of development and production environments by defining essential services, like PHP, a web server, and a database, in a single YAML file. This guide provides a streamlined approach to setting up a robust Laravel environment using Docker Compose, focusing on simplicity and efficiency.

> **Acknowledgment** >  > Docker would like to thank [Sergei Shitikov](https://github.com/rw4lll) for his contribution to this guide.

The demonstrated examples can be found in [this GitHub repository](https://github.com/dockersamples/laravel-docker-examples). Docker Compose offers a straightforward approach to connecting multiple containers for Laravel, though similar setups can also be achieved using tools like Docker Swarm, Kubernetes, or individual Docker containers.

This guide is intended for educational purposes, helping developers adapt and optimize configurations for their specific use cases. Additionally, there are existing tools that support Laravel in containers:

  * [Laravel Sail](https://laravel.com/docs/12.x/sail): An official package for easily starting Laravel in Docker.   * [Laradock](https://github.com/laradock/laradock): A community project that helps run Laravel applications in Docker.

## What youâll learn

  * How to use Docker Compose to set up a Laravel development and production environment.   * Defining services that make Laravel development easier, including PHP-FPM, Nginx, and database containers.   * Best practices for managing Laravel environments using containerization.

## Whoâs this for?

  * Developers who work with Laravel and want to streamline environment management.   * DevOps engineers seeking efficient ways to manage and deploy Laravel applications.

## Modules

  1. [Prerequisites for Setting Up Laravel with Docker Compose](https://docs.docker.com/guides/frameworks/laravel/prerequisites/)

Ensure you have the required tools and knowledge before setting up Laravel with Docker Compose.

  2. [Laravel Production Setup with Docker Compose](https://docs.docker.com/guides/frameworks/laravel/production-setup/)

Set up a production-ready environment for Laravel using Docker Compose.

  3. [Laravel Development Setup with Docker Compose](https://docs.docker.com/guides/frameworks/laravel/development-setup/)

Set up a Laravel development environment using Docker Compose.

  4. [Common Questions on Using Laravel with Docker](https://docs.docker.com/guides/frameworks/laravel/common-questions/)

Find answers to common questions about setting up and managing Laravel environments with Docker Compose, including troubleshooting and best practices.