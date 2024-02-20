# pip install vaderSentiment
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def sentiment_scores(sentence):
    # Create a SentimentIntensityAnalyzer object
    sid_onj = SentimentIntensityAnalyzer()

    # define a sentiment dictionary
    sentiment_dict = sid_onj.polarity_scores(sentence)

    print("Overall sentiment dictionary is ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']* 100, "% Negative")
    print("sentence was rated as ", sentiment_dict['pos']* 100, "% Positive")
    print("sentence was rated as ", sentiment_dict['neu']* 100, "% Neutral")

    print("Sentence Overall rated as ", end = " ")

    if (sentiment_dict['compound'] >= 0.05):
        print("Positive")
    elif (sentiment_dict['compound'] < -0.05):
        print("Positive")
    else:
        print("Neutral")

sentence = "We won the game and we are in first place"
print(sentence)
sentiment_scores(sentence)
