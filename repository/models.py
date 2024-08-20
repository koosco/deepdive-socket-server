from sqlalchemy import Column, String, BigInteger, ForeignKey, TIMESTAMP, text, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Memo(Base):
    __tablename__ = 'memo'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text)
    voice_file_url = Column(String(255))
    summary_content = Column(Text)
