#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  alertmailer.py
#  
#  Copyright 2017 stak <stakovahflow666@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  This python application will connect via SMTP in order to
#  send alerts to defined email addresses.
#  Personally used in order to track when servers/desktops
#  go online in a home network.
#  
#  Todo: 
#  Upload Windows, Linux, and Mac information for the
#  application to be run at boot.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os, sys, smtplib, socket, platform, urllib2, time, base64
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import datetime


# Define our global variables:
# Timestamp:
trampstamp = datetime.datetime.now()

# Get the local machine's hostname:
hostname = socket.gethostname()

# Mail server:
mailserver = 'smtp.gmail.com'
mailport = 587

# Sender's email address:
fromaddr = '<from-address>@gmail.com'
fromname = '<email sender name>'

# Sender's password:
obscurePass = base64.b64decode('<super secret squirrel base64-encoded password>')
"""
Note: To obtain the base64-encoded password, run the 
following commands at the Python CLI:
>>> import base64
>>> base64.b64encode ('yourdrowssap')
"""

# Recipient's email address:
toaddr = '<to-address>@gmail.com'

# Sleep timer:
backoff = 10

# Unable to reach remote host debug message:
netdown = 'Nope. D.E.D. Dead. Not yet party time.'

# Able to reach remote host debug message:
netup   = 'It\'s live! Time to party!\n'

# Email signature:
mailSig = 'Thanks!\n'
mailSig = mailSig + '--<signature name>\n'
mailSig = mailSig + '<from-address>@gmail.com'

# We're going to reach out to Google anyway, so 
# that's the predefined variable
# Remote host to test internet connectivity:
remotehost = 'www.google.com'

# Set the debug flag: 0 == off, 1 == on
# (This just prints stuff so you see what the recipient sees)
debugger = 0

# If debugging is on, set output to stdout (1) & stderr (2):
if debugger == 1:
	sys.stdout = sys.__stdout__
	sys.stderr = sys.__stderr__
# If debugging is off, set output to /dev/null (*nix) or nul (Windows):
else:
	sys.stdout = open(os.devnull, 'w')
	sys.stderr = open(os.devnull, 'w')

# Our emailer:
def mailer():
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = hostname + ' -- Online'
	
	body = str(trampstamp) + ' \n' 
	body = body + '%s host %s is online\n\n' % (opsys, hostname)
	body = body + mailSig
	
	print body
	
	# Plain text email:
	msg.attach(MIMEText(body,'plain'))
	# Define server with SMTP server name and port:
	server = smtplib.SMTP(mailserver, mailport)
	server.starttls()
	# Log into SMTP server:
	server.login(fromaddr, obscurePass)
	text = msg.as_string()
	
	# Time to send the email:
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	
	print 'done!'

def testconnection():
	while True:
		# If there's a response, let's get out of here:
		response = os.system(pingcmd)
		if response == 0:
			print netup
			return
		# If there's no response, let's keep trying:
		else:
			print netdown
			time.sleep(backoff)
			pass


# define our globals and get to work:
# OS we are running:
ostype = platform.system().lower()

# Seeing "Darwin" for a Mac is annoying:
if (ostype == 'darwin'):
	opsys = 'mac'
else:
	opsys = platform.system()

# Set ping arguments based on OS: 
if ostype == "windows":
	pingcmd = 'ping -n 1 ' + remotehost + ' > nul 2>&1'
else:
	pingcmd = 'ping -c 1 ' + remotehost + ' > /dev/null 2>&1'


# Time to ping the remote host:
testconnection()
# Once an ICMP ping reply is received, send the email alert:
mailer()
