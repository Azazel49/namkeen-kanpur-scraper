import json
import pandas as pd

BIG_BUSINESS_KEYWORDS = ["pvt", "ltd", "private", "limited", "industries", "group", "corporate", "manufacturing"]
SMALL_BUSINESS_KEYWORDS = ["bhandar", "gruh udyog", "traders", "sweets", "namkeen", "house", "brothers"]

def classify_business_size(name):
    name_lower = name.lower()
    if any(keyword in name_lower for keyword in BIG_BUSINESS_KEYWORDS):
        return "Big"
    return "Small"

def process_uco_leads(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    leads = []
    for item in data:
        name = item.get("name", "Unknown")
        size = classify_business_size(name)
        lead = {
            "Business Name": name,
            "Classification": size,
            "Contact Number": item.get("phone", "N/A"),
            "Address": item.get("address", "N/A"),
            "Website/Link": item.get("url", "N/A"),
            "Platform Rating": item.get("rating", "N/A")
        }
        leads.append(lead)
    df = pd.DataFrame(leads)
    prime_targets = df[df["Classification"] == "Small"]
    df.to_csv("kanpur_all_karkhanas.csv", index=False)
    prime_targets.to_csv("kanpur_prime_small_karkhanas.csv", index=False)
    print(f"Processed {len(df)} leads, {len(prime_targets)} small targets.")

if __name__ == "__main__":
    process_uco_leads("results.json")
