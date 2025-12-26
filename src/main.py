import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Scrape SaaS product reviews")
    parser.add_argument("--company", required=True, help="Company name")
    parser.add_argument("--source", required=True, choices=["g2", "capterra"], help="Review source")
    parser.add_argument("--start_date", required=True, help="Start date YYYY-MM-DD")
    parser.add_argument("--end_date", required=True, help="End date YYYY-MM-DD")
    return parser.parse_args()

def main():
    args = parse_args()
    print("Inputs received:")
    print(vars(args))

if __name__ == "__main__":
    main()
