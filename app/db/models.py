from sqlalchemy import Column, String

from app.db.session import Base


class Job(Base):
    __tablename__ = "jobs"

    job_id = Column(String, primary_key=True, index=True)

    query = Column(String, nullable=False)

    status = Column(String, nullable=False)