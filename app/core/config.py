from pydantic import BaseModel

class Setting(BaseModel):
    PROJECT_NAME: str = "Book Management API"
    SQLALCHEMY_DATABASE_URL: str = (
        "mysql+pymysql://fastapi_user:fastapi_password@localhost:33067/fastapi_books"
    )

settings = Setting()
