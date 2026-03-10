# 🌩️ AWS-Resume-Analyzer

### Intelligent Resume Analysis using AWS + MLOps + DevOps

Detect • Analyze • Score • Recommend
AI-Powered Resume Evaluation using **SageMaker Inference**

---

## 🚀 Project Overview

Cloud Resume Analyzer is a cloud-native ML-powered system designed to evaluate resumes against job descriptions and generate intelligent insights.

The system uses Natural Language Processing and Machine Learning deployed on AWS SageMaker to analyze resumes and provide:

• Resume Score
• Skill Matching Percentage
• Missing Skills Detection
• Improvement Recommendations

This project demonstrates real-world Cloud + DevOps + MLOps engineering, combining scalable infrastructure, ML inference, and automated deployment pipelines.

---

## 🎯 Problem It Solves

In modern recruitment workflows:

• Recruiters manually screen thousands of resumes
• Resume-job matching is time consuming
• Skill gaps are difficult to identify quickly
• Candidates lack feedback on resume quality

This platform automates resume evaluation using AI-driven analysis and cloud scalability.

---

## 🧠 Key Capabilities

✔ Resume Parsing & NLP Processing
✔ Job Description Matching
✔ Resume Scoring Engine
✔ Skill Gap Detection
✔ ML Inference via SageMaker
✔ Cloud-native architecture
✔ Dockerized backend services
✔ Infrastructure as Code using Terraform
✔ Automated CI/CD pipeline

---

# ☁️ System Architecture

The platform supports two deployment architectures to demonstrate different cloud deployment models.

---

# 🖥️ Architecture 1 — EC2 Compute Architecture

Backend API runs inside Docker containers on EC2.

```
Client
 ↓
EC2 Instance
 ↓
Docker Container
 ↓
FastAPI Backend
 ↓
SageMaker Endpoint
 ↓
ML Resume Analyzer
 ↓
DynamoDB
```

### Workflow

1. User uploads resume and job description
2. FastAPI backend processes input
3. Resume data sent to SageMaker endpoint
4. ML model evaluates resume
5. Results stored in DynamoDB

---

# 🌍 Architecture 2 — CDN + Static Frontend

Frontend is hosted on S3 + CloudFront CDN while backend runs on EC2.

```
User
 ↓
CloudFront CDN
 ↓
S3 Static Frontend
 ↓
FastAPI API (EC2)
 ↓
SageMaker Endpoint
 ↓
ML Resume Analyzer
 ↓
DynamoDB
```

### Workflow

1. User accesses web interface via CDN
2. Static frontend served from S3
3. Frontend sends API request to FastAPI
4. Backend invokes SageMaker model
5. Results stored in DynamoDB

---

# 🤖 Machine Learning Layer

The ML model is deployed using AWS SageMaker Endpoint.

### Responsibilities

• Resume Parsing
• Skill Extraction
• Job Matching
• Resume Scoring
• Recommendation Generation

Both architectures interact with the same centralized ML inference endpoint.

---

# ⚙️ Infrastructure as Code

Infrastructure provisioning is managed using Terraform.

Terraform automates deployment of:

• EC2 Instances
• S3 Buckets
• CloudFront CDN
• DynamoDB Tables
• IAM Roles & Policies

This ensures repeatable and scalable infrastructure deployment.

---

# 🔄 CI/CD Pipeline

The project includes a GitHub Actions CI/CD pipeline.

### Pipeline Flow

```
Developer Push
     ↓
GitHub Actions
     ↓
Build Docker Image
     ↓
Terraform Infrastructure Deployment
     ↓
Application Deployment
```

This implements a complete DevOps automation workflow.

---

# 📂 Project Structure

```
AWS-Resume-Analyzer
│
├── .github/workflows
│   └── ci-cd.yml
│
├── app
│   ├── api
│   │   ├── analyze.py
│   │   ├── history.py
│   │   └── upload.py
│   │
│   ├── models
│   │   ├── jd_parser.py
│   │   └── resume_parser.py
│   │
│   ├── services
│   │   ├── dynamodb_service.py
│   │   ├── matching.py
│   │   ├── nlp_engine.py
│   │   ├── preprocessing.py
│   │   ├── recommendations.py
│   │   ├── s3_service.py
│   │   ├── sagemaker_service.py
│   │   └── scoring.py
│   │
│   ├── utils
│   │   ├── file_utils.py
│   │   └── text_utils.py
│   │
│   ├── config.py
│   ├── main.py
│   └── requirements.txt
│
├── deploy
│   ├── docker
│   │   ├── Dockerfile
│   │   └── docker-compose.yml
│   │
│   └── scripts
│       ├── deploy.sh
│       ├── start.sh
│       └── entrypoint.sh
│
├── frontend
│   ├── public
│   │   └── index.html
│   ├── src
│   └── package.json
│
├── infra
│   ├── iam
│   │   └── iam_policies.json
│   │
│   └── terraform
│       ├── backend.tf
│       ├── main.tf
│       ├── provider.tf
│       ├── variables.tf
│       └── outputs.tf
│
├── ml
│   └── sagemaker
│       ├── deploy_endpoint.py
│       ├── inference.py
│       ├── model.tar.gz
│       └── requirements.txt
│
├── temp_uploads
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

---

# 🛠️ Technologies Used

### Cloud

• AWS EC2
• AWS S3
• AWS CloudFront
• AWS DynamoDB
• AWS SageMaker

### DevOps

• Docker
• Terraform
• GitHub Actions

### Backend

• Python
• FastAPI
• NLP Processing

### Frontend

• HTML

---

# 🌟 Future Improvements

• User authentication system
• Kubernetes deployment
• Automated ML retraining pipeline
• Advanced resume analytics dashboard

---

# 👨‍💻 Author
Aditya Banerjee
B.Tech CSE — Cloud & DevOps Engineer
Focused on AWS • DevOps •FinOps • Intelligent Automation

---
## 📜 License

MIT License

---
⭐ This project demonstrates real-world cloud architecture by integrating AWS services, DevOps automation, and MLOps-based AI inference into a scalable production-style system.
