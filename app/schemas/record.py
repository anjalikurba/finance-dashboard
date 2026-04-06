from pydantic import BaseModel
from datetime import date

class RecordCreate(BaseModel):
    amount: float
    type: str
    category: str
    date: date
    notes: str

class RecordResponse(RecordCreate):
    id: int

    class Config:
        orm_mode = True