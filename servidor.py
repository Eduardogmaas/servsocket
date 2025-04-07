import socket 

#exemplo fornecido pelo tutorial disponivel nos slides da atividade
#def server (host ='localhost', port=42000, timeout=60):
#    data_payload = 1024 #Tamanho máximo da mensagem 1024 bytes
    # Criação do TCP socket
#    sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
    # Habilita reutilização de endereço e porta address/port 
#    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # Bind the socket to the port
#    server_address = (host, port)
#    print ("Starting up echo server  on %s port %s" % server_address)
#    sock.bind(server_address)
    # Listen to clients, argument specifies the max no. of queued connections
#    sock.listen(32) 
#    i = 0
#    while True: 
#        print ("Waiting to receive message from client")
#        client, address = sock.accept() 
#        data = client.recv(data_payload) 
#        if data:
#            print ("Data: %s" %data)
#            client.send(data)
#            print ("sent %s bytes back to %s" % (data, address))
#            # end connection
#            client.close()
#            i+=1
#            if i>=32: break           
#server()    

#exemplo adaptado
def server(host='localhost', port=42000, timeout=60):
    data_payload = 1024  # Tamanho máximo da mensagem (em bytes)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print(f"Iniciando servidor IRC em {host} na porta {port}")
    sock.bind(server_address)
    sock.listen(5)  # permite até 5 conexões pendentes

    while True:
        print("Aguardando conexão do cliente...")
        client_socket, client_address = sock.accept()
        client_socket.settimeout(timeout)

        try:
            print(f"Conexão recebida de {client_address}")
            # Recebe o nome do usuário
            username = client_socket.recv(data_payload).decode('utf-8')
            print(f"Usuário conectado: {username}")

            # Espera mensagem
            print("Aguardando mensagem do cliente...")
            message = client_socket.recv(data_payload).decode('utf-8')
            if message:
                print(f"[{username}]: {message}")
                # Envia a mesma mensagem de volta
                client_socket.sendall(f"[Servidor echo] {message}".encode('utf-8'))

        except socket.timeout:
            print("Tempo de conexão excedido. Encerrando conexão.")
        except Exception as e:
            print(f"Erro durante a conexão: {e}")
        finally:
            print("Encerrando conexão com o cliente.")
            client_socket.close()

server()