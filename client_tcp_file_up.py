import socket
import sys
import base64
def main():
    serverIp = "127.0.0.1"
    serverPort = 8081
    # creat Socket tcp
    print("Starting socket:Tcp...")
    socketTcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverAddress = (serverIp, serverPort)
    # connect on server
    while True:
        try:
            print("Connecting to server @%s:%d" % (serverIp, serverPort))
            socketTcpClient.connect(serverAddress)
            break
        except Exception:
            print("Can't connect to server!")
            continue

    # upload data
    print("upload file!")
    file_name = input('Please input your file name!\n>>')
    socketTcpClient.send(file_name.encode())
    while True:
        flag = socketTcpClient.recv(1024)
        if flag:
            with open(file_name, 'rb') as f:
                buf = base64.b64encode(f.read())
                socketTcpClient.send(buf)
                print("finished uploading!")
            break
    socketTcpClient.close()


main()