# Minha primeira ferramenta de pentest construida no curso de pentest

import socket # importa a biblioteca SOCKET

host = input(str("Digite o host que quer fazer o scan!:")) #solicita entrada do site ou IP do host

ports = [80, 443, 1443, 21, 22, 3306, 25] # portas escaneadas

for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client.settimeout(0.1) # seta tempo de espera pelo programa
	code = client.connect_ex((host ,port))
	print(code)
	if code == 0:
		print(port, "OPEN") # printa na tela o numero da porta e OPEN caso esteja aberta ou fechada


#response = client.recv(1024)
#print(response.decode())
