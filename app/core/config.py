from pydantic import BaseModel

class Setting(BaseModel):
    PROJECT_NAME: str = "Book Management API"
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///.app.db"

settings = Setting()