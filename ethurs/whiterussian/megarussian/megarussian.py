import struct, random, re
from socket import *

SIGNATURE_FILE = "signature.secret"
SECRET_FILE = "flag.txt"
HOST = ""
PORT = 7331

secrets = {}

def serve():
    s = socket(AF_INET, SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    while True:
        data, addr = s.recvfrom(999)
        print "Received {} bytes from {}:{}.".format(len(data), *addr)
        s.sendto(mega_russian(data), addr)
    return

def sign(secret, title):
    signature = file(SIGNATURE_FILE).read()
    sec_chars = secret[:2]
    title = sec_chars + title
    hashed = ""
    for i in range(len(title)):
        hashed += "%02x" % (ord(title[i]) ^ ord(signature[i % len(signature)]))
    return hashed

def mega_russian(data):
    response = "Welcome to MegaRussian: best secure secret sharing service in country.\n"
    upload_pat = re.compile(r"upload #(.+)# #(..+)#")
    download_pat = re.compile(r"download #(..+)# #(.+)#")
    up = upload_pat.match(data.strip())
    down = download_pat.match(data.strip())
    if up:
        secret = up.group(1)
        title = up.group(2)
        if title != 'megasecret_superuber_top_secret_magic_stuff':
            auth = sign(secret, title)
            secrets[title] = (secret, auth)
            response += "Your secret is stored! Please retain the following authentication code: %s.\n" % auth
        else:
            response += "You cannot overwrite this master secret!\n"
    elif down:
        title = down.group(1)
        auth = down.group(2)
        if title in secrets.keys():
            the_secret = secrets[title]
            if the_secret[1] == auth:
                response += "Here is your secret: %s.\n" % the_secret[0]
            else:
                response += "That is the wrong authentication code!\n"
        else:
            response += "That secret does not exist!\n"
    else:
        response += """To upload, send a request like so: "upload #<secret># #<title>#"
To download: "download #<title># #<authentication>#"
"""
    return response
    
mega_secret = "Here is your flag: " + file(SECRET_FILE).read()
mega_title = 'megasecret_superuber_top_secret_magic_stuff'
secrets[mega_title] = (mega_secret, sign(mega_secret, mega_title))
serve()
