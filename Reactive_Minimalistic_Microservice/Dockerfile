# Verwenden Sie das offizielle OpenJDK-Image als Basis
FROM openjdk:22-ea-21-slim-bullseye
# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopieren Sie die JAR-Datei in das Arbeitsverzeichnis
COPY target/gateway-0.0.1-SNAPSHOT.jar /app/app.jar

# Festlegen des Befehls zum Ausführen der Anwendung
CMD ["java", "-Xmx7000m", "-jar", "app.jar"]

# 1) build image: docker build -t reactive_mini_8gb .
# 2) run image: docker run -p 8081:8080 --cpus=8 --memory=8g --name reactive_mini_8gb reactive_mini_8gb