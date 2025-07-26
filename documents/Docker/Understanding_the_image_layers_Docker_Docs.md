# Understanding the image layers | Docker Docs

**URL:** https://docs.docker.com/get-started/docker-concepts/building-images/understanding-image-layers
**Word Count:** 1252
**Links Count:** 95
**Scraped:** 2025-07-16 01:54:44
**Status:** completed

---

Back

[Get started](https://docs.docker.com/get-started/)

  * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)   * [Reference](https://docs.docker.com/reference/)

* * *

# Understanding the image layers

Page options

Copy page as Markdown for LLMs

View page as plain text

Ask questions with Docs AI

Table of contents

* * *

## Explanation

As you learned in [What is an image?](https://docs.docker.com/get-started/docker-concepts/the-basics/what-is-an-image/), container images are composed of layers. And each of these layers, once created, are immutable. But, what does that actually mean? And how are those layers used to create the filesystem a container can use?

### Image layers

Each layer in an image contains a set of filesystem changes - additions, deletions, or modifications. Letâs look at a theoretical image:

  1. The first layer adds basic commands and a package manager, such as apt.   2. The second layer installs a Python runtime and pip for dependency management.   3. The third layer copies in an applicationâs specific requirements.txt file.   4. The fourth layer installs that applicationâs specific dependencies.   5. The fifth layer copies in the actual source code of the application.

This example might look like:

![screenshot of the flowchart showing the concept of the image layers](https://docs.docker.com/get-started/docker-concepts/building-images/images/container_image_layers.webp)

![screenshot of the flowchart showing the concept of the image layers](https://docs.docker.com/get-started/docker-concepts/building-images/images/container_image_layers.webp)

This is beneficial because it allows layers to be reused between images. For example, imagine you wanted to create another Python application. Due to layering, you can leverage the same Python base. This will make builds faster and reduce the amount of storage and bandwidth required to distribute the images. The image layering might look similar to the following:

![screenshot of the flowchart showing the benefits of the image layering](https://docs.docker.com/get-started/docker-concepts/building-images/images/container_image_layer_reuse.webp)

![screenshot of the flowchart showing the benefits of the image layering](https://docs.docker.com/get-started/docker-concepts/building-images/images/container_image_layer_reuse.webp)

Layers let you extend images of others by reusing their base layers, allowing you to add only the data that your application needs.

### Stacking the layers

Layering is made possible by content-addressable storage and union filesystems. While this will get technical, hereâs how it works:

  1. After each layer is downloaded, it is extracted into its own directory on the host filesystem.   2. When you run a container from an image, a union filesystem is created where layers are stacked on top of each other, creating a new and unified view.   3. When the container starts, its root directory is set to the location of this unified directory, using `chroot`.

When the union filesystem is created, in addition to the image layers, a directory is created specifically for the running container. This allows the container to make filesystem changes while allowing the original image layers to remain untouched. This enables you to run multiple containers from the same underlying image.

## Try it out

In this hands-on guide, you will create new image layers manually using the [`docker container commit`](https://docs.docker.com/reference/cli/docker/container/commit/) command. Note that youâll rarely create images this way, as youâll normally [use a Dockerfile](https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/). But, it makes it easier to understand how itâs all working.

### Create a base image

In this first step, you will create your own base image that you will then use for the following steps.

  1. [Download and install](https://www.docker.com/products/docker-desktop/) Docker Desktop.

  2. In a terminal, run the following command to start a new container:                    $ docker run --name=base-container -ti ubuntu          

Once the image has been downloaded and the container has started, you should see a new shell prompt. This is running inside your container. It will look similar to the following \(the container ID will vary\):                    root@d8c5ca119fcd:/#          

  3. Inside the container, run the following command to install Node.js:                    $ apt update && apt install -y nodejs          

When this command runs, it downloads and installs Node inside the container. In the context of the union filesystem, these filesystem changes occur within the directory unique to this container.

  4. Validate if Node is installed by running the following command:                    $ node -e 'console.log("Hello world!")'          

You should then see a âHello world\!â appear in the console.

  5. Now that you have Node installed, youâre ready to save the changes youâve made as a new image layer, from which you can start new containers or build new images. To do so, you will use the [`docker container commit`](https://docs.docker.com/reference/cli/docker/container/commit/) command. Run the following command in a new terminal:                    $ docker container commit -m "Add node" base-container node-base          

  6. View the layers of your image using the `docker image history` command:                    $ docker image history node-base          

You will see output similar to the following:                    IMAGE          CREATED          CREATED BY                                      SIZE      COMMENT          d5c1fca2cdc4   10 seconds ago   /bin/bash                                       126MB     Add node          2b7cc08dcdbb   5 weeks ago      /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B          <missing>      5 weeks ago      /bin/sh -c #(nop) ADD file:07cdbabf782942af0â¦   69.2MB          <missing>      5 weeks ago      /bin/sh -c #(nop)  LABEL org.opencontainers.â¦   0B          <missing>      5 weeks ago      /bin/sh -c #(nop)  LABEL org.opencontainers.â¦   0B          <missing>      5 weeks ago      /bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH     0B          <missing>      5 weeks ago      /bin/sh -c #(nop)  ARG RELEASE                  0B          

Note the âAdd nodeâ comment on the top line. This layer contains the Node.js install you just made.

  7. To prove your image has Node installed, you can start a new container using this new image:                    $ docker run node-base node -e "console.log('Hello again')"          

With that, you should get a âHello againâ output in the terminal, showing Node was installed and working.

  8. Now that youâre done creating your base image, you can remove that container:                    $ docker rm -f base-container          

> **Base image definition** >  > A base image is a foundation for building other images. It's possible to use any images as a base image. However, some images are intentionally created as building blocks, providing a foundation or starting point for an application. >  > In this example, you probably wonât deploy this `node-base` image, as it doesnât actually do anything yet. But itâs a base you can use for other builds.

### Build an app image

Now that you have a base image, you can extend that image to build additional images.

  1. Start a new container using the newly created node-base image:                    $ docker run --name=app-container -ti node-base          

  2. Inside of this container, run the following command to create a Node program:                    $ echo 'console.log("Hello from an app")' > app.js          

To run this Node program, you can use the following command and see the message printed on the screen:                    $ node app.js          

  3. In another terminal, run the following command to save this containerâs changes as a new image:                    $ docker container commit -c "CMD node app.js" -m "Add app" app-container sample-app          

This command not only creates a new image named `sample-app`, but also adds additional configuration to the image to set the default command when starting a container. In this case, you are setting it to automatically run `node app.js`.

  4. In a terminal outside of the container, run the following command to view the updated layers:                    $ docker image history sample-app          

Youâll then see output that looks like the following. Note the top layer comment has âAdd appâ and the next layer has âAdd nodeâ:                    IMAGE          CREATED              CREATED BY                                      SIZE      COMMENT          c1502e2ec875   About a minute ago   /bin/bash                                       33B       Add app          5310da79c50a   4 minutes ago        /bin/bash                                       126MB     Add node          2b7cc08dcdbb   5 weeks ago          /bin/sh -c #(nop)  CMD ["/bin/bash"]            0B          <missing>      5 weeks ago          /bin/sh -c #(nop) ADD file:07cdbabf782942af0â¦   69.2MB          <missing>      5 weeks ago          /bin/sh -c #(nop)  LABEL org.opencontainers.â¦   0B          <missing>      5 weeks ago          /bin/sh -c #(nop)  LABEL org.opencontainers.â¦   0B          <missing>      5 weeks ago          /bin/sh -c #(nop)  ARG LAUNCHPAD_BUILD_ARCH     0B          <missing>      5 weeks ago          /bin/sh -c #(nop)  ARG RELEASE                  0B          

  5. Finally, start a new container using the brand new image. Since you specified the default command, you can use the following command:                    $ docker run sample-app          

You should see your greeting appear in the terminal, coming from your Node program.

  6. Now that youâre done with your containers, you can remove them using the following command:                    $ docker rm -f app-container          

## Additional resources

If youâd like to dive deeper into the things you learned, check out the following resources:

  * [`docker image history`](https://docs.docker.com/reference/cli/docker/image/history/)   * [`docker container commit`](https://docs.docker.com/reference/cli/docker/container/commit/)

## Next steps

As hinted earlier, most image builds donât use `docker container commit`. Instead, youâll use a Dockerfile which automates these steps for you.

[Writing a Dockerfile](https://docs.docker.com/get-started/docker-concepts/building-images/writing-a-dockerfile/)