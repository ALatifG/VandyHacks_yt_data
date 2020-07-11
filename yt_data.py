from googleapiclient.discovery import build

api_key = 'AIzaSyCsTGj90PwHrlmC8k37EHoZTlqhZJXQddA'

youtube = build('youtube', 'v3', developerKey=api_key)

request = youtube.search().list(
    part='snippet',
    q='soccer vanderbilt',
    maxResults=100,

)

response = request.execute()

print(response)