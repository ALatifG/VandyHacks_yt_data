from googleapiclient.discovery import build
import json
import os
import httplib2
import ssl
import _ssl
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize
# from video_info import *

# api_key = 'AIzaSyBfTDySVjzI9Mh8opXzF5Ls46GgO9Nz7v4'
# api_key = os.environ.get('API_KEY')


"""This program is the backend of a desired chrome extension that scrapes
youtube data using google's youtube Applicaton Programming Interface (API)
to display video information after a user types a text into the search box. 
This extension provides information like comment sentiment, likes, and dislikes
without clicking on the video to see that info"""

# access the search data base of the api to access a json
# object of search results. Takes in search input and number of results to be analysed
def get_search_outcome_ids(youtube, search_input, max_results):
    request = youtube.search().list(
        part='snippet',

        q=search_input,
        maxResults = max_results
    )

    response = request.execute()

    # retrieve video ids from json/dictionary
    vid_ids = []
    for item in response['items']:
        if 'videoId' in item:
            vid_ids.append(item['id']['videoId'])
    
    return vid_ids


# takes the list of ids as param and accesses their stats to be displayed
def get_video_stats(youtube, video_id):
    stats_request = youtube.videos().list(
        part='statistics',
        id=video_id
    )

    stats_response = stats_request.execute()

    vid_stats = []
    for stat in stats_response['items']:
        vid_stats.append(stat['statistics'])
    # vid_stat = stats_response['items']['statistics']

    return vid_stats


# access the comment_threads data from api and appends each comment in a list
def get_comment_threads(youtube, video_id, comments=[], token=""):
    results = youtube.commentThreads().list(
        part="snippet",
        pageToken=token,
        videoId=video_id,
        textFormat="plainText"
    ).execute()

    for item in results["items"]:
        comment = item["snippet"]["topLevelComment"]
        text = comment["snippet"]["textDisplay"]
        comments.append(text)

    # wraps to next page if needed
    if "nextPageToken" in results:
        return get_comment_threads(youtube, video_id, comments, results["nextPageToken"])
    else:
        return comments

# writes the comments in a list to a .txt file for analysis
def write_comments_to_file(comments):
    # encodes text into utf-8 so python understands it and can write it to file
    with open('youtube_comments.txt', 'w', encoding='utf-8') as filehandle:
         filehandle.writelines("%s\n" % comment for comment in comments)

def process_comments(youtube, comments):

    #tokenize comments into single words
    #tokenized_sents = [word_tokenize(i) for i in comments]
    str2 = " ".join(comments)

    # create a TextBlob object
    obj = TextBlob(str2)

    sentiment = obj.sentiment.polarity

    return sentiment

def display_info(likes, dislikes, sentiment):
    print(likes, 'likes')
    print(dislikes, 'dislikes')

    if(sentiment > 0):
        print("General positive sentiment")
    elif(sentiment == 0):
        print("General neutral sentiment")
    else:
        print("General Negative sentiment")

def main():
    # gets the api key securely from a local computer
    # access the api using the key and version number
    api_key = 'AIzaSyBCtVzJ4Y55mu1-WJf3uotea2tLP5oIhd4'
    youtube = build('youtube', 'v3', developerKey=api_key)

    # get input
    search_text = input("Input search text: ")
    video_ids = get_search_outcome_ids(youtube, search_text, max_results=20)

    likes = 0
    dislikes = 0
    # info = videoInfo(0, 0, 0)
    for video_id in video_ids:
        comments = get_comment_threads(youtube, video_id)
        sentiment = process_comments(youtube, comments)
        
        video_stat = get_video_stats(youtube, video_id)
        if 'likeCount' not in video_stat[0]:
            likes = 0
        else:
            likes = int(video_stat[0]['likeCount'])
        if 'dislikeCount' not in video_stat[0]:
            dislikes = 0
        else:
            dislikes = int(video_stat[0]['dislikeCount'])

        sentiment = process_comments(youtube, comments)
        display_info(likes, dislikes, sentiment)

if __name__ == '__main__':
    main()

