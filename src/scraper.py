import requests
from bs4 import BeautifulSoup
from utils import is_within_range

def scrape_g2(company, start_date, end_date):
    reviews = []
    page = 1

    while True:
        url = f"https://www.g2.com/products/{company.lower()}/reviews?page={page}"
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

        if response.status_code != 200:
            break

        soup = BeautifulSoup(response.text, "html.parser")
        review_blocks = soup.select("div.paper")

        if not review_blocks:
            break

        for block in review_blocks:
            title = block.select_one("h3")
            body = block.select_one("div[itemprop='reviewBody']")
            date = block.select_one("time")

            if not (title and body and date):
                continue

            if not is_within_range(date["datetime"], start_date, end_date):
                continue

            reviews.append({
                "title": title.text.strip(),
                "review": body.text.strip(),
                "date": date["datetime"],
                "source": "g2"
            })

        page += 1

    return reviews

def scrape_capterra(company, start_date, end_date):
    return []

def scrape_reviews(company, source, start_date, end_date):
    if source == "g2":
        return scrape_g2(company, start_date, end_date)
    elif source == "capterra":
        return scrape_capterra(company, start_date, end_date)
    else:
        raise ValueError("Unsupported source")
