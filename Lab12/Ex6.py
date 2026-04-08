# Retrieve mortgage rate data from Hawaii Board of Realtors

import requests
from bs4 import BeautifulSoup

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"

# Get the webpage
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find the mortgage rate table
table = soup.find("table")

# Find all rows in table
rows = table.find_all("tr")

print("Hawaii Mortgage Rates:\n")

# Loop through rows and extract data
for row in rows[1:]:  # Skip header row
    cols = row.find_all("td")
    
    if len(cols) > 0:
        bank = cols[0].text.strip()
        rates = [col.text.strip() for col in cols[1:]]
        
        print("Bank:", bank)
        print("Rates:", rates)
        print()