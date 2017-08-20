import time
import serial
import socket

ser = serial.Serial(
  port='/dev/ttyS0',
  baudrate = 9600,
  parity=serial.PARITY_NONE,
  stopbits=serial.STOPBITS_ONE,
  bytesize=serial.EIGHTBITS,
  timeout=1
)

EndCom = "\xff\xff\xff"
ser.write('ipadd.txt="hello"'+EndCom)