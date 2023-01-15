import re
import numpy as np
import emoji

def translate_emoji(tweet):
    if tweet == None or tweet == "":
      tweet = tweet
    else:
      tweet = emoji.demojize(tweet).replace(":", "").replace("_", " ")
    return tweet

def remove_email(tweet):
    email = re.compile(r'[\w\.-]+@[\w\.-]+')
    return email.sub(r'',tweet)
     
def clean_tweet(tweets):
    cleaned_tweets = []
    hashtags = []
    for tweet in tweets:
        
        # Remove mentions
        tweet = re.sub(r'@\w+', '', tweet)
        
        # Remove links
        tweet = re.sub(r'http\S+', '', tweet)
        tweet = re.sub(r'www\S+', '', tweet)
        tweet = re.sub(r'bit.ly/\S+', '', tweet) # remove bitly links
        tweet = tweet.strip('[link]') # remove [links]
        
        # Remove email address
        tweet = remove_email(tweet)
        
        # Translate emojis
        tweet = translate_emoji(tweet)
        
        # Capture hashtags
        hashtag_list = re.findall(r'#\w+', tweet)
        if len(hashtag_list) == 0:
            hashtag_list = []
            
        hashtags.append(hashtag_list[1:])
        
        # Remove hashtags
        tweet = re.findall(r"#(\w+)", tweet)
        
        # Remove &amp
        tweet = re.sub(r'&amp ', '', tweet)
        
        # Remove special characters
        tweet = re.sub('([_]+)', "", tweet)
        
        # remove any unnecessary spaces
        tweet = " ".join(tweet.split())
        
        cleaned_tweets.append(tweet)
    return cleaned_tweets, hashtags

def create_bank_col(df):
    bank = df[1]
    if "fnb" in df[0].lower():
        bank =  bank+"FNB;"
    if "nedbank" in df[0].lower():
        bank =  bank+"Nedbank;"
    if "absa" in df[0].lower():
        bank =  bank+"ABSA;"
    if "standard" in df[0].lower():
        bank =  bank+"Standard;"
    if "capitec" in df[0].lower():
        bank =  bank+"Capitec;"
    return bank 