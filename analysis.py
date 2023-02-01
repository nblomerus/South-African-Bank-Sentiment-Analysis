import pandas as pd
import matplotlib.pyplot as plt
import glob
from utilities import clean_tweet
from tqdm.notebook import tqdm
tqdm.pandas()
import tweetnlp
from textblob import TextBlob

def get_pred(model, tweet):
    ouput = model.predict(tweet)
    return ouput['label'] 

def get_sentiment(tweet):
    # check polarity of tweet and return sentiment
    analysis = TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def get_polarity(tweet):
    return TextBlob(tweet).sentiment.polarity

# Load models from tweetnlp
# model_hate_speech = tweetnlp.load_model('hate')
# model_offensive_language = tweetnlp.load_model('offensive')
model_sentiment = tweetnlp.load_model('sentiment')
# model_topic = tweetnlp.load_model('topic_classification', multi_label=False) 