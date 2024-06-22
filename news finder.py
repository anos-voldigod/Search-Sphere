import requests

def search_articles_with_api(api_key, keyword):
    base_url = "https://newsapi.org/v2/everything"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "User-Agent": "Your App Name/1.0"
    }
    params = {
        "q": keyword,
        "apiKey": api_key, 
    }

    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()  
        articles = response.json().get('articles', [])
        return articles
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"Request error occurred: {err}")
    
    return []

def main():
    api_key = "0d71b932190e42faa13fb8cf710bcbfd"  
    keyword = input("Enter the keyword: ")
    articles = search_articles_with_api(api_key, keyword)

    if articles:
        print("\nFound Articles:\n")
        for article in articles:
            print(f"Title: {article['title']}")
            print(f"Link: {article['url']}\n")
    else:
        print("No articles found for the given keyword.")

if __name__ == "__main__":
    main()
