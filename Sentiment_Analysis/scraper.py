import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def scrape_reviews(url, max_pages=10):
    logging.info("Starting review scraping...")
    
    # Corrected Edge options
    options = webdriver.EdgeOptions()
    
    # Install the correct Edge WebDriver and initialize the service
    service = Service(EdgeChromiumDriverManager().install())  
    driver = webdriver.Edge(service=service, options=options)  # Correct order of arguments

    driver.get(url)
    time.sleep(5)

    reviews = []
    for page in range(max_pages):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ZmyHeo")))
            review_elements = driver.find_elements(By.CLASS_NAME, "ZmyHeo")
            reviews.extend([review.text.strip() for review in review_elements if review.text.strip()])

            next_button = driver.find_elements(By.XPATH, "//span[text()='Next']")
            if next_button:
                driver.execute_script("arguments[0].click();", next_button[0])
                time.sleep(3)
            else:
                break
        except Exception as e:
            logging.warning(f"Error on page {page + 1}: {e}")
            break

    driver.quit()
    logging.info(f"Scraped {len(reviews)} reviews.")
    return reviews
