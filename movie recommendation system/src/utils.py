import requests
import re

TMDB_API_KEY = "f2556ff35a6d3357f574af21ce4a7c56"

def extract_title_and_year(full_title):
    match = re.match(r"^(.*?)(?:\s*\((\d{4})\))?$", full_title.strip())
    if match:
        return match.group(1).strip(), match.group(2)
    return full_title, None

def get_poster_and_description(full_title):
    title, year = extract_title_and_year(full_title)

    try:
        tmdb_url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": TMDB_API_KEY,
            "query": title
        }
        if year:
            params["year"] = year

        res = requests.get(tmdb_url, params=params)
        data = res.json()
        if data.get("results"):
            result = data["results"][0]
            poster_path = result.get("poster_path")
            overview = result.get("overview", "")
            poster_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None
            return poster_url, overview
    except Exception as e:
        print(f"Error fetching poster/description: {e}")

    return None, None
