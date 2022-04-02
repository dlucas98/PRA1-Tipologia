import argparse
from datetime import datetime
from brScraper import brScraper

def main():
    output_file = "output.csv"

    # Parse the command line arguments
    parser = argparse.ArgumentParser(description="Dates to scrape basketball-reference.com")
    parser.add_argument("-s", "--startDate", help="Start date (DD-MM-YYYY)", default=None)
    parser.add_argument("-e", "--endDate", help="End date (DD-MM-YYYY)", default=None)
    parser.add_argument("-o", "--output", help="Output file name", default=output_file)
    args = parser.parse_args()

    startDate = datetime.strptime(args.startDate, "%d-%m-%Y") if args.startDate else None
    endDate = datetime.strptime(args.endDate, "%d-%m-%Y") if args.endDate else None

    scraper = brScraper(startDate, endDate)

    scraper.scrape()


if __name__ == "__main__":
    main()