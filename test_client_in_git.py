from threading import Thread
import socket



host = '127.0.0.1'
port = 12346

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))


def rec(client_socket):
    while True:
        print("waiting")
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")

Thread(target=rec, args=(client_socket,)).start()


class Test_client():
    def __init__(self) -> None:
        pass

    def chek_alpha(data):
        try:
            data = data.isalpha()
        except:
            print("the details is uncorrect.")

    "set first name=Moshe, second name=Berdichevsky, id=123456789, phone=0544123456, date=3/4/2022, dept=-300"
    def cut_the_details(data):
        set = 'set'
        a = data[2][5:-1]
        b = data[4][5:-1]
        c = data[5][3:-1]
        d = data[6][6:-1]
        e = data[7][5:-1]
        f = data[8][5:]
        list_of_cusomer = set,a,b,c,d,e,f

        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        return list_of_cusomer

test = Test_client

while True:
    message = input("==> ").lower()
    message = message.split()
    print(message)

    
    if message[0] == "set":
        if message[1] == "first":
            if message[2][:5] == "name=":
                if message[3] == "second":
                    if message[4][:5] == "name=":
                        if message[5][:3] == "id=":
                            if message[6][:6] == "phone=":
                                if message[7][:5] == "date=":
                                    if message[8][:5] == "dept=":
                                        print("succsesful")
                                        message = test.cut_the_details(message)
                                    else:
                                        print("you need to type 'dept='")
                                        continue
                                else:
                                    print("you need to type 'date='")
                                    continue
                            else:
                                print("you need to type 'phone='")
                                continue        
                        else:
                            print("you need to type 'id='")
                            continue
                    else:
                        print("you need to type 'name='")
                        continue
                else:
                    print("you need to type 'second'")
                    continue
            else:
                print("you need to type 'name='")
                continue
        else:
            print("you need to type 'first'")
            continue

    if "quit" in message or "bye" in message:
        break
    message =" ".join(message)
    print(message)
    client_socket.send(message.encode('utf-8'))
    print("sended")



client_socket.close()
