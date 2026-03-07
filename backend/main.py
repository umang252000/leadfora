from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from agents.lead_agent import find_leads
from dotenv import load_dotenv
from fastapi.responses import FileResponse
from services.export_service import export_leads_to_csv

load_dotenv()

app = FastAPI(title="Leadfora AI Lead Hunter")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class LeadQuery(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "Leadfora Agent Running"}

@app.get("/export-leads")
def export_leads():

    file_path = export_leads_to_csv()

    return FileResponse(
        path=file_path,
        filename="leadfora_leads.csv",
        media_type="text/csv"
    )

@app.post("/search-leads")
async def search_leads(data: LeadQuery):

    result = await find_leads(data.query)

    print("DEBUG RESULT:", result)

    # remove MongoDB ObjectId
    clean_leads = []
    for lead in result["leads"]:
        clean_lead = dict(lead)
        clean_lead.pop("_id", None)
        clean_leads.append(clean_lead)

    return {
        "status": "success",
        "query": data.query,
        "total_leads": len(clean_leads),
        "results": clean_leads,
        "activity": result["activity"]
    }