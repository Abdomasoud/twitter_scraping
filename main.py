# importing the required libraries
import time
import requests
from bs4 import BeautifulSoup
import schedule

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

# Twitter scraper function
def scrape_twitter_account(url, ticker):
    """
        Scrape a Twitter account for mentions
        of a ticker symbol.
        Args:
            url: The URL of the Twitter account.
            ticker: The ticker symbol to search for.
        Returns:
            The number of times the ticker symbol was mentioned.
    """
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            tweets = soup.find_all('div', {'data-testid': 'tweet'})
            count = 0
            for tweet in tweets:
                # tweet text
                print(tweet.get_text())
                if ticker in tweet.get_text():
                    count += 1
            return count
        else:
            print(f"Failed to retrieve {url}")
            return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0

# Scheduled job
def job():
    """
        Scrape all Twitter accounts for $TSLA mentions
        of a ticker symbol and print the total count in last 15 minuts.
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
