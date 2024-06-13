from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import schedule
import time
import os

# Twitter accounts to scrape
twitter_accounts = [
    "https://twitter.com/Mr_Derivatives",
    "https://twitter.com/warrior_0719",
    "https://twitter.com/ChartingProdigy",
    "https://twitter.com/allstarcharts",
    "https://twitter.com/yuriymatso",
    "https://twitter.com/TriggerTrades",
    "https://twitter.com/AdamMancini4",
    "https://twitter.com/CordovaTrades",
    "https://twitter.com/Barchart",
    "https://twitter.com/RoyLMattox"
]

# Ticker to search for & interval in minutes
ticker = "$TSLA"
interval_minutes = 15

# Set up Selenium WebDriver
options = Options()
options.headless = True
# chromedriver path
service = Service(os.getcwd() + '/chromedriver.exe') 

# Twitter scraper function using Selenium
def scrape_twitter_account(url, ticker):
    """
    Scrape a Twitter account for mentions of a ticker symbol.
    Args:
        url: The URL of the Twitter account.
        ticker: The ticker symbol to search for.
    Returns:
        The number of times the ticker symbol was mentioned.
    """
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)
    time.sleep(5)  # Allow time for tweets to load
    tweets = driver.find_elements(By.XPATH, "//div[@data-testid='tweetText']")
    count = 0
    for tweet in tweets:
        tweet_text = tweet.text
        # print(tweet_text)
        if ticker in tweet_text:
            count += 1
    driver.quit()
    return count

# Scheduled job
def job():
    """
    Scrape all Twitter accounts for $TSLA mentions
    and print the total count in the last 15 minutes.
    """
    total_count = 0
    for account in twitter_accounts:
        count = scrape_twitter_account(account, ticker)
        total_count += count
    print(f"'{ticker}' was mentioned '{total_count}' times in the last '{interval_minutes}' minutes.")

# Schedule the job
schedule.every(interval_minutes).minutes.do(job)

# Run the scheduler
while True:
    schedule.run_pending()
    time.sleep(1)
