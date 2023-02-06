# South-African-Bank-Sentiment-Analysis
# Overview
This is project is aimed at analyzing public opinion towards various South African banks. The project uses natural language processing techniques to process large amounts of data from sources such as social media and news articles. The analysis will provide insights into customer satisfaction, areas of improvement and general public perception of the banks. The results of this project can be useful for the banks to improve their services and reputation in the South African market.
# Dataset
The dataset for this project was collected using the sntwitter module. A total of 4,688,142 tweets were scraped using the following search dictionary:

```
bank_dict = {'fnb': ['fnb', 'FNBSA', 'fnbSouthAfrica'],
             'absa': ['absa', 'absaSA', 'ABSASouthAfrica'],
             'nedbank': ['nedbank', 'NEDBANKSA', 'nedbankSouthAfrica'],
             'capitec': ['capitec', 'CapitecBank', 'capitecSA'],
             'standard_bank': ['standard bank','standardbank', 'StandardbankSA']}
```
The tweets were collected between 1 January 2006 to 1 January 2023. Each tweet contains the following information:

Tweet text
Date and time of tweet
Tweet author
Number of retweets
Number of likes

Note: The data collected may contain inaccuracies or unrepresentative samples, as it is based on public tweets and may not accurately reflect the overall sentiment towards the banks.
# NLP models
For the natural language processing (NLP) tasks in this project, the tweetnlp module developed by CardiffNLP (available at https://github.com/cardiffnlp/tweetnlp) was used. The module provides several pre-trained models for sentiment analysis, hate speech detection, offensive language detection and topic detection.

Sentiment Analysis Model:
The sentiment analysis model is used to classify the sentiment of the tweets as positive, negative, or neutral. This information is crucial in understanding the overall public opinion towards the banks.

Hate Speech Detection Model:
The hate speech detection model identifies tweets that contain hateful language or discriminatory content. This information can be used to exclude such tweets from the sentiment analysis and provide a more accurate representation of public opinion.

Offensive Language Detection Model:
The offensive language detection model identifies tweets that contain offensive language. This information can be used to exclude such tweets from the sentiment analysis and provide a more accurate representation of public opinion.

Topic Detection Model:
The topic detection model identifies the main topics discussed in the tweets. This information can be used to understand what specific issues or topics are being discussed in relation to the banks.

Disclaimer: These models may not always produce accurate results, as the models are based on pre-existing training data and may not generalize well to the specific domain of South African bank sentiment analysis.
# Current State of the Project
I have conducted the exploratory analysis for this project and intended on releasing the full dataset on Kaggle.

Currently, I am busy with the design and development of the Tableau dashboard.
