# 🌩️ Cloud Native AI – Concepts, Tools & Practical Guide

## 📌 Overview
**Cloud Native AI** is the practice of building, deploying, and managing AI/ML workloads using **cloud native principles** — scalability, resilience, automation, and portability — typically powered by **Kubernetes** and container-based architectures.

This repository is my learning journal, experiments, and implementations for **Cloud Native AI**.

---

## 🚀 What is Cloud Native AI?

Cloud Native AI combines:
- **AI/ML** → Training, inference, and serving of machine learning and deep learning models.
- **Cloud Native** → Containers, Kubernetes, CI/CD, observability, and scalability across hybrid/multi-cloud environments.

**Why it matters:**
- **Elastic compute** → Scale GPU/TPU workloads up/down on demand.
- **Portable** → Run across AWS, GCP, Azure, or on-prem Kubernetes.
- **Automated** → Continuous training, testing, and deployment pipelines.
- **Observable** → Track infrastructure, model performance, and drift.

```
┌─────────────────────────────────────────────────────┐
│                  Cloud Native AI Stack              │
├─────────────────────────────────────────────────────┤
│ Infra: Kubernetes, GPU Nodes, Knative               │
│ AI DevOps: Kubeflow, MLflow, Feast, Airflow, Ray    │
│ Serving: KServe, Seldon, NVIDIA Triton, ONNX Runtime│
│ Data: Spark, BigQuery, Delta Lake                   │
│ Observability: Prometheus, Grafana, Evidently AI    │
└─────────────────────────────────────────────────────┘
```
## 🛠️ Tools & Technologies (NOT LIMITED TO STACK ABOVE & BELOW)

### **1. Infrastructure**
- **Kubernetes** → Orchestrates containerized AI workloads.
- **GPU/TPU Scheduling** → `nvidia-device-plugin`, GPU node pools.
- **Serverless for AI** → Knative, AWS Lambda, Google Cloud Run.

### **2. AI/ML DevOps**
- **Kubeflow** → ML pipelines, distributed training, hyperparameter tuning.
- **MLflow** → Experiment tracking & model registry.
- **KServe** → Model serving with autoscaling.
- **Seldon Core** → Multi-model serving & A/B testing.
- **Feast** → Feature store.

### **3. Data Engineering / ETL**
- **Apache Airflow / Argo Workflows** → Pipeline orchestration.
- **Spark on Kubernetes** → Large-scale data processing.
- **Delta Lake / BigQuery / Snowflake** → Data lakes & warehouses.

### **4. Monitoring & Observability**
- **Prometheus + Grafana** → Metrics & dashboards.
- **OpenTelemetry** → Tracing.
- **Evidently AI** → Model drift detection.

### **5. AI Optimization**
- **Ray** → Distributed compute.
- **ONNX Runtime** → Optimized inference.
- **NVIDIA Triton** → High-performance multi-framework inference.

---

## 🔄 Example Workflow

1. **Data Ingestion**
   - Source: Kafka, Pub/Sub, S3 → Store in BigQuery/Delta Lake.

2. **Model Training**
   - Use Kubeflow Pipelines on GPU nodes.
   - Track experiments in MLflow.

3. **Model Serving**
   - Deploy with KServe/Seldon on Kubernetes.
   - Autoscale with KEDA.

4. **Monitoring**
   - Prometheus + Grafana for infrastructure metrics.
   - Evidently AI for accuracy drift.

---

## 📚 Learning Goals in this Repository
- Understand **Cloud Native AI architecture** and principles.
- Build a **GPU-enabled Kubernetes cluster** for AI workloads.
- Create **Kubeflow ML pipelines** for training.
- Deploy and autoscale models using **KServe/Seldon**.
- Implement **monitoring and drift detection**.

---

## 📖 References
- [Kubeflow](https://www.kubeflow.org/)
- [KServe](https://kserve.github.io/website/)
- [MLflow](https://mlflow.org/)
- [Ray](https://www.ray.io/)
- [NVIDIA Triton](https://developer.nvidia.com/nvidia-triton-inference-server)

---

## 🧑‍💻 Author
This repository is maintained by **SANDEEP KUMAR SEERAM** — AI/ML, Cloud, and Kubernetes enthusiast exploring **Cloud Native AI**.

<span style="color:red">This text is red</span>  
<span style="color:blue">This text is blue</span>  
<span style="color:green;font-weight:bold">This is bold green</span>