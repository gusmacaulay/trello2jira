import json
from jsonbender import bend, K, S, F
import pycurl
import sys
from StringIO import StringIO
from datetime import datetime


def dateFix(hashID):
    return datetime.fromtimestamp(int(hashID[0:8], 16)).strftime("%Y-%m-%d %H:%M:%S")

key = sys.argv[1]
board = sys.argv[2]

print "key: " + key
print "board: " + board

buffer = StringIO()
c = pycurl.Curl()
# c.setopt(c.VERBOSE, True)
c.setopt(c.URL, 'https://api.trello.com/1/boards/' + board + '/cards?key=' + key)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
source = json.loads(body)
print (json.dumps(source))
mapping = {
    'card': (S('name')),
    'created': (S('id')) >> (F(dateFix))
    }

for card in source:
    result = bend(mapping, card)
    print(json.dumps(result))
