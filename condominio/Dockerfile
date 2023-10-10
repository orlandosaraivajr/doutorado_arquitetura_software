FROM openjdk:22-slim

ARG JAR_FILE=target/*.jar

COPY ${JAR_FILE} /tmp/app.jar

EXPOSE 8082

ENTRYPOINT ["java","-jar","/tmp/app.jar"]