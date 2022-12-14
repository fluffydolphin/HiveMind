# HiveMind - Simple bot net in python

## What is HiveMind?
HiveMind is basically a bot net using sockets in python that can run pretty much all cli commands in Linux, Windows and MacOS (but has only been properly tested in Ubuntu Linux).

1. The server binds sockets together so that the client and bots can connect.
2. After the server is up you connect how ever many bots you want.
3. Then you can connact as a client with the password (default 1212 and is just expsed in text) and send cli commands to the bots simultaneously
4. There is also a slightly modified version of Slowloris (credit to the contributors at https://github.com/gkbrk/slowloris) so you can run a DDOS attack (educational purposes), but that's just an example you can pretty much put anything you want in there as long as you can run it in cli.

## How to install and run?

How to install git for cloning

1. Install git
   ```sh
   sudo apt install git
   ```



Cloning using git.

1. Clone the repo
   ```sh
   git clone https://github.com/fluffydolphin/HiveMind.git
   ```
   
2. Cd into HiveMind
   ```sh
   cd HiveMind
   ```
   
2. Cd into server, client or bot
   ```sh
   cd server
   ```
   ```sh
   cd client
   ```
   ```sh
   cd bot
   ```
3. Run command for either server, client or bot
   ```sh
   python3 server
   ```
   ```sh
   python3 client
   ```
   ```sh
   python3 bot
   ```
  
That's all it takes to install and run HiveMind.

## Commands and Configuration for HiveMind
It is possible to modify the behaviour of HiveMind with cli
arguments. In order to get an up-to-date help document, just run
`client -h`.

you can change the server ip on the client and bot but not on the server, the default host ip on the server is 0.0.0.0 (localhost).

* -p, --port
* * Port of the Server, default 5000 
* -b, --bot
* * The bot number this is (this argument is only for the bots)


These commands are for after you have started HiveMind and adjusted the behaviour

* !help!
* * Shows you this
* !connected!
* * Shows you how many and which bots are connected
* !slowloris!
* * Shows you the help command for Slowloris https://github.com/fluffydolphin/HiveMind/blob/master/README.md#configuration-options-for-slowloris
* !quit!
* * This is used for quiting either the client or the bot (you have to use this or else you will get a broken pipe error) 


## Configuration options for Slowloris
It is possible to modify the behaviour of slowloris with cli
arguments. In order to get an up-to-date help document, just run
`slowloris -h`(if you run any of these arguments that give a direct output to the cli then they will not be displayed in the client, but they are still outputting on the bots).

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
* * Time you want it to run for (not consistent can differ by about 2 or 3 attacks and if this argument is not added then it will go untill you go to all bots and control + c)
