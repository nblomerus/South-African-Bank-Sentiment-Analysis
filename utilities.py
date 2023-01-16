import re
import numpy as np
import emoji

def clean_tweet(text):  

    pat1 = r'@[^ ]+'                   #@signs
    pat2 = r'https?://[A-Za-z0-9./]+'  #links
    pat3 = r'\'s'                      #floating s's
    pat4 = r'\#\w+'                     # hashtags
    pat5 = r'&amp '
    pat6 = r'[^A-Za-z\s]'         #remove non-alphabet
    combined_pat = r'|'.join((pat1, pat2,pat3,pat4,pat5, pat6))
    text = re.sub(combined_pat,"",text).lower()
    #remove extra spaces
    text = re.sub(r'\s+',' ',text)
    return text.strip()


# translate emjois for text and check for multiple repeated emojis
def translate_emoji(tweet):
    if tweet == None or tweet == "":
      tweet = tweet
    else:
        # add space between words and emojis
        tweet = re.sub(r'(\w+)([^\w\s])', r'\1 \2', tweet)
        tweet = emoji.demojize(tweet).replace(":", "").replace("_", " ")
      # check for multiple repeated words
        tweet = re.sub(r'(\w+)( \1)+', r'\1', tweet)
    return tweet

def remove_email(tweet):
    email = re.compile(r'[\w\.-]+@[\w\.-]+')
    return email.sub(r'',tweet)
     
def get_hashtags(tweets):

    hashtags = []
    for tweet in tweets:
        hashtag_list = re.findall(r'#\w+', tweet)
        if len(hashtag_list) == 0:
            hashtag_list = []
        hashtags.append(hashtag_list[1:])
    return hashtags

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