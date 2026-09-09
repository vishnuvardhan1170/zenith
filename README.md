# Enterprise-Grade Flask & MongoDB Kubernetes Cluster

A highly available, production-ready microservices architecture showcasing advanced DevOps engineering. This repository deploys a Python Flask web application tightly coupled with a MongoDB backend and Mongo-Express administrative dashboard, orchestrated entirely within Kubernetes.

## Project Highlights
**Automated Kubernetes Orchestration:** Production-grade Deployment and Service manifests utilizing precise readiness/liveness probes for self-healing infrastructure.

**Secure State & Configuration Management:** Zero-cleartext secrets utilizing Kubernetes Secret objects and injected environmental contexts.

**Persistent Storage Lifecycles:** Zero-data-loss database layer via PersistentVolumeClaim (PVC) bindings ensuring storage state survives pod lifecycles.

**Optimized Containerization:** Multi-stage Dockerfile configurations designed to minimize attack surfaces and image footprints.

## Quick Start & Deployment Blueprint

### 1. Provision Persistent Storage Layer
```bash
kubectl apply -f k8s/mongo-data-pvc.yaml
```
### 2. Deploy Applications & Database Workloads
```bash
kubectl apply -f k8s/
```
### 3. To Verify the Pods
```bash
kubectl get pods
```
### 4. Stop the Deployments and Services
```bash
kubectl delete -f k8s/
```

## Deploy using Docker Compose

### 1. Launch the Stack
Run the following command from the root directory of the repository:
```bash
docker-compose up -d
```

### 2. Verify Running Containers
Check that all three services are up and healthy:
```bash
docker-compose ps
```

### 3. To Stop & Remove the Containers
To stop the application and completely remove the containers while preserving your data volumes, run:
```bash
docker-compose down
```
