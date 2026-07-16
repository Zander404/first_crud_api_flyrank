# 🚀 FastAPI Application

A simple and high-performance API built with FastAPI and Pydantic.

# 🛠️ Prerequisites

Before getting started, make sure you have the following installed on your machine:

- [Python 3.10+](https://python.org)
- [Pip](https://pypa.io) (Python package manager)

# 🔧 Installation & Setup

Follow these steps to get your development environment running locally:

## 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <PROJECT_FOLDER_NAME>
```

## 2. Create and activate a virtual environment (venv)

On Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows (PowerShell):

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

## 3. Install the dependencies

```bash
pip install -r requirements.txt
```

_(If you don't have a `requirements.txt` file yet, install the core packages manually using: `pip install fastapi uvicorn pydantic`)_

# 🏃 Running the Application

To start the local development server, run the following command:

```bash
uvicorn main:app --reload
```

> 💡 _Note: Replace `main:app` with your entry file name and your FastAPI instance name (e.g., if your file is `routes.py` and your instance is named `router`, run `uvicorn routes:router --reload`)._

The server will start locally at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

# 📄 Interactive API Documentation

FastAPI automatically generates interactive documentation for your endpoints. Once the server is running, you can access it here:

- **Swagger UI (Interactive Docs):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc (Alternative Docs):** [http://localhost:8000/redocs](http://localhost:8000/redocs)
