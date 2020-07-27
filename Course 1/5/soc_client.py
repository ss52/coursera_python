import socket


sock = socket.socket()  # лучше использовать конструкцию with ...
sock.connect(("127.0.0.1", 10001))
# sock = socket.create_connection(("127.0.0.1", 10001))  # вот так короче
sock.sendall("ping".encode("utf8"))
sock.close()
