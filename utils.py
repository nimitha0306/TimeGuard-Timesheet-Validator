import csv
from io import StringIO
from models import TimesheetEntry

def parse_timesheet(csv_content: str):
    rows = []
    reader = csv.DictReader(StringIO(csv_content))
    for row in reader:
        rows.append(
            TimesheetEntry(
                date=row["date"].strip(),
                startTime=row["startTime"].strip(),
                endTime=row["endTime"].strip(),
                project=row["project"].strip(),
            )
        )
    return rows
