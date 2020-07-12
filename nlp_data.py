from textblob import Textblob
import nltk
from nltk.tokenize import word_tokenize


# items[] is a list hence can be processed directly by nltk library using sent_tokenizer() and
# word_tokenizer after which we can run the sentiment analysis and find the average of analyzing all the
# comments.


#TODO: my ANACONDA crashed and couldn't download any libraries, but this should work.
#TODO: I have added the import statements above to yt_data. Here's the function to add to yt_data.


def process_comments(youtube, comments):

    #tokenize comments into single words
    tokenized_sents = [word_tokenize(i) for i in comments]

    # create a TextBlob object
    obj = Textblob(tokenized_sents)

    sentiment = obj.sentiment.polarity

    return sentiment








