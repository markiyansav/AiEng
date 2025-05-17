from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

# This is our data model - what an application looks like
class Candidate(BaseModel):
    candidate_id: str
    name: str
    email: str
    job_id: str

# This is our "database" - just a list in memory
applications: List[Candidate] = []


# @app.get("/")
# def read_root():
#     return {"message": "Welcome to the Age Calculator API"}


# @app.post("/application")
# def postApplication():
#     return {"message": "Application submitted successfully"} 

# @app.post("/apply/{candidate_id}")
# def applyForCandidate(candidate_id: int):
#     return {
#         "status": "success",
#         "message": f"Application for candidateID: {candidate_id} successfully submitted"}
    

@app.post("/applications")
def postApplications(candidate: Candidate):
    applications.append(candidate)
    return {
        "status": "success",
        "message": f"Application submitted for {candidate.name}"
    }

@app.get("/applications")
def getApplication(
    company_name: str = Query(None, description="optional query param for company name"),
    candidate_email: str = Query(None, description="optional query param for candidate email")
):
    if company_name:
        return {
            "status": "success",
            "message": f"Here is your application for {company_name}"
        }
    elif candidate_email:
        return {
            "status": "success",
            "message": f"Here is your application for {candidate_email}"
        }
    else:
        return {
            "status": "success",
            "message": "Here are all of your applications"
        }

@app.get("/applications/{candidate_id}")
def getApplicationById(candidate_id: str):
    for app in applications:
        if app.candidate_id == candidate_id:
            return {
                "status": "success",
                "message": f"Application found for candidate ID: {candidate_id}"
            }
    return {
        "status": "success",
        "message": "Application not found"
    }

@app.put("/applications/{candidate_id}")
def putApplications(
    candidate_id: str = Path(..., description="The ID of the candidate to update"),
    email: str = Query(None, description="New email address"),
    job_id: str = Query(None, description="New job ID")
):
    for app in applications:
        if app.candidate_id == candidate_id:
            if email:
                app.email = email
                return {
                    "status": "success",
                    "message": f"Email updated to {email}"
                }
            if job_id:
                app.job_id = job_id
                return {
                    "status": "success",
                    "message": f"Job ID updated to {job_id}"
                }
    return {
        "status": "success",
        "message": "Application not found"
    }

@app.delete("/applications/{candidate_id}")
def deleteApplication(candidate_id: str):
    for i, app in enumerate(applications):
        if app.candidate_id == candidate_id:
            applications.pop(i)
            return {
                "status": "success",
                "message": f"Application for {candidate_id} has been deleted"
            }
    return {
        "status": "success",
        "message": "Application not found"
    }
