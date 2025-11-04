# 🚀 MLOPS-Project

A complete **end-to-end MLOps pipeline** for automating the lifecycle of a machine learning model — from data ingestion and preprocessing to model training, versioning, deployment, and monitoring.

---

## 📁 Project Structure

| Folder/File | Description |
|--------------|-------------|
| `.dvc/` | Configuration for data versioning using DVC |
| `.github/workflows/` | CI/CD pipelines for testing and deployment |
| `data/` | Contains raw and processed datasets |
| `k8s/` | Kubernetes manifests for containerized deployment |
| `metrics/` | Model evaluation metrics and logs |
| `models/` | Saved trained model weights |
| `src/` | Core source code (data ingestion, training, evaluation, inference) |
| `Dockerfile` | Docker build configuration |
| `app.py` | Main application entry point (API or service) |
| `params.yaml` | Configurable parameters and hyperparameters |
| `dvc.yaml` / `dvc.lock` | DVC pipeline definition and lock file |
| `requirements.txt` | Python dependencies list |

---

## ✅ Key Features

- **Data Version Control (DVC):** Efficient tracking of datasets and models  
- **CI/CD Integration:** Automated build, test, and deploy pipelines using GitHub Actions  
- **Containerization:** Docker support for consistent environment setup  
- **Scalable Deployment:** Ready-to-use Kubernetes configuration files  
- **Monitoring:** Logs and metrics collection for model evaluation and tracking  
- **Configurable Pipelines:** Parameter management via `params.yaml`

---

## 🧰 Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher  
- Docker  
- Git  
- DVC (`pip install dvc[s3]`)  
- (Optional) Kubernetes or Minikube for deployment  

---

## ⚙️ Installation

```bash
# Clone the repository
git clone https://github.com/Devendhake18/MLOPS-Project.git
cd MLOPS-Project

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required dependencies
pip install -r requirements.txt
```

| Name | PRN Number |
|------|-------------|
| Deven Dhake | 22070126062 | 
| Manan Tandel | 22070126062 | 
| Madhusudan Hasbe | 22070126062| 
