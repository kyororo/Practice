
import argparse

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "API KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def search(options):

  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,developerKey=DEVELOPER_KEY)

  search_response = youtube.search().list(
    part = 'id,snippet',
    q = options.q,
    order = options.order,
    maxResults = options.max_results,
    type = 'video',
  ).execute()

  videos = []
  channels = []
  playlists = []

  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append("%s [%s]" % 
        (
          search_result["snippet"]["title"],
          #search_result["statistics"]["viewCount"],
          search_result["snippet"]["channelId"]
        )
      )
  print("Videos:\n", "\n".join(videos), "\n")
  #print(search_response['items'])

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description='api test')
  parser.add_argument("--q", help="Search term", default="にじさんじ")
  parser.add_argument("--order", help="order", default="viewCount")
  parser.add_argument("--max-results", help="Max results", default=25)
  
  args = parser.parse_args()
 
  try:
    search(args)
  except HttpError as e:
    print("An HTTP error %d occurred:\n%s" % (e.resp.status, e.content))

  
