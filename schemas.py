from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class ApplicationBase(BaseModel):
    company_name: str
    role: str
    date_applied: date
    status: str
    reminder_date: Optional[datetime] = None

class ApplicationCreate(ApplicationBase):
    pass

class ApplicationUpdate(ApplicationBase):
    pass

class ApplicationResponse(ApplicationBase):
    id: int

    class Config:
        from_attributes = True
