from datetime import datetime
from dateutil.parser import parse

def is_within_range(date_str, start_date, end_date):
    review_date = parse(date_str).date()
    start = datetime.fromisoformat(start_date).date()
    end = datetime.fromisoformat(end_date).date()
    return start <= review_date <= end
