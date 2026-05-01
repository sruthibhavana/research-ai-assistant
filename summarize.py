import os
import requests
import time

def summarize_results(query, search_results):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a research assistant.

Query: {query}

Search Results:
{search_results}

IMPORTANT:
- Return ONLY valid JSON
- No markdown, no explanation

Format:
{{
  "summary": "string",
  "key_points": ["point1", "point2"],
  "sources": ["url1", "url2"]
}}
"""

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    # 🔥 Retry logic
    for attempt in range(3):
        response = requests.post(url, json=data, headers=headers)
        result = response.json()

        try:
            content = result["choices"][0]["message"]["content"]
            if "{" in content:  # basic validation
                return result
        except:
            pass

        print(f"Retrying LLM call... ({attempt+1}/3)")
        time.sleep(1)

    return result  # last attempt


def refine_query(user_query):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
        "Content-Type": "application/json"
    }

    prompt = f"""
Convert this user query into a better search query.

User Query: {user_query}

Return ONLY a clean improved search query.
"""

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, json=data, headers=headers)

    return response.json()