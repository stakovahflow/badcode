#!/usr/bin/env python2
import os, sys, subprocess, time, datetime
import multiprocessing as mp

CONFIG=''
ACCOUNT=''
CONFDIR='/home/stak/.openvpn/'
AUTHFILE=CONFDIR + 'auth.txt'
COMMAND='sudo /usr/sbin/openvpn --config %s' % (CONFDIR)
LOCKDIR='/home/stak/.log/'
LOCKFILE=LOCKDIR + 'openvpn.lock'
LINE=(os.system("printf '%*s\n' \"${COLUMNS:-$(tput cols)}\" '' | tr ' ' -"))
r=0

if not os.path.exists(LOCKDIR):
    os.makedirs(LOCKDIR)

if not os.path.exists(CONFDIR):
	print("Configuration directory doesn't exist.")
	print("Creating '%s' now" % CONFDIR)
	print("You'll probably want to populate it from here:")
	print("http://proxpn.com/updater/locations.html")
	exit(0)

def EXTIP():
	IP=subprocess.Popen("curl -s http://ipecho.net/plain", shell=True, stdout=subprocess.PIPE).stdout
	CURRENTIP = IP.read()
	return CURRENTIP.decode()

def DATED():
	DATE=str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
	return DATE

def getIP():
	retries = 2
	while retries > 0:

		try:
			while os.path.exists(LOCKFILE):
				CURSORUP = '\033[F'
				ERASELN  = '\033[K'
				print(CURSORUP + ERASELN + DATED() + ": Current external IP: %s" % (EXTIP()))
				time.sleep(5)
		except:
			print("error getting IP.")
			retries = retries - 1
			exit(0)

def startVPN():
	try:
		if (len(sys.argv) != 2):
			print 'Australia - 1'
			print 'New York - 2'
			print 'Seattle - 3'
			print 'Frankfurt - 4'
			print 'Los Angeles - 5'
			print 'Miami - 6'
			print 'Amsterdam - 7'
			print 'Sweden - 8'
			print 'London - 9'
		else:
			ACCOUNT=sys.argv[1]
		if os.path.isfile(LOCKFILE):
			L=open(LOCKFILE,'r')
			LPID=L.readline()
			print ("already running %s" % (LPID))
			sys.exit(0)
		else:
			os.getpid()
			L=open(LOCKFILE,'w')
			L.write('%s' % (os.getpid()))
			L.close()
		#print 'RESOLV.CONF:'
		#os.system("cat /etc/resolv.conf")
		# 'Australia - 1'
		if (ACCOUNT == '1'):
			CONFIG='udp-au3_udp.ovpn'
		# 'New York - 2'
		elif (ACCOUNT == '2'):
			CONFIG='udp-bny2_udp.ovpn'
		# 'Los Angeles - 3'
		elif (ACCOUNT == '3'):
			CONFIG='udp-la3_udp.ovpn'
		# 'Zurich - 4'
		elif (ACCOUNT == '4'):
			CONFIG='udp-zch1_udp.ovpn'
		# 'Toronto - 5'
		elif (ACCOUNT == '5'):
			CONFIG='udp-tor1_udp.ovpn'
		# 'Miami - 6'
		elif (ACCOUNT == '6'):
			CONFIG='udp-mfl2_udp.ovpn'
		# 'Amsterdam - 7'
		elif (ACCOUNT == '7'):
			CONFIG='udp-ams1_udp.ovpn'
		# 'Sweden - 8'
		elif (ACCOUNT == '8'):
			CONFIG='udp-swe1_udp.ovpn'
		# 'London - 9'
		elif (ACCOUNT == '9'):
			CONFIG='udp-uk1_udp.ovpn'
		else:
			print 'no such VPN profile exists'
			sys.exit(0)
		print CONFIG
		print ('%s%s' % (COMMAND,CONFIG))
		os.system('sudo mv /etc/resolv.conf /etc/resolv.conf.old')
		os.system('sudo cp /etc/resolv.conf.DEFAULT /etc/resolv.conf;sudo chmod a+r /etc/resolv.conf')
		os.system('%s%s' % (COMMAND,CONFIG))
		os.system('sudo mv /etc/resolv.conf.old /etc/resolv.conf')
		time.sleep(1)
		print 'RESOLV.CONF:'
		os.system("cat /etc/resolv.conf")
		secs = 5
		print ''
		os.system("rfkill block 2")
		time.sleep(2)
		os.system("rm -f %s" % LOCKFILE)
		os.system("rfkill unblock 2")
		
		while ( secs > 0 ):
			CURSORUP = '\033[F'
			ERASELN  = '\033[K'
			discoball = str(secs)
			print(CURSORUP + ERASELN + discoball)
			time.sleep(1)
			secs=secs - 1
		print('Thanks for calling!')
	except:
		print('OOPS!')
		print('Thanks for calling!')
	"""os.system('reset')"""
	
if __name__=='__main__':
	if (os.path.exists(LOCKFILE)):
		print("removing lockfile: %s" % LOCKFILE)
		os.system("rm -f %s" % LOCKFILE)
	else:
		p1 = mp.Process(target = getIP)
		p1.start()
		p2 = mp.Process(target = startVPN)
		p2.start()

exit(0)
