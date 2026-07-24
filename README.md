# FastAPI Application

A simple and high-performance API built with FastAPI, Pydantic, and SQLite for managing tasks via CRUD operations. This project automatically sets up its own relational database upon startup.

# 🛠️ Why SQLite Was Chosen

For this project, **SQLite** was selected as the database engine due to the following advantages:

- **Zero Configuration:** No external server installation or configuration is required.
- **File-Based:** The entire database resides in a single disk file, making it highly portable.
- **Lightweight & Fast:** Ideal for local development, testing environments, and low-traffic applications.
- **Seamless Integration:** Works out-of-the-box with Python's built-in libraries and SQLAlchemy.

---

# 📁 Database Storage Location

The database file is automatically generated and stored locally in the root directory of the project:

- **Filename:** `development.db`
- **Path:** `./development.db`

_Note: This file is typically excluded from version control via `.gitignore` to keep data local to each deployment._

---

# 🛠️ Prerequisites

Before getting started, make sure you have the following installed on your machine:

- [Python 3.10+](https://python.org)
- [Pip](https://pypa.io) (Python package manager)

# 🔧 Installation & Setup

Follow these steps to get your development environment running locally. **The database will be created automatically on the first run.**

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

_(If you don't have a `requirements.txt` file yet, install the core packages manually using: `pip install fastapi uvicorn pydantic sqlalchemy`)_

---

# 🏃 Running the Application

To start the local development server, run the following command:

```bash
uvicorn main:app --reload
```

> 💡 _Note: Replace `main:app` with your entry file name and your FastAPI instance name (e.g., if your file is `routes.py` and your instance is named `router`, run `uvicorn routes:router --reload`)._

The server will start locally at: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

# 📄 Interactive API Documentation

FastAPI automatically generates interactive documentation for your endpoints. Once the server is running, you can access it here:

- **Swagger UI (Interactive Docs):** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc (Alternative Docs):** [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

# 📊 Database Viewer Screenshot

Below is a visualization of the database structure and data using a DB viewer tool (e.g., DBeaver / SQLite Browser):

![Database Viewer](path/to/your/screenshot.png)
_(Note: Replace this placeholder path with the actual location of your screenshot in the repository, e.g., `./assets/db_screenshot.png`)_

---

# 🔍 Example SQL Query Executed

Here is an example of a SQL query used by the API backend to retrieve all completed tasks:

```sql
SELECT id, title, description, is_completed
FROM tasks
WHERE is_completed = 1;
```
