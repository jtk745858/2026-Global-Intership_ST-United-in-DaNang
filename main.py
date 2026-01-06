import socket

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) #set timeout to 1 second
    result = sock.connect_ex((ip,port))
    
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    else:
        print(f"[-] Port {port} is CLOSED")
    sock.close()
    
if __name__ == "__main__":
    print("-" * 50)
    print("Simple port Scanner v1.0  - Starting")
    print("-" * 50)
    target = input("Enter the target IP address:")
    ports = [21, 22, 23, 80, 443, 8080]
    
    print(f"\nStarting port scan on {target}...\n")
    for port in ports:
        scan_port(target, port)
    
    print("Scan Completed.")