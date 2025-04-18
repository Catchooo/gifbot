import os, requests

from dotenv import load_dotenv

load_dotenv()

GIPHY_API_KEY = os.getenv("GIPHY_API_KEY")

def search_gif(query):
    url = f"https://api.giphy.com/v1/gifs/search"

    params = {
        'api_key' : GIPHY_API_KEY,
        'q' : query,
        'limit' : 1,
        'rating' : '8'

    }

    response = requests.get(url,params=params)

    data = response.json()

    if data ['data']:
        gif_url = data["data"][0]["images"]["original"]["url"]
        return gif_url
    

if __name__ == '__main__':
    search_gif('cat')
