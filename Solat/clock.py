import time
from time import sleep
minutes = "22:31:00"
while 0 == 0:
	print(time.strftime("%H:%M:%S",time.localtime(time.time())))
	
	if minutes == time.strftime("%H:%M:%S",time.localtime(time.time())):
		print ("Alarm Triggered")
		print (chr(7))
	else:
		print ("Alarm Not Triggered")
	sleep(1)