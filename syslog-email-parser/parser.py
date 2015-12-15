#!/usr/bin/python

# Author: James Attard [info@jamesattard.com]
# Date: 12/12/2015
# Client: Help Scout

import re

logfile = "./test-sample.log"

file = open(logfile, 'r')
for line in file:
	# Match only Relevant lines (i.e. contain an email address)
	match = re.search(r'id=[\w\.-]+@[\w\.-]+', line)
	if match is not None:
		print "Line: " + line
		# MessageID starts with "id="
		messageid = re.search(r'id=([\w\.-]+@[\w\.-]+)', line)
		print "Message ID: " + messageid.group(1)
		# Topic starts with with "T="
		topic = re.search(r'T=("+[\w\W]+)', line)
		print "Topic: " + topic.group(1)
