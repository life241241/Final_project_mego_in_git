


import csv
import socket
import time
from threading import Thread


file_to_chek = 'test2.csv'

with open (r"C:\Users\LIFE2\Desktop\mego\.py\class 1\test2.py\test2.csv", 'r' ,newline="") as filecsv:
# with open (r"C:\Users\LIFE2\Desktop\mego\.py\class 1\test2.py\db.csv", 'r' ,newline="") as filecsv:

# with open (r"C:\Users\LIFE2\Desktop\mego\.py\class 1\test2.py\db.csv", 'r' ,newline="") as filecsv:
            list_clients = []

            reader = csv.reader(filecsv)
            for row in reader:
                list_clients.append(row)
            list_clients.sort(key=lambda x: int(x[5]),reverse=True)


class Test_of_list_csv:
    def __init__(self,file_csv):
        self.file = file_csv
    
    def chek_len_id(self,file):
        total_errors = 0
        for i in file:
            if len(i[2]) != 9:
                # print(f"The id {i[2]} of {i[0]} {i[1]} is not correct!")
                total_errors +=1
        return total_errors
            
    def chek_len_phone(self,file):
        total_errors = 0
        for i in file:
            if len(i[3]) != 10:
                # print(f"The number {i[3]} of {i[0]} {i[1]} is not correct!")
                total_errors +=1
        return total_errors

    def chek_no_value(self,file):
        num = 0
        total_errors = 0
        for row in file:
            num += 1
            for i in range(len(row)):
                if row[i] == '':
                    # print(f"it's no value in line {num}")
                    total_errors +=1
        return total_errors

    def chek_name_id(self,file):
        total_errors = 0
        for i in range(len(file)):
            for j in range(i+1,len(file)):
                if file[i][2] == file[j][2]:
                    # print("The id is not the same value on the names")
                    total_errors  += 1
                    # check_name(file[i][0],file[i][1],file[j][0],file[j][1])
                    break
        return total_errors
    
    def total_dept(self,file):
        list_dept = []
        for k in file:
            if len(list_dept) == 0:
                list_dept.append(k)
                continue
            for t in list_dept:
                if k[2] == t[2]:
                    t[5] = str(int(t[5]) + int(k[5]))
                    break
                if list_dept[-1] == t:
                    list_dept.append(k)
                    break
                
        return list_dept


test = Test_of_list_csv(list_clients)
a = test.chek_len_id(list_clients)
b = test.chek_len_phone(list_clients)
c = test.chek_no_value(list_clients)
d = test.chek_name_id(list_clients)
e = test.total_dept(list_clients)
# print(list_clients)
list_clients = e
print(f"Deitails to fix:\n {a} id's is not correct,\n {b} phon's is not correct,\n {c} value is missing,\n {d} id's is not the same names.")






class File:
    def __init__(self,filename):
        self.filename = filename
        # print(self.sort_name())
        




    def write_in_csv(self,data):
        with open(self.filename, "w", newline="") as csvfile:

            writer = csv.writer(csvfile)
            data = [data]
            writer.writerow(data)
    


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

    

    def sort_name1(self,value,list_client):
        list_client_name = []
        # value = "".join(value)
        for row in list_client:
            if row[0] == value:
                list_client_name.append(row)
        list_client_name.sort(key=lambda x: int(x[5]),reverse=True)
        return list_client_name
    

    def sort_id(self,value,list_client):
        list_client_id = []
        for row in list_client:
            if row[2] == value:
                list_client_id.append(row)
        return list_client_id
    

    def sort_last_name(self,value,list_client):
        list_client_name = []
        # value = "".join(value)
        for row in list_client:
            if row[1] == value:
                list_client_name.append(row)
        # list_client_name.sort(key=lambda x: int(x[5]),reverse=True)
        return list_client_name
    def sort_phone(self,value,list_client):
        list_phone = []
        for row in list_client:
            if row[3] == value:
                list_phone.append(row)
        return list_phone
        



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
        if data2[0] == "select":
            if data2[1] == "dept":
                return_data2 = file.sort_dept1(data2[2],list_clients)
            elif data2[1] == "first" and data2[2] == "name":
                return_data2 = file.sort_name1(data2[3],list_clients)
            elif data2[1] == "last" and data2[2] == "name":
                return_data2 = file.sort_last_name(data2[3],list_clients)
            elif data2[1] == "id":
                return_data2 = file.sort_id(data2[2],list_clients)
            elif data2[1] == "phone":
                return_data2 = file.sort_phone(data2[2],list_clients)
        else:
            return_data2 = ["Enter again your search!"]
        print(return_data2)



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
