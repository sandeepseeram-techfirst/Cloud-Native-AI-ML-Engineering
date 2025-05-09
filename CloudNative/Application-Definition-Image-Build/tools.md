## Common Tools & Technologies


| **Category**                | **Tool**                                | **Description**                                           |
|-----------------------------|-----------------------------------------|-----------------------------------------------------------|
| **Container Build**         | Docker                                  | Most common tool for building OCI container images        |
|                             | Podman                                  | Daemonless container build/run alternative                |
|                             | Buildah                                 | Scriptable container image builder                        |
|                             | Kaniko                                  | Builds images in Kubernetes without Docker daemon         |
|                             | img                                     | Builds OCI/Docker images without root privileges          |
|                             | Google Cloud Build                      | Serverless CI/CD & build service                          |
|                             | AWS CodeBuild                           | Managed build service                                     |
|                             | Azure Container Registry Tasks          | Native image builds in Azure                              |
| **Build Automation**        | Cloud Native Buildpacks (Paketo, Heroku)| Auto-generate Docker images from source without Dockerfile|
|                             | Jib                                     | Java image builder without Dockerfile                     |
|                             | Skaffold                                | Local dev + image build automation for Kubernetes         |
|                             | Tilt                                    | Local microservice dev + rebuild automation               |
| **Declarative App Definition** | Helm                                  | Package manager for Kubernetes apps                       |
|                             | Kustomize                               | Kubernetes-native config customization                    |
|                             | Jsonnet                                 | Data templating for configs                               |
|                             | Cue                                     | Data validation and configuration                         |
| **Registry**                | Docker Hub                              | Public container registry                                 |
|                             | Harbor                                  | CNCF-hosted secure container registry                      |
|                             | Quay                                    | Red Hat container registry                                |
| **Security Scanning**       | Trivy                                   | Image vulnerability scanner                               |
|                             | Clair                                   | Static analysis for vulnerabilities                       |
|                             | Grype                                   | CLI vulnerability scanner                                 |
