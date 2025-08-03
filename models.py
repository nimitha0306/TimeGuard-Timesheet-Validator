from pydantic import BaseModel
from typing import List

class TimesheetEntry(BaseModel):
    date: str
    startTime: str
    endTime: str
    project: str

class ValidationReport(BaseModel):
    missingEntries: List[TimesheetEntry]
    extraEntries: List[TimesheetEntry]
