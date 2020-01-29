#!/bin/bash/python3
import pyttsx3,socket,subprocess,time
target_ip="192.168.1.2"
target_port=2200
a=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
a.bind((target_ip,target_port))
while true:
	msg=a.recvfrom(100)
	print(msg)
	audio=pyttsx3.init()
	audio.say(msg[0].decode('ascii'))
	audio.runAndWait()
	time.sleep(1)
	subprocess.getoutput("touch  "+msg[1][0]+".txt")
	with open(msg[1][0]+".txt","a") as f:
		f.write(msg[0].decode('ascii'))

