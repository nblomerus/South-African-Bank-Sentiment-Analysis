# Twitter Analysis of Popular South African Banks
# Overview
This is project is aimed at analyzing public opinion towards various South African banks. The project uses natural language processing techniques to process large amounts of data. The analysis will provide insights into customer satisfaction, areas of improvement and general public perception of the banks. The results of this project can be useful for the banks to improve their services and reputation in the South African market.
# Dataset
The dataset for this project was collected using the sntwitter module. A total of 5,591,765 tweets were scraped using the following search dictionary:

```
bank_dict = {'fnb': ['fnb', 'FNBSA', 'fnbSouthAfrica'],
             'absa': ['absa', 'absaSA', 'ABSASouthAfrica'],
             'nedbank': ['nedbank', 'NEDBANKSA', 'nedbankSouthAfrica'],
             'capitec': ['capitec', 'CapitecBank', 'capitecSA', 'capitecbankSA'],
             'standard_bank': ['standard bank','standardbank', 'StandardbankSA', 'standardbankZA', 'standardbankSouthAfrica']}
```
The tweets were collected between 1 January 2006 to 1 January 2023. Each tweet contains the following information:

Tweet text
Date and time of tweet
Tweet author
Number of retweets
Number of likes

All data sources have been upload to Kaggle [here](https://www.kaggle.com/datasets/nicholasblomerus/twitter-analysis-of-popular-south-african-banks). Data has been stored in both parquet and excel file formats. You can use the df_to_excel notebook to convert the parquet files to excel sheets.

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

# Tableau Story
The results of the data analysis were visualized using Tableau to create an interactive story. The story includes various visualizations, including line charts, scatterplots, bar charts, and word clouds, to provide insights into the online presence and engagement of South Africa's top banks on Twitter.

## Twitter Statistics
https://user-images.github<img width="698" alt="dashboard1" src="https://user-images.githubusercontent.com/98228593/221432930-e81bf1c3-21f3-4484-84a2-eebd9cfeacbe.png">

## Best times to Tweet
<img width="695" alt="dashboard2" src="https://user-images.githubusercontent.com/98228593/221432946-8a9e5d0d-c426-4708-a5d1-4125bf50d4be.png">

## Sentiment Analysis
<img width="700" alt="dashboard3" src="https://user-images.githubusercontent.com/98228593/221432961-a8bba6fd-f74c-47f2-a8ad-3f4cbda17196.png">

## Effects of Sport
<img width="694" alt="dashboard4" src="https://user-images.githubusercontent.com/98228593/221433009-0b581214-1489-468a-828e-05c3c740e3eb.png">

## Hashtag Analysis 
<img width="686" alt="dashboard6" src="https://user-images.githubusercontent.com/98228593/221433027-b3cc7bfb-e628-4c8d-b443-b1873c863f75.png">

## Top Tweets
<img width="703" alt="dashboard7" src="https://user-images.githubusercontent.com/98228593/221433034-07fa4345-7500-447d-9b89-78e7d4085fdd.png">

Due to the large number  of tweets it was not possilbe to publish this workbook to Tableau Public. If you would like workbook please feel free to contact me on LinkedIn. I hope whom every sees this Tableau story gains some insight.


usercontent.com/98228593/221222657-9516e0bd-bc0b-4f6c-9750-6121c2405748.mp4


