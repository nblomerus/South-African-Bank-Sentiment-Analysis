import re
import numpy as np
import emoji

bank_dict = {'fnb': ['fnb', 'FNBSA', 'fnbSouthAfrica'],
            'absa': ['absa', 'absaSA', 'ABSASouthAfrica'],
            'nedbank': ['nedbank', 'NEDBANKSA', 'nedbankSouthAfrica'],
            'capitec': ['capitec', 'CapitecBank', 'capitecSA'],
            'standard_bank': ['standard bank','standardbank', 'StandardbankSA']}

def clean_tweet(text):  

    pat1 = r'@[^ ]+'                   #@signs
    pat2 = r'https?://[A-Za-z0-9./]+'  #links
    pat3 = r'\'s'                      #floating s's
    pat4 = r'\#\w+'                     # hashtags
    pat5 = r'&amp '
    pat6 = r'[^A-Za-z\s]'         #remove non-alphabet
    # remove patter rt
    pat7 = r'(?<!\w)RT(?!\w)'
    combined_pat = r'|'.join((pat1, pat2, pat3, pat4, pat5, pat6, pat7))
    text = re.sub(combined_pat,"",text).lower()
    #remove extra spaces
    text = re.sub(r'\s+',' ',text)
    return text.strip().lower()


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
     
def get_hashtags(tweet):
    hashtags = re.findall(r'#\w+', tweet)
    return [hashtag.replace('#', '') for hashtag in hashtags]

def get_banks(tweet, bank_dict=bank_dict):
    banks = []
    for bank, search_terms in bank_dict.items():
        for term in search_terms:
            if term.lower() in tweet.lower():
                banks.append(bank)
                break
    return banks

def get_pred(model, tweet):
    ouput = model.predict(tweet)
    return ouput['label'] 