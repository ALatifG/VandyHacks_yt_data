from googleapiclient.discovery import build
import json

api_key = 'AIzaSyCsTGj90PwHrlmC8k37EHoZTlqhZJXQddA'

youtube = build('youtube', 'v3', developerKey=api_key)

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