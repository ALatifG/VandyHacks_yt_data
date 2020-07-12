from googleapiclient.discovery import build
import json
import os
import httplib2
import ssl
import _ssl
# import video_info

"""This program is the backend of a desired chrome extension that scrapes
youtube data using google's youtube Aplicaton Programming Interface (API)
to display video information after a user types a text into the search box. 
This extension provides information like comment sentiment, likes, and dislikes
without clicking on the video to see that info"""

# access the search data base of the api to access a json
# object of search results. Takes in search input and number of results to be analysed
def get_search_outcome_ids(youtube, search_input, max_results):
    request = youtube.search().list(
        part = 'snippet',
        q= search_input,
        maxResults = max_results
    )

    response = request.execute()

    # retrieve video ids from json/dictionary
    vid_ids = []
    for item in response['items']:
        vid_ids.append(item['id']['videoId'])
    
    return vid_ids

# takes the list of ids as param and accesse their stats to be displayed
def get_video_stats(youtube, video_ids):
    stats_request = youtube.videos().list(
        part = 'statistics',
        id = video_ids
    )

    stats_response = stats_request.execute()

    vid_stats =[]
    for stat in stats_response['items']:
        vid_stats.append(stat['statistics'])

    return vid_stats

# access the comment_threads data from api and appends each comment in a list
def get_comment_threads(youtube, video_id, comments=[], token=""):
    results = youtube.commentThreads().list(
        part = "snippet",
        pageToken = token,
        videoId = video_id,
        textFormat = "plainText"
    ).execute()

    for item in results["items"]:
        comment = item["snippet"]["topLevelComment"]
        text = comment["snippet"]["textDisplay"]
        comments.append(text)

    if "nextPageToken" in results: #wraps to next page if needed
        return get_comment_threads(youtube, video_id, comments, results["nextPageToken"])
    else:
        return comments

# writes the comments in a list to a .txt file for analysis
# def write_comments_to_file(comments):
    # TODO: first find a way to encode the comments so python understands all the characters
    # with open('youtube_comments.txt', 'w') as filehandle:
        #  filehandle.writelines("%s\n" % comment for comment in comments)

def main():
    # gets the api key securely from a local computer
    api_key = os.environ.get('API_KEY')

    # access the api using the key and version number
    youtube = build('youtube', 'v3', developerKey=api_key)

    # get input
    search_text = input("Input search text: ")
    video_ids = get_search_outcome_ids(youtube, search_text, max_results=20)

    video_stats = get_video_stats(youtube, video_ids)
    print(video_ids)
    print()
    print(video_stats)

    # for video in video_ids:
    #     comments = get_comment_threads(youtube, video)
    #     write_comments_to_file(comments)
    # stats = videoInfo(3, 5, -1)
    # stats.display_stats()

if __name__ == '__main__':
    main()