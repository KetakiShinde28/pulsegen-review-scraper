# PulseGen Review Scraper

A Python-based CLI tool to scrape SaaS product reviews from multiple platforms within a specified time range and export them into JSON format.

---

## Project Structure

pulsegen-review-scraper/
│
├── src/
│ ├── main.py
│ ├── scraper.py
│ ├── utils.py
│ └── output.py
│
├── data/
│ └── sample_output.json
│
├── requirements.txt
├── README.md
└── .gitignore

yaml
Copy code

---

## Setup Instructions

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
Usage
bash
Copy code
python src/main.py \
  --company notion \
  --source g2 \
  --start_date 2023-01-01 \
  --end_date 2023-12-31
Command-line Arguments
--company : Name of the company / product

--source : Review source (g2, capterra, trustradius)

--start_date : Start date in YYYY-MM-DD format

--end_date : End date in YYYY-MM-DD format

Output
Reviews are saved as a JSON file in the data/ directory.

File naming format:

php-template
Copy code
data/<company>_<source>_reviews.json
Sample Review Object
json
Copy code
{
  "title": "Great product",
  "review": "Easy to use and very flexible",
  "date": "2023-05-14",
  "source": "g2"
}
Notes & Limitations
Review platform HTML structures may change over time.

Some queries may return empty results depending on data availability and selected date range.

This script is intended for assignment and evaluation purposes.

Bonus
A third SaaS review source (TrustRadius) has been integrated using the same interface and workflow as G2 and Capterra.
