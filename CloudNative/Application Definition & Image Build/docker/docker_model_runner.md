# Docker Model Runner

## What is Docker Model Runner
Docker Model Runner is a **beta feature** in Docker Desktop (version 4.40+) and Docker Engine that allows developers to run, manage, and serve AI models locally using the same Docker workflows they already use for containers.  
Models are packaged as **OCI artifacts**, making them easy to distribute through Docker Hub or other registries.

---

## How it Works

### 1. Native Inference Engine
- Runs a **host-native inference engine** (built on llama.cpp) outside of containers for better performance.
- Loads models into memory when needed and unloads them after inactivity to save system resources.

### 2. Model Packaging & Distribution
- Models are stored as **OCI artifacts**, which can be pulled from Docker Hub or any compatible registry.
- Works with CI/CD pipelines and Docker’s registry ecosystem.

### 3. API Integration & Access
- Provides an **OpenAI-compatible API** for quick integration with existing applications.
- Access methods:
  - Inside containers via `model-runner.docker.internal`
  - From the host via Docker socket
  - Over TCP (e.g., `localhost:12434`) if enabled

### 4. CLI Commands
- `docker model pull` – download a model
- `docker model ls` / `docker model list` – list local models
- `docker model run` – run a model interactively
- `docker model rm` – remove a model

---

## Use Cases

- **Local LLM Development**  
  Build and test large language models locally for faster iteration without incurring cloud costs or risking data exposure.

- **Standardized Workflows**  
  Switch between models using the same commands and structure as containers.

- **Integration with Docker Tools**  
  Works with Docker Compose, Testcontainers, and other Docker ecosystem tools for complex setups.

- **Cross-Platform AI**  
  Supports Apple Silicon (Metal GPU acceleration) and NVIDIA GPUs on Windows (more platforms coming soon).

- **Model Publishing**  
  Share models with your team or publicly by pushing to registries.

---

## Example Workflow

### Step 1: Enable Model Runner
In Docker Desktop:  
`Settings → Features in Development → Beta → Enable Model Runner`  
Restart Docker after enabling.

### Step 2: Pull & Run a Model
```bash
docker model pull ai/smollm2:360M-Q4_K_M
docker model run ai/smollm2:360M-Q4_K_M "Explain Docker in simple terms."

curl http://localhost:12434/engines/llama.cpp/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"ai/smollm2:360M-Q4_K_M","messages":[{"role":"user","content":"Hello!"}]}'
