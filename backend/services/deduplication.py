def deduplicate_leads(leads):

    unique = {}
    
    for lead in leads:
        
        key = (lead.get("email"), lead.get("linkedin"), lead.get("company"))
        
        if key not in unique:
            unique[key] = lead

    return list(unique.values())