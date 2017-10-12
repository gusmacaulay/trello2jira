Trello2Jira
===========

Trello2Jira grabs trello cards via the trello rest api and transforms them into Jira json import format. Functionality very basic but it works with Jira json import (tested with Jira 6.4.6). issueType is hardcoded to 'Bug'.

Install
=======

virtualenv env

. env/bin/activate

pip install -r requirements.txt

Usage
=====

python trello2jira.py YOUR_TRELLO_KEY  BOARD_ID  JIRA_PROJECT_NAME > jira.json
