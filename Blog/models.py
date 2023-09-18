from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from .database import Base
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__ = "blogs"
    id = Column(Integer, primary_key=True, index=True)
    title: Mapped[str] = mapped_column()
    body: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    creator = relationship("User", back_populates="blogs")


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    blogs = relationship("Blog", back_populates="creator")
