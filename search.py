import os
import requests

def search_web(query):
    url = "https://api.tavily.com/search"
    
    headers = {
        "Authorization": f"Bearer {os.getenv('TAVILY_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "query": query,
        "max_results": 5
    }

    response = requests.post(url, json=data, headers=headers)
    results = response.json()

    cleaned_results = []

    for item in results.get("results", []):
        cleaned_results.append({
            "title": item.get("title"),
            "url": item.get("url"),
            "content": item.get("content")
        })

    return cleaned_results 
if __name__ == "__main__":
    result = search_web("AI in healthcare")
    print(result)