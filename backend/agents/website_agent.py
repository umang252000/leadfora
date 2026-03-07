from services.tinyfish_client import run_web_agent


async def website_agent(company):

    goal = f"""
    Visit company website: {company}

    Steps:
    1. Open website
    2. Visit about page
    3. Visit team page
    4. Extract leadership

    Return JSON:
    name
    role
    company
    """

    result = await run_web_agent(goal)

    return result