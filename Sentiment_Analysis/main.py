import logging
from scraper import scrape_reviews
from sentiment_analysis import analyze_sentiments
from visualizations import generate_visualizations

# Setup logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def main():
    # Step 1: Scrape reviews
    url = "https://www.flipkart.com/boat-airdopes-supreme-w-4-mics-ai-enx-tech-50-hrs-playback-multi-point-connectivity-bluetooth/product-reviews/itm47a93966ad11e?pid=ACCGWU2ABQ3EAUM8&lid=LSTACCGWU2ABQ3EAUM8BAYBSU&marketplace=FLIPKART"
    reviews = scrape_reviews(url, max_pages=10)

    if not reviews:
        logging.error("No reviews were scraped. Exiting...")
        return

    # Step 2: Analyze sentiments
    analyzed_data = analyze_sentiments(reviews)

    # Step 3: Generate visualizations
    generate_visualizations(analyzed_data)

    # Step 4: Save results
    analyzed_data.to_csv("analyzed_reviews.csv", index=False)
    analyzed_data.to_json("analyzed_reviews.json", orient="records")
    logging.info("Results saved to 'analyzed_reviews.csv' and 'analyzed_reviews.json'.")

if __name__ == "__main__":
    main()