from fastapi import FastAPI, UploadFile, File
from fastapi.responses import HTMLResponse
from utils import parse_timesheet
from service import get_validation_report
import uuid

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()

@app.post("/timesheets")
async def upload_timesheet(file: UploadFile = File(...)):
    content = await file.read()
    entries = parse_timesheet(content.decode("utf-8"))
    report = get_validation_report(entries)
    return {"timesheetId": "dummy", "report": report.dict()}

@app.get("/reports/{id}")
async def get_report(id: str):
    return {"missingEntries": [], "extraEntries": []}
