import socket

hostname=input("masukan web yang akan di cek : ")
ip_adress=socket.gethostbyname(hostname)

print(f'hasil scan dari {hostname}')
print(f'ip adress nya : {ip_adress}')