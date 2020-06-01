import youtube_dl
import os
import time




def podcastit(myyturl):
  ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
  # Add all the available extractors
  ydl.add_default_info_extractors()
  #
  result = ydl.extract_info(myyturl
  ,   download=False # We just want to extract the info
    )
  #
  if 'entries' in result:
    # Can be a playlist or a list of videos
    Video = result ['entries'] [0]
  else:
    # Just a video
   video = result
  #
  for format in video['formats']:
    if format['ext'] == 'm4a':
      audio_url = format['url']
  print(audio_url)
  #
  # for a in video:
  #   print(a)
  #
  #
  title = video['title']
  description = (video['description'])
  duration = (video['duration'])    # need to match this podcast length
  #
  # file writing here
  #
  #
  audio_url = audio_url.replace("&","&amp;")
  #
  filenames = ['podcast.rss', 'addon.txt']
  with open('temp.rss', 'w') as outfile:
      for fname in filenames:
          with open(fname) as infile:
              for line in infile:
                  outfile.write(line.replace("YTHERE",myyturl).replace("TITLEHERE",title).replace("DESCRIPTIONHERE",description).replace("URLHERE",audio_url).replace("</channel></rss>","").replace("<!-- EOF -->","</channel></rss>"))
  #
  ###
  timestr = time.strftime("%Y%m%d%H%M%S")
  #
  #
  os.rename('temp.rss','podcast.rss')



filename = 'input.txt'

os.system("cp podcastog.rss podcast.rss")

with open(filename) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
content = [x.strip() for x in content] 

for  a in content:
  podcastit(a)