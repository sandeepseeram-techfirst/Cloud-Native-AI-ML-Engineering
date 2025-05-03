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
