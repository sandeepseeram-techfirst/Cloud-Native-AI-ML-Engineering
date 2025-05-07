# 🛠️ Helm Cheat Sheet

Helm is a package manager for Kubernetes, used to deploy and manage applications via **Charts**.

---

## 📦 Installation & Version
```bash
helm version                        # Show Helm client & server version
helm help                           # Show help for Helm commands

## 📦 Search

helm search hub <keyword>           # Search Helm Hub for charts
helm search repo <keyword>          # Search in local repos
helm search hub mysql               # Search MySQL charts in Helm Hub

## 📦 Repository 

helm repo list                      # List added repositories
helm repo add <repo_name> <repo_url> # Add a repository
helm repo add bitnami https://charts.bitnami.com/bitnami
helm repo update                    # Update repositories
helm repo remove <repo_name>        # Remove a repository

## Installing Charts 

helm install <release_name> <chart>          # Install a chart
helm install myapp bitnami/nginx             # Install from repo
helm install myapp ./mychart                 # Install from local directory
helm install myapp ./mychart --dry-run       # Simulate install
helm install myapp bitnami/nginx --set key=value  # Override values
helm install myapp bitnami/nginx -f values.yaml   # Use custom values file

## Upgrading Releases

helm upgrade <release_name> <chart>          # Upgrade release
helm upgrade <release_name> <chart> --set key=value
helm upgrade <release_name> <chart> -f values.yaml
helm upgrade --install <release_name> <chart> # Upgrade or install if not present


## Rollbacks 

helm rollback <release_name> <revision_number>   # Rollback to a specific revision
helm history <release_name>                      # View release history

## Listing and Status

helm list                          # List all releases in current namespace
helm list -A                       # List releases across all namespaces
helm status <release_name>         # Get status of a release
helm get all <release_name>        # Get all release information
helm get values <release_name>     # Get values used for a release
helm get manifest <release_name>   # Get Kubernetes manifest
helm get notes <release_name>      # Get chart notes
