import json
import pandas as pd

# Keywords to classify the size of the karkhana
BIG_BUSINESS_KEYWORDS = ["pvt", "ltd", "private", "limited", "industries", "group", "corporate", "manufacturing"]
SMALL_BUSINESS_KEYWORDS = ["bhandar", "gruh udyog", "traders", "sweets", "namkeen", "house", "brothers", "snacks"]

def classify_business_size(name):
    name_lower = name.lower()
    
    # Check for big business indicators first
    if any(keyword in name_lower for keyword in BIG_BUSINESS_KEYWORDS):
        return "Big"
        
    # Default to small if no big keywords are found
    return "Small"

def process_uco_leads(json_file_path):
    print(f"Loading scraped data from {json_file_path}...")
    
    try:
        with open(json_file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        print(f"Error: {json_file_path} not found. Please run the Apify scraper first.")
        return
        
    leads = []
    
    for item in data:
        name = item.get("name", "Unknown")
        size = classify_business_size(name)
        
        lead = {
            "Business Name": name,
            "Classification": size,
            "Contact Number": item.get("phone", "N/A"),
            "Address": item.get("address", "N/A"),
            "Platform Source": item.get("platform", "Unknown"),
            "Website/Link": item.get("url", "N/A"),
            "Platform Rating": item.get("rating", "N/A")
        }
        leads.append(lead)
        
    # Convert to a DataFrame for easy viewing and exporting
    df = pd.DataFrame(leads)
    
    if df.empty:
        print("No data found in the JSON file.")
        return

    # Filter to show only Small Karkhanas
    prime_targets = df[df["Classification"] == "Small"]
    
    # Save to CSV
    df.to_csv("kanpur_all_karkhanas.csv", index=False)
    prime_targets.to_csv("kanpur_prime_small_karkhanas.csv", index=False)
    
    print(f"Successfully processed {len(df)} total leads.")
    print(f"Found {len(prime_targets)} small karkhanas ready for UCO deals!")
    print("Exported to 'kanpur_prime_small_karkhanas.csv'")

if __name__ == "__main__":
    process_uco_leads("results.json")
