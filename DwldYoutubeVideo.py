from __future__ import unicode_literals
import youtube_dl

import csv
import time
import os
filename = "VidList.txt"

cmd = "MoveScript.bat"
returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)


class MyLogger(object):
	def debug(self, msg):
		pass

	def warning(self, msg):
		pass

	def error(self, msg):
		print(msg)

def my_hook(d):
	if d['status'] == 'finished':
		print('Done downloading, now converting ...')

#ydl_opts = {
#	'format': 'bestaudio/best',
#	'postprocessors': [{
#		'key': 'FFmpegExtractAudio',
#		'preferredcodec': 'mp3',
#		'preferredquality': '192',
#	}],
#	'logger': MyLogger(),
#	'progress_hooks': [my_hook],
#}
#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#	ydl.download(['https://www.youtube.com/watch?v=ow1QqW0jzTo'])

with youtube_dl.YoutubeDL() as ydl:
	with open(filename) as csv_file:
		csv_reader = csv.reader(csv_file, delimiter='\t')
		line_count = 0
		for row in csv_reader:
			print (row[0])
			ydl.download([row[0]])
			#time.sleep(4)
cmd = "MoveScript.bat"
returned_value = os.system(cmd)  # returns the exit code in unix
print('returned value:', returned_value)
