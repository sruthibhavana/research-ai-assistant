from search import search_web
from summarize import summarize_results, refine_query
import json

def trim_results(results, max_items=5):
    """Limit number of results and shorten content"""
    trimmed = []
    for r in results[:max_items]:
        trimmed.append({
            "title": r["title"],
            "url": r["url"],
            "content": r["content"][:300]  # 🔥 limit content length
        })
    return trimmed


def main():
    query = input("Enter your research query: ")

    current_query = query
    all_results = []

    for step in range(2):
        print(f"\n--- Step {step+1} ---\n")

        print("Refining query...\n")
        refined = refine_query(current_query)

        try:
            refined_query = refined["choices"][0]["message"]["content"].strip()
        except:
            refined_query = current_query

        print("Using search query:", refined_query, "\n")

        print("Searching...\n")
        results = search_web(refined_query)

        # 🔥 Trim results before storing
        trimmed = trim_results(results, max_items=3)
        all_results.extend(trimmed)

        # Stop early if enough
        if len(all_results) >= 5:
            break

        current_query = refined_query

    print("Summarizing...\n")
    response = summarize_results(query, all_results)

    try:
        output = response["choices"][0]["message"]["content"]

        if "```" in output:
            output = output.split("```")[1]
            output = output.replace("json", "").strip()

        parsed = json.loads(output)

        print("\n===== FINAL OUTPUT =====\n")
        print("SUMMARY:\n", parsed["summary"])

        print("\nKEY POINTS:")
        for point in parsed["key_points"]:
            print("-", point)

        print("\nSOURCES:")
        for src in parsed["sources"]:
            print("-", src)

    except Exception as e:
        print("Error parsing response:", e)
        print(response)


if __name__ == "__main__":
    main()