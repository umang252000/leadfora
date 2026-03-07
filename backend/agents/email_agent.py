from services.tinyfish_client import run_web_agent


async def email_agent(company):

    goal = f"""
    Find email contacts for company: {company}

    Steps:
    1. Visit contact page
    2. Visit team page
    3. Extract public email addresses

    Return JSON:
    name
    email
    company
    """

    result = await run_web_agent(goal)

    return result