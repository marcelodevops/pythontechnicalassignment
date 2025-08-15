# Merck technical assignment Documentation

---

# Technical assignment: You are tasked with creaGng a simplified cloud-based applicaGon deployment pipeline using GitHub AcGons and AWS services.


  
### Description
I developed a CI/CD pipeline for a containerized Python application using GitHub Actions, Docker, AWS ECR, AWS ECS, AWS Cloudformation. 

### Requirements
- You will create a basic Python REST API and deploy it to AWS using a CI/CD pipeline.
- The REST API shall have at least two endpoints, one for checking the applicaGon health and one
to retrieve (dummy) data and shall require authenGcaGon.
- The applicaGon should be containerized using Docker. Please use the AWS Free Tier, and GitHub
repositories as applicable.
- Please use AWS CDK or CloudFormaGon to define the infrastructure.
- Write tests where relevant and follow market standard pracGces.
- Ensure to document the code and your approach to the soluGon.

### Acceptance Criteria
- A functional GitHub Actions pipeline that builds, tests, and deploys python app and infrasturture.
- Successful deployment of the Dockerized application to AWS ECS.
- Test and security scans are performed as part of the pipeline.
- `/healthcheck` endpoint to check application health status.
- Complete documentation.

---


---

## Prerequisites

Before beginning, ensure you have:
1. GitHub Repository for version control and triggering the pipeline.
2. AWS Account with permissions for ECR and ECS.
3. AWS CLI configured on your local machine.
4. VS Code or any text editor of choice.

---

## Key Technologies & Tools

- **GitHub Actions**: For CI/CD, including building, testing, security scanning, and deployment.
- **AWS Cloudformation**: For provisioning EKS and related resources.
- **AWS ECR**: As the Docker image registry.
- **AWS ECS**: To deploy the containerized application in a Kubernetes cluster.
- **Docker**: For containerizing the Python application.
- **Security Tools**: Trivy, Bandit, and Safety for scanning code and Docker images for vulnerabilities.

---

## Repository Structure

```
.
├── .github/
│   └── workflows/
│       └── cicd.yaml
├── cloudformation-templates/
│   ├── infrastructure.yaml
│   └── service.yaml
├── templates/
│   └── login.html
│   └── base.html
├── tests/
│   └── test_app.py
├── app.py
└── Dockerfile
└── Requirements.txt
└── README.md
```

