# Podman 
Podman is a daemonless container engine for developing, managing, and running OCI Containers on your Linux System. 
Containers can either be run as root or in rootless mode.

## Key Features

- **Daemonless Architecture**: No background service; each command spawns its own process.
- **Rootless Containers**: Can run containers as a non-root user.
- **Docker Compatibility**: Supports `docker` CLI via `alias docker=podman`.
- **Pod Support**: Groups multiple containers into a single pod, similar to Kubernetes.
- **OCI Compliance**: Works with OCI images and runtimes (e.g., `runc`, `crun`).
- **Integration with Kubernetes**: Can generate Kubernetes YAML from existing containers or pods.

---


+----------------------------+
|        User CLI            |
|   (podman run / build)     |
+-------------+--------------+
              |
              v
+----------------------------+
| Podman (daemonless binary) |
| - uses containers/storage  |
| - invokes Buildah / Skopeo |
+------+---------------------+
       |
       v
+----------------------------+      +----------------+
| OCI runtimes / helpers     | <--> | Registry / Repo|
| - runc / crun / kata       |      | DockerHub/Quay |
+----------------------------+      +----------------+
