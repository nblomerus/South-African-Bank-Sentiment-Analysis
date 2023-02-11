import re
import numpy as np
import emoji
import pandas as pd
from tqdm import tqdm

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
    # remove the # from the hashtag
    [hashtag.replace('#', '') for hashtag in hashtags]
    return ','.join(hashtags)

def get_banks(tweet, bank_dict=bank_dict):
    banks = []
    for bank, search_terms in bank_dict.items():
        for term in search_terms:
            if term.lower() in tweet.lower():
                banks.append(bank)
                
    return banks

def get_pred(model, tweet):
    ouput = model.predict(tweet)
    return ouput['label'] 

def generate_df_hashtags(df):
    # get hashtags from tweet
    df_copy = df.copy()
    # df_copy.head()
    df_copy['Hashtags'] = df_copy['Tweet'].apply(get_hashtags)
    # # remove '#' from hashtags
    df_copy['Hashtags'] = df_copy['Hashtags'].str.replace('#', '')
    # # remove duplicates from hashtags per tweet
    df_copy['Hashtags'] = df_copy['Hashtags'].apply(lambda x: ','.join(set(x.split(','))))
    df_copy['Hashtag_List'] = df_copy['Hashtags'].str.split(',')
    df_hashtags = pd.DataFrame(df_copy['Hashtag_List'].tolist()).fillna('').add_prefix('hashtag_')

    # reset index to match df_copy
    df_copy.reset_index(inplace=True)
    df_copy = df_copy.set_index('Tweet_Id')

    df_hashtags = df_hashtags.set_index(df_copy.index)
    # # add columns 'Bank' from df to df_hashtags
    df_hashtags['Bank'] = df_copy['Bank']
    df_hashtags.reset_index(inplace=True)
    return df_hashtags

def generate_df_tweet_words(df):
    # get words from tweet
    df_copy = df.copy()
    df_copy['Tweet_Words'] = df_copy['Tweet'].str.split()
    df_tweet_words = pd.DataFrame(df_copy['Tweet_Words'].tolist()).fillna('').add_prefix('word_')

    # reset index to match df_copy
    df_copy.reset_index(inplace=True)
    df_copy = df_copy.set_index('Tweet_Id')

    df_tweet_words = df_tweet_words.set_index(df_copy.index)
    # # add columns 'Bank' from df to df_hashtags
    df_tweet_words['Bank'] = df_copy['Bank']
    df_tweet_words.reset_index(inplace=True)
    df_tweet_words['Bank'] = df_tweet_words['Bank']
    return df_tweet_words

def split_dataframe_to_excel(df, folder, file_prefix, max_rows_per_file=1000):
    # calculate the number of files to create
    num_files = (len(df) - 1) // max_rows_per_file + 1
    
    # split the dataframe into multiple dataframes
    dfs = [df.iloc[i*max_rows_per_file:(i+1)*max_rows_per_file, :] for i in range(num_files)]
    
    # write each dataframe to a separate Excel file
    for i, df_chunk in tqdm(enumerate(dfs)):
        df_chunk.to_excel(f'{folder}/{file_prefix}_{i+1}.xlsx', index=False)