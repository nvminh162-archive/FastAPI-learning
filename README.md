# Book Management

python -m venv venv

venv\Scripts\activate

python -m pip install "fastapi[standard]" sqlalchemy alembic pymysql python-multipart

alembic init migrations
docker compose up -d
alembic revision --autogenerate -m "init tables"
alembic upgrade head

uvicorn app.main:app --reload

```
Host: localhost
Port: 33067
Database: fastapi_books
User: fastapi_user
Password: fastapi_password
```