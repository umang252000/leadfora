import os
import httpx
from dotenv import load_dotenv

load_dotenv()

TINYFISH_API_KEY = os.getenv("TINYFISH_API_KEY")

TINYFISH_URL = "https://agent.tinyfish.ai/v1/automation/run"


async def run_web_agent(goal: str):

    payload = {
        "url": "https://tinyfish.ai",
        "goal": goal
    }

    headers = {
        "X-API-Key": TINYFISH_API_KEY,
        "Content-Type": "application/json"
    }

    try:

        async with httpx.AsyncClient(timeout=180) as client:

            response = await client.post(
                TINYFISH_URL,
                json=payload,
                headers=headers
            )

            response.raise_for_status()

            return response.json()

    except httpx.ReadTimeout:
        return {"error": "TinyFish request timeout"}

    except Exception as e:
        return {"error": str(e)}