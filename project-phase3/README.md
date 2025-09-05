# ⚙️ Final DevOps Project – Phase 3


Welcome to my Phase 3 Final DevOps Project!  
The goal was to build a **complete CI/CD pipeline** for a simple Flask application, deploying it all the way to Kubernetes using Jenkins, Docker, and Helm.  

---

## 🧩 What’s Inside?
- **Flask App** – with endpoints:
  - `/` – home  
  - `/health/live` – Liveness check  
  - `/health/ready` – Readiness check  
- **Docker** – containerizes the app  
- **Kubernetes + Minikube** – runs the container in a cluster  
- **Helm** – manages deployment and service  
- **Jenkins** – automates the flow: Build → Push → Deploy → Test  

---

## 📂 Pipeline Stages
1. **Checkout** – pull code from GitHub  
2. **Build & Push** – build Docker image & push to DockerHub *(only if app code changes)*  
3. **Deploy with Helm** – install/upgrade the release *(also redeploys if Helm chart changes)*  
4. **Test Service** – verify rollout status and service availability  

---

## 🔄 Pipeline Flow

```text
   GitHub Commit
        │
        ▼
   [ Jenkins ]
        │
 ┌──────┴─────────┐
 │  Checkout Code │
 └──────┬─────────┘
        ▼
   Build & Push Docker Image
        │
        ▼
    Deploy with Helm
        │
        ▼
   Test Rollout & Service
        │
        ▼
   ✅ Running Flask App on Kubernetes
```

---

## 🔍 Run the App
Get the service URL from Minikube:
```bash
minikube service myflaskapp-mychart --url
```

Open the URL in your browser → you should see:  
```
Hello, World!
```

