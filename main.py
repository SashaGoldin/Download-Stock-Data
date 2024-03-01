import requests
from datetime import datetime
import time

ticker = input("Enter a ticker symbol: ")
from_date = input("Enter start date yyyy/mm/dd: ")
to_date = input("Enter end date yyyy/mm/dd: ")

from_datetime = datetime.strptime(from_date, "%Y/%m/%d")
to_datetime = datetime.strptime(to_date, "%Y/%m/%d")

epoch1 = int(time.mktime(from_datetime.timetuple()))
epoch2 = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={epoch1}&period2={epoch2}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

content = requests.get(url, headers=headers).content
print(content)

with open("data.csv", "wb") as file:
  file.write(content)