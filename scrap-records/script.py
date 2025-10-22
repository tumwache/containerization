import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

# Base URL of ODPC data handlers register (the public listing page)
BASE_URL = "https://www.odpc.go.ke/registered-data-handlers/"

# Storage for all extracted records
records = []

# Function to extract table data from a given page
def extract_page(page_num):
    print(f"Fetching page {page_num}...")
    # The ODPC register loads dynamically, so we mimic DataTables AJAX endpoint
    url = f"https://www.odpc.go.ke/registered-data-handlers/?dtpage={page_num}"
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table")
    if not table:
        print(f"⚠️ No table found on page {page_num}")
        return []

    rows = table.find_all("tr")[1:]  # skip header
    page_records = []

    for row in rows:
        cols = [td.get_text(strip=True) for td in row.find_all("td")]
        if len(cols) >= 6:
            page_records.append({
                "Name": cols[0],
                "Type": cols[1],
                "Current State": cols[2],
                "Registration Number": cols[3],
                "County": cols[4],
                "Country": cols[5],
            })
    return page_records

# Scrape multiple pages
page = 1
while True:
    page_data = extract_page(page)
    if not page_data:
        print("No more data found — stopping.")
        break
    records.extend(page_data)
    page += 1
    time.sleep(2)  # polite delay between requests

# Convert to DataFrame and export to Excel
df = pd.DataFrame(records)
df.to_excel("odpc_registered_data_handlers.xlsx", index=False)

print(f"✅ Done! Extracted {len(df)} entries.")
print("File saved as odpc_registered_data_handlers.xlsx")
