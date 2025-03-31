from sqlalchemy import Column, String, Integer, Float, JSON, DateTime
from .base import BaseModel

class Repository(BaseModel):
    __tablename__ = 'repositories'

    name = Column(String(255), nullable=False)
    full_name = Column(String(255), unique=True, nullable=False)
    description = Column(String(1000))
    html_url = Column(String(255))
    stars = Column(Integer, default=0)
    language_stats = Column(JSON)  # Store language statistics as JSON
    last_analyzed = Column(DateTime)

    def __repr__(self):
        return f"<Repository {self.full_name}>" 