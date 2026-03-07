from services.tinyfish_client import run_web_agent


async def linkedin_agent(query):

    goal = f"""
    Find LinkedIn company pages for: {query}

    Return JSON format:
    {{
      "leads": [
        {{
          "company": "",
          "website": "",
          "linkedin": ""
        }}
      ]
    }}
    """

    response = await run_web_agent(goal)

    if not response:
        return []

    result = response.get("result", {})

    leads = result.get("leads", [])

    return leads