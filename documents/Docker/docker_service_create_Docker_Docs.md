# docker service create | Docker Docs

**URL:** https://docs.docker.com/reference/cli/docker/service/create
**Word Count:** 5884
**Links Count:** 578
**Scraped:** 2025-07-16 01:57:40
**Status:** completed

---

Back

[Reference](https://docs.docker.com/reference/)

  * [Get started](https://docs.docker.com/get-started/)   * [Guides](https://docs.docker.com/guides/)   * [Manuals](https://docs.docker.com/manuals/)

* * *

# docker service create

Description| Create a new service   ---|---   Usage| `docker service create [OPTIONS] IMAGE [COMMAND] [ARG...]`      Swarm This command works with the Swarm orchestrator.

## Description

Creates a service as described by the specified parameters.

> Note >  > This is a cluster management command, and must be executed on a swarm manager node. To learn about managers and workers, refer to the [Swarm mode section](https://docs.docker.com/engine/swarm/) in the documentation.

## Options

Option| Default| Description   ---|---|---   `--cap-add`| | API 1.41+ Add Linux capabilities   `--cap-drop`| | API 1.41+ Drop Linux capabilities   `--config`| | API 1.30+ Specify configurations to expose to the service   `--constraint`| | Placement constraints   `--container-label`| | Container labels   `--credential-spec`| | API 1.29+ Credential spec for managed service account \(Windows only\)   `-d, --detach`| | API 1.29+ Exit immediately instead of waiting for the service to converge   `--dns`| | API 1.25+ Set custom DNS servers   `--dns-option`| | API 1.25+ Set DNS options   `--dns-search`| | API 1.25+ Set custom DNS search domains   `--endpoint-mode`| `vip`| Endpoint mode \(vip or dnsrr\)   `--entrypoint`| | Overwrite the default ENTRYPOINT of the image   `-e, --env`| | Set environment variables   `--env-file`| | Read in a file of environment variables   `--generic-resource`| | User defined resources   `--group`| | API 1.25+ Set one or more supplementary user groups for the container   `--health-cmd`| | API 1.25+ Command to run to check health   `--health-interval`| | API 1.25+ Time between running the check \(ms|s|m|h\)   `--health-retries`| | API 1.25+ Consecutive failures needed to report unhealthy   `--health-start-interval`| | API 1.44+ Time between running the check during the start period \(ms|s|m|h\)   `--health-start-period`| | API 1.29+ Start period for the container to initialize before counting retries towards unstable \(ms|s|m|h\)      `--health-timeout`| | API 1.25+ Maximum time to allow one check to run \(ms|s|m|h\)   `--host`| | API 1.25+ Set one or more custom host-to-IP mappings \(host:ip\)   `--hostname`| | API 1.25+ Container hostname   `--init`| | API 1.37+ Use an init inside each service container to forward signals and reap processes      `--isolation`| | API 1.35+ Service container isolation mode   `-l, --label`| | Service labels   `--limit-cpu`| | Limit CPUs   `--limit-memory`| | Limit Memory   `--limit-pids`| | API 1.41+ Limit maximum number of processes \(default 0 = unlimited\)   `--log-driver`| | Logging driver for service   `--log-opt`| | Logging driver options   `--max-concurrent`| | API 1.41+ Number of job tasks to run concurrently \(default equal to --replicas\)      `--mode`| `replicated`| Service mode \(`replicated`, `global`, `replicated-job`, `global-job`\)      `--mount`| | Attach a filesystem mount to the service   `--name`| | Service name   `--network`| | Network attachments   `--no-healthcheck`| | API 1.25+ Disable any container-specified HEALTHCHECK   `--no-resolve-image`| | API 1.30+ Do not query the registry to resolve image digest and supported platforms      `--oom-score-adj`| | API 1.46+ Tune host's OOM preferences \(-1000 to 1000\)   `--placement-pref`| | API 1.28+ Add a placement preference   `-p, --publish`| | Publish a port as a node port   `-q, --quiet`| | Suppress progress output   `--read-only`| | API 1.28+ Mount the container's root filesystem as read only   `--replicas`| | Number of tasks   `--replicas-max-per-node`| | API 1.40+ Maximum number of tasks per node \(default 0 = unlimited\)   `--reserve-cpu`| | Reserve CPUs   `--reserve-memory`| | Reserve Memory   `--restart-condition`| | Restart when condition is met \(`none`, `on-failure`, `any`\) \(default `any`\)      `--restart-delay`| | Delay between restart attempts \(ns|us|ms|s|m|h\) \(default 5s\)   `--restart-max-attempts`| | Maximum number of restarts before giving up   `--restart-window`| | Window used to evaluate the restart policy \(ns|us|ms|s|m|h\)   `--rollback-delay`| | API 1.28+ Delay between task rollbacks \(ns|us|ms|s|m|h\) \(default 0s\)   `--rollback-failure-action`| | API 1.28+ Action on rollback failure \(`pause`, `continue`\) \(default `pause`\)   `--rollback-max-failure-ratio`| | API 1.28+ Failure rate to tolerate during a rollback \(default 0\)   `--rollback-monitor`| | API 1.28+ Duration after each task rollback to monitor for failure \(ns|us|ms|s|m|h\) \(default 5s\)      `--rollback-order`| | API 1.29+ Rollback order \(`start-first`, `stop-first`\) \(default `stop-first`\)      `--rollback-parallelism`| `1`| API 1.28+ Maximum number of tasks rolled back simultaneously \(0 to roll back all at once\)      `--secret`| | API 1.25+ Specify secrets to expose to the service   `--stop-grace-period`| | Time to wait before force killing a container \(ns|us|ms|s|m|h\) \(default 10s\)      `--stop-signal`| | API 1.28+ Signal to stop the container   `--sysctl`| | API 1.40+ Sysctl options   `-t, --tty`| | API 1.25+ Allocate a pseudo-TTY   `--ulimit`| | API 1.41+ Ulimit options   `--update-delay`| | Delay between updates \(ns|us|ms|s|m|h\) \(default 0s\)   `--update-failure-action`| | Action on update failure \(`pause`, `continue`, `rollback`\) \(default `pause`\)      `--update-max-failure-ratio`| | API 1.25+ Failure rate to tolerate during an update \(default 0\)   `--update-monitor`| | API 1.25+ Duration after each task update to monitor for failure \(ns|us|ms|s|m|h\) \(default 5s\)      `--update-order`| | API 1.29+ Update order \(`start-first`, `stop-first`\) \(default `stop-first`\)   `--update-parallelism`| `1`| Maximum number of tasks updated simultaneously \(0 to update all at once\)      `-u, --user`| | Username or UID \(format: <name|uid>\[:<group|gid>\]\)   `--with-registry-auth`| | Send registry authentication details to swarm agents   `-w, --workdir`| | Working directory inside the container      ## Examples

### Create a service               $ docker service create --name redis redis:7.4.1          dmu1ept4cxcfe8k8lhtux3ro3          $ docker service create --mode global --name redis2 redis:7.4.1          a8q9dasaafudfs8q8w32udass          $ docker service ls          ID            NAME    MODE        REPLICAS  IMAGE     dmu1ept4cxcf  redis   replicated  1/1       redis:7.4.1     a8q9dasaafud  redis2  global      1/1       redis:7.4.1     

#### Create a service using an image on a private registry \(--with-registry-auth\)

If your image is available on a private registry which requires login, use the `--with-registry-auth` flag with `docker service create`, after logging in. If your image is stored on `registry.example.com`, which is a private registry, use a command like the following:               $ docker login registry.example.com          $ docker service  create \       --with-registry-auth \       --name my_service \       registry.example.com/acme/my_image:latest     

This passes the login token from your local client to the swarm nodes where the service is deployed, using the encrypted WAL logs. With this information, the nodes are able to log in to the registry and pull the image.

### Create a service with 5 replica tasks \(--replicas\)

Use the `--replicas` flag to set the number of replica tasks for a replicated service. The following command creates a `redis` service with `5` replica tasks:               $ docker service create --name redis --replicas=5 redis:7.4.1          4cdgfyky7ozwh3htjfw0d12qv     

The above command sets the _desired_ number of tasks for the service. Even though the command returns immediately, actual scaling of the service may take some time. The `REPLICAS` column shows both the actual and desired number of replica tasks for the service.

In the following example the desired state is `5` replicas, but the current number of `RUNNING` tasks is `3`:               $ docker service ls          ID            NAME   MODE        REPLICAS  IMAGE     4cdgfyky7ozw  redis  replicated  3/5       redis:7.4.1     

Once all the tasks are created and `RUNNING`, the actual number of tasks is equal to the desired number:               $ docker service ls          ID            NAME   MODE        REPLICAS  IMAGE     4cdgfyky7ozw  redis  replicated  5/5       redis:7.4.1     

### Create a service with secrets \(--secret\)

Use the `--secret` flag to give a container access to a [secret](https://docs.docker.com/reference/cli/docker/secret/create/).

Create a service specifying a secret:               $ docker service create --name redis --secret secret.json redis:7.4.1          4cdgfyky7ozwh3htjfw0d12qv     

Create a service specifying the secret, target, user/group ID, and mode:               $ docker service create --name redis \         --secret source=ssh-key,target=ssh \         --secret source=app-key,target=app,uid=1000,gid=1001,mode=0400 \         redis:7.4.1          4cdgfyky7ozwh3htjfw0d12qv     

To grant a service access to multiple secrets, use multiple `--secret` flags.

Secrets are located in `/run/secrets` in the container if no target is specified. If no target is specified, the name of the secret is used as the in memory file in the container. If a target is specified, that is used as the filename. In the example above, two files are created: `/run/secrets/ssh` and `/run/secrets/app` for each of the secret targets specified.

### Create a service with configs \(--config\)

Use the `--config` flag to give a container access to a [config](https://docs.docker.com/reference/cli/docker/config/create/).

Create a service with a config. The config will be mounted into `redis-config`, be owned by the user who runs the command inside the container \(often `root`\), and have file mode `0444` or world-readable. You can specify the `uid` and `gid` as numerical IDs or names. When using names, the provided group/user names must pre-exist in the container. The `mode` is specified as a 4-number sequence such as `0755`.               $ docker service create --name=redis --config redis-conf redis:7.4.1     

Create a service with a config and specify the target location and file mode:               $ docker service create --name redis \       --config source=redis-conf,target=/etc/redis/redis.conf,mode=0400 redis:7.4.1     

To grant a service access to multiple configs, use multiple `--config` flags.

Configs are located in `/` in the container if no target is specified. If no target is specified, the name of the config is used as the name of the file in the container. If a target is specified, that is used as the filename.

### Create a service with a rolling update policy               $ docker service create \       --replicas 10 \       --name redis \       --update-delay 10s \       --update-parallelism 2 \       redis:7.4.1     

When you run a [service update](https://docs.docker.com/reference/cli/docker/service/update/), the scheduler updates a maximum of 2 tasks at a time, with `10s` between updates. For more information, refer to the [rolling updates tutorial](https://docs.docker.com/engine/swarm/swarm-tutorial/rolling-update/).

### Set environment variables \(-e, --env\)

This sets an environment variable for all tasks in a service. For example:               $ docker service create \       --name redis_2 \       --replicas 5 \       --env MYVAR=foo \       redis:7.4.1     

To specify multiple environment variables, specify multiple `--env` flags, each with a separate key-value pair.               $ docker service create \       --name redis_2 \       --replicas 5 \       --env MYVAR=foo \       --env MYVAR2=bar \       redis:7.4.1     

### Create a service with specific hostname \(--hostname\)

This option sets the docker service containers hostname to a specific string. For example:               $ docker service create --name redis --hostname myredis redis:7.4.1     

### Set metadata on a service \(-l, --label\)

A label is a `key=value` pair that applies metadata to a service. To label a service with two labels:               $ docker service create \       --name redis_2 \       --label com.example.foo="bar" \       --label bar=baz \       redis:7.4.1     

For more information about labels, refer to [apply custom metadata](https://docs.docker.com/config/labels-custom-metadata/).

### Add bind mounts, volumes or memory filesystems \(--mount\)

Docker supports three different kinds of mounts, which allow containers to read from or write to files or directories, either on the host operating system, or on memory filesystems. These types are data volumes \(often referred to simply as volumes\), bind mounts, tmpfs, and named pipes.

A **bind mount** makes a file or directory on the host available to the container it is mounted within. A bind mount may be either read-only or read-write. For example, a container might share its host's DNS information by means of a bind mount of the host's `/etc/resolv.conf` or a container might write logs to its host's `/var/log/myContainerLogs` directory. If you use bind mounts and your host and containers have different notions of permissions, access controls, or other such details, you will run into portability issues.

A **named volume** is a mechanism for decoupling persistent data needed by your container from the image used to create the container and from the host machine. Named volumes are created and managed by Docker, and a named volume persists even when no container is currently using it. Data in named volumes can be shared between a container and the host machine, as well as between multiple containers. Docker uses a _volume driver_ to create, manage, and mount volumes. You can back up or restore volumes using Docker commands.

A **tmpfs** mounts a tmpfs inside a container for volatile data.

A **npipe** mounts a named pipe from the host into the container.

Consider a situation where your image starts a lightweight web server. You could use that image as a base image, copy in your website's HTML files, and package that into another image. Each time your website changed, you'd need to update the new image and redeploy all of the containers serving your website. A better solution is to store the website in a named volume which is attached to each of your web server containers when they start. To update the website, you just update the named volume.

For more information about named volumes, see [Data Volumes](https://docs.docker.com/storage/volumes/).

The following table describes options which apply to both bind mounts and named volumes in a service:

Option| Required| Description   ---|---|---   **type**| |  The type of mount, can be either `volume`, `bind`, `tmpfs`, or `npipe`. Defaults to `volume` if no type is specified.

  * `volume`: mounts a [managed volume](https://docs.docker.com/reference/cli/docker/volume/create/) into the container.   * `bind`: bind-mounts a directory or file from the host into the container.   * `tmpfs`: mount a tmpfs in the container   * `npipe`: mounts named pipe from the host into the container \(Windows containers only\).

   **src** or **source**|  for `type=bind` and `type=npipe`| 

  * `type=volume`: `src` is an optional way to specify the name of the volume \(for example, `src=my-volume`\). If the named volume does not exist, it is automatically created. If no `src` is specified, the volume is assigned a random name which is guaranteed to be unique on the host, but may not be unique cluster-wide. A randomly-named volume has the same lifecycle as its container and is destroyed when the _container_ is destroyed \(which is upon `service update`, or when scaling or re-balancing the service\)   * `type=bind`: `src` is required, and specifies an absolute path to the file or directory to bind-mount \(for example, `src=/path/on/host/`\). An error is produced if the file or directory does not exist.   * `type=tmpfs`: `src` is not supported.

   **dst** or **destination** or **target**|  yes| Mount path inside the container, for example `/some/path/in/container/`. If the path does not exist in the container's filesystem, the Engine creates a directory at the specified location before mounting the volume or bind mount.   **readonly** or **ro**| |  The Engine mounts binds and volumes `read-write` unless `readonly` option is given when mounting the bind or volume. Note that setting `readonly` for a bind-mount may not make its submounts `readonly` depending on the kernel version. See also `bind-recursive`.

  * `true` or `1` or no value: Mounts the bind or volume read-only.   * `false` or `0`: Mounts the bind or volume read-write.

      #### Options for bind mounts

The following options can only be used for bind mounts \(`type=bind`\):

Option| Description   ---|---   **bind-propagation**|  See the bind propagation section.   **consistency**|  The consistency requirements for the mount; one of

  * `default`: Equivalent to `consistent`.   * `consistent`: Full consistency. The container runtime and the host maintain an identical view of the mount at all times.   * `cached`: The host's view of the mount is authoritative. There may be delays before updates made on the host are visible within a container.   * `delegated`: The container runtime's view of the mount is authoritative. There may be delays before updates made in a container are visible on the host.

   **bind-recursive**|  By default, submounts are recursively bind-mounted as well. However, this behavior can be confusing when a bind mount is configured with `readonly` option, because submounts may not be mounted as read-only, depending on the kernel version. Set `bind-recursive` to control the behavior of the recursive bind-mount.      A value is one of:     

  * <`enabled`: Enables recursive bind-mount. Read-only mounts are made recursively read-only if kernel is v5.12 or later. Otherwise they are not made recursively read-only.   * <`disabled`: Disables recursive bind-mount.   * <`writable`: Enables recursive bind-mount. Read-only mounts are not made recursively read-only.   * <`readonly`: Enables recursive bind-mount. Read-only mounts are made recursively read-only if kernel is v5.12 or later. Otherwise the Engine raises an error.

When the option is not specified, the default behavior correponds to setting `enabled`.   **bind-nonrecursive**| ` bind-nonrecursive` is deprecated since Docker Engine v25.0. Use `bind-recursive`instead.      A value is optional:     

  * `true` or `1`: Equivalent to `bind-recursive=disabled`.   * `false` or `0`: Equivalent to `bind-recursive=enabled`.

      ##### Bind propagation

Bind propagation refers to whether or not mounts created within a given bind mount or named volume can be propagated to replicas of that mount. Consider a mount point `/mnt`, which is also mounted on `/tmp`. The propagation settings control whether a mount on `/tmp/a` would also be available on `/mnt/a`. Each propagation setting has a recursive counterpoint. In the case of recursion, consider that `/tmp/a` is also mounted as `/foo`. The propagation settings control whether `/mnt/a` and/or `/tmp/a` would exist.

The `bind-propagation` option defaults to `rprivate` for both bind mounts and volume mounts, and is only configurable for bind mounts. In other words, named volumes do not support bind propagation.

  * **`shared`** : Sub-mounts of the original mount are exposed to replica mounts, and sub-mounts of replica mounts are also propagated to the original mount.   * **`slave`** : similar to a shared mount, but only in one direction. If the original mount exposes a sub-mount, the replica mount can see it. However, if the replica mount exposes a sub-mount, the original mount cannot see it.   * **`private`** : The mount is private. Sub-mounts within it are not exposed to replica mounts, and sub-mounts of replica mounts are not exposed to the original mount.   * **`rshared`** : The same as shared, but the propagation also extends to and from mount points nested within any of the original or replica mount points.   * **`rslave`** : The same as `slave`, but the propagation also extends to and from mount points nested within any of the original or replica mount points.   * **`rprivate`** : The default. The same as `private`, meaning that no mount points anywhere within the original or replica mount points propagate in either direction.

For more information about bind propagation, see the [Linux kernel documentation for shared subtree](https://www.kernel.org/doc/Documentation/filesystems/sharedsubtree.txt).

#### Options for named volumes

The following options can only be used for named volumes \(`type=volume`\):

Option| Description   ---|---   **volume-driver**|  Name of the volume-driver plugin to use for the volume. Defaults to `"local"`, to use the local volume driver to create the volume if the volume does not exist.   **volume-label**|  One or more custom metadata \("labels"\) to apply to the volume upon creation. For example, `volume-label=mylabel=hello-world,my-other-label=hello-mars`. For more information about labels, refer to [apply custom metadata](https://docs.docker.com/config/labels-custom-metadata/).   **volume-nocopy**|  By default, if you attach an empty volume to a container, and files or directories already existed at the mount-path in the container \(`dst`\), the Engine copies those files and directories into the volume, allowing the host to access them. Set `volume-nocopy` to disable copying files from the container's filesystem to the volume and mount the empty volume.      A value is optional:     

  * `true` or `1`: Default if you do not provide a value. Disables copying.   * `false` or `0`: Enables copying.

   **volume-opt**|  Options specific to a given volume driver, which will be passed to the driver when creating the volume. Options are provided as a comma-separated list of key/value pairs, for example, `volume-opt=some-option=some-value,volume-opt=some-other-option=some-other-value`. For available options for a given driver, refer to that driver's documentation.      #### Options for tmpfs

The following options can only be used for tmpfs mounts \(`type=tmpfs`\);

Option| Description   ---|---   **tmpfs-size**|  Size of the tmpfs mount in bytes. Unlimited by default in Linux.   **tmpfs-mode**|  File mode of the tmpfs in octal. \(e.g. `"700"` or `"0700"`.\) Defaults to `"1777"` in Linux.      #### Differences between "--mount" and "--volume"

The `--mount` flag supports most options that are supported by the `-v` or `--volume` flag for `docker run`, with some important exceptions:

  * The `--mount` flag allows you to specify a volume driver and volume driver options _per volume_ , without creating the volumes in advance. In contrast, `docker run` allows you to specify a single volume driver which is shared by all volumes, using the `--volume-driver` flag.

  * The `--mount` flag allows you to specify custom metadata \("labels"\) for a volume, before the volume is created.

  * When you use `--mount` with `type=bind`, the host-path must refer to an _existing_ path on the host. The path will not be created for you and the service will fail with an error if the path does not exist.

  * The `--mount` flag does not allow you to relabel a volume with `Z` or `z` flags, which are used for `selinux` labeling.

#### Create a service using a named volume

The following example creates a service that uses a named volume:               $ docker service create \       --name my-service \       --replicas 3 \       --mount type=volume,source=my-volume,destination=/path/in/container,volume-label="color=red",volume-label="shape=round" \       nginx:alpine     

For each replica of the service, the engine requests a volume named "my-volume" from the default \("local"\) volume driver where the task is deployed. If the volume does not exist, the engine creates a new volume and applies the "color" and "shape" labels.

When the task is started, the volume is mounted on `/path/in/container/` inside the container.

Be aware that the default \("local"\) volume is a locally scoped volume driver. This means that depending on where a task is deployed, either that task gets a _new_ volume named "my-volume", or shares the same "my-volume" with other tasks of the same service. Multiple containers writing to a single shared volume can cause data corruption if the software running inside the container is not designed to handle concurrent processes writing to the same location. Also take into account that containers can be re-scheduled by the Swarm orchestrator and be deployed on a different node.

#### Create a service that uses an anonymous volume

The following command creates a service with three replicas with an anonymous volume on `/path/in/container`:               $ docker service create \       --name my-service \       --replicas 3 \       --mount type=volume,destination=/path/in/container \       nginx:alpine     

In this example, no name \(`source`\) is specified for the volume, so a new volume is created for each task. This guarantees that each task gets its own volume, and volumes are not shared between tasks. Anonymous volumes are removed after the task using them is complete.

#### Create a service that uses a bind-mounted host directory

The following example bind-mounts a host directory at `/path/in/container` in the containers backing the service:               $ docker service create \       --name my-service \       --mount type=bind,source=/path/on/host,destination=/path/in/container \       nginx:alpine     

### Set service mode \(--mode\)

The service mode determines whether this is a _replicated_ service or a _global_ service. A replicated service runs as many tasks as specified, while a global service runs on each active node in the swarm.

The following command creates a global service:               $ docker service create \      --name redis_2 \      --mode global \      redis:7.4.1     

### Specify service constraints \(--constraint\)

You can limit the set of nodes where a task can be scheduled by defining constraint expressions. Constraint expressions can either use a _match_ \(`==`\) or _exclude_ \(`!=`\) rule. Multiple constraints find nodes that satisfy every expression \(AND match\). Constraints can match node or Docker Engine labels as follows:

node attribute| matches| example   ---|---|---   `node.id`| Node ID| `node.id==2ivku8v2gvtg4`   `node.hostname`| Node hostname| `node.hostname!=node-2`   `node.role`| Node role \(`manager`/`worker`\)| `node.role==manager`   `node.platform.os`| Node operating system| `node.platform.os==windows`   `node.platform.arch`| Node architecture| `node.platform.arch==x86_64`   `node.labels`| User-defined node labels| `node.labels.security==high`   `engine.labels`| Docker Engine's labels| `engine.labels.operatingsystem==ubuntu-24.04`      `engine.labels` apply to Docker Engine labels like operating system, drivers, etc. Swarm administrators add `node.labels` for operational purposes by using the [`docker node update`](https://docs.docker.com/reference/cli/docker/node/update/) command.

For example, the following limits tasks for the redis service to nodes where the node type label equals queue:               $ docker service create \       --name redis_2 \       --constraint node.platform.os==linux \       --constraint node.labels.type==queue \       redis:7.4.1     

If the service constraints exclude all nodes in the cluster, a message is printed that no suitable node is found, but the scheduler will start a reconciliation loop and deploy the service once a suitable node becomes available.

In the example below, no node satisfying the constraint was found, causing the service to not reconcile with the desired state:               $ docker service create \       --name web \       --constraint node.labels.region==east \       nginx:alpine          lx1wrhhpmbbu0wuk0ybws30bc     overall progress: 0 out of 1 tasks     1/1: no suitable node (scheduling constraints not satisfied on 5 nodes)          $ docker service ls     ID                  NAME     MODE         REPLICAS   IMAGE               PORTS     b6lww17hrr4e        web      replicated   0/1        nginx:alpine     

After adding the `region=east` label to a node in the cluster, the service reconciles, and the desired number of replicas are deployed:               $ docker node update --label-add region=east yswe2dm4c5fdgtsrli1e8ya5l     yswe2dm4c5fdgtsrli1e8ya5l          $ docker service ls     ID                  NAME     MODE         REPLICAS   IMAGE               PORTS     b6lww17hrr4e        web      replicated   1/1        nginx:alpine     

### Specify service placement preferences \(--placement-pref\)

You can set up the service to divide tasks evenly over different categories of nodes. One example of where this can be useful is to balance tasks over a set of datacenters or availability zones. The example below illustrates this:               $ docker service create \       --replicas 9 \       --name redis_2 \       --placement-pref spread=node.labels.datacenter \       redis:7.4.1     

This uses `--placement-pref` with a `spread` strategy \(currently the only supported strategy\) to spread tasks evenly over the values of the `datacenter` node label. In this example, we assume that every node has a `datacenter` node label attached to it. If there are three different values of this label among nodes in the swarm, one third of the tasks will be placed on the nodes associated with each value. This is true even if there are more nodes with one value than another. For example, consider the following set of nodes:

  * Three nodes with `node.labels.datacenter=east`   * Two nodes with `node.labels.datacenter=south`   * One node with `node.labels.datacenter=west`

Since we are spreading over the values of the `datacenter` label and the service has 9 replicas, 3 replicas will end up in each datacenter. There are three nodes associated with the value `east`, so each one will get one of the three replicas reserved for this value. There are two nodes with the value `south`, and the three replicas for this value will be divided between them, with one receiving two replicas and another receiving just one. Finally, `west` has a single node that will get all three replicas reserved for `west`.

If the nodes in one category \(for example, those with `node.labels.datacenter=south`\) can't handle their fair share of tasks due to constraints or resource limitations, the extra tasks will be assigned to other nodes instead, if possible.

Both engine labels and node labels are supported by placement preferences. The example above uses a node label, because the label is referenced with `node.labels.datacenter`. To spread over the values of an engine label, use `--placement-pref spread=engine.labels.<labelname>`.

It is possible to add multiple placement preferences to a service. This establishes a hierarchy of preferences, so that tasks are first divided over one category, and then further divided over additional categories. One example of where this may be useful is dividing tasks fairly between datacenters, and then splitting the tasks within each datacenter over a choice of racks. To add multiple placement preferences, specify the `--placement-pref` flag multiple times. The order is significant, and the placement preferences will be applied in the order given when making scheduling decisions.

The following example sets up a service with multiple placement preferences. Tasks are spread first over the various datacenters, and then over racks \(as indicated by the respective labels\):               $ docker service create \       --replicas 9 \       --name redis_2 \       --placement-pref 'spread=node.labels.datacenter' \       --placement-pref 'spread=node.labels.rack' \       redis:7.4.1     

When updating a service with `docker service update`, `--placement-pref-add` appends a new placement preference after all existing placement preferences. `--placement-pref-rm` removes an existing placement preference that matches the argument.

### Specify memory requirements and constraints for a service \(--reserve-memory and --limit-memory\)

If your service needs a minimum amount of memory in order to run correctly, you can use `--reserve-memory` to specify that the service should only be scheduled on a node with this much memory available to reserve. If no node is available that meets the criteria, the task is not scheduled, but remains in a pending state.

The following example requires that 4GB of memory be available and reservable on a given node before scheduling the service to run on that node.               $ docker service create --reserve-memory=4GB --name=too-big nginx:alpine     

The managers won't schedule a set of containers on a single node whose combined reservations exceed the memory available on that node.

After a task is scheduled and running, `--reserve-memory` does not enforce a memory limit. Use `--limit-memory` to ensure that a task uses no more than a given amount of memory on a node. This example limits the amount of memory used by the task to 4GB. The task will be scheduled even if each of your nodes has only 2GB of memory, because `--limit-memory` is an upper limit.               $ docker service create --limit-memory=4GB --name=too-big nginx:alpine     

Using `--reserve-memory` and `--limit-memory` does not guarantee that Docker will not use more memory on your host than you want. For instance, you could create many services, the sum of whose memory usage could exhaust the available memory.

You can prevent this scenario from exhausting the available memory by taking into account other \(non-containerized\) software running on the host as well. If `--reserve-memory` is greater than or equal to `--limit-memory`, Docker won't schedule a service on a host that doesn't have enough memory. `--limit-memory` will limit the service's memory to stay within that limit, so if every service has a memory-reservation and limit set, Docker services will be less likely to saturate the host. Other non-service containers or applications running directly on the Docker host could still exhaust memory.

There is a downside to this approach. Reserving memory also means that you may not make optimum use of the memory available on the node. Consider a service that under normal circumstances uses 100MB of memory, but depending on load can "peak" at 500MB. Reserving 500MB for that service \(to guarantee can have 500MB for those "peaks"\) results in 400MB of memory being wasted most of the time.

In short, you can take a more conservative or more flexible approach:

  * **Conservative** : reserve 500MB, and limit to 500MB. Basically you're now treating the service containers as VMs, and you may be losing a big advantage containers, which is greater density of services per host.

  * **Flexible** : limit to 500MB in the assumption that if the service requires more than 500MB, it is malfunctioning. Reserve something between the 100MB "normal" requirement and the 500MB "peak" requirement". This assumes that when this service is at "peak", other services or non-container workloads probably won't be.

The approach you take depends heavily on the memory-usage patterns of your workloads. You should test under normal and peak conditions before settling on an approach.

On Linux, you can also limit a service's overall memory footprint on a given host at the level of the host operating system, using `cgroups` or other relevant operating system tools.

### Specify maximum replicas per node \(--replicas-max-per-node\)

Use the `--replicas-max-per-node` flag to set the maximum number of replica tasks that can run on a node. The following command creates a nginx service with 2 replica tasks but only one replica task per node.

One example where this can be useful is to balance tasks over a set of data centers together with `--placement-pref` and let `--replicas-max-per-node` setting make sure that replicas are not migrated to another datacenter during maintenance or datacenter failure.

The example below illustrates this:               $ docker service create \       --name nginx \       --replicas 2 \       --replicas-max-per-node 1 \       --placement-pref 'spread=node.labels.datacenter' \       nginx     

### Attach a service to an existing network \(--network\)

You can use overlay networks to connect one or more services within the swarm.

First, create an overlay network on a manager node the docker network create command:               $ docker network create --driver overlay my-network          etjpu59cykrptrgw0z0hk5snf     

After you create an overlay network in swarm mode, all manager nodes have access to the network.

When you create a service and pass the `--network` flag to attach the service to the overlay network:               $ docker service create \       --replicas 3 \       --network my-network \       --name my-web \       nginx          716thylsndqma81j6kkkb5aus     

The swarm extends my-network to each node running the service.

Containers on the same network can access each other using [service discovery](https://docs.docker.com/engine/network/drivers/overlay/#container-discovery).

Long form syntax of `--network` allows to specify list of aliases and driver options: `--network name=my-network,alias=web1,driver-opt=field1=value1`

### Publish service ports externally to the swarm \(-p, --publish\)

You can publish service ports to make them available externally to the swarm using the `--publish` flag. The `--publish` flag can take two different styles of arguments. The short version is positional, and allows you to specify the published port and target port separated by a colon \(`:`\).               $ docker service create --name my_web --replicas 3 --publish 8080:80 nginx     

There is also a long format, which is easier to read and allows you to specify more options. The long format is preferred. You cannot specify the service's mode when using the short format. Here is an example of using the long format for the same service as above:               $ docker service create --name my_web --replicas 3 --publish published=8080,target=80 nginx     

The options you can specify are:

Option| Short syntax| Long syntax| Description   ---|---|---|---   published and target port| `--publish 8080:80`| `--publish published=8080,target=80`| The target port within the container and the port to map it to on the nodes, using the routing mesh \(`ingress`\) or host-level networking. More options are available, later in this table. The key-value syntax is preferred, because it is somewhat self-documenting.   mode| Not possible to set using short syntax.| `--publish published=8080,target=80,mode=host`| The mode to use for binding the port, either `ingress` or `host`. Defaults to `ingress` to use the routing mesh.   protocol| `--publish 8080:80/tcp`| `--publish published=8080,target=80,protocol=tcp`| The protocol to use, `tcp` , `udp`, or `sctp`. Defaults to `tcp`. To bind a port for both protocols, specify the `-p` or `--publish` flag twice.      When you publish a service port using `ingress` mode, the swarm routing mesh makes the service accessible at the published port on every node regardless if there is a task for the service running on the node. If you use `host` mode, the port is only bound on nodes where the service is running, and a given port on a node can only be bound once. You can only set the publication mode using the long syntax. For more information refer to [Use swarm mode routing mesh](https://docs.docker.com/engine/swarm/ingress/).

### Provide credential specs for managed service accounts \(--credentials-spec\)

This option is only used for services using Windows containers. The `--credential-spec` must be in the format `file://<filename>` or `registry://<value-name>`.

When using the `file://<filename>` format, the referenced file must be present in the `CredentialSpecs` subdirectory in the docker data directory, which defaults to `C:\ProgramData\Docker\` on Windows. For example, specifying `file://spec.json` loads `C:\ProgramData\Docker\CredentialSpecs\spec.json`.

When using the `registry://<value-name>` format, the credential spec is read from the Windows registry on the daemon's host. The specified registry value must be located in:               HKLM\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Virtualization\Containers\CredentialSpecs     

### Create services using templates

You can use templates for some flags of `service create`, using the syntax provided by the Go's [text/template](https://pkg.go.dev/text/template) package.

The supported flags are the following :

  * `--hostname`   * `--mount`   * `--env`

Valid placeholders for the Go template are listed below:

Placeholder| Description   ---|---   `.Service.ID`| Service ID   `.Service.Name`| Service name   `.Service.Labels`| Service labels   `.Node.ID`| Node ID   `.Node.Hostname`| Node Hostname   `.Task.ID`| Task ID   `.Task.Name`| Task name   `.Task.Slot`| Task slot      #### Template example

In this example, we are going to set the template of the created containers based on the service's name, the node's ID and hostname where it sits.               $ docker service create \         --name hosttempl \         --hostname="{{.Node.Hostname}}-{{.Node.ID}}-{{.Service.Name}}"\         busybox top          va8ew30grofhjoychbr6iot8c          $ docker service ps va8ew30grofhjoychbr6iot8c          ID            NAME         IMAGE                                                                                   NODE          DESIRED STATE  CURRENT STATE               ERROR  PORTS     wo41w8hg8qan  hosttempl.1  busybox:latest@sha256:29f5d56d12684887bdfa50dcd29fc31eea4aaf4ad3bec43daf19026a7ce69912  2e7a8a9c4da2  Running        Running about a minute ago          $ docker inspect --format="{{.Config.Hostname}}" 2e7a8a9c4da2-wo41w8hg8qanxwjwsg4kxpprj-hosttempl          x3ti0erg11rjpg64m75kej2mz-hosttempl     

### Specify isolation mode on Windows \(--isolation\)

By default, tasks scheduled on Windows nodes are run using the default isolation mode configured for this particular node. To force a specific isolation mode, you can use the `--isolation` flag:               $ docker service create --name myservice --isolation=process microsoft/nanoserver     

Supported isolation modes on Windows are:

  * `default`: use default settings specified on the node running the task   * `process`: use process isolation \(Windows server only\)   * `hyperv`: use Hyper-V isolation

### Create services requesting Generic Resources \(--generic-resources\)

You can narrow the kind of nodes your task can land on through the using the `--generic-resource` flag \(if the nodes advertise these resources\):               $ docker service create \         --name cuda \         --generic-resource "NVIDIA-GPU=2" \         --generic-resource "SSD=1" \         nvidia/cuda     

### Running as a job

Jobs are a special kind of service designed to run an operation to completion and then stop, as opposed to running long-running daemons. When a Task belonging to a job exits successfully \(return value 0\), the Task is marked as "Completed", and is not run again.

Jobs are started by using one of two modes, `replicated-job` or `global-job`               $ docker service create --name myjob \                             --mode replicated-job \                             bash "true"     

This command will run one Task, which will, using the `bash` image, execute the command `true`, which will return 0 and then exit.

Though Jobs are ultimately a different kind of service, they a couple of caveats compared to other services:

  * None of the update or rollback configuration options are valid. Jobs can be updated, but cannot be rolled out or rolled back, making these configuration options moot.   * Jobs are never restarted on reaching the `Complete` state. This means that for jobs, setting `--restart-condition` to `any` is the same as setting it to `on-failure`.

Jobs are available in both replicated and global modes.

#### Replicated Jobs

A replicated job is like a replicated service. Setting the `--replicas` flag will specify total number of iterations of a job to execute.

By default, all replicas of a replicated job will launch at once. To control the total number of replicas that are executing simultaneously at any one time, the `--max-concurrent` flag can be used:               $ docker service create \         --name mythrottledjob \         --mode replicated-job \         --replicas 10 \         --max-concurrent 2 \         bash "true"     

The above command will execute 10 Tasks in total, but only 2 of them will be run at any given time.

#### Global Jobs

Global jobs are like global services, in that a Task is executed once on each node matching placement constraints. Global jobs are represented by the mode `global-job`.

Note that after a Global job is created, any new Nodes added to the cluster will have a Task from that job started on them. The Global Job does not as a whole have a "done" state, except insofar as every Node meeting the job's constraints has a Completed task.