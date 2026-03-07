from services.tinyfish_client import run_web_agent


async def crunchbase_agent(query):

    goal = f"""
    Find companies on Crunchbase related to: {query}

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