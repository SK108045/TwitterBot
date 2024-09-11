import requests
import tweepy
import os
import vertexai
from vertexai.generative_models import GenerativeModel
import random
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/path/to/your/service-account-file.json"
os.environ['API_KEY'] = 'YOUR_GOOGLE_API_KEY'
os.environ['SEARCH_ENGINE_ID'] = 'YOUR_SEARCH_ENGINE_ID'

vertexai.init(project='YOUR_PROJECT_ID', location="us-central1")

model = GenerativeModel(model_name="gemini-1.5-flash-001")

api_key = 'YOUR_TWITTER_API_KEY'
api_key_secret = 'YOUR_TWITTER_API_KEY_SECRET'
access_token = 'YOUR_TWITTER_ACCESS_TOKEN'
access_token_secret = 'YOUR_TWITTER_ACCESS_TOKEN_SECRET'
bearer_token = 'YOUR_TWITTER_BEARER_TOKEN'

auth = tweepy.OAuth1UserHandler(api_key, api_key_secret, access_token, access_token_secret)
api = tweepy.API(auth)

client = tweepy.Client(bearer_token=bearer_token,
                       consumer_key=api_key,
                       consumer_secret=api_key_secret,
                       access_token=access_token,
                       access_token_secret=access_token_secret)

# below are sample prompts, you can add as many as you like
prompts = [
    "Generate a short funny tweet that will make people laugh. Don't just begin with 'Just'. Use different words.Output only the Tweet",
    "Write a witty short tweet that will engage followers. Don't just begin with 'Just'. Use different words.Output only the Tweet",
    # ... (rest of the prompts)
]
# here i am shuffling the list of prompts to avoid repeating them
random.shuffle(prompts)
prompt = random.choice(prompts)

response = model.generate_content(prompt)

tweet = response.text.replace('\n', ' ').strip()[:280]

print("Generated Tweet:", tweet)

API_KEY = os.getenv('API_KEY', 'YOUR_GOOGLE_API_KEY')
SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID', 'YOUR_SEARCH_ENGINE_ID')

def extract_keywords(tweet):
    tweet = re.sub(r'[^\w\s]', '', tweet.lower())
    words = tweet.split()
    keywords = [word for word in words if word not in ENGLISH_STOP_WORDS]
    return keywords

def search_images(query, api_key, search_engine_id):
    url = 'https://www.googleapis.com/customsearch/v1'
    params = {
        'key': api_key,
        'cx': search_engine_id,
        'q': query,
        'searchType': 'image',
        'num': 1
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    results = response.json()
    if 'items' in results:
        return results['items'][0].get('link')
    return None

def download_image(url, file_path):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    with open(file_path, 'wb') as file:
        file.write(response.content)

def tweet_image_with_text(api, client, tweet):
    keywords = extract_keywords(tweet)
    query = ' '.join(keywords[:3])
    best_image_url = search_images(query, API_KEY, SEARCH_ENGINE_ID)
    if best_image_url:
        try:
            image_path = 'image.jpg'
            download_image(best_image_url, image_path)
            media = api.media_upload(image_path)
            response = client.create_tweet(text=tweet, media_ids=[media.media_id_string])
            print("Tweet posted successfully!", response)
            os.remove(image_path)
        except requests.exceptions.HTTPError as e:
            print(f"Failed to download image: {e}")
    else:
        print("No images found.")

if __name__ == "__main__":
    tweet_image_with_text(api, client, tweet)
