def scrape_g2(company, start_date, end_date):
    return []

def scrape_capterra(company, start_date, end_date):
    return []

def scrape_reviews(company, source, start_date, end_date):
    if source == "g2":
        return scrape_g2(company, start_date, end_date)
    elif source == "capterra":
        return scrape_capterra(company, start_date, end_date)
    else:
        raise ValueError("Unsupported source")
