from typing import Type

from sqlalchemy.orm import Session

from config.database import get_db
from repository.models import Memo


class MemoRepository:
    def __init__(self, db: Session):
        self.db = db

    def save(self, title: str, content: str) -> Memo:
        memo = Memo(title=title, content=content)
        self.db.add(memo)
        self.db.commit()
        self.db.refresh(memo)

        return memo

    def get_memo(self) -> Type[Memo] | None:
        return self.db.query(Memo).first()


if __name__ == '__main__':
    repo = MemoRepository(get_db())
    repo.save('title1', 'content1')
