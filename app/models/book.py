from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import func

from app.db.base import Base


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False, unique=True, index=True)
    bio = Column(Text, nullable=True)
    published_year = Column(Integer, nullable=False)

    author_id = Column(
        Integer, ForeignKey("authors.id", ondelete="RESTRICT"), nullable=False
    )
    categories_id = Column(
        Integer, ForeignKey("categories.id", ondelete="RESTRICT"), nullable=False
    )

    cover_image = Column(
        String(255), nullable=True, nullable=False
    )  # save path, static/covers/nvminh162.png

    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationship author & category
    books = relationship("Author", back_populates="books")
    books = relationship("Category", back_populates="books")
