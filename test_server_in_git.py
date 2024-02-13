


import csv
import socket
import time
from threading import Thread


# def write_in_csv(data_from_client):
#     # פתיחת קובץ CSV לכתיבה
#     with open("test2.csv", "w", newline="") as csvfile:

#         # יצירת כותב CSV
#         writer = csv.writer(csvfile)

#         # כתיבת הכותרת
#         # writer.writerow(data_first[0])

#         # כתיבת שאר הנתונים
#         # for row in data:
#         #     writer.writerow(row)
#         for row in data_from_client:
#             writer.writerow(row)
# data1 = [["rivka","dush","207401308","0583239186","-34","08.02.24"]]#,["chaim","reich","207089616","0533149731","-52","08.02.24"],["david","reich","234774438","0556666666","-100","08.02.24"]]
# פתיחת קובץ CSV לכתיבה

def write_in_csv(data):
    with open("test2.csv", "w", newline="") as csvfile:

        # יצירת כותב CSV
        writer = csv.writer(csvfile)
        data = [data]
        # כתיבת הכותרת
        # writer.writerow(data_first[0])
        writer.writerow(data)
        # כתיבת שאר הנתונים
        # for row in data:
        #     writer.writerow(row)
        # for row in data:
        #     writer.writerow(row)
def sort_in_csv():
    with open("test.csv", "r", newline="") as csvfile:
        list_of_all_client = []
    # יצירת קורא CSV
        reader = csv.reader(csvfile)

    # קריאה שורה אחר שורה
        for row in reader:
            # print(row)



            # for i in row:
            #     if i == None:
            #         i = "Error"
            list_of_all_client.append(row)

            list_of_all_client.sort(key=lambda x: int(x[4]))
        # print(list_of_all_client)
            print(f"id number: {row[2]},dept: {row[4]}")
    return [row[2],row[4]]
        # return f"id number: {row[2]},dept: {row[4]}"

        # total = -1000
        # list_min = []
        # מיון לפי חוב 
        # for list1 in list_of_all_client:
        #     if (int(list1[4])) > total:
        #         total = int(list1[4])
        #         list_min = list1

        # print(f"total: {total},list_minimum: {list_min}")







def handle_connection(socket, server_socket):
    while True:
        # Receive data from the client and echo it back
        data = socket.recv(1024).decode()
        data2 = ''
        if data == "select dept":
            data2 = sort_in_csv()
        # print(f"Received data: {data}")

        # time.sleep(1) 
        # write_in_csv(data.encode('utf-8'))  
        data3 = [[data]]  
        # write_in_csv(data)
        # write_in_csv(data1)
        print(data)

        # Echo back the received data
        socket.sendall(data2.encode())
        

        # Close the connection with the client
        # client_socket.close()

        if "bye" in data:
            server_socket.close()

host = '127.0.0.1'
port = 12346

# Create a TCP socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for 5 incoming connections
server_socket.listen(5)

print(f"Server listening on {host}:{port}")

while True:
    # Wait for a connection from a client
    # try:
    # read_in_csv()

    print("waiting")
    client_socket, client_address = server_socket.accept()
    # except OSError:
    #     break
    print(f"Accepted connection from {client_address}")

    t = Thread(target=handle_connection, args=(client_socket, server_socket))
    t.start()

        