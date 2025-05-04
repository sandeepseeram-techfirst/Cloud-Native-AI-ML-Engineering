# Run a container (detached)
podman run -d --name web nginx:latest

# List running containers
podman ps

# List all containers (including stopped)
podman ps -a

# Build image from Dockerfile
podman build -t myapp:1.0 .

# Push image to registry
podman push myapp:1.0 docker.io/youruser/myapp:1.0

# Create a pod and run a container inside it
podman pod create --name mypod
podman run --pod mypod --name web nginx:latest

# Generate Kubernetes YAML from a pod
podman generate kube mypod > mypod.yaml

# Play Kubernetes YAML locally
podman play kube mypod.yaml

# Inspect a container or image
podman inspect container-or-image

# Run in rootless troubleshooting context
podman unshare   # get a shell in the user namespace
