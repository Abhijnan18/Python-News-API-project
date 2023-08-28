import requests

def fetch_news(api_key, country='us'):
    url = f'https://newsapi.org/v2/top-headlines'
    params = {
        'apiKey': api_key,
        'country': country
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    return data

def display_news(news_data):
    if news_data['status'] == 'ok':
        articles = news_data['articles']
        for idx, article in enumerate(articles, start=1):
            print(f"News {idx}: {article['title']}")
            print(f"Source: {article['source']['name']}")
            print(f"Published At: {article['publishedAt']}")
            print(f"Description: {article['description']}\n")
    else:
        print("Error fetching news.")

if __name__ == "__main__":
    api_key = "4b04180b9150446fa6ecc2044531fa7a"
    country_code = input("Enter the country code (e.g., us, gb, in): ")
    
    news_data = fetch_news(api_key, country=country_code)
    display_news(news_data)
