# Multi-Platform Namkeen Manufacturers Scraper for Kanpur

This repository contains a robust workflow to scrape Namkeen manufacturers from platforms like **IndiaMart** and **JustDial** (using Apify actors). It classifies them into **Small** and **Big** businesses, exporting the highly approachable small-business leads to a CSV for UCO outreach.

## Files
- `results.json` – Combined output from the Apify actors (replace with real data).
- `process_uco.py` – Python script that handles the data processing, filtering, and CSV generation.
- `kanpur_all_karkhanas.csv` – All scraped leads (auto-generated).
- `kanpur_prime_small_karkhanas.csv` – Only the small-business targets (auto-generated).

## Usage
1. **Run the Apify Actors via Roo Code**
   Use Roo Code to run both an IndiaMart scraper and a JustDial scraper. Format their combined output into the `results.json` file.
2. **Install Dependencies**
   ```bash
   pip install pandas
