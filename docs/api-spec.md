# Cybercrime Report API

POST /api/report
Purpose: Submit a cybercrime report

Request Fields:
- name
- phone
- email
- incident_type
- description
- incident_date
- location
- evidence_file (optional)

Response:
- report_id
- status
