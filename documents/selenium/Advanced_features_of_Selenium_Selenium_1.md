# Advanced features of Selenium | Selenium

**URL:** https://www.selenium.dev/documentation/grid/advanced_features/_print
**Word Count:** 3251
**Links Count:** 89
**Scraped:** 2025-07-17 06:17:48
**Status:** completed

---

This is the multi-page printable view of this section. Click here to print.

[Return to the regular view of this page](https://www.selenium.dev/documentation/grid/advanced_features/).

# Advanced features of Selenium

To get all the details of the advanced features, understand how it works, and how to set up your own, please browse thorough the following sections.

  * 1: Observability in Selenium Grid   * 2: GraphQL query support   * 3: Grid endpoints   * 4: Customizing a Node   * 5: External datastore

# 1 - Observability in Selenium Grid

## Table of Contents

  * [Selenium Grid](https://www.selenium.dev/documentation/grid/advanced_features/observability/#selenium-grid)   * [Observability](https://www.selenium.dev/documentation/grid/advanced_features/observability/#observability)     * [Distributed tracing](https://www.selenium.dev/documentation/grid/advanced_features/observability/#distributed-tracing)     * [Event logging](https://www.selenium.dev/documentation/grid/advanced_features/observability/#event-logging)   * [Grid Observability](https://www.selenium.dev/documentation/grid/advanced_features/observability/#grid-observability)     * [Visualizing Traces](https://www.selenium.dev/documentation/grid/advanced_features/observability/#visualizing-traces)     * [Leveraging event logs](https://www.selenium.dev/documentation/grid/advanced_features/observability/#leveraging-event-logs)   * [References](https://www.selenium.dev/documentation/grid/advanced_features/observability/#references)

## Selenium Grid

Grid aids in scaling and distributing tests by executing tests on various browser and operating system combinations.

## Observability

Observability has three pillars: traces, metrics and logs. Since Selenium Grid 4 is designed to be fully distributed, observability will make it easier to understand and debug the internals.

## Distributed tracing

A single request or transaction spans multiple services and components. Tracing tracks the request lifecycle as each service executes the request. It is useful in debugging in an error scenario. Some key terms used in tracing context are:

**Trace** Tracing allows one to trace a request through multiple services, starting from its origin to its final destination. This request’s journey helps in debugging, monitoring the end-to-end flow, and identifying failures. A trace depicts the end-to-end request flow. Each trace has a unique id as its identifier.

**Span** Each trace is made up of timed operations called spans. A span has a start and end time and it represents operations done by a service. The granularity of span depends on how it is instrumented. Each span has a unique identifier. All spans within a trace have the same trace id.

**Span Attributes** Span attributes are key-value pairs which provide additional information about each span.

**Events** Events are timed-stamped logs within a span. They provide additional context to the existing spans. Events also contain key-value pairs as event attributes.

## Event logging

Logging is essential to debug an application. Logging is often done in a human-readable format. But for machines to search and analyze the logs, it has to have a well-defined format. Structured logging is a common practice of recording logs consistently in a fixed format. It commonly contains fields like:

  * Timestamp   * Logging level   * Logger class   * Log message \(This is further broken down into fields relevant to the operation where the log was recorded\)

Logs and events are closely related. Events encapsulate all the possible information available to do a single unit of work. Logs are essentially subsets of an event. At the crux, both aid in debugging. Refer following resources for detailed understanding:

  1. <https://www.honeycomb.io/blog/how-are-structured-logs-different-from-events/>   2. <https://charity.wtf/2019/02/05/logs-vs-structured-events/>

## Grid Observability

Selenium server is instrumented with tracing using OpenTelemetry. Every request to the server is traced from start to end. Each trace consists of a series of spans as a request is executed within the server. Most spans in the Selenium server consist of two events:

  1. Normal event - records all information about a unit of work and marks successful completion of the work.   2. Error event - records all information till the error occurs and then records the error information. Marks an exception event.

Running Selenium server

  1. [Standalone](https://github.com/SeleniumHQ/selenium/wiki/Selenium-Grid-4#standalone-mode)   2. [Hub and Node](https://github.com/SeleniumHQ/selenium/wiki/Selenium-Grid-4#hub-and-node)   3. [Fully Distributed](https://github.com/SeleniumHQ/selenium/wiki/Selenium-Grid-4#fully-distributed)   4. [Docker](https://github.com/SeleniumHQ/selenium/wiki/Selenium-Grid-4#using-docker)

## Visualizing Traces

All spans, events and their respective attributes are part of a trace. Tracing works while running the server in all of the above-mentioned modes.

By default, tracing is enabled in the Selenium server. Selenium server exports the traces via two exporters:

  1. Console - Logs all traces and their included spans at FINE level. By default, Selenium server prints logs at INFO level and above. The **log-level** flag can be used to pass a logging level of choice while running the Selenium Grid jar/s.

              java -jar selenium-server-4.0.0-<selenium-version>.jar standalone --log-level FINE     

  2. Jaeger UI - OpenTelemetry provides the APIs and SDKs to instrument traces in the code. Whereas Jaeger is a tracing backend, that aids in collecting the tracing telemetry data and providing querying, filtering and visualizing features for the data.

Detailed instructions of visualizing traces using Jaeger UI can be obtained by running the command :               java -jar selenium-server-4.0.0-<selenium-version>.jar info tracing     

[A very good example and scripts to run the server and send traces to Jaeger](https://github.com/manoj9788/tracing-selenium-grid)

## Leveraging event logs

Tracing has to be enabled for event logging as well, even if one does not wish to export traces to visualize them.   **By default, tracing is enabled. No additional parameters need to be passed to see logs on the console.** All events within a span are logged at FINE level. Error events are logged at WARN level.

All event logs have the following fields :

Field| Field value| Description   ---|---|---   Event time| eventId| Timestamp of the event record in epoch nanoseconds.   Trace Id| tracedId| Each trace is uniquely identified by a trace id.   Span Id| spanId| Each span within a trace is uniquely identified by a span id.   Span Kind| spanKind| Span kind is a property of span indicating the type of span. It helps in understanding the nature of the unit of work done by the Span.   Event name| eventName| This maps to the log message.   Event attributes| eventAttributes| This forms the crux of the event logs, based on the operation executed, it has JSON formatted key-value pairs. This also includes a handler class attribute, to show the logger class.      Sample log               FINE [LoggingOptions$1.lambda$export$1] - {       "traceId": "fc8aef1d44b3cc8bc09eb8e581c4a8eb",       "spanId": "b7d3b9865d3ddd45",       "spanKind": "INTERNAL",       "eventTime": 1597819675128886121,       "eventName": "Session request execution complete",       "attributes": {         "http.status_code": 200,         "http.handler_class": "org.openqa.selenium.grid.router.HandleSession",         "http.url": "\u002fsession\u002fdd35257f104bb43fdfb06242953f4c85",         "http.method": "DELETE",         "session.id": "dd35257f104bb43fdfb06242953f4c85"       }     }     

In addition to the above fields, based on [OpenTelemetry specification](https://github.com/open-telemetry/opentelemetry-specification/blob/master/specification/trace/semantic_conventions/exceptions.md) error logs consist of :

Field| Field value| Description   ---|---|---   Exception type| exception.type| The class name of the exception.   Exception message| exception.message| Reason for the exception.   Exception stacktrace| exception.stacktrace| Prints the call stack at the point of time when the exception was thrown. Helps in understanding the origin of the exception.      Sample error log               WARN [LoggingOptions$1.lambda$export$1] - {       "traceId": "7efa5ea57e02f89cdf8de586fe09f564",       "spanId": "914df6bc9a1f6e2b",       "spanKind": "INTERNAL",       "eventTime": 1597820253450580272,       "eventName": "exception",       "attributes": {         "exception.type": "org.openqa.selenium.ScriptTimeoutException",         "exception.message": "Unable to execute request: java.sql.SQLSyntaxErrorException: Table 'mysql.sessions_mappa' doesn't exist ..." (full message will be printed),         "exception.stacktrace": "org.openqa.selenium.ScriptTimeoutException: java.sql.SQLSyntaxErrorException: Table 'mysql.sessions_mappa' doesn't exist\nBuild info: version: '4.0.0-alpha-7', revision: 'Unknown'\nSystem info: host: 'XYZ-MacBook-Pro.local', ip: 'fe80:0:0:0:10d5:b63a:bdc6:1aff%en0', os.name: 'Mac OS X', os.arch: 'x86_64', os.version: '10.13.6', java.version: '11.0.7'\nDriver info: driver.version: unknown ...." (full stack will be printed),         "http.handler_class": "org.openqa.selenium.grid.distributor.remote.RemoteDistributor",         "http.url": "\u002fsession",         "http.method": "POST"       }     }     

Note: Logs are pretty printed above for readability. Pretty printing for logs is turned off in Selenium server.

The steps above should set you up for seeing traces and logs.

## References

  1. [Understanding Tracing](https://lightstep.com/blog/opentelemetry-101-what-is-tracing/)   2. [OpenTelemetry Tracing API Specification](https://github.com/open-telemetry/opentelemetry-specification/blob/master/specification/trace/api.md#status)   3. [Selenium Wiki](https://github.com/SeleniumHQ/selenium/wiki)   4. [Structured logs vs events](https://www.honeycomb.io/blog/how-are-structured-logs-different-from-events/)   5. [Jaeger framework](https://github.com/jaegertracing/jaeger)

# 2 - GraphQL query support

GraphQL is a query language for APIs and a runtime for fulfilling those queries with your existing data. It gives users the power to ask for exactly what they need and nothing more.

## Enums

Enums represent possible sets of values for a field.

For example, the `Node` object has a field called `status`. The state is an enum \(specifically, of type `Status`\) because it may be `UP` , `DRAINING` or `UNAVAILABLE`.

## Scalars

Scalars are primitive values: `Int`, `Float`, `String`, `Boolean`, or `ID`.

When calling the GraphQL API, you must specify nested subfield until you return only scalars.

## Structure of the Schema

The structure of grid schema is as follows:               {         session(id: "<session-id>") : {             id,             capabilities,             startTime,             uri,             nodeId,             nodeUri,             sessionDurationMillis             slot : {                 id,                 stereotype,                 lastStarted             }         }         grid: {             uri,             totalSlots,             nodeCount,             maxSession,             sessionCount,             version,             sessionQueueSize         }         sessionsInfo: {             sessionQueueRequests,             sessions: [                 {                     id,                     capabilities,                     startTime,                     uri,                     nodeId,                     nodeUri,                     sessionDurationMillis                     slot : {                         id,                         stereotype,                         lastStarted                     }                 }             ]         }         nodesInfo: {             nodes : [                 {                     id,                     uri,                     status,                     maxSession,                     slotCount,                     sessions: [                         {                             id,                             capabilities,                             startTime,                             uri,                             nodeId,                             nodeUri,                             sessionDurationMillis                             slot : {                                 id,                                 stereotype,                                 lastStarted                             }                         }                     ],                     sessionCount,                     stereotypes,                     version,                     osInfo: {                         arch,                         name,                         version                     }                 }             ]         }     }     

## Querying GraphQL

The best way to query GraphQL is by using `curl` requests. The query is interpreted as JSON. Ensure double quotes are properly escaped to avoid unexpected errors. GraphQL allows you to fetch only the data that you want, nothing more nothing less.

Some of the example GraphQL queries are given below. You can build your own queries as you like.

### Querying the number of `maxSession` and `sessionCount` in the grid :               curl -X POST -H "Content-Type: application/json" --data '{"query": "{ grid { maxSession, sessionCount } }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

Generally on local machine the `<LINK_TO_GRAPHQL_ENDPOINT>` would be `http://localhost:4444/graphql`

### Querying all details for session, node and the Grid :               curl -X POST -H "Content-Type: application/json" --data '{"query":"{ grid { uri, maxSession, sessionCount }, nodesInfo { nodes { id, uri, status, sessions { id, capabilities, startTime, uri, nodeId, nodeUri, sessionDurationMillis, slot { id, stereotype, lastStarted } }, slotCount, sessionCount }} }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

### Query for getting the current session count in the Grid :               curl -X POST -H "Content-Type: application/json" --data '{"query":"{ grid { sessionCount } }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

### Query for getting the max session count in the Grid :               curl -X POST -H "Content-Type: application/json" --data '{"query":"{ grid { maxSession } }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

### Query for getting all session details for all nodes in the Grid :               curl -X POST -H "Content-Type: application/json" --data '{"query":"{ sessionsInfo { sessions { id, capabilities, startTime, uri, nodeId, nodeId, sessionDurationMillis } } }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

### Query to get slot information for all sessions in each Node in the Grid :               curl -X POST -H "Content-Type: application/json" --data '{"query":"{ sessionsInfo { sessions { id, slot { id, stereotype, lastStarted } } } }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

### Query to get session information for a given session:               curl -X POST -H "Content-Type: application/json" --data '{"query":"{ session (id: \"<session-id>\") { id, capabilities, startTime, uri, nodeId, nodeUri, sessionDurationMillis, slot { id, stereotype, lastStarted } } } "}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

### Querying the capabilities of each node in the grid :               curl -X POST -H "Content-Type: application/json" --data '{"query": "{ nodesInfo { nodes { stereotypes } } }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

### Querying the status of each node in the grid :               curl -X POST -H "Content-Type: application/json" --data '{"query": "{ nodesInfo { nodes { status } } }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

### Querying the URI of each node and the grid :               curl -X POST -H "Content-Type: application/json" --data '{"query": "{ nodesInfo { nodes { uri } } }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

### Query for getting the current requests in the New Session Queue:               curl -X POST -H "Content-Type: application/json" --data '{"query":"{ sessionsInfo { sessionQueueRequests } }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

### Query for getting the New Session Queue size :               curl -X POST -H "Content-Type: application/json" --data '{"query":"{ grid { sessionQueueSize } }"}' -s <LINK_TO_GRAPHQL_ENDPOINT>     

# 3 - Grid endpoints

## Grid

### Grid Status

Grid status provides the current state of the Grid. It consists of details about every registered Node. For every Node, the status includes information regarding Node availability, sessions, and slots.               curl --request GET 'http://localhost:4444/status'     

### Delete session

Deleting the session terminates the WebDriver session, quits the driver and removes it from the active sessions map. Any request using the removed session-id or reusing the driver instance will throw an error.               curl --request DELETE 'http://localhost:4444/session/<session-id>'     

### Which URL should I use?

In the Standalone mode, the Grid URL is the Standalone server address.

In the Hub-Node mode, the Grid URL is the Hub server address.

In the fully distributed mode, the Grid URL is the Router server address.

Default URL for all the above modes is http://localhost:4444.

## Distributor

### Remove Node

To remove the Node from the Grid, use the curl command enlisted below. It does not stop any ongoing session running on that Node. The Node continues running as it is unless explicitly killed. The Distributor is no longer aware of the Node and hence any matching new session request will not be forwarded to that Node.

In the Standalone mode, the Distributor URL is the Standalone server address.

In the Hub-Node mode, the Distributor URL is the Hub server address.               curl --request DELETE 'http://localhost:4444/se/grid/distributor/node/<node-id>' --header 'X-REGISTRATION-SECRET: <secret> '     

In the fully distributed mode, the URL is the Router server address.               curl --request DELETE 'http://localhost:4444/se/grid/distributor/node/<node-id>' --header 'X-REGISTRATION-SECRET: <secret>'     

If no registration secret has been configured while setting up the Grid, then use               curl --request DELETE 'http://<Router-URL>/se/grid/distributor/node/<node-id>' --header 'X-REGISTRATION-SECRET;'     

### Drain Node

Node drain command is for graceful node shutdown. Draining a Node stops the Node after all the ongoing sessions are complete. However, it does not accept any new session requests.

In the Standalone mode, the Distributor URL is the Standalone server address.

In the Hub-Node mode, the Distributor URL is the Hub server address.               curl --request POST 'http://localhost:4444/se/grid/distributor/node/<node-id>/drain' --header 'X-REGISTRATION-SECRET: <secret> '     

In the fully distributed mode, the URL is the Router server address.               curl --request POST 'http://localhost:4444/se/grid/distributor/node/<node-id>/drain' --header 'X-REGISTRATION-SECRET: <secret>'     

If no registration secret has been configured while setting up the Grid, then use               curl --request POST 'http://<Router-URL>/se/grid/distributor/node/<node-id>/drain' --header 'X-REGISTRATION-SECRET;'     

## Node

The endpoints in this section are applicable for Hub-Node mode and fully distributed Grid mode where the Node runs independently. The default Node URL is http://localhost:5555 in case of one Node. In case of multiple Nodes, use [Grid status](https://www.selenium.dev/documentation/grid/advanced_features/endpoints/#grid-status) to get all Node details and locate the Node address.

### Status

The Node status is essentially a health-check for the Node. Distributor pings the node status at regular intervals and updates the Grid Model accordingly. The status includes information regarding availability, sessions, and slots.               curl --request GET 'http://localhost:5555/status'     

### Drain

Distributor passes the [drain](https://www.selenium.dev/documentation/grid/advanced_features/endpoints/#drain-node) command to the appropriate node identified by the node-id. To drain the Node directly, use the curl command enlisted below. Both endpoints are valid and produce the same result. Drain finishes the ongoing sessions before stopping the Node.               curl --request POST 'http://localhost:5555/se/grid/node/drain' --header 'X-REGISTRATION-SECRET: <secret>'     

If no registration secret has been configured while setting up the Grid, then use               curl --request POST 'http://<node-URL>/se/grid/node/drain' --header 'X-REGISTRATION-SECRET;'     

### Check session owner

To check if a session belongs to a Node, use the curl command enlisted below.               curl --request GET 'http://localhost:5555/se/grid/node/owner/<session-id>' --header 'X-REGISTRATION-SECRET: <secret>'     

If no registration secret has been configured while setting up the Grid, then use               curl --request GET 'http://<node-URL>/se/grid/node/owner/<session-id>' --header 'X-REGISTRATION-SECRET;'     

It will return true if the session belongs to the Node else it will return false.

### Delete session

Deleting the session terminates the WebDriver session, quits the driver and removes it from the active sessions map. Any request using the removed session-id or reusing the driver instance will throw an error.               curl --request DELETE 'http://localhost:5555/se/grid/node/session/<session-id>' --header 'X-REGISTRATION-SECRET: <secret>'     

If no registration secret has been configured while setting up the Grid, then use               curl --request DELETE 'http://<node-URL>/se/grid/node/session/<session-id>' --header 'X-REGISTRATION-SECRET;'     

## New Session Queue

### Clear New Session Queue

New Session Request Queue holds the new session requests. To clear the queue, use the curl command enlisted below. Clearing the queue rejects all the requests in the queue. For each such request, the server returns an error response to the respective client. The result of the clear command is the total number of deleted requests.

In the Standalone mode, the Queue URL is the Standalone server address.

In the Hub-Node mode, the Queue URL is the Hub server address.               curl --request DELETE 'http://localhost:4444/se/grid/newsessionqueue/queue' --header 'X-REGISTRATION-SECRET: <secret>'     

In the fully distributed mode, the Queue URL is Router server address.               curl --request DELETE 'http://localhost:4444/se/grid/newsessionqueue/queue' --header 'X-REGISTRATION-SECRET: <secret>'     

If no registration secret has been configured while setting up the Grid, then use               curl --request DELETE 'http://<Router-URL>/se/grid/newsessionqueue/queue' --header 'X-REGISTRATION-SECRET;'     

### Get New Session Queue Requests

New Session Request Queue holds the new session requests. To get the current requests in the queue, use the curl command enlisted below. The response returns the total number of requests in the queue and the request payloads.

In the Standalone mode, the Queue URL is the Standalone server address.

In the Hub-Node mode, the Queue URL is the Hub server address.               curl --request GET 'http://localhost:4444/se/grid/newsessionqueue/queue'     

In the fully distributed mode, the Queue URL is Router server address.               curl --request GET 'http://localhost:4444/se/grid/newsessionqueue/queue'     

# 4 - Customizing a Node

## How to customize a Node

There are times when we would like a Node to be customized to our needs.

For e.g., we may like to do some additional setup before a session begins execution and some clean-up after a session runs to completion.

Following steps can be followed for this:

  * Create a class that extends `org.openqa.selenium.grid.node.Node`

  * Add a static method \(this will be our factory method\) to the newly created class whose signature looks like this:

`public static Node create(Config config)`. Here:

    * `Node` is of type `org.openqa.selenium.grid.node.Node`     * `Config` is of type `org.openqa.selenium.grid.config.Config`   * Within this factory method, include logic for creating your new Class.

  * To wire in this new customized logic into the hub, start the node and pass in the fully qualified class name of the above class to the argument `--node-implementation`

Let’s see an example of all this:

### Custom Node as an uber jar

  1. Create a sample project using your favourite build tool \(**Maven** |**Gradle**\).   2. Add the below dependency to your sample project.      * [org.seleniumhq.selenium/selenium-grid](https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-grid)   3. Add your customized Node to the project.   4. Build an [uber jar](https://imagej.net/develop/uber-jars) to be able to start the Node using `java -jar` command.   5. Now start the Node using the command:

              java -jar custom_node-server.jar node \     --node-implementation org.seleniumhq.samples.DecoratedLoggingNode     

**Note:** If you are using Maven as a build tool, please prefer using [maven-shade-plugin](https://maven.apache.org/plugins/maven-shade-plugin) instead of [maven-assembly-plugin](https://maven.apache.org/plugins/maven-assembly-plugin) because maven-assembly plugin seems to have issues with being able to merge multiple Service Provider Interface files \(`META-INF/services`\)

### Custom Node as a regular jar

  1. Create a sample project using your favourite build tool \(**Maven** |**Gradle**\).   2. Add the below dependency to your sample project.      * [org.seleniumhq.selenium/selenium-grid](https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-grid)   3. Add your customized Node to the project.   4. Build a jar of your project using your build tool.   5. Now start the Node using the command:

              java -jar selenium-server-4.6.0.jar \     --ext custom_node-1.0-SNAPSHOT.jar node \     --node-implementation org.seleniumhq.samples.DecoratedLoggingNode     

Below is a sample that just prints some messages on to the console whenever there’s an activity of interest \(session created, session deleted, a webdriver command executed etc.,\) on the Node.

Sample customized node               package org.seleniumhq.samples;          import java.io.IOException;     import java.net.URI;     import java.util.UUID;     import java.util.function.Supplier;     import org.openqa.selenium.Capabilities;     import org.openqa.selenium.NoSuchSessionException;     import org.openqa.selenium.WebDriverException;     import org.openqa.selenium.grid.config.Config;     import org.openqa.selenium.grid.data.CreateSessionRequest;     import org.openqa.selenium.grid.data.CreateSessionResponse;     import org.openqa.selenium.grid.data.NodeId;     import org.openqa.selenium.grid.data.NodeStatus;     import org.openqa.selenium.grid.data.Session;     import org.openqa.selenium.grid.log.LoggingOptions;     import org.openqa.selenium.grid.node.HealthCheck;     import org.openqa.selenium.grid.node.Node;     import org.openqa.selenium.grid.node.local.LocalNodeFactory;     import org.openqa.selenium.grid.security.Secret;     import org.openqa.selenium.grid.security.SecretOptions;     import org.openqa.selenium.grid.server.BaseServerOptions;     import org.openqa.selenium.internal.Either;     import org.openqa.selenium.io.TemporaryFilesystem;     import org.openqa.selenium.remote.SessionId;     import org.openqa.selenium.remote.http.HttpRequest;     import org.openqa.selenium.remote.http.HttpResponse;     import org.openqa.selenium.remote.tracing.Tracer;          public class DecoratedLoggingNode extends Node {            private Node node;            protected DecoratedLoggingNode(Tracer tracer, NodeId nodeId, URI uri, Secret registrationSecret, Duration sessionTimeout) {         super(tracer, nodeId, uri, registrationSecret, sessionTimeout);       }            public static Node create(Config config) {         LoggingOptions loggingOptions = new LoggingOptions(config);         BaseServerOptions serverOptions = new BaseServerOptions(config);         URI uri = serverOptions.getExternalUri();         SecretOptions secretOptions = new SecretOptions(config);         NodeOptions nodeOptions = new NodeOptions(config);         Duration sessionTimeout = nodeOptions.getSessionTimeout();              // Refer to the foot notes for additional context on this line.         Node node = LocalNodeFactory.create(config);              DecoratedLoggingNode wrapper = new DecoratedLoggingNode(loggingOptions.getTracer(),             node.getId(),             uri,             secretOptions.getRegistrationSecret(),             sessionTimeout);         wrapper.node = node;         return wrapper;       }            @Override       public Either<WebDriverException, CreateSessionResponse> newSession(           CreateSessionRequest sessionRequest) {         return perform(() -> node.newSession(sessionRequest), "newSession");       }            @Override       public HttpResponse executeWebDriverCommand(HttpRequest req) {         return perform(() -> node.executeWebDriverCommand(req), "executeWebDriverCommand");       }            @Override       public Session getSession(SessionId id) throws NoSuchSessionException {         return perform(() -> node.getSession(id), "getSession");       }            @Override       public HttpResponse uploadFile(HttpRequest req, SessionId id) {         return perform(() -> node.uploadFile(req, id), "uploadFile");       }            @Override       public HttpResponse downloadFile(HttpRequest req, SessionId id) {         return perform(() -> node.downloadFile(req, id), "downloadFile");       }            @Override       public TemporaryFilesystem getDownloadsFilesystem(UUID uuid) {         return perform(() -> {           try {             return node.getDownloadsFilesystem(uuid);           } catch (IOException e) {             throw new RuntimeException(e);           }         }, "downloadsFilesystem");       }            @Override       public TemporaryFilesystem getUploadsFilesystem(SessionId id) throws IOException {         return perform(() -> {           try {             return node.getUploadsFilesystem(id);           } catch (IOException e) {             throw new RuntimeException(e);           }         }, "uploadsFilesystem");            }            @Override       public void stop(SessionId id) throws NoSuchSessionException {         perform(() -> node.stop(id), "stop");       }            @Override       public boolean isSessionOwner(SessionId id) {         return perform(() -> node.isSessionOwner(id), "isSessionOwner");       }            @Override       public boolean isSupporting(Capabilities capabilities) {         return perform(() -> node.isSupporting(capabilities), "isSupporting");       }            @Override       public NodeStatus getStatus() {         return perform(() -> node.getStatus(), "getStatus");       }            @Override       public HealthCheck getHealthCheck() {         return perform(() -> node.getHealthCheck(), "getHealthCheck");       }            @Override       public void drain() {         perform(() -> node.drain(), "drain");       }            @Override       public boolean isReady() {         return perform(() -> node.isReady(), "isReady");       }            private void perform(Runnable function, String operation) {         try {           System.err.printf("[COMMENTATOR] Before %s()%n", operation);           function.run();         } finally {           System.err.printf("[COMMENTATOR] After %s()%n", operation);         }       }            private <T> T perform(Supplier<T> function, String operation) {         try {           System.err.printf("[COMMENTATOR] Before %s()%n", operation);           return function.get();         } finally {           System.err.printf("[COMMENTATOR] After %s()%n", operation);         }       }     }     

**_Foot Notes:_**

In the above example, the line `Node node = LocalNodeFactory.create(config);` explicitly creates a `LocalNode`.

There are basically 2 types of _user facing implementations_ of `org.openqa.selenium.grid.node.Node` available.

These classes are good starting points to learn how to build a custom Node and also to learn the internals of a Node.

  * `org.openqa.selenium.grid.node.local.LocalNode` \- Used to represent a long running Node and is the default implementation that gets wired in when you start a `node`.     * It can be created by calling `LocalNodeFactory.create(config);`, where:       * `LocalNodeFactory` belongs to `org.openqa.selenium.grid.node.local`       * `Config` belongs to `org.openqa.selenium.grid.config`   * `org.openqa.selenium.grid.node.k8s.OneShotNode` \- This is a special reference implementation wherein the Node gracefully shuts itself down after servicing one test session. This class is currently not available as part of any pre-built maven artifact.     * You can refer to the source code [here](https://github.com/SeleniumHQ/selenium/blob/trunk/java/src/org/openqa/selenium/grid/node/k8s/OneShotNode.java) to understand its internals.     * To build it locally refer [here](https://github.com/SeleniumHQ/selenium/blob/trunk/deploys/k8s/README.md).     * It can be created by calling `OneShotNode.create(config)`, where:       * `OneShotNode` belongs to `org.openqa.selenium.grid.node.k8s`       * `Config` belongs to `org.openqa.selenium.grid.config`

# 5 - External datastore

## Table of Contents

  * [Introduction](https://www.selenium.dev/documentation/grid/advanced_features/external_datastore/#introduction)   * [Setup](https://www.selenium.dev/documentation/grid/advanced_features/external_datastore/#setup)   * [Database backed Session Map](https://www.selenium.dev/documentation/grid/advanced_features/external_datastore/#database-backed-session-map)     * [Steps](https://www.selenium.dev/documentation/grid/advanced_features/external_datastore/#steps)   * [Redis backed Session Map](https://www.selenium.dev/documentation/grid/advanced_features/external_datastore/#redis-backed-session-map)     * [Steps](https://www.selenium.dev/documentation/grid/advanced_features/external_datastore/#steps)

## Introduction

Selenium Grid allows you to persist information related to currently running sessions into an external data store. The external data store could be backed by your favourite database \(or\) Redis Cache system.

## Setup

  * [Coursier](https://get-coursier.io/docs/cli-installation) \- As a dependency resolver, so that we can download maven artifacts on the fly and make them available in our classpath   * [Docker](https://docs.docker.com/engine/install/) \- To manage our PostGreSQL/Redis docker containers.

## Database backed Session Map

For the sake of this illustration, we are going to work with PostGreSQL database.

We will spin off a PostGreSQL database as a docker container using a docker compose file.

### Steps

You can skip this step if you already have a PostGreSQL database instance available at your disposal.

  * Create a sql file named `init.sql` with the below contents:

              CREATE TABLE IF NOT EXISTS sessions_map(         session_ids varchar(256),         session_caps text,         session_uri varchar(256),         session_stereotype text,         session_start varchar(256)      );     

  * In the same directory as the `init.sql`, create a file named `docker-compose.yml` with its contents as below:

              version: '3.8'     services:       db:         image: postgres:9.6-bullseye         restart: always         environment:           - POSTGRES_USER=seluser           - POSTGRES_PASSWORD=seluser           - POSTGRES_DB=selenium_sessions         ports:           - "5432:5432"         volumes:         - ./init.sql:/docker-entrypoint-initdb.d/init.sql     

We can now start our database container by running:               docker-compose up -d     

_Our database name is`selenium_sessions` with its username and password set to `seluser`_

If you are working with an already running PostGreSQL DB instance, then you just need to create a database named `selenium_sessions` and the table `sessions_map` using the above mentioned SQL statement.

  * Create a Selenium Grid configuration file named `sessions.toml` with the below contents:

              [sessions]     implementation = "org.openqa.selenium.grid.sessionmap.jdbc.JdbcBackedSessionMap"     jdbc-url = "jdbc:postgresql://localhost:5432/selenium_sessions"     jdbc-user = "seluser"     jdbc-password = "seluser"     

_Note:_ If you plan to use an existing PostGreSQL DB instance, then replace `localhost:5432` with the actual host and port number of your instance.

  * Below is a simple shell script \(let’s call it `distributed.sh`\) that we will use to bring up our distributed Grid.

              SE_VERSION=<current_selenium_version>     JAR_NAME=selenium-server-${SE_VERSION}.jar     PUBLISH="--publish-events tcp://localhost:4442"     SUBSCRIBE="--subscribe-events tcp://localhost:4443"     SESSIONS="--sessions http://localhost:5556"     SESSIONS_QUEUE="--sessionqueue http://localhost:5559"     echo 'Starting Event Bus'     java -jar $JAR_NAME event-bus $PUBLISH $SUBSCRIBE --port 5557 &     echo 'Starting New Session Queue'     java -jar $JAR_NAME sessionqueue --port 5559 &     echo 'Starting Sessions Map'     java -jar $JAR_NAME \     --ext $(coursier fetch -p org.seleniumhq.selenium:selenium-session-map-jdbc:${SE_VERSION} org.postgresql:postgresql:42.3.1) \     sessions $PUBLISH $SUBSCRIBE --port 5556 --config sessions.toml &     echo 'Starting Distributor'     java -jar $JAR_NAME  distributor $PUBLISH $SUBSCRIBE $SESSIONS $SESSIONS_QUEUE --port 5553 --bind-bus false &     echo 'Starting Router'     java -jar $JAR_NAME router $SESSIONS --distributor http://localhost:5553 $SESSIONS_QUEUE --port 4444 &     echo 'Starting Node'     java -jar $JAR_NAME node $PUBLISH $SUBSCRIBE &     

  * At this point the current directory should contain the following files:

    * `docker-compose.yml`     * `init.sql`     * `sessions.toml`     * `distributed.sh`   * You can now spawn the Grid by running `distributed.sh` shell script and quickly run a test. You will notice that the Grid now stores session information into the PostGreSQL database.

In the line which spawns a `SessionMap` on a machine:               export SE_VERSION=<current_selenium_version>     java -jar selenium-server-${SE_VERSION}.jar \     --ext $(coursier fetch -p org.seleniumhq.selenium:selenium-session-map-jdbc:${SE_VERSION} org.postgresql:postgresql:42.3.1) \     sessions --publish-events tcp://localhost:4442 \     --subscribe-events tcp://localhost:4443 \     --port 5556 --config sessions.toml      

  * The variable names from the above script have been replaced with their actual values for clarity.   * Remember to substitute `localhost` with the actual hostname of the machine where your `Event-Bus` is running.   * The arguments being passed to `coursier` are basically the GAV \(Group Artifact Version\) Maven co-ordinates of:     * [selenium-session-map-jdbc](https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-session-map-jdbc) which is needed to help us store sessions information in database     * [postgresql](https://mvnrepository.com/artifact/org.postgresql/postgresql) which is needed to help us talk PostGreSQL database.   * `sessions.toml` is the configuration file that we created earlier.

## Redis backed Session Map

We will spin off a Redis Cache docker container using a docker compose file.

### Steps

You can skip this step if you already have a Redis Cache instance available at your disposal.

  * Create a file named `docker-compose.yml` with its contents as below:

              version: '3.8'     services:       redis:         image: redis:bullseye         restart: always         ports:           - "6379:6379"     

We can now start our Redis container by running:               docker-compose up -d     

  * Create a Selenium Grid configuration file named `sessions.toml` with the below contents:

              [sessions]     scheme = "redis"     implementation = "org.openqa.selenium.grid.sessionmap.redis.RedisBackedSessionMap"     hostname = "localhost"     port = 6379     

_Note:_ If you plan to use an existing Redis Cache instance, then replace `localhost` and `6379` with the actual host and port number of your instance.

  * Below is a simple shell script \(let’s call it `distributed.sh`\) that we will use to bring up our distributed grid.

              SE_VERSION=<current_selenium_version>     JAR_NAME=selenium-server-${SE_VERSION}.jar     PUBLISH="--publish-events tcp://localhost:4442"     SUBSCRIBE="--subscribe-events tcp://localhost:4443"     SESSIONS="--sessions http://localhost:5556"     SESSIONS_QUEUE="--sessionqueue http://localhost:5559"     echo 'Starting Event Bus'     java -jar $JAR_NAME event-bus $PUBLISH $SUBSCRIBE --port 5557 &     echo 'Starting New Session Queue'     java -jar $JAR_NAME sessionqueue --port 5559 &     echo 'Starting Session Map'     java -jar $JAR_NAME \     --ext $(coursier fetch -p org.seleniumhq.selenium:selenium-session-map-redis:${SE_VERSION}) \     sessions $PUBLISH $SUBSCRIBE --port 5556 --config sessions.toml &     echo 'Starting Distributor'     java -jar $JAR_NAME  distributor $PUBLISH $SUBSCRIBE $SESSIONS $SESSIONS_QUEUE --port 5553 --bind-bus false &     echo 'Starting Router'     java -jar $JAR_NAME router $SESSIONS --distributor http://localhost:5553 $SESSIONS_QUEUE --port 4444 &     echo 'Starting Node'     java -jar $JAR_NAME node $PUBLISH $SUBSCRIBE &     

  * At this point the current directory should contain the following files:

    * `docker-compose.yml`     * `sessions.toml`     * `distributed.sh`   * You can now spawn the Grid by running `distributed.sh` shell script and quickly run a test. You will notice that the Grid now stores session information into the Redis instance. You can perhaps make use of a Redis GUI such as [TablePlus](https://tableplus.com/) to see them \(Make sure that you have setup a debug point in your test, because the values will get deleted as soon as the test runs to completion\).

In the line which spawns a `SessionMap` on a machine:               export SE_VERSION=<current_selenium_version>     java -jar selenium-server-${SE_VERSION}.jar \     --ext $(coursier fetch -p org.seleniumhq.selenium:selenium-session-map-redis:${SE_VERSION}) \     sessions --publish-events tcp://localhost:4442 \     --subscribe-events tcp://localhost:4443 \     --port 5556 --config sessions.toml      

  * The variable names from the above script have been replaced with their actual values for clarity.   * Remember to substitute `localhost` with the actual hostname of the machine where your `Event-Bus` is running.   * The arguments being passed to `coursier` are basically the GAV \(Group Artifact Version\) Maven co-ordinates of:     * [selenium-session-map-redis](https://mvnrepository.com/artifact/org.seleniumhq.selenium/selenium-session-map-redis) which is needed to help us store sessions information in Redis Cache.   * `sessions.toml` is the configuration file that we created earlier.