prayerTimes = [0,1,2,3,4,5]
time = 5

def updateSolat(time,prayterTimes):
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

updateSolat(time,prayerTimes)
