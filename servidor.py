import socket 

def server (host ='localhost', port=42000):
    data_payload = 1024 #Tamanho máximo da mensagem 1024 b
    # Criação do TCP socket
    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Habilita reutilização de endereço e porta address/port 
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
    server_address = (host, port)
    print ("Starting up echo server  on %s port %s" % server_address)
    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
    sock.listen(32) 
    i = 0
    while True: 
        print ("Waiting to receive message from client")
        client, address = sock.accept() 
        data = client.recv(data_payload) 
        if data:
            print ("Data: %s" %data)
            client.send(data)
            print ("sent %s bytes back to %s" % (data, address))
            # end connection
            client.close()
            i+=1
            if i>=32: break           
server()    