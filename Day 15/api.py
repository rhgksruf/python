# API
from googleapiclient.discovery import build

key = "AlzaSyA8VRK8GqobS2yWJHn4Aj7-VDnqei_H82g"

#youtube api 클라이언트 생성
youtube = build('youtube','v3', developerKey=key)

result=youtube.commentThreads().list(
    part='snippet',
    videoId='kW_z-NMuZIU',
    maxResults=100,
).execute()

# for i in result['items']:
#     print(i)

for i in result['item']:
    comment = i['snippet']['topLevelComment']['snippet']['textDisplay']
    print(comment)







