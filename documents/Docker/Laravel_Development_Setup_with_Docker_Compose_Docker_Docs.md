# Laravel Development Setup with Docker Compose | Docker Docs

**URL:** https://docs.docker.com/guides/frameworks/laravel/development-setup
**Word Count:** 1010
**Links Count:** 65
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

# Laravel Development Setup with Docker Compose

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

This guide demonstrates how to configure a **development** environment for a Laravel application using Docker and Docker Compose. It builds **on top of** the production image for PHP-FPM and then adds developer-focused featuresâlike Xdebugâto streamline debugging. By basing the development container on a known production image, you keep both environments closely aligned.

This setup includes PHP-FPM, Nginx, and PostgreSQL services \(although you can easily swap PostgreSQL for another database, like MySQL or MariaDB\). Everything runs in containers, so you can develop in isolation without altering your host system.

> Note >  > To experiment with a ready-to-run configuration, download the [Laravel Docker Examples](https://github.com/dockersamples/laravel-docker-examples) repository. It contains pre-configured setups for both development and production.

## Project structure               my-laravel-app/     âââ app/     âââ bootstrap/     âââ config/     âââ database/     âââ public/     âââ docker/     â   âââ common/     â   â   âââ php-fpm/     â   â       âââ Dockerfile     â   âââ development/     â   â   âââ php-fpm/     â   â   â   âââ entrypoint.sh     â   â   âââ workspace/     â   â   â   âââ Dockerfile     â   â   âââ nginx     â   â       âââ Dockerfile     â   â       âââ nginx.conf     â   âââ production/     âââ compose.dev.yaml     âââ compose.prod.yaml     âââ .dockerignore     âââ .env     âââ vendor/     âââ ...

This layout represents a typical Laravel project, with Docker configurations stored in a unified `docker` directory. Youâll find **two** Compose files â `compose.dev.yaml` \(for development\) and `compose.prod.yaml` \(for production\) â to keep your environments separate and manageable.

The environment includes a `workspace` service, a sidecar container for tasks like building front-end assets, running Artisan commands, and other CLI tools your project may require. While this extra container may seem unusual, itâs a familiar pattern in solutions like **Laravel Sail** and **Laradock**. It also includes **Xdebug** to aid in debugging.

## Create a Dockerfile for PHP-FPM

This Dockerfile **extends** the production image by installing Xdebug and adjusting user permissions to ease local development. That way, your development environment stays consistent with production while still offering extra debug features and improved file mounting.               # Builds a dev-only layer on top of the production image     FROM production AS development          # Use ARGs to define environment variables passed from the Docker build command or Docker Compose.     ARG XDEBUG_ENABLED=true     ARG XDEBUG_MODE=develop,coverage,debug,profile     ARG XDEBUG_HOST=host.docker.internal     ARG XDEBUG_IDE_KEY=DOCKER     ARG XDEBUG_LOG=/dev/stdout     ARG XDEBUG_LOG_LEVEL=0          USER root          # Configure Xdebug if enabled     RUN if [ "${XDEBUG_ENABLED}" = "true" ]; then \         pecl install xdebug && \         docker-php-ext-enable xdebug && \         echo "xdebug.mode=${XDEBUG_MODE}" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \         echo "xdebug.idekey=${XDEBUG_IDE_KEY}" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \         echo "xdebug.log=${XDEBUG_LOG}" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \         echo "xdebug.log_level=${XDEBUG_LOG_LEVEL}" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \         echo "xdebug.client_host=${XDEBUG_HOST}" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini ; \         echo "xdebug.start_with_request=yes" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini ; \     fi          # Add ARGs for syncing permissions     ARG UID=1000     ARG GID=1000          # Create a new user with the specified UID and GID, reusing an existing group if GID exists     RUN if getent group ${GID}; then \           group_name=$(getent group ${GID} | cut -d: -f1); \           useradd -m -u ${UID} -g ${GID} -s /bin/bash www; \         else \           groupadd -g ${GID} www && \           useradd -m -u ${UID} -g www -s /bin/bash www; \           group_name=www; \         fi          # Dynamically update php-fpm to use the new user and group     RUN sed -i "s/user = www-data/user = www/g" /usr/local/etc/php-fpm.d/www.conf && \         sed -i "s/group = www-data/group = $group_name/g" /usr/local/etc/php-fpm.d/www.conf               # Set the working directory     WORKDIR /var/www          # Copy the entrypoint script     COPY ./docker/development/php-fpm/entrypoint.sh /usr/local/bin/entrypoint.sh     RUN chmod +x /usr/local/bin/entrypoint.sh          # Switch back to the non-privileged user to run the application     USER www-data          # Change the default command to run the entrypoint script     ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]          # Expose port 9000 and start php-fpm server     EXPOSE 9000     CMD ["php-fpm"]

## Create a Dockerfile for Workspace

A workspace container provides a dedicated shell for asset compilation, Artisan/Composer commands, and other CLI tasks. This approach follows patterns from Laravel Sail and Laradock, consolidating all development tools into one container for convenience.               # docker/development/workspace/Dockerfile     # Use the official PHP CLI image as the base     FROM php:8.4-cli          # Set environment variables for user and group ID     ARG UID=1000     ARG GID=1000     ARG NODE_VERSION=22.0.0          # Install system dependencies and build libraries     RUN apt-get update && apt-get install -y --no-install-recommends \         curl \         unzip \         libpq-dev \         libonig-dev \         libssl-dev \         libxml2-dev \         libcurl4-openssl-dev \         libicu-dev \         libzip-dev \         && docker-php-ext-install -j$(nproc) \         pdo_mysql \         pdo_pgsql \         pgsql \         opcache \         intl \         zip \         bcmath \         soap \         && pecl install redis xdebug \         && docker-php-ext-enable redis xdebug\         && curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer \         && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*          # Use ARG to define environment variables passed from the Docker build command or Docker Compose.     ARG XDEBUG_ENABLED     ARG XDEBUG_MODE     ARG XDEBUG_HOST     ARG XDEBUG_IDE_KEY     ARG XDEBUG_LOG     ARG XDEBUG_LOG_LEVEL          # Configure Xdebug if enabled     RUN if [ "${XDEBUG_ENABLED}" = "true" ]; then \         docker-php-ext-enable xdebug && \         echo "xdebug.mode=${XDEBUG_MODE}" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \         echo "xdebug.idekey=${XDEBUG_IDE_KEY}" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \         echo "xdebug.log=${XDEBUG_LOG}" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \         echo "xdebug.log_level=${XDEBUG_LOG_LEVEL}" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini && \         echo "xdebug.client_host=${XDEBUG_HOST}" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini ; \         echo "xdebug.start_with_request=yes" >> /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini ; \     fi          # If the group already exists, use it; otherwise, create the 'www' group     RUN if getent group ${GID}; then \           useradd -m -u ${UID} -g ${GID} -s /bin/bash www; \         else \           groupadd -g ${GID} www && \           useradd -m -u ${UID} -g www -s /bin/bash www; \         fi && \         usermod -aG sudo www && \         echo 'www ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers          # Switch to the non-root user to install NVM and Node.js     USER www          # Install NVM (Node Version Manager) as the www user     RUN export NVM_DIR="$HOME/.nvm" && \         curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.0/install.sh | bash && \         [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh" && \         nvm install ${NODE_VERSION} && \         nvm alias default ${NODE_VERSION} && \         nvm use default          # Ensure NVM is available for all future shells     RUN echo 'export NVM_DIR="$HOME/.nvm"' >> /home/www/.bashrc && \         echo '[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"' >> /home/www/.bashrc && \         echo '[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"' >> /home/www/.bashrc          # Set the working directory     WORKDIR /var/www          # Override the entrypoint to avoid the default php entrypoint     ENTRYPOINT []          # Default command to keep the container running     CMD ["bash"]

> Note >  > If you prefer a **one-service-per-container** approach, simply omit the workspace container and run separate containers for each task. For example, you could use a dedicated `php-cli` container for your PHP scripts, and a `node` container to handle the asset building.

## Create a Docker Compose Configuration for development

Here's the `compose.yaml` file to set up the development environment:               services:       web:         image: nginx:latest # Using the default Nginx image with custom configuration.         volumes:           # Mount the application code for live updates           - ./:/var/www           # Mount the Nginx configuration file           - ./docker/development/nginx/nginx.conf:/etc/nginx/nginx.conf:ro         ports:           # Map port 80 inside the container to the port specified by 'NGINX_PORT' on the host machine           - "80:80"         environment:           - NGINX_HOST=localhost         networks:           - laravel-development         depends_on:           php-fpm:             condition: service_started # Wait for php-fpm to start            php-fpm:         # For the php-fpm service, we will use our common PHP-FPM Dockerfile with the development target         build:           context: .           dockerfile: ./docker/common/php-fpm/Dockerfile           target: development           args:             UID: ${UID:-1000}             GID: ${GID:-1000}             XDEBUG_ENABLED: ${XDEBUG_ENABLED:-true}             XDEBUG_MODE: develop,coverage,debug,profile             XDEBUG_HOST: ${XDEBUG_HOST:-host.docker.internal}             XDEBUG_IDE_KEY: ${XDEBUG_IDE_KEY:-DOCKER}             XDEBUG_LOG: /dev/stdout             XDEBUG_LOG_LEVEL: 0         env_file:           # Load the environment variables from the Laravel application           - .env         user: "${UID:-1000}:${GID:-1000}"         volumes:           # Mount the application code for live updates           - ./:/var/www         networks:           - laravel-development         depends_on:           postgres:             condition: service_started # Wait for postgres to start            workspace:         # For the workspace service, we will also create a custom image to install and setup all the necessary stuff.         build:           context: .           dockerfile: ./docker/development/workspace/Dockerfile           args:             UID: ${UID:-1000}             GID: ${GID:-1000}             XDEBUG_ENABLED: ${XDEBUG_ENABLED:-true}             XDEBUG_MODE: develop,coverage,debug,profile             XDEBUG_HOST: ${XDEBUG_HOST:-host.docker.internal}             XDEBUG_IDE_KEY: ${XDEBUG_IDE_KEY:-DOCKER}             XDEBUG_LOG: /dev/stdout             XDEBUG_LOG_LEVEL: 0         tty: true # Enables an interactive terminal         stdin_open: true # Keeps standard input open for 'docker exec'         env_file:           - .env         volumes:           - ./:/var/www         networks:           - laravel-development            postgres:         image: postgres:16         ports:           - "${POSTGRES_PORT:-5432}:5432"         environment:           - POSTGRES_DB=app           - POSTGRES_USER=laravel           - POSTGRES_PASSWORD=secret         volumes:           - postgres-data-development:/var/lib/postgresql/data         networks:           - laravel-development            redis:         image: redis:alpine         networks:           - laravel-development          networks:       laravel-development:          volumes:       postgres-data-development:

> Note >  > Ensure you have an `.env` file at the root of your Laravel project with the necessary configurations. You can use the `.env.example` file as a template.

## Run your development environment

To start the development environment, use:               $ docker compose -f compose.dev.yaml up --build -d     

Run this command to build and start the development environment in detached mode. When the containers finish initializing, visit <http://localhost/> to see your Laravel app in action.

## Summary

By building on top of the production image and adding debug tools like Xdebug, you create a Laravel development workflow that closely mirrors production. The optional workspace container simplifies tasks like asset building and running Artisan commands. If you prefer a separate container for every service \(e.g., a dedicated `php-cli` and `node` container\), you can skip the workspace approach. Either way, Docker Compose provides an efficient, consistent way to develop your Laravel project.

[Common Questions on Using Laravel with Docker Â»](https://docs.docker.com/guides/frameworks/laravel/common-questions/)