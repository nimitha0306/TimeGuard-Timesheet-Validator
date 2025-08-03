# TimeGuard-Timesheet-Validator
TimeGuard is a simple Python web app built with FastAPI that checks if an employee’s timesheet entries match calendar events. It helps identify missing hours or extra entries using a web dashboard.

#Features
- Upload timesheet as a CSV file
- Compare entries with calendar data
- Show missing and extra time entries
- Simple browser UI to view results
- REST APIs for integration and testing

#Technologies Used
- Python 3.11
- FastAPI (for backend APIs)
- Uvicorn (ASGI server)
- HTML/CSS (basic UI)
- CSV, JSON (data formats)

#steps
1)Install dependencies(pip install -r requirements.txt)
2)Run the FastAPI server(python -m uvicorn main:app )
3)Then open your browser and go to:(http://localhost:8000)
4)You can also access the API documentation at:(http://localhost:8000/docs)

Project Structure
timeguard/
├── main.py                 # FastAPI application
├── service.py              # Validation logic
├── utils.py                # CSV parser
├── models.py               # Data models
├── static/index.html       # Frontend UI
├── resources/
│   └── sample_timesheet.csv
├── storage/
│   └── mock_calendar.json
├── tests/
│   └── test_validator.py
├── requirements.txt        # Dependencies

#Sample Files
✅ Timesheet CSV
date,startTime,endTime,project
2025-08-01,09:00,11:00,Project A
2025-08-01,14:00,15:00,Project C

#Calendar JSON
{
  "2025-08-01": [
  
    { "startTime": "09:00", "endTime": "11:00", "project": "Project A" },
    { "startTime": "11:30", "endTime": "13:00", "project": "Project B" }
  ] 
}




