from fastapi import FastAPI

app = FastAPI()

@app.post("/api/report")
def submit_report():
    return {
        "report_id": "CRV-001",
        "status": "Report submitted successfully"
    }
