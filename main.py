import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) #set timeout to 1 second
    result = sock.connect_ex((ip,port))
    
    if result == 0:
        print(f"[+] Port {port} is OPEN")
        
    sock.close()
    
# port list
target_ip = "127.0.0.1"
ports = [21, 22, 80, 445, 8080]

print(f"Scanning {target_ip} ...")
for port in ports:
    scan_port(target_ip, port)