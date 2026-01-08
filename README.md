# US President Lookup App

A sleek, containerized web application built with **Flask** and designed for **Google Cloud Run**. 
This app demonstrates how to build, containerize, and deploy a Python application that allows users to look up US Presidents by their order of office.

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0-green?style=for-the-badge&logo=flask)
![Google Cloud Run](https://img.shields.io/badge/Google_Cloud-Run-4285F4?style=for-the-badge&logo=google-cloud)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?style=for-the-badge&logo=docker)

## ✨ Features

-   **Interactive UI**: Clean, responsive HTML5/CSS3 interface.
-   **Instant Lookup**: Enter a number (1-47) to get the President's name.
-   **Production Ready**: Uses `gunicorn` for robust handling of requests.
-   **Cloud Native**: Fully containerized with Docker, optimized for Cloud Run.
-   **Observability**: Structured logging for seamless integration with Cloud Logging.

## 🚀 Quick Start

### Run Locally

1.  **Clone the repository**
    ```bash
    git clone https://github.com/pankajberkeleyhaas/us-president-lookup.git
    cd us-president-lookup
    ```

2.  **Install dependencies**
    ```bash
    cd app
    pip install -r requirements.txt
    ```

3.  **Run the app**
    ```bash
    python main.py
    ```

4.  **Open in Browser**
    Visit `http://localhost:8080` to see it in action!

### 🐳 Run with Docker

```bash
cd app
docker build -t president-lookup .
docker run -p 8080:8080 president-lookup
```

## 🎮 Usage Examples

### Web Interface
Simply enter a number in the box and hit "Lookup".

-   **Input**: `1`
-   **Output**: `George Washington`

-   **Input**: `16`
-   **Output**: `Abraham Lincoln`

-   **Input**: `44`
-   **Output**: `Barack Obama`

### API Usage
You can also use `curl` to interact with the backend:

```bash
curl -X POST -d "number=16" http://localhost:8080/
```
**Response**: HTML content containing "Abraham Lincoln".

## ☁️ Deploy to Google Cloud Run

Deploy this app to the cloud in one command!

```bash
# 1. Set your Project ID
export GOOGLE_CLOUD_PROJECT="your-project-id"

# 2. Build via Cloud Build
cd app
gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/president-lookup

# 3. Deploy to Cloud Run
gcloud run deploy president-lookup \
    --image gcr.io/$GOOGLE_CLOUD_PROJECT/president-lookup \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated
```

## 📂 Project Structure

```
├── app/
│   ├── main.py              # Flask Application Logic
│   ├── templates/
│   │   └── index.html       # Frontend Interface
│   ├── Dockerfile           # Container Configuration
│   └── requirements.txt     # Python Dependencies
├── .gitignore
└── README.md                # Documentation
```

---
*Built for the Cloud. Deployed with ease.*
