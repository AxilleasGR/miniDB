from database import Database
import socket 
import sys
from io import StringIO
import re

def trexa(receiver):
    good = False
    try:
        if receiver:  
            usr_input = conn.recv(1024)
            usr_input = usr_input.decode("utf-8")
            db = Database('vsmdb', load=True)
            splitted = usr_input.split(" ", 3)
            try:
                if splitted[0] == "SELECT":
                    if splitted[1] == "*":
                        good = True
                        table = splitted[3]
                        output = sys.stdout
                        dbout = StringIO()
                        sys.stdout = dbout
                        db.select(table,'*')
                        sys.stdout = output
                        dbout_string = dbout.getvalue()
            except:
                conn.sendall(str.encode("Lathos kati"))                            
    except:
        conn.sendall(str.encode("Lathos kati"))
        conn.close()
    if(good):
        conn.sendall(str.encode(dbout_string))
    else:
        conn.sendall(str.encode("Lathos kati"))
    print("The info you requested has been sent")
    conn.close()
    exit()

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(('127.0.0.1',54321))
        s.listen()        
        conn, addr = s.accept()        
        with conn:
            trexa(True)
            s.close()
            continue