import socket
hostname = socket.gethostname()
IPAddress = socket.gethostbyname(hostname)
print("Your Computer name is: " + hostname)
print("Your Ip address is :" + IPAddress)
