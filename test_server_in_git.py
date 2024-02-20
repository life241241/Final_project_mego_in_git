


import csv
import socket
import time
from threading import Thread


file_to_chek = 'test2.csv'

with open ('test2.csv', 'r' ,newline="") as filecsv:
            list_clients = []

            reader = csv.reader(filecsv)
            total_value = 0
            for row in reader:
                for i in range(len(row)):
                    if row[i] == '':
                        row[i] = 'No value'
                        total_value += 1 
                    for j in range(len(list_clients)):
                        if row[2] == list_clients[j][2]:
                            list_clients[j][5] = str(int(list_clients[j][5]) + int(row[5]))
                            row = None
                            break
                    if row is None:
                        break
                if row is not None:
                    list_clients.append(row)
            list_clients.sort(key=lambda x: int(x[5]),reverse=True)
            # print(list_of_all_clients)
            # for row1 in list_clients:
            #     a = " ".join(row1)
            #     list_clients.append(a)
                # print(row1)
print(list_clients)
print (f"total of no value:{total_value}")







class File:
    def __init__(self,filename):
        self.filename = filename
        # print(self.sort_name())
        




    def write_in_csv(self,data):
        with open(self.filename, "w", newline="") as csvfile:

            writer = csv.writer(csvfile)
            data = [data]
            writer.writerow(data)
        
    def sort_dept(self):
        with open(self.filename, "r", newline="") as csvfile:
            list_of_all_client = []
            reader = csv.reader(csvfile)

        # קריאה שורה אחר שורה
            for row in reader:
                list_of_all_client.append(row)

                list_of_all_client.sort(key=lambda x: int(x[4]))
                # print(f"id number: {row[2]},dept: {row[4]}")
        return [row[2],row[4]]
    


    def sort_dept1(self,value,list_client):
        list_dept = []
        value = "".join(value)
        if value[0] == '>':
            value = int(value[1:])
            for line in list_client:
                if int(line[5]) > value:
                    list_dept.append(line)
        elif value[0] == '<':
            value = int(value[1:])
            for line in list_client:
                if int(line[5]) < value:
                    list_dept.append(line)
        elif value[0] == "=":
            value = int(value[1:])
            for line in list_client:
                if int(line[5]) == value:
                    list_dept.append(line)
        elif value[0] == "!" and value[1] == "=":
            value = int(value[2:])
            for line in list_client:
                if int(line[5]) != value:
                    list_dept.append(line)
        list_dept.sort(key=lambda x: int(x[5]),reverse=True)
        return list_dept

    

    def sort_name(self):
        with open(self.filename,'r',newline="") as csvfile:
            list_of_all_clients = []
            list_of_all_clients1 = []
            reader = csv.reader(csvfile)
            for row in reader:
                list_of_all_clients.append(row)
                list_of_all_clients.sort(key=lambda x: str(x[0]))
            # print(list_of_all_clients)
            for row1 in list_of_all_clients:
                a = " ".join(row1)
                list_of_all_clients1.append(a)
                # print(row1)
        print(list_of_all_clients1)
        return list_of_all_clients1
    

    def sort_name1(self,value,list_client):
        list_client_name = []
        # value = "".join(value)
        for row in list_client:
            if row[0] == value:
                list_client_name.append(row)
        list_client_name.sort(key=lambda x: int(x[5]),reverse=True)
        return list_client_name
        



def handle_connection(socket, server_socket, file):
    while True:
        # Receive data from the client and echo it back
        data = socket.recv(1024).decode()
        # data = input("enter a value: ")
        print(data)
        data2 = data.split()
        print(data2)
        # data2 = " ".join(data2)
        # data2 = 'test'
        if data2[0] == "select" and data2[1] == "dept":
            return_data2 = file.sort_dept1(data2[2],list_clients)
            print(return_data2)
            # data2 = " ".join(data2)
        
        elif data2[0] == "select" and data2[1] == "first" and data2[2] == "name":
            return_data2 = file.sort_name1(data2[3],list_clients)

        return_data2 = "\n".join([" ".join(item) for item in return_data2])


        socket.sendall(return_data2.encode())
        # socket.sendall(data.decode())
        

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
file = File('test2.csv')
while True:
    # Wait for a connection from a client


    print("waiting")
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    t = Thread(target=handle_connection, args=(client_socket, server_socket, file))
    t.start()
