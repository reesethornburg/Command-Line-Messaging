# A2
A2 is a Python project made of two scripts (server.py and client.py) that is meant to simulate a messaging app able to support up to three clients. It was created as a requirement for the completion of Assignment 2 in CS3640 at the University of Iowa by Reese Thornburg (hawkid: rethornburg).

## server.py

The server.py script is the Python file that will initialize the server for the messaging app. In order to run, call the server.py file along with the port number you wish to use (e.g. 5000).

```bash
python3 server.py 'your port number here'
```

## client.py

The client.py script is the Python file that is used to initialize the client side of the script. In order to run the client script, you need both the port number and IP of the server. For testing, 'localhost' was used in the place of the IP address. The script is called as follows.

```bash
python3 client.py 'your IP address here' 'your port number here'
```

## Credit Reel

### A Complete Guide to Socket Programming in Python
[A Complete Guide to Socket Programming in Python](https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python) by Serhii Orlivski was extremely helpful in setting up the sockets in a way that they could connect with one another as well as providing examples for what socket programming should look like.

### Python Socket Documentation
The Python3 [Socket](https://docs.python.org/3/library/socket.html) documenation offered insight into what the various functions and methods under the socket library did.

### Python Threading Documentation
The Python3 [Threading](https://docs.python.org/3/library/threading.html) documentation offered insight into what the various functions and methods under the threading library did.

### CS 50 Software Design and Implementation
Lecture 19 of [CS 50 Software Design and Implementation](https://www.cs.dartmouth.edu/~campbell/cs50/socketprogramming.html) from Dartmouth University helped to introduce and explain the purpose of sockets. This site was obtained through the homepage of the CS3640 Canvas page.

### Lecture 9 Socket Programming
[Lecture 9 Socket Programming](https://sites.radford.edu/~hlee3/classes/itec350_spring2021/ClassNotes/Lecture9_SocketProgramming.pdf) slides from Radford University helped to introduce and explain the purpose of sockets. This site was obtained through the homepage of the CS3640 Canvas page.

### Make a README
[Make a README](https://www.makeareadme.com/) was useful in showing the formatting and syntax of a README and .md files.
