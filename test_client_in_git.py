from threading import Thread
import socket
from customer import Customer


host = '127.0.0.1'
port = 12346

# Create a TCP socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

def rec(client_socket):
    print("waiting")
    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode('utf-8')}")

Thread(target=rec, args=(client_socket,)).start()

def details():
    list_of_details = ''
    a_name = input("first_name:")
    list_of_details + a_name
    a_last_name = input("second_name:")
    list_of_details.append(a_last_name)
    a_id = input("id:")
    list_of_details.append(a_id)
    a_phone = input("phone:")
    list_of_details.append(a_phone)
    a_date = input("date:")
    list_of_details.append(a_date)
    a_dept = input("dept:")
    list_of_details.append(a_dept)
    return list_of_details

while True:
    # Send data to the server
    message = input("==> ")
    # print(message)
    # a = [["set", "first name=Moshe", "second name=Berdichevsky", "id=123456789", "phone=0544123456", "date=3/4/2022","dept=-300"]]




    a = ["rivka","dush","207401308","0583239186","-34","08.02.24"]
    



    # message = str(a)
    # message = str(a)
    # if message == "set":
    #     a = details()
    #     message = a
    # if message[0] == "select":
    #     message = message[1]
    client_socket.send(message.encode('utf-8'))
    print("sended")

    # Receive the echoed data from the server
    if "done" in message or "bye" in message:
        break

# Close the connection with the server
client_socket.close()
