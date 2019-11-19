import socket

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(2)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(data)
    conn1, addr1 = s.accept()
    with conn1:
        print('Connected by', addr1)
        while True:
            data1 = conn1.recv(1024)
            if not data1: break
            conn1.sendall(data1)
