from fastapi import FastAPI, Query, Path
from pydantic import BaseModel

app = FastAPI()



class Candidate(BaseModel):
    candidate_id: str
    name: str
    email: str
    job_id: str



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
        return {"status": "success",
                "message": f"Here is your application for {company_name}"}

    elif candidate_email:
        return {"status": "success",
                "message": f"Here is your application for {candidate_email}"}

    else:
        return {"status": "success",
                "message": " Here is all of your applications" }
    
@app.put("/applications/{candidate_id}")
def putApplications(
    candidate_id: str = Path(..., description="The ID of the candidate to update"),
    email: str = Query(None, description="New email address"),
    job_id: str = Query(None, description="New job ID")
):
    return {
        "status": "success",
        "message": f"Application for {candidate_id} successfully updated"
    }


