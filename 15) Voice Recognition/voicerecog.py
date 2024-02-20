# pip install setuptools
# pip install SpeechRecognition
# pip install pyaudio

import speech_recognition as sr
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

recog = sr.Recognizer()

print(sr.Microphone.list_microphone_names())

mic = sr.Microphone(1)

def sentiment_scores(sentence):
    # Note that we can obtain the pos, neg, neu scores but as we noted
    # they are not always end result indicative of the sentiment
    # instead we are concerned with a normalized compound score
    sid_onj = SentimentIntensityAnalyzer()

    # define a sentiment dictionary
    sentiment_dict = sid_onj.polarity_scores(sentence)

    if (sentiment_dict['compound'] >= 0.05):
        return 'Positive'
    elif (sentiment_dict['compound'] <= -0.05):
        return 'Negative'
    else:
        return 'Neutral'

x = 'hey'
while x != 'bye':
    with mic as source:
        audio = recog.listen(source)
        x = recog.recognize_google(audio)
        print(x)
        print(sentiment_scores(x))

print('All done')
