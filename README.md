# Namkeen Manufacturers Scraper for Kanpur

This repository contains a simple workflow to scrape Namkeen manufacturers from IndiaMart (using an Apify actor), classify them into **Small** and **Big** businesses, and export the small‑business leads to CSV for outreach.

## Files
- `results.json` – Sample output from the Apify actor (replace with real data).
- `process_uco.py` – Python script that classifies businesses based on name keywords and writes two CSV files:
  - `kanpur_all_karkhanas.csv` – All scraped leads.
  - `kanpur_prime_small_karkhanas.csv` – Only the small‑business targets.
- `README.md` – This documentation.

## Usage
1. **Run the Apify actor** (replace with your own API token if needed):
   ```bash
   apify run natanielsantos/indiamart-scraper --input-file input.json
   ```
   The actor will produce a JSON file (e.g., `results.json`).
2. **Install dependencies**:
   ```bash
   python -m pip install pandas
   ```
3. **Process the data**:
   ```bash
   python process_uco.py
   ```
   The script reads `results.json`, classifies each entry, and creates the CSV files.

## Classification Logic
- **Big business** keywords: `pvt`, `ltd`, `private`, `limited`, `industries`, `group`, `corporate`, `manufacturing`.
- **Small business** keywords: `bhandar`, `gruh udyog`, `traders`, `sweets`, `namkeen`, `house`, `brothers`.
  If a name contains any big‑business keyword it is marked **Big**; otherwise it defaults to **Small**.

## License
This project is open‑source and released under the MIT License.
