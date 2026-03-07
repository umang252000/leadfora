def score_lead(lead):

    score = 0

    role = (lead.get("role") or "").lower()
    company = (lead.get("company") or "").lower()

    # Decision makers score higher
    if "ceo" in role:
        score += 40

    if "cto" in role:
        score += 35

    if "founder" in role:
        score += 40

    if "vp" in role:
        score += 30

    if "director" in role:
        score += 25

    # Company relevance boost
    if "ai" in company:
        score += 20

    if "tech" in company:
        score += 10

    # Email bonus
    if lead.get("email"):
        score += 10

    return score


def score_leads(leads):

    for lead in leads:

        score = score_lead(lead)

        lead["score"] = score

        if score > 70:
            lead["priority"] = "High"

        elif score > 40:
            lead["priority"] = "Medium"

        else:
            lead["priority"] = "Low"

    return leads