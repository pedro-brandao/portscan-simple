# Minha primeira ferramenta de pentest construida no curso de pentest
'''
Portscan
'''

import socket

host = input(str("Digite o host que quer fazer o scan!:"))

ports = [80, 443, 1443, 21, 22, 3306, 25]

for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.1)
	code = client.connect_ex((host ,port))
	print(code)
	if code == 0:
		print(port, "OPEN")


#response = client.recv(1024)
#print(response.decode())
