# Book Management

python -m venv venv

venv\Scripts\activate

python -m pip install "fastapi[standard]" sqlalchemy alembic python-multipart

uvicorn app.main:app --reload