# Use the official OpenJDK image as the base
FROM openjdk:22-ea-21-slim-bullseye

# Set the working directory in the container
WORKDIR /app

# Copy the JAR file into the working directory
COPY target/gateway-0.0.1-SNAPSHOT.jar /app/app.jar

# Set the command to run the application
CMD ["java", "-jar", "app.jar"]

# 1) build image: docker build -t normal_mini .
# 2) run image: docker run -p 8080:8080 --cpus=8 --memory=1g --name normal_mini normal_mini