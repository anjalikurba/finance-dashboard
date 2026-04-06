from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.record import Record
from app.schemas.record import RecordCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/records")
def create_record(record: RecordCreate, db: Session = Depends(get_db)):
    new_record = Record(**record.dict())
    db.add(new_record)
    db.commit()
    db.refresh(new_record)
    return new_record

@router.get("/records")
def get_records(db: Session = Depends(get_db)):
    return db.query(Record).all()