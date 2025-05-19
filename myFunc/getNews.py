import requests
from bs4 import BeautifulSoup # type: ignore

def scrape_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Example: Extracting all article titles
    articles = soup.find_all('article')
    news_list = []
    for article in articles:
        title_element = article.find('h2')
        link_element = article.find('a')
        if title_element and link_element:
            title = title_element.text.strip()
            link = link_element['href']
            news_list.append({'title': title, 'link': link})
    return news_list

def getGolfNewvn(url = "https://www.golfnews.vn/chuyen-muc/tin-trong-nuoc-3"):
    news = scrape_news(url)
    print(news)

getGolfNewvn()