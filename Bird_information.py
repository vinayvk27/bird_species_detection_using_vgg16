import requests
import streamlit as st

def get_wikipedia_info(bird_name):
    base_url = "https://en.wikipedia.org/w/api.php"

    # Step 1: Search for bird information
    search_params = {
        "action": "query",
        "list": "search",
        "srsearch": bird_name,
        "format": "json"
    }

    search_response = requests.get(base_url, params=search_params)
    search_data = search_response.json()

    # Check if there are any search results
    if "query" in search_data and "search" in search_data["query"] and search_data["query"]["search"]:
        # Step 2: Retrieve page content
        page_title = search_data["query"]["search"][0]["title"]
        content_params = {
            "action": "query",
            "titles": page_title,
            "prop": "extracts",
            "exintro": True,
            "format": "json"
        }

        content_response = requests.get(base_url, params=content_params)
        content_data = content_response.json()

        # Step 3: Extract relevant information
        page_id = list(content_data["query"]["pages"].keys())[0]
        bird_info = content_data["query"]["pages"][page_id]["extract"]

        # Print or use the information as needed
    
        return bird_info

    else:
        print(f"No information found for {bird_name}")

# Example usage
get_wikipedia_info("Peregrine Falcon")
