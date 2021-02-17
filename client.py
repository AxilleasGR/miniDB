import socket

input_query = input(
    "Insert the query you want to send to the server\n example: SELECT * FROM classroom\nInput: ")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sok:
    while True:
        sok.connect(('127.0.0.1',54321))
        sok.sendall(input_query.encode())
        data = sok.recv(1000)
        print('Received response from server\n', data.decode('utf8', 'strict'))
        sok.close()
        print("Goodbye")
        exit()