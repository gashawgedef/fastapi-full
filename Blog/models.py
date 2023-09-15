from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship ,Mapped,mapped_column

from .database import Base


class Blog(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    title:  Mapped[str] = mapped_column()
    body:  Mapped[str] = mapped_column()