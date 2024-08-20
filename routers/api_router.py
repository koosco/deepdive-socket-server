from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from config.database import get_db
from repository.memo_repository import MemoRepository

router = APIRouter()


@router.get("/api/memo")
def get_memo(db: Session = Depends(get_db)):
    memo_repo = MemoRepository(db)
    memo = memo_repo.get_memo()
    return {"id": memo.id, "content": memo.content}
