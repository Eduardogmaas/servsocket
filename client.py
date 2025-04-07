import socket

#exemplo fornecido pelo tutorial disponivel nos slides da atividade
#def client(host = 'localhost', port=42000): 
    # Create a TCP/IP socket 
#    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # Connect the socket to the server 
#    server_address = (host, port) 
#    print ("Connecting to %s port %s" % server_address) 
#    sock.connect(server_address) 
    # Send data 
#    try: 
        # Send data 
#        message = "Test message. This will be echoed" 
#        print ("Sending %s" % message) 
#        sock.sendall(message.encode('utf-8')) 
        # Look for the response 
#        amount_received = 0 
#        amount_expected = len(message) 
#        while amount_received < amount_expected: 
#            data = sock.recv(16) 
#            amount_received += len(data) 
#            print ("Received: %s" % data) 
#    except socket.error as e: 
#        print ("Socket error: %s" %str(e)) 
#    except Exception as e: 
#        print ("Other exception: %s" %str(e)) 
#    finally: 
#        print ("Closing connection to the server") 
#        sock.close() 
#client()

#exemplo adaptado
def client(host='localhost', port=42000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)

    try:
        print(f"Conectando ao servidor {host} na porta {port}...")
        sock.connect(server_address)

        # Envia nome do usuário
        username = input("Digite seu nome de usuário: ")
        sock.sendall(username.encode('utf-8'))

        # Envia mensagem
        message = input("Digite uma mensagem para enviar: ")
        sock.sendall(message.encode('utf-8'))

        # Recebe resposta do servidor
        data = sock.recv(1024)
        print(f"Resposta do servidor: {data.decode('utf-8')}")

    except socket.error as e:
        print(f"Erro de socket: {e}")
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        print("Encerrando conexão com o servidor.")
        sock.close()

client()
