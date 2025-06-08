import requests
import base64


class TwitterAPI():
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret

    # Step 1: Get Bearer Token
    def get_bearer_token(self):
        key_secret = f"{self.api_key}:{self.api_secret}".encode('ascii')
        b64_encoded_key = base64.b64encode(key_secret).decode('ascii')

        url = "https://api.twitter.com/oauth2/token"
        headers = {
            "Authorization": f"Basic {b64_encoded_key}",
            "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        }
        data = {"grant_type": "client_credentials"}

        response = requests.post(url, headers=headers, data=data)
        if response.status_code != 200:
            raise Exception(f"Cannot get bearer token: {response.text}")
        return response.json()['access_token']

    # Step 2: Search Tweets
    def search_crypto_tweets(self, bearer_token, query="cryptocurrency OR bitcoin OR ethereum", max_results=10):
        url = "https://api.twitter.com/2/tweets/search/recent"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        params = {
            "query": query,
            "max_results": max_results,
            "tweet.fields": "created_at,text,author_id",
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Search error: {response.status_code} - {response.text}")
        return response.json()
    
    def test(self):
        print("Testing TwitterAPI class...")

    # Step 2: Search Tweets from Elon Musk
    def search_elon_tweets(self, bearer_token, query="from:44196397", max_results=10):
        url = "https://api.twitter.com/2/tweets/search/recent"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        params = {
            "query": query,
            "max_results": max_results,
            "tweet.fields": "created_at,text,author_id,public_metrics,lang,geo,referenced_tweets,conversation_id",
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code != 200:
            raise Exception(f"Search error: {response.status_code} - {response.text}")
        return response.json()
# Step 3: Run it all

