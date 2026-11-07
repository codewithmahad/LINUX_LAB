# Java service command reference

Commands to try in a **separate Spring Boot project**, saved here for application practice. This repository has no Spring Boot application or JAR to run.

The project needs a configured Maven Wrapper and an executable JAR. Replace `target/app.jar` with the actual artifact path and use a profile configured for that application.

## Build and run

From the application directory:

```bash
./mvnw verify
SPRING_PROFILES_ACTIVE=dev java -jar target/app.jar
```

Run the application after the build succeeds. Its startup logs stay in this terminal.

## Inspect from another terminal

```bash
curl -i --max-time 5 http://localhost:8080/api/users
ss -ltnp 'sport = :8080'
```

Use an endpoint the application exposes. `curl -i` shows headers and the body; it does not fail just because an HTTP error status was returned. A scripted check needs an explicit success condition, such as `curl --fail` for HTTP 400+ responses.

`ss` inspects listening TCP sockets on port 8080. Process details depend on the account's access permissions.

If the application is configured to write `app.log`:

```bash
tail -n 50 -f app.log
```

Spring Boot's [running guide](https://docs.spring.io/spring-boot/reference/using/running-your-application.html) and [configuration reference](https://docs.spring.io/spring-boot/reference/features/external-config.html), the [Maven Wrapper guide](https://maven.apache.org/tools/wrapper/), and the [curl manual](https://curl.se/docs/manpage.html) cover the details.

For an existing Ubuntu service example, see [DeployLatch's operations guide](https://github.com/codewithmahad/deploylatch/blob/main/docs/OPERATIONS.md).

[Back to the learning map](../../README.md#learning-map)
