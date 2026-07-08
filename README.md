# Python Web Service on EKS
This repository contains a lightweight Python application containerized for deployment on Amazon EKS.
## Prerequisites
 * Docker installed
 * AWS CLI configured with appropriate permissions
 * kubectl installed
 * An existing EKS Cluster
## Getting Started
### 1. Local Development
To run the application locally:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py

```
### 2. Build and Push to ECR
 1. Authenticate to your ECR registry:
   ```bash
   aws ecr get-login-password --region <REGION> | docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com
   
   ```
 2. Build the image:
   ```bash
   docker build -t <REPO_NAME> .
   
   ```
 3. Tag and Push:
   ```bash
   docker tag <REPO_NAME>:latest <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/<REPO_NAME>:latest
   docker push <ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/<REPO_NAME>:latest
   
   ```
### 3. Deploy to EKS
Ensure your kubectl is pointed to your cluster:
```bash
aws eks update-kubeconfig --name <CLUSTER_NAME>

```
Apply the Kubernetes manifests:
```bash
kubectl apply -f k8s/

```
### 4. Verification
Check the status of your deployment:
```bash
kubectl get pods
kubectl get svc
