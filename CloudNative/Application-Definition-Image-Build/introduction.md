# Application Definition and Image Build
Application Definition and Image Build usually refers to how you define your microservice’s behavior, configuration, dependencies, and runtime environment, and then package it into a deployable image (often a container image).

## It has two main parts:

### Application Definition

Describes what the application is, how it should run, and what it needs.

- Includes source code, configuration files, runtime instructions, environment variables, API definitions, and sometimes deployment manifests.

Purpose: Make the service self-contained, reproducible, and portable.

### Image Build

Converts your defined application into a deployable artifact — most commonly a container image (Docker, OCI format).

- The image contains everything needed to run the app: compiled code, libraries, configuration, and runtime.


# How it Works — Step by Step 

## Step 1 — Source Code & Application Definition

- Write the microservice code (Java, Go, Python, Node.js, etc.).

### Define:

- Dependencies (e.g., requirements.txt in Python, pom.xml in Maven, package.json in Node.js).

- Configuration (e.g., .env files, config maps, YAML).

- Entry point (e.g., main() function or CMD in Dockerfile).

- Service interfaces (REST APIs via OpenAPI spec, gRPC proto files, event schema).

## Step 2 — Image Build Process 

Dockerfile or Build tool defines:

- Base image (e.g., FROM python:3.12-slim)

- Copy application files

- Install dependencies

- Define runtime command

## Step 3 -  Integration into CI/CD

### CI/CD pipelines:

- Pull latest source code from Git

- Run tests & linting

- Build image

- Push image to registry

- Deploy to Kubernetes / another orchestrator


