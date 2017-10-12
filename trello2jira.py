import json
from jsonbender import bend, K, S, F
import pycurl
import sys
from StringIO import StringIO
from datetime import datetime


def dateFix(hashID):
    return datetime.fromtimestamp(int(hashID[0:8], 16)).strftime("%Y-%m-%dT%H:%M:%S")

key = sys.argv[1]
token = sys.argv[2]
board = sys.argv[3]
project = sys.argv[4]

buffer = StringIO()
c = pycurl.Curl()
c.setopt(c.VERBOSE, True)
c.setopt(c.URL, 'https://api.trello.com/1/boards/' + board + '/cards?key=' + key + '&token=' + token)
c.setopt(c.WRITEDATA, buffer)
c.perform()
c.close()

body = buffer.getvalue()
source = json.loads(body)
mapping = {
    'summary': (S('name')),
    'description' : (S('desc')),
    'updated': (S('dateLastActivity')),
    'created': (S('id')) >> (F(dateFix)),
    'issueType': 'Task'
    }

issues = []
for card in source:
    result = bend(mapping, card)
    issues.append(result)


print(json.dumps({"projects" : [{"name" : project, "issues":issues}]}))

