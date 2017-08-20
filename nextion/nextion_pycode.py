import time
import serial
#
ser = serial.Serial(
  port='/dev/ttyS0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)
#b0 is an element in nextion 
count = 0
while (count < 9):
	EndCom = "\xff\xff\xff"
	ser.write('b0.txt="Some"'+EndCom)
	time.sleep(1)
	ser.write('b0.txt="Times"'+EndCom)
	time.sleep(1)
	time.sleep(1)
	ser.write('b0.txt="You"'+EndCom)
	time.sleep(1)
	time.sleep(1)
	ser.write('b0.txt="Gotta"'+EndCom)
	time.sleep(1)
	time.sleep(1)
	ser.write('b0.txt="Run"'+EndCom)
	time.sleep(1)
	time.sleep(1)
	ser.write('b0.txt="Before"'+EndCom)
	time.sleep(1)
	time.sleep(1)
	ser.write('b0.txt="You"'+EndCom)
	time.sleep(1)
	ser.write('b0.txt="Can "'+EndCom)
	time.sleep(1)
	time.sleep(1)
	ser.write('b0.txt="Walk "'+EndCom)
	time.sleep(1)
	count = count + 1
