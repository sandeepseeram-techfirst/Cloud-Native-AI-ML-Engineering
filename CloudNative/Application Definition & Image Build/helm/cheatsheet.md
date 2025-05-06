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
