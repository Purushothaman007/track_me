from pydantic import BaseModel
from datetime import date
from typing import Optional

class ApplicationBase(BaseModel):
    company_name: str
    role: str
    date_applied: date
    status: str
    reminder_date: Optional[date] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(ApplicationBase):
    pass

class ApplicationResponse(ApplicationBase):
    id: int

    class Config:
        orm_mode = True # Use 'from_attributes' instead of 'orm_mode' if using Pydantic V2
