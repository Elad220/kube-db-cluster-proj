import mysql.connector
import socket

# listening on port 5005 for requests
PORT_NUM = 5005

# internal ip address for sql pod 
sql_pod_ip = "172.17.0.3"

# run script until requested exit
while True:

    # create socket and listen on requested port using service ip
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('172.17.0.4', PORT_NUM))
    s.listen()
    conn, addr = s.accept()

    # start connection sequence
    with conn:
        print('Connected by', addr)
        while True:
            input_id = conn.recv(1024)
            if not input_id:
                print("No input!")
                break
            input_id = int(input_id)
            input_id = str(input_id)
            print("You entered:", input_id)

            # connect to mysql db
            mydb = mysql.connector.connect(
                host=sql_pod_ip,
                user="",
                password="password",
                database="addressBook"
            )

            # execute my select query
            mycursor = mydb.cursor()
            mycursor.execute("SELECT * FROM addressBook WHERE ID = %s", (input_id,))

            # get the appropriate result for input id and send it back to starter script
            myresult = mycursor.fetchone()
            myresult = str(myresult)
            conn.sendall(myresult.encode())
            mycursor.close()

    s.close()
