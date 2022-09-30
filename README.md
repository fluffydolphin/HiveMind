# HiveMind - Simple bot net in python

## What is HiveMind?
HiveMind is basically a bot net using sockets in python that can run pretty much all cli commands in Linux, Windows and MacOS (but has only been properly tested in Ubuntu Linux).

1. The server binds sockets togeather so that the client and bots can connect.
2. After the server is up you connect how ever many bots you want.
3. Then you can connact as a client with the password (default 1212 and is just expsed in text) and send cli commands to the bot simultaneously
4. There is also a slightly modified version of Slowloris (credit to the contributors at https://github.com/gkbrk/slowloris) so you can run a DDOS attack (educational purposes), but that's just an example you can pretty much put anything you want in there as long as you can run it in cli.

## How to install and run?

How to install git for cloning

1. Install git
   ```sh
   sudo apt install git
   ```



If you want to clone using git, here's how you do it.

1. Clone the repo
   ```sh
   git clone https://github.com/fluffydolphin/HiveMind.git
   ```
2. Cd into server, client or bot
   ```js
   cd server
   ```
   ```js
   cd client
   ```
   ```js
   cd bot
   ```
3. Run command for either server, client or bot
   ```js
   python3 server
   ```
   ```js
   python3 client
   ```
   ```js
   python3 bot
   ```
  
That's all it takes to install and run HiveMind.

## Commands and Configuration for HiveMind

* !help!
* * Shows you this
* !connected!
* * Shows you how many and which bots are connected

* When you run bot.py it will ask you what number bot you want this to be eg 1, 10 or 12 and the full bot name will be bot- the number you selected eg bot-2, bot-8 or bot-17. 


## Configuration options for Slowloris
It is possible to modify the behaviour of slowloris with command-line
arguments. In order to get an up-to-date help document, just run
`slowloris -h`.

* -p, --port
* * Port of webserver, usually 80
* -s, --sockets
* * Number of sockets to use in the test
* -v, --verbose
* * Increases logging (output on terminal)
* -ua, --randuseragents
* * Randomizes user-agents with each request
* -x, --useproxy
* * Use a SOCKS5 proxy for connecting
* --https
* * Use HTTPS for the requests
* --sleeptime
* * Time to sleep between each header sent
* --duration
* * Time you want it to run for (not consistent can differ by about 2 or 3 attacks)
