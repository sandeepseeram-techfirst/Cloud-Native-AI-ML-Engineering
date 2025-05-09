# Skaffold 
Skaffold is an open-source command-line tool created by Google that helps developers build, push, and deploy applications to Kubernetes—quickly and repeatedly—without manually running multiple commands every time you make a change.

- It focuses on developer workflows for Kubernetes-based applications, automating the boring, repetitive steps.

Skaffold automates the entire build → push → deploy → verify cycle.

- Auto-Build: Detects code changes and rebuilds the image automatically.

- Auto-Push: Pushes the new image to your registry (or skips this step if using a local cluster like Minikube or Kind).

- Auto-Deploy: Updates Kubernetes manifests (including Helm/Kustomize) and redeploys automatically.

- Log Streaming: Streams logs from your Kubernetes pods so you can see app output immediately.

- Port Forwarding: Makes local services accessible without extra configuration.


Skaffold removes the friction from Kubernetes app development by automating the steps between writing code and seeing it run in your cluster. It’s like a live-reload tool but for Kubernetes.