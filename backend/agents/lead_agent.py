import asyncio

from agents.linkedin_agent import linkedin_agent
from agents.crunchbase_agent import crunchbase_agent
from services.lead_scoring import score_leads
from services.deduplication import deduplicate_leads
from services.lead_storage import store_leads


async def find_leads(query: str):

    activity = []

    activity.append("Query received")

    # Start agents
    activity.append("LinkedIn Agent searching profiles")
    linkedin_task = linkedin_agent(query)

    activity.append("Crunchbase Agent discovering companies")
    crunchbase_task = crunchbase_agent(query)

    try:
        results = await asyncio.gather(
            linkedin_task,
            crunchbase_task
        )

    except Exception as e:
        return {
            "leads": [],
            "activity": activity + [f"Agent error: {str(e)}"]
        }

    linkedin_results = results[0]
    crunchbase_results = results[1]

    all_leads = []

    if isinstance(linkedin_results, list):
        all_leads.extend(linkedin_results)

    if isinstance(crunchbase_results, list):
        all_leads.extend(crunchbase_results)

    activity.append("Deduplicating leads")

    unique_leads = deduplicate_leads(all_leads)

    # 👉 If agents return nothing → use demo dataset
    if not unique_leads:

        activity.append("No leads found. Using demo dataset")

        unique_leads = [
            {
                "name": "Jonas Weber",
                "role": "AI Engineer",
                "company": "Aleph Alpha",
                "email": "jonas@aleph-alpha.com"
            },
            {
                "name": "Anna Fischer",
                "role": "ML Researcher",
                "company": "DeepL",
                "email": "anna@deepl.com"
            },
            {
                "name": "Lukas Schmidt",
                "role": "Data Scientist",
                "company": "Celonis",
                "email": "lukas@celonis.com"
            },
            {
                "name": "Mia Hoffmann",
                "role": "AI Product Manager",
                "company": "Black Forest Labs",
                "email": "mia@blackforestlabs.ai"
            },
            {
                "name": "David Klein",
                "role": "AI Developer",
                "company": "Aleph AI",
                "email": "david@aleph-ai.com"
            }
        ]

    activity.append("Scoring leads with AI")

    scored_leads = score_leads(unique_leads)

    activity.append("Saving leads to database")

    try:
        store_leads(scored_leads)
    except Exception:
        activity.append("Database storage skipped")

    activity.append("Workflow complete — leads ready")

    return {
        "leads": scored_leads,
        "activity": activity
    }