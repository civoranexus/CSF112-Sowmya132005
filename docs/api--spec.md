# API Specification – Cybercrime Reporting Portal (Citizen Module)

This document defines the initial backend API endpoints required for the
cybercrime reporting system. These APIs are part of the backend skeleton
and will be enhanced in later phases.

---

# 1. Submit Cybercrime Report

**Endpoint:** `/api/report`  
**Method:** POST  

# Description
Allows a citizen to submit a cybercrime complaint with basic incident details.

# Request Body
```json
{
  "name": "string",
  "phone": "string",
  "incident_type": "string",
  "description": "string"
}
