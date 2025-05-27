from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests
from bs4 import BeautifulSoup
from datetime import date

app = FastAPI()

FATF_SOURCE_URL = "https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/increased-monitoring-february-2025.html"

@app.get("/check")
def check_country(country: str = Query(..., description="Country to check")):
    grey_listed_countries = [
        "Turkey", "South Africa", "Nigeria", "Philippines", "Kenya", "Barbados",
        "Burkina Faso", "Cameroon", "Croatia", "Democratic Republic of the Congo",
        "Haiti", "Jamaica", "Mali", "Mozambique", "Senegal", "South Sudan",
        "Syria", "Tanzania", "Uganda", "United Arab Emirates", "Vietnam", "Yemen"
    ]

    is_greylisted = country.strip().lower() in [c.lower() for c in grey_listed_countries]

    return {
        "country": country,
        "status": "Greylisted" if is_greylisted else "Not Greylisted",
        "last_updated": "2025-02-21",
        "source_url": "https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/increased-monitoring-february-2025.html"
    }

