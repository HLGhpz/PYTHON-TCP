import socket
import sys
import base64


def main():
    hostIp = "127.0.0.1"
    hostPort = 8081
    length = 0
    # creat Socket tcp
    print("Starting socket:Tcp...")
    socketTcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # bind ip and port
    print("Tcp server listen @%s:%d" % (hostIp, hostPort))
    hostAddress = (hostIp, hostPort)
    socketTcpServer.bind(hostAddress)
    socketTcpServer.listen(5)

    while True:
        # accept client
        socketClient, (clientIp, clientPort) = socketTcpServer.accept()
        print("Connection accepted from @%s:%d." % (clientIp, clientPort))
        #msg="welcome client!\r\n"
        # socketClient.send(msg.encode('utf-8'))
        # receive data
        print("waiting for data...")

        while True:
            flie_name = socketClient.recv(1024)
            if flie_name:
                flie_name = flie_name.decode()
                socketClient.send('OK'.encode())
                while True:
                    data = socketClient.recv(1024)
                    if not data:
                        break
                    length += len(data)
                    with open('recv' + flie_name, 'ab+') as f:
                        f.write((base64.b64decode(data)))
            socketClient.close()
            print("Close Socket")
            break


main()
