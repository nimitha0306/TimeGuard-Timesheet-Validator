import json
from models import TimesheetEntry, ValidationReport
from typing import List

def read_calendar(file_path="storage/mock_calendar.json"):
    with open(file_path, 'r') as f:
        return json.load(f)

def is_match(a: TimesheetEntry, b: TimesheetEntry):
    return (
        a.date == b.date
        and a.startTime == b.startTime
        and a.endTime == b.endTime
        and a.project.strip().lower() == b.project.strip().lower()
    )

def get_validation_report(timesheet_entries: List[TimesheetEntry]):
    calendar = read_calendar()
    cal_entries = []
    for date, slots in calendar.items():
        for e in slots:
            cal_entries.append(TimesheetEntry(date=date, **e))

    missing = [e for e in cal_entries if not any(is_match(e, t) for t in timesheet_entries)]
    extra = [t for t in timesheet_entries if not any(is_match(t, c) for c in cal_entries)]

    return ValidationReport(missingEntries=missing, extraEntries=extra)
