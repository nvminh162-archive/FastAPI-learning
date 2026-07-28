# Book Management

python -m venv venv

venv\Scripts\activate

python -m pip install "fastapi[standard]" sqlalchemy alembic python-multipart

alembic init migrations
alembic revision --autogenerate -m "init tables"
alemic upgrade head

uvicorn app.main:app --reload