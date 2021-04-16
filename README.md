# RevShell
A tool to grant access to a target machine via a reverse shell

## Instructions
Editing the client.py file 

Fill in the host in

    host = ''
    This should be the IP or Hostname of the Attacker machine

Run the server script on the attacker machine using

    python3 server.py
    
Run the client script on the target machine

    python3 client.py

## Creating Windows executable (Only on linux)

To create aa windows executable, run the setup.sh in terminal

    bash setup.sh
    
The script will install cx_Freeze and build the executable. At the end it will show the path to the executable. (It's usually somewhere inside the build folder)

## The interactive shell
The interactive shell starts with a #

Commands for the interactive shell

    list - lists out the connections received
    select <target number> - selects target
    connect - connects to the reverse shell
    quit - quits out of the program and drops all connections

The reverse shell after connection becomes >>> with the current working directory preceding it

Commands for the reverse shell

    os info - prints info about the OS
    quit - quits the reverse shell, but does not drop the connection.
    
## Using the scripts

To connect back to a previous connection, use the list command in interactive shell, select the connection and connect

![image](https://user-images.githubusercontent.com/70275323/114598481-918bcc00-9caf-11eb-8621-99fc5f26623e.png)

Interactive shell has started.

![image](https://user-images.githubusercontent.com/70275323/114598671-cac43c00-9caf-11eb-96ad-9528eb58e625.png)

The Connection sent by the client has been accepted.
(The script shows an error, and retries once completing the connection on the second try)

![image](https://user-images.githubusercontent.com/70275323/114598917-137bf500-9cb0-11eb-8f53-2be4066552da.png)

Listing connections and selecting them by serial number

![image](https://user-images.githubusercontent.com/70275323/114599075-40c8a300-9cb0-11eb-8d8f-71dfc245e2bb.png)

After connection, the interactive prompt changes to the reverse shell (#> becomes >>>)
The client will now accept single line commands

![image](https://user-images.githubusercontent.com/70275323/114599974-6dc98580-9cb1-11eb-87ec-f8458bf9a04b.png)

As you can see, most basic single line commands work perfectly.
Some commands like 

        echo <text to write> > <filename>    # or
        cd ..
        
        
Will cause the script to execute the command but freeze the scipt. 

Plans for the next update include - 

Allowing creation of files

Fixing the broken change directory function

Support for windows, .exe file, and autorun disk payload

Coming soon
