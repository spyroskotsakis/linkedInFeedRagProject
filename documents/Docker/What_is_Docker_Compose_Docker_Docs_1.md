# What is Docker Compose? | Docker Docs

**URL:** https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-docker-compose/
**Word Count:** 885
**Links Count:** 86
**Scraped:** 2025-07-16 01:48:31
**Status:** completed

---

Back

[Get started](https://docs.docker.com/get-started/)

  * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

# What is Docker Compose?

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Explanation

If you've been following the guides so far, you've been working with single container applications. But, now you're wanting to do something more complicated - run databases, message queues, caches, or a variety of other services. Do you install everything in a single container? Run multiple containers? If you run multiple, how do you connect them all together?

One best practice for containers is that each container should do one thing and do it well. While there are exceptions to this rule, avoid the tendency to have one container do multiple things.

You can use multiple `docker run` commands to start multiple containers. But, you'll soon realize you'll need to manage networks, all of the flags needed to connect containers to those networks, and more. And when you're done, cleanup is a little more complicated.

With Docker Compose, you can define all of your containers and their configurations in a single YAML file. If you include this file in your code repository, anyone that clones your repository can get up and running with a single command.

It's important to understand that Compose is a declarative tool - you simply define it and go. You don't always need to recreate everything from scratch. If you make a change, run `docker compose up` again and Compose will reconcile the changes in your file and apply them intelligently.

> **Dockerfile versus Compose file** >  > A Dockerfile provides instructions to build a container image while a Compose file defines your running containers. Quite often, a Compose file references a Dockerfile to build an image to use for a particular service.

## Try it out

In this hands-on, you will learn how to use a Docker Compose to run a multi-container application. You'll use a simple to-do list app built with Node.js and MySQL as a database server.

### Start the application

Follow the instructions to run the to-do list app on your system.

  1. [Download and install](https://www.docker.com/products/docker-desktop/) Docker Desktop.

  2. Open a terminal and [clone this sample application](https://github.com/dockersamples/todo-list-app).                    git clone https://github.com/dockersamples/todo-list-app           

  3. Navigate into the `todo-list-app` directory:                    cd todo-list-app          

Inside this directory, you'll find a file named `compose.yaml`. This YAML file is where all the magic happens\! It defines all the services that make up your application, along with their configurations. Each service specifies its image, ports, volumes, networks, and any other settings necessary for its functionality. Take some time to explore the YAML file and familiarize yourself with its structure.

  4. Use the [`docker compose up`](https://docs.docker.com/reference/cli/docker/compose/up/) command to start the application:                    docker compose up -d --build          

When you run this command, you should see an output like this:                    [+] Running 5/5          â app 3 layers [â£¿â£¿â£¿]      0B/0B            Pulled          7.1s            â e6f4e57cc59e Download complete                          0.9s            â df998480d81d Download complete                          1.0s            â 31e174fedd23 Download complete                          2.5s            â 43c47a581c29 Download complete                          2.0s          [+] Running 4/4            â ¸ Network todo-list-app_default           Created         0.3s            â ¸ Volume "todo-list-app_todo-mysql-data"  Created         0.3s            â Container todo-list-app-app-1           Started         0.3s            â Container todo-list-app-mysql-1         Started         0.3s          

A lot happened here\! A couple of things to call out:

     * Two container images were downloaded from Docker Hub - node and MySQL      * A network was created for your application      * A volume was created to persist the database files between container restarts      * Two containers were started with all of their necessary config

If this feels overwhelming, don't worry\! You'll get there\!

  5. With everything now up and running, you can open <http://localhost:3000> in your browser to see the site. Feel free to add items to the list, check them off, and remove them.

![A screenshot of a webpage showing the todo-list application running on port 3000](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-app.webp)

![A screenshot of a webpage showing the todo-list application running on port 3000](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-app.webp)

  6. If you look at the Docker Desktop GUI, you can see the containers and dive deeper into their configuration.

![A screenshot of Docker Desktop dashboard showing the list of containers running todo-list app](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-containers.webp)

![A screenshot of Docker Desktop dashboard showing the list of containers running todo-list app](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-containers.webp)

### Tear it down

Since this application was started using Docker Compose, it's easy to tear it all down when you're done.

  1. In the CLI, use the [`docker compose down`](https://docs.docker.com/reference/cli/docker/compose/down/) command to remove everything:                    docker compose down          

You'll see output similar to the following:                    [+] Running 3/3          â Container todo-list-app-mysql-1  Removed        2.9s          â Container todo-list-app-app-1    Removed        0.1s          â Network todo-list-app_default    Removed        0.1s          

> **Volume persistence** >  > By default, volumes _aren't_ automatically removed when you tear down a Compose stack. The idea is that you might want the data back if you start the stack again. >  > If you do want to remove the volumes, add the `--volumes` flag when running the `docker compose down` command: >           >          docker compose down --volumes >          [+] Running 1/0 >          â Volume todo-list-app_todo-mysql-data  Removed >          

  2. Alternatively, you can use the Docker Desktop GUI to remove the containers by selecting the application stack and selecting the **Delete** button.

![A screenshot of the Docker Desktop GUI showing the containers view with an arrow pointing to the "Delete" button](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-delete.webp)

![A screenshot of the Docker Desktop GUI showing the containers view with an arrow pointing to the "Delete" button](https://docs.docker.com/get-started/docker-concepts/the-basics/images/todo-list-delete.webp)

> **Using the GUI for Compose stacks** >  > Note that if you remove the containers for a Compose app in the GUI, it's removing only the containers. You'll have to manually remove the network and volumes if you want to do so.

In this walkthrough, you learned how to use Docker Compose to start and stop a multi-container application.

## Additional resources

This page was a brief introduction to Compose. In the following resources, you can dive deeper into Compose and how to write Compose files.

  * [Overview of Docker Compose](https://docs.docker.com/compose/)   * [Overview of Docker Compose CLI](https://docs.docker.com/compose/reference/)   * [How Compose works](https://docs.docker.com/compose/intro/compose-application-model/)