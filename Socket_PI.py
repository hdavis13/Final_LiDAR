import socket
import RPi.GPIO as GPIO

#set sensor to angle 0-1 and 300RPM
IP_ADDRESS = "0.0.0.0" #should be 192.168.1.77 if on local machine
PORT_NO = 2368

IP_ADDRESS_LOCAL = "127.0.0.1"
PORT_NO_LOCAL = 6789

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((IP_ADDRESS, PORT_NO))

sending_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
array = [NONE]*50

while True:
  GPIO.setmode(GPIO.BCM) #initialize GPIO output pin
  GPIO.setup(18, GPIO.OUT)
  array = server_socket.recv(1248)[0:45]
  avg = int(array[44])
  print(avg)
  if avg < 3:
    GPIO.output(18, GPIO.HIGH)
  else:
    GPIO.output(18, GPIO.LOW)
    GPIO.cleanup()