import os,requests
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API')
GOOGLE_CX = os.getenv('GOOGLE_CX')

def image_search(query):
    url = f"https://www.googleapis.com/customsearch/v1"

    params = {
        'key' : GOOGLE_API_KEY,
        'cx' : GOOGLE_CX,
        'searchType' : "image",
        'q' :  query,
        "num": 1,
        "safe":"active"
    }

    response = requests.get(url,params=params)
    data = response.json()
    
    if "items" in data:
        image_url = data['items'][0]['link']
        return image_url

if __name__ == '__main__':
    image_search('cat')
