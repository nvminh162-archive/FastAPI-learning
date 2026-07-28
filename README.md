# Book Management

python -m venv venv

venv\Scripts\activate

python -m pip install "fastapi[standard]" sqlalchemy alembic python-multipart

alembic init migrations

uvicorn app.main:app --reload