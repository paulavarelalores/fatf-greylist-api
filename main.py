from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
import requests
from bs4 import BeautifulSoup
from datetime import date

app = FastAPI()

FATF_SOURCE_URL = "https://www.fatf-gafi.org/en/publications/High-risk-and-other-monitored-jurisdictions/increased-monitoring-february-2025.html"

@app.get("/check")
def check_country(country: str = Query(..., description="Country to check")):
    try:
        response = requests.get(FATF_SOURCE_URL)
        if response.status_code != 200:
            return JSONResponse(
                status_code=500,
                content={"error": "Failed to fetch FATF data."}
            )

        content = response.text.lower()
        is_greylisted = country.lower() in content

        return {
            "country": country,
            "status": "Greylisted" if is_greylisted else "Not Greylisted",
            "last_updated": "2025-02-21",
            "source_url": FATF_SOURCE_URL
        }

    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": str(e)}
        )
