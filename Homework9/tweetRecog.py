# pip install vaderSentiment

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    # Note that we can obtain the pos, neg, neu scores but as we noted
    # they are not always end result indicative of the sentiment
    # instead we are concerned with a normalized compound score
    sid_onj = SentimentIntensityAnalyzer()

    # define a sentiment dictionary
    sentiment_dict = sid_onj.polarity_scores(sentence)

##    if (sentiment_dict['compound'] >= 0.05):
##        return 'Positive'
##    elif (sentiment_dict['compound'] <= -0.05):
##        return 'Negative'
##    else:
##        return 'Neutral'
##    print(sentence, ":", round(sentiment_dict['neg']* 100, 2), "% Negative")
##    print(sentence, ":", round(sentiment_dict['pos']* 100, 2), "% Positive")
##    print(sentence, ":", round(sentiment_dict['neu']* 100, 2), "% Neutral")

    print("Sentence Overall rated as ", end = " ")

    if (sentiment_dict['compound'] >= 0.05):
        print(sentence, ":", round(sentiment_dict['pos']* 100, 2), "% Positive")
    elif (sentiment_dict['compound'] < -0.05):
        print(sentence, ":", round(sentiment_dict['neg']* 100, 2), "% Negative")
    else:
        print(sentence, ":", round(sentiment_dict['neu']* 100, 2), "% Neutral")


import csv
import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

df = pd.read_csv('someIMDBdata.csv')

# Store a list of sentiments that come back
# Call the function for each sentence = tweet and it will return one score
# that we will plop into the sentiment list

sentiment = []

# Iterate through the individual tweets
for i in range(len(df)):
    sentiment.append(sentiment_scores(df.loc[i,"review"]))
##
##df['sentimentValue'] = sentiment
##print(df)
