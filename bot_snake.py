import socket
import random

class MySocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        try:
            self.sock.connect((host, port))
            print("Connection OK!")
        except:
            print("Connection failed")

    def mysend(self, msg):
        totalsent = 0
        try:
            sent = self.sock.send(msg[totalsent:])
            print("message sent!")
        except:
            if sent == 0:
                raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent
        print(str(totalsent) + " char sent")

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        chunk = self.sock.recv(1024)
        if chunk == b'':
            raise RuntimeError("socket connection broken")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)

    def mychat(self, msg):
        totalsent = 0
        try:
            sent = self.sock.send(msg[totalsent:])
            print("chat sent!")
        except:
            raise RuntimeError("socket connection broken")
        totalsent = totalsent + sent
        print(str(totalsent) + " char chat sent")

def getGame(msg):
    array = msg.split("|")
    width = array[1]
    height = array[2]
    player_id = array[3]
    print("GAME Packet")
    print("width: " + str(width))
    print("height: " + str(height))
    print("player_id: " + str(player_id))

def getPlayer(msg, socket):
    array = msg.split("\\n")
    for word in array:
        if 'player' in word and 'Sautchuk' in word:
            print(word)
        if 'pos' in word:
            print(word)
        elif 'tick' in word:
            moveSnake(socket)

def getDie(msg):
    array = msg.split("\\n")
    for word in array:
        if 'pos' in word:
            print(word)

def moveSnake(socket):
    directions = ['left', 'right', 'up', 'down']
    direction = random.choice(directions)
    print(direction)
    msg = 'move|' + direction + '\n'
    socket.mysend(msg.encode())

socketTest = MySocket()    
socketTest.connect("gpn-tron.duckdns.org", 4000)
print(socketTest.myreceive())
socketTest.mysend(b'join|Sautchuk|passsupersecret\n')
#msg = b'player|0|masterX244\nplayer|1|Frog2\nplayer|2|bot0\nplayer|3|John Doe v2\nplayer|4|blah\nplayer|5|bene-bot\nplayer|6|deki\nplayer|7|anselm\nplayer|8|vbot\nplayer|9|bot1\nplayer|10|I tried python, but it slow\nplayer|11|the better random!\nplayer|12|SolidTux\nplayer|13|moku\nplayer|14|bot diffv2\nplayer|15|hemi3\nplayer|16|Have you tried Rust?\nplayer|17|Open Source Anarcho Communist\nplayer|18|NobodysNightmare\nplayer|19|Where_am_I\nplayer|20|michael-1.0.3\nplayer|21|runs in O(n!)\nplayer|22|Sautchuk\nplayer|23|julian\nplayer|24|oolongSlayer\nplayer|25|GLaDOS v0.0\nplayer|26|Clutch Machine\nplayer|27|Kontroller\nplayer|28|Logogistiksv0.0\npos|0|0|0\npos|1|2|2\npos|2|4|4\npos|3|6|6\npos|4|8|8\npos|5|10|10\npos|6|12|12\npos|7|14|14\npos|8|16|16\npos|9|18|18\npos|10|20|20\npos|11|22|22\npos|12|24|24\npos|13|26|26\npos|14|28|28\npos|15|30|30\npos|16|32|32\npos|17|34|34\npos|18|36|36\npos|19|38|38\npos|20|40|40\npos|21|42|42\npos|22|44|44\npos|23|46|46\npos|24|48|48\npos|25|50|50\npos|26|52|52\npos|27|54|54\npos|28|56|56\ntick\nmessage|0|Red 5 standing by\nmessage|28|Let t'
#getPlayer(str(msg))
while True:
    msg = str(socketTest.myreceive())
    print(msg)
    if 'game' in str(msg):
        getGame(msg)
    elif 'die' in msg:
        getDie(msg)
    elif 'lose' in msg:
        print(msg)
    elif 'player' in msg:
        getPlayer(msg, socketTest)
    elif 'tick':
        moveSnake(socketTest)        
