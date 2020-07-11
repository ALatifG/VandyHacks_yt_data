from googleapiclient.discovery import build
import json

api_key = 'AIzaSyCsTGj90PwHrlmC8k37EHoZTlqhZJXQddA'

youtube = build('youtube', 'v3', developerKey=api_key)

<<<<<<< HEAD
request = youtube.channels().list(
    part = 'statistics',
    forUsername = "TechGuyWeb"
)

response = request.execute()
# print(response)

search = youtube.search().list(
    part = 'snippet'
    q = 
)

search_response = search.execute()
search_js = json.loads(search_response)
=======
request = youtube.search().list(
    part='snippet',
    q='soccer vanderbilt',
    maxResults=100,

)

response = request.execute()

print(response)
>>>>>>> 6de1844a183d807e5678118eac73d239966b7fdb
