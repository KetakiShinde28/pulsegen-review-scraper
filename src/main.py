import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Scrape SaaS product reviews")
    parser.add_argument("--company", required=True, help="Company name")
    parser.add_argument("--source", required=True, choices=["g2", "capterra", "trustradius"], help="Review source")
    parser.add_argument("--start_date", required=True, help="Start date YYYY-MM-DD")
    parser.add_argument("--end_date", required=True, help="End date YYYY-MM-DD")
    return parser.parse_args()

from scraper import scrape_reviews
from output import save_to_json

def main():
    args = parse_args()

    reviews = scrape_reviews(
        company=args.company,
        source=args.source,
        start_date=args.start_date,
        end_date=args.end_date
    )

    output_file = save_to_json(reviews, args.company, args.source)
    print(f"Saved {len(reviews)} reviews to {output_file}")


if __name__ == "__main__":
    main()
