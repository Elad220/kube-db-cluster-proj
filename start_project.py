import socket
PORT = 30007
running = True
IP = input("Please enter minikube ip: ")
while running:
    input_ID = input("(to quit enter 'q') Please enter the requested ID: ")
    if input_ID == 'q':
        print("Exiting..")
        running = False
        break
    elif len(input_ID) < 8 or len(input_ID) > 9:
        print("Invalid input, try again!")
        continue
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        x = socket.gethostname()
        s.connect((IP, PORT))
        s.sendall(bytes(input_ID, encoding='utf8'))
        data = s.recv(1024)
    print(data.decode())