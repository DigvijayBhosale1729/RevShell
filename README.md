# RevShell
A tool to grant access to a target machine via a reverse shell

## Instructions
Edit the client.py file 
Fill in the host in

    host = ''
    This should be the IP or Hostname of the Attacker machine

Run the server script on the attacker machine using

    python3 server.py
    
Run the client script on the target machine

    python3 client.py
    
###The interactive shell
The interactive shell starts with a #
The reverse shell after connection becomes >>> with the current working directory preceding it
Commands for the interactive shell

    list - lists out the connections received
    select <target number> - selects target
    connect - connects to the reverse shell
    quit - quits out of the program and drops all connections

Commands for the reverse shell

    os info - prints info about the OS
    quit - quits the reverse shell, but does not drop the connection.
