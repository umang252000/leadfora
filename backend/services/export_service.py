import csv
from database.mongo import leads_collection


def export_leads_to_csv():

    leads = list(leads_collection.find({}, {"_id": 0}))

    file_path = "leads.csv"

    if not leads:
        return file_path

    keys = leads[0].keys()

    with open(file_path, "w", newline="") as f:

        writer = csv.DictWriter(f, fieldnames=keys)

        writer.writeheader()

        writer.writerows(leads)

    return file_path