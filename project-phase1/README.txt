Final DevOps Project.

Overview:
This project deploys a Flask app on Kubernetes.
It includes:
- Docker image creation
- Deployment, Service, ConfigMap, CronJob, and HPA
- All steps tested and working

How to build Docker image:
docker build -t stas696970/my_python_image:v2 .
docker push stas696970/my_python_image:v2

How to apply Kubernetes manifests:
sudo k3s kubectl apply -f configmap.yaml
sudo k3s kubectl apply -f deployment.yaml
sudo k3s kubectl apply -f service.yaml
sudo k3s kubectl apply -f cronjob.yaml
sudo k3s kubectl apply -f hpa.yaml

How to check:
sudo k3s kubectl get pods
sudo k3s kubectl get svc
sudo k3s kubectl get cronjob
sudo k3s kubectl get hpa

Open the app in browser:
http://172.20.202.222:30001

Author:
Stas genkin

