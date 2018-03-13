import urllib.request, json 
import time
from time import sleep
updateTime=["00:00:00","16:10:00","17:06:00"]

def updateSolat():
	with urllib.request.urlopen("https://mpt.i906.my/mpt.json?code=sgr-6&filter=1") as url:
		data = json.loads(url.read().decode())
		prayterTimes=data['response']['times']
		#print(prayterTimes)
		#time.strftime("%H:%M:%S",time.localtime(prayterTimes[]))
		print("Subuh  : {}".format(time.strftime("%H:%M:%S",time.localtime(prayterTimes[0]))))
		print("Imsak  : {}".format(time.strftime("%H:%M:%S",time.localtime(prayterTimes[1]))))
		print("Zohor  : {}".format(time.strftime("%H:%M:%S",time.localtime(prayterTimes[2]))))
		print("Asar   : {}".format(time.strftime("%H:%M:%S",time.localtime(prayterTimes[3]))))
		print("Magrib : {}".format(time.strftime("%H:%M:%S",time.localtime(prayterTimes[4]))))
		print("Isyak  : {}".format(time.strftime("%H:%M:%S",time.localtime(prayterTimes[5]))))
		print("triggers")
		print(prayterTimes)
		return prayterTimes

def SolatDefinition(time,prayterTimes):
	if prayterTimes.index(time)==0:
		print ("subuh")
	elif prayterTimes.index(time)==1:
		print ("imsak")
	elif prayterTimes.index(time)==2:
		print ("Zohor")
	elif prayterTimes.index(time)==3:
		print ("Asar")
	elif prayterTimes.index(time)==4:
		print ("Magrib")
	elif prayterTimes.index(time)==5:
		print ("Isyak")

prayterTimes=updateSolat()
time.strftime("%H:%M:%S",time.localtime(time.time())) # tuple 
while 0 == 0:
	clock=int(time.time())
	#print(clock)
#	print(time.strftime("%H:%M:%S",time.localtime(time.time())))
#	if minutes == time.strftime("%H:%M:%S",time.localtime(time.time())):
#	if minutes == time.strftime("%H:%M:%S",time.localtime(time.time())):
	if clock in prayterTimes:
		print ("Waktu Solat")
		SolatDefinition(clock,prayterTimes)
		print (chr(7))
	if time.strftime("%H:%M:%S",time.localtime(time.time())) in updateTime:
		prayterTimes=updateSolat()
	sleep(1)