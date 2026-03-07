from database.mongo import leads_collection


def store_leads(leads):

    if not leads:
        return

    leads_collection.insert_many(leads)