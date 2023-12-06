# Verwenden Sie das offizielle OpenJDK-Image als Basis
FROM openjdk:22-ea-21-slim-bullseye
# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopieren Sie die JAR-Datei in das Arbeitsverzeichnis
COPY target/gateway-0.0.1-SNAPSHOT.jar /app/app.jar

# Festlegen des Befehls zum Ausführen der Anwendung
CMD ["java", "-jar", "app.jar"]