from twitterAPI.datafromAPI import TwitterAPI
from persistData.saveDataLocally import SaveCSVData

def main():
    API_KEY="7nZ2AzagJ3yyRt0SYPBooW0F3"
    API_SECRET="TqxkmUUVkNb1QpLJcF47OIxAVcEjTe3GK3Qhtlkn58Iu7Xu5PB"
    api = TwitterAPI(API_KEY, API_SECRET)
#    api.test()
    bearer_token = api.get_bearer_token()
    
    #tweets_data = api.search_crypto_tweets(bearer_token, max_results=10)

    tweets_data = api.search_elon_tweets(bearer_token, max_results=100)


    # Save the Crypt tweets data to a CSV file
    #saveCsv = SaveCSVData("/Users/arpan/Documents/Github/Python/SentimentalAnalysis/data/tweets_data.csv")
    
    # Save the Elon musk tweets data to a CSV file
    saveCsv = SaveCSVData("/Users/arpan/Documents/Github/Python/SentimentalAnalysis/data/elonmusk.csv")

    saveCsv.save_data(tweets_data)

    print("\n🪙 Recent Tweets on Cryptocurrency:\n")
    for tweet in tweets_data.get("data", []):
        print(f"{tweet['created_at']} - {tweet['text']}\n")

if __name__ == "__main__":
    main()