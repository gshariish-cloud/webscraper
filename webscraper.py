import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(url)

if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

  
    headlines = soup.find_all("h2")

  
    with open("headlines.txt", "w", encoding="utf-8") as file:

        file.write("Top News Headlines\n")
        file.write("=" * 40 + "\n\n")

        for i, headline in enumerate(headlines, start=1):

            text = headline.get_text(strip=True)

            if text:
                file.write(f"{i}. {text}\n")

    print("Headlines saved to headlines.txt")

else:
    print("Failed to fetch webpage")
