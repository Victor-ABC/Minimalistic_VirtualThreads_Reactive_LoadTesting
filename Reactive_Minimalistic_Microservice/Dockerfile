# Verwenden Sie das offizielle OpenJDK-Image als Basis
FROM openjdk:22-ea-21-slim-bullseye
# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopieren Sie die JAR-Datei in das Arbeitsverzeichnis
COPY target/gateway-0.0.1-SNAPSHOT.jar /app/app.jar

# Festlegen des Befehls zum Ausführen der Anwendung
CMD ["java", "-Xmx400m", "-jar", "app.jar"]

# 1) build image: docker build -t reactive_mini_256mb .
# 2) run image: docker run -p 8081:8080 --cpus=8 --memory=1g --name reactive_mini_256mb reactive_mini_256mb