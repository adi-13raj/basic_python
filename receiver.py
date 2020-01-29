import socket
target_ip="192.168.1.47"
target_port=2200
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
msg=input("plz enter your message  :  ")
newmsg=msg.encode('ascii')
print(newmsg)
x.sendto(newmsg,(target_ip,target_port))

