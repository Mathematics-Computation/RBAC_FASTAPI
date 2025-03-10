

# **RBAC API with FastAPI, Alembic & PostgreSQL**  

This project implements a **Role-Based Access Control (RBAC) API** using **FastAPI**, **SQLAlchemy**, **Alembic**, and **PostgreSQL** (hosted on Neon). It follows best practices for database migrations and version control using Alembic.  

## **Features**  
- User authentication & role management  
- Database migrations with Alembic  
- Integration with a remote **PostgreSQL database on Neon**  
- CRUD operations for users, roles, and permissions  

---

## **Setup & Installation**  

### 1 **Clone the Repository**  
```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2 **Set Up a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3 **Install Dependencies**  
```bash
pip install -r requirements.txt
```

### 4 **Set Up Environment Variables**  
Create a `.env` file and add your **Neon PostgreSQL database URL**:  
```
DATABASE_URL=postgresql+asyncpg://user:password@neon-database-url/dbname
```

---

##  **Database Migrations with Alembic**  

### **Initialize Alembic**  
If not already set up:  
```bash
alembic init alembic
```

### **Configure `alembic/env.py`**  
Modify `alembic/env.py` to use environment variables:
```python
import os
from dotenv import load_dotenv
from sqlalchemy import engine_from_config, pool
from alembic import context
from models import Base

load_dotenv()
config = context.config
db_url = os.environ.get("DATABASE_URL")
if db_url:
    config.set_main_option("sqlalchemy.url", db_url)

target_metadata = Base.metadata
```

### **Generate and Apply Migrations**  
#### **1 Create Migration Script**  
```bash
alembic revision --autogenerate -m "Initial migration"
```
#### **2 Apply Migrations to the Database**  
```bash
alembic upgrade head
```
This ensures your PostgreSQL database schema is up-to-date.

---

##  **Running the API**  
```bash
uvicorn main:app --reload
```
The API will be available at:  
 **http://127.0.0.1:8000/docs** (Swagger UI)

---


## **Key Learnings & Takeaways**  
This project demonstrates:  
 **Database Migrations** with Alembic  
 **PostgreSQL Connection** with a remote Neon database  
 **FastAPI for REST API Development**  
 **Environment Variables for Secure Configurations**  

---

## **Future Enhancements**  
- Implement JWT-based authentication  
- Add unit tests for API endpoints  
- Improve error handling  

---


